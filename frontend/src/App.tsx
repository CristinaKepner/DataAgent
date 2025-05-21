import React from 'react';
import { Layout } from 'antd';

const { Header, Content } = Layout;

const App: React.FC = () => {
  return (
    <Layout>
      <Header>标注平台</Header>
      <Content>
        {/* 标注区域 */}
      </Content>
    </Layout>
  );
};

export default App;