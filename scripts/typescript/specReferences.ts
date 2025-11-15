export interface McpSpecReference {
  title: string;
  url: string;
  summary: string;
}

const coreSpec: McpSpecReference = {
  title: 'Model Context Protocol Specification',
  url: 'https://modelcontextprotocol.io/spec',
  summary: 'Authoritative source for the evolving MCP standard.'
};

export function getCoreSpecification(): McpSpecReference {
  return coreSpec;
}
