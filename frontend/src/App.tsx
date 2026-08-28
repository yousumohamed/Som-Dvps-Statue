import React, { useState, useEffect } from 'react';

interface MetricNode {
  id: string;
  name: string;
  status: 'healthy' | 'degraded' | 'down';
  latencyMs: number;
}

export const App: React.FC = () => {
  const [nodes, setNodes] = useState<MetricNode[]>([]);
  const [loading, setLoading] = useState<boolean>(true);

  useEffect(() => {
    // Quick polling simulation for status metrics
    const timer = setTimeout(() => {
      setNodes([
        { id: 'node-01', name: 'Mogadishu Edge Relay', status: 'healthy', latencyMs: 12 },
        { id: 'node-02', name: 'Hargeisa Telemetry Ingress', status: 'healthy', latencyMs: 24 },
        { id: 'node-03', name: 'Garowe Vault Cluster', status: 'degraded', latencyMs: 140 },
      ]);
      setLoading(false);
    }, 400);

    return () => clearTimeout(timer);
  }, []);

  return (
    <div className="statue-dashboard p-6 max-w-4xl mx-auto">
      <header className="border-b pb-4 mb-6">
        <h1 className="text-2xl font-bold tracking-tight">Somalia DevOps Statue Console</h1>
        <p className="text-sm text-gray-500">Real-time infrastructure health and node telemetry</p>
      </header>

      {loading ? (
        <div className="animate-pulse text-sm">Fetching metrics feed...</div>
      ) : (
        <div className="grid gap-4">
          {nodes.map((node) => (
            <div key={node.id} className="p-4 border rounded-lg flex justify-between items-center">
              <div>
                <p className="font-medium">{node.name}</p>
                <p className="text-xs text-gray-400">ID: {node.id}</p>
              </div>
              <div className="text-right">
                <span className={`inline-block px-2 py-1 text-xs rounded ${node.status === 'healthy' ? 'bg-green-100 text-green-800' : 'bg-yellow-100 text-yellow-800'}`}>
                  {node.status}
                </span>
                <p className="text-xs mt-1 text-gray-500">{node.latencyMs}ms</p>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default App;
