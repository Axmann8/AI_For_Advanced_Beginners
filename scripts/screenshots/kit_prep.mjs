// Gives every Notion node a realistic (sample) database link, the way a reader pastes their own.
import { withApi } from './api.mjs';
const SAMPLE = {
  Inbox: 'https://www.notion.so/your-workspace/1a2b3c4d5e6f47a8b9c0d1e2f3a4b5c6?v=7d8e9f0a1b2c43d4e5f6a7b8c9d0e1f2',
  Tasks: 'https://www.notion.so/your-workspace/2b3c4d5e6f7a48b9c0d1e2f3a4b5c6d7?v=8e9f0a1b2c3d44e5f6a7b8c9d0e1f2a3',
  Briefings: 'https://www.notion.so/your-workspace/3c4d5e6f7a8b49c0d1e2f3a4b5c6d7e8?v=9f0a1b2c3d4e45f6a7b8c9d0e1f2a3b4',
  Log: 'https://www.notion.so/your-workspace/4d5e6f7a8b9c40d1e2f3a4b5c6d7e8f9?v=0a1b2c3d4e5f46a7b8c9d0e1f2a3b4c5',
};
await withApi(async (api) => {
  const r = await api('GET', '/workflows');
  for (const w of r.data) {
    const full = (await api('GET', '/workflows/' + w.id)).data;
    let changed = 0;
    for (const n of full.nodes) {
      const db = n.parameters?.databaseId;
      if (db && typeof db === 'object' && /PASTE/.test(db.value || '')) {
        const key = /INBOX/i.test(db.value) ? 'Inbox' : /TASK/i.test(db.value) ? 'Tasks' : /BRIEF/i.test(db.value) ? 'Briefings' : 'Log';
        db.value = SAMPLE[key]; db.mode = 'url'; changed++;
      }
    }
    if (changed) {
      const res = await api('PATCH', '/workflows/' + w.id, { nodes: full.nodes, connections: full.connections, versionId: full.versionId, name: full.name });
      console.log(w.name, 'patched', changed, res.status, res.message || '');
    }
  }
});
