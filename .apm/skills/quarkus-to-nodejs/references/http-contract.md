# Bounded HTTP contract fixture

This dependency-free Node.js example checks the same success, missing-route and service-failure statuses as the repository's Quarkus baseline. It does not reproduce Quarkus event-bus delivery, security or persistence. The Python test runner extracts this single `javascript` block into a temporary test file; no JavaScript automation script is shipped in the repository.

```javascript
import http from 'node:http';
import { once } from 'node:events';
import test from 'node:test';
import assert from 'node:assert/strict';

async function greeting(fail) {
  if (fail) throw new Error('unavailable');
  return { message: 'hello' };
}

function createApp() {
  return http.createServer(async (request, response) => {
    const path = new URL(request.url, 'http://localhost').pathname;
    if (request.method !== 'GET' || !['/hello', '/failure'].includes(path)) {
      response.writeHead(404).end();
      return;
    }
    try {
      const body = await greeting(path === '/failure');
      response.writeHead(200, { 'content-type': 'application/json' });
      response.end(JSON.stringify(body));
    } catch {
      response.writeHead(503).end();
    }
  });
}

test('HTTP contract and owned server cleanup', async () => {
  const server = createApp();
  server.listen(0, '127.0.0.1');
  await once(server, 'listening');
  try {
    const base = `http://127.0.0.1:${server.address().port}`;
    const response = await fetch(`${base}/hello`, { signal: AbortSignal.timeout(5000) });
    assert.equal(response.status, 200);
    assert.match(response.headers.get('content-type'), /^application\/json/);
    assert.deepEqual(await response.json(), { message: 'hello' });
    for (const [path, status] of [['/missing', 404], ['/failure', 503]]) {
      const other = await fetch(base + path, { signal: AbortSignal.timeout(5000) });
      assert.equal(other.status, status);
      await other.text();
    }
  } finally {
    await new Promise((resolve, reject) => server.close(error => error ? reject(error) : resolve()));
  }
  assert.equal(server.listening, false);
});
```
