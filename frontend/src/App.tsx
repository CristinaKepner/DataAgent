import React from 'react';
import { Layout, Tabs } from 'antd';
import PDFAnnotator from './components/PDFAnnotator';

const { Header, Content } = Layout;
const { TabPane } = Tabs;

const App: React.FC = () => {
  return (
    <Layout>
      <Header>大模型数据标注平台</Header>
      <Content>
        <Tabs defaultActiveKey="1">
          <TabPane tab="PDF标注" key="1">
            <PDFAnnotator />
          </TabPane>
          {/* 其他标注类型 */}
        </Tabs>
      </Content>
    </Layout>
  );
};

export default App;