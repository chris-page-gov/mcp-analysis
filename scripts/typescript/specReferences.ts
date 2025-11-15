export interface McpSpecReference {
  title: string;
  url: string;
  summary: string;
}

const coreSpec: McpSpecReference = {
  title: 'Model Context Protocol Specification',
  url: 'https://modelcontextprotocol.io/specification',
  summary: 'Mintlify-hosted portal for the current and historical MCP protocol versions.',
};

export function getCoreSpecification(): McpSpecReference {
  return coreSpec;
}
