import { withApi } from './api.mjs';
await withApi(async (api) => {
  const r = await api('GET', '/workflows?includeScopes=false');
  for (const w of r.data || []) {
    await api('POST', `/workflows/${w.id}/archive`);
    const d = await api('DELETE', `/workflows/${w.id}`);
    console.log('deleted', w.name, d.status);
  }
  const c = await api('GET', '/credentials');
  for (const cr of c.data || []) { const d = await api('DELETE', `/credentials/${cr.id}`); console.log('deleted cred', cr.name, d.status); }
});
