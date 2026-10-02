import { withApi } from './api.mjs';
await withApi(async (api) => {
  let creds = (await api('GET', '/credentials')).data;
  if (!creds.find(c => c.type === 'httpBearerAuth')) {
    const r = await api('POST', '/credentials', { name: 'Bearer Auth account', type: 'httpBearerAuth', data: { token: 'a-long-random-token-for-claude' } });
    console.log('bearer', r.status); creds = (await api('GET', '/credentials')).data;
  }
  const by = (t) => { const c = creds.find(c => c.type === t); return c ? { id: c.id, name: c.name } : null; };
  const map = { 'n8n-nodes-base.notion': ['notionApi'], 'n8n-nodes-base.notionTool': ['notionApi'],
    '@n8n/n8n-nodes-langchain.lmChatAnthropic': ['anthropicApi'], 'n8n-nodes-base.webhook': ['httpHeaderAuth'],
    '@n8n/n8n-nodes-langchain.mcpTrigger': ['httpBearerAuth'] };
  const r = await api('GET', '/workflows');
  for (const w of r.data) {
    const full = (await api('GET', '/workflows/' + w.id)).data; let n = 0;
    for (const node of full.nodes) for (const t of map[node.type] || []) {
      if (by(t) && !(node.credentials && node.credentials[t])) { node.credentials = { ...(node.credentials || {}), [t]: by(t) }; n++; }
    }
    if (n) { const p = await api('PATCH', '/workflows/' + w.id, { nodes: full.nodes, connections: full.connections, versionId: full.versionId, name: full.name }); console.log(w.name, n, p.status, p.message || ''); }
  }
});
