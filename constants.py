# -*- coding: utf-8 -*-

TABLE_CONFIG = {
                'zcfzb' : {'begin':{'title':u'合并资产负债表','len':9}, 'end':{'title':u'公司资产负债表','len':10}},
                'lrb' : {'begin':{'title':u'合并利润表','len':7}, 'end':{'title':u'公司利润表','len':8}},
                'xjllb' : {'begin':{'title':u'合并现金流量表','len':9}, 'end':{'title':u'公司现金流量表','len':10}},
                }

TABLE_FIELDS = {
                'zcfzb' : (
                            (u'货币资金', None),
                            (u'结算备付金', None),
                            (u'拆出资金', None),
                            (u'以公允价值计量且其变动计入当期损益的金融资产', None),
                            (u'以公允价值计量且其变动计入当期损益的衍生金融资产', None),
                            (u'衍生金融资产', None),
                            (u'交易性金融资产', None),
                            (u'应收票据', None),
                            (u'应收账款', None),
                            (u'预付款项', None),
                            (u'应收保费', None),
                            (u'应收分保账款', None),
                            (u'应收分保合同准备金', None),
                            (u'应收利息', None),
                            (u'应收股利', None),
                            (u'其他应收款', None),
                            (u'买入返售金融资产', None),
                            (u'存货', None),
                            (u'划分为持有待售的资产', None),
                            (u'一年内到期的非流动资产', None),
                            (u'其他流动资产', None),
                            (u'流动资产合计', None),
                            (u'发放委托贷款及垫款', u'发放贷款及垫款'),
                            (u'发放贷款和垫款', u'发放贷款及垫款'),
                            (u'发放贷款及垫款', None),
                            (u'可供出售金融资产', None),
                            (u'持有至到期投资', None),
                            (u'长期应收款', None),
                            (u'长期股权投资', None),
                            (u'投资性房地产', None),
                            (u'固定资产', None),
                            (u'在建工程', None),
                            (u'工程物资', None),
                            (u'固定资产清理', None),
                            (u'生产性生物资产', None),
                            (u'油气资产', None),
                            (u'无形资产', None),
                            (u'开发支出', None),
                            (u'商誉', None),
                            (u'长期待摊费用', None),
                            (u'递延所得税资产', None),
                            (u'其他非流动资产', None),
                            (u'非流动资产合计', None),
                            (u'资产总计', None),
                            (u'短期借款', None),
                            (u'向中央银行借款', None),
                            (u'吸收存款及同业存放', None),
                            (u'交易性金融负债', None),
                            (u'拆入资金', None),
                            (u'以公允价值计量且其变动计入当期损益的金融负债', None),
                            (u'以公允价值计量且其变动计入当期损益的衍生金融负债', None),
                            (u'衍生金融负债', None),
                            (u'应付票据', None),
                            (u'应付账款', None),
                            (u'预收款项', None),
                            (u'卖出回购金融资产款', None),
                            (u'应付手续费及佣金', None),
                            (u'应付职工薪酬', None),
                            (u'应交税费', None),
                            (u'应付利息', None),
                            (u'应付股利', None),
                            (u'其他应付款', None),
                            (u'应付分保账款', None),
                            (u'保险合同准备金', None),
                            (u'代理买卖证券款', None),
                            (u'代理承销证券款', None),
                            (u'划分为持有待售的负债', None),
                            (u'一年内到期的非流动负债', None),
                            (u'其他流动负债', None),
                            (u'流动负债合计', None),
                            (u'长期借款', None),
                            (u'应付债券', None),
                            (u'长期应付款', None),
                            (u'长期应付职工薪酬', None),
                            (u'专项应付款', None),
                            (u'预计负债', None),
                            (u'递延收益', None),
                            (u'递延所得税负债', None),
                            (u'其他非流动负债', None),
                            (u'非流动负债合计', None),
                            (u'负债合计', None),
                            (u'股本', None),
                            (u'其他权益工具', None),
                            (u'资本公积', None),
                            (u'库存股', None),
                            (u'其他综合收益', None),
                            (u'专项储备', None),
                            (u'盈余公积', None),
                            (u'一般风险准备', None),
                            (u'未分配利润', None),
                            (u'外币报表折算差额', None),
                            (u'归属于母公司股东权益合计', None),
                            (u'归属于母公司所有者权益合计', None),
                            (u'少数股东权益', None),
                            (u'股东权益合计', None),
                            (u'所有者权益合计', None),
                            (u'负债和股东权益总计', None),
                           ),
                'lrb' : (
                            (u'营业总收入', None),
                            (u'营业收入', None),
                            (u'利息收入', None),
                            (u'已赚保费', None),
                            (u'手续费及佣金收入', None),
                            (u'营业总成本', None),
                            (u'营业成本', None),
                            (u'利息支出', None),
                            (u'手续费及佣金支出', None),
                            (u'退保金', None),
                            (u'赔付支出净额', None),
                            (u'提取保险合同准备金净额', None),
                            (u'保单红利支出', None),
                            (u'分保费用', None),
                            (u'营业税金及附加', None),
                            (u'销售费用', None),
                            (u'管理费用', None),
                            (u'财务费用', None),
                            (u'资产减值损失', None),
                            (u'公允价值变动收益', None),
                            (u'投资收益', None),
                            (u'其中：对联营企业和合营企业的投资收益', None),
                            (u'汇兑收益', None),
                            (u'营业利润', None),
                            (u'营业外收入', None),
                            (u'其中：非流动资产处置利得', None),
                            (u'营业外支出', None),
                            (u'其中：非流动资产处置损失', None),
                            (u'利润总额', None),
                            (u'所得税费用', None),
                            (u'净利润', None),
                            (u'归属于母公司所有者的净利润', None),
                            (u'少数股东损益', None),
                            (u'其他综合收益的税后净额', None),
                            (u'归属母公司所有者的其他综合收益的税后净额', None),
                            (u'归属于少数股东的其他综合收益的税后净额', None),
                            (u'综合收益总额', None),
                            (u'归属于母公司所有者的综合收益总额', None),
                            (u'归属于少数股东的综合收益总额', None),
                            (u'基本每股收益', None),
                            (u'稀释每股收益', None),
                           ),
                'xjllb' : (
                            (u'销售商品、提供劳务收到的现金', None),
                            (u'吸收存款及同业存款净增加额', u'吸收存款和同业存放款项净增加额'),
                            (u'吸收存款和同业存放款项净增加额', None),
                            (u'客户存款和同业存放款项净增加额', None),
                            (u'向中央银行借款净增加额', None),
                            (u'向其他金融机构拆入资金净增加额', None),
                            (u'收到原保险合同保费取得的现金', None),
                            (u'收到再保险业务现金净额', None),
                            (u'保户储金及投资款净增加额', None),
                            (u'处置以公允价值计量且其变动计入当期损益的金融资产净增加额', None),
                            (u'收取利息、手续费及佣金收到的现金', None),
                            (u'收取利息、手续费及佣金的现金', u'收取利息、手续费及佣金收到的现金'),
                            (u'拆入资金净增加额', None),
                            (u'回购业务资金净增加额', None),
                            (u'回购业务资金减少额', u'回购业务资金净增加额'),
                            (u'收到的税费返还', None),
                            (u'存放中央银行款项净减少额', None),
                            (u'收到其他与经营活动有关的现金', None),
                            (u'收到的其他与经营活动有关的现金', u'收到其他与经营活动有关的现金'),
                            (u'经营活动现金流入小计', None),
                            (u'购买商品、接受劳务支付的现金', None),
                            (u'客户贷款及垫款净增加额', u'发放贷款及垫款净增加额'),
                            (u'发放贷款及垫款净增加额', None),
                            (u'存放中央银行款项净增加额', u'存放中央银行和同业款项净增加额'),
                            (u'存放中央银行和同业款项净增加额', None),
                            (u'支付原保险合同赔付款项的现金', None),
                            (u'支付利息、手续费及佣金支付的现金', None),
                            (u'支付利息、手续费及佣金的现金', u'支付利息、手续费及佣金支付的现金'),
                            (u'支付保单红利的现金', None),
                            (u'支付给职工以及为职工支付的现金', None),
                            (u'支付的各项税费', None),
                            (u'拆入资金净减少额', None),
                            (u'回购业务资金净减少额', None),
                            (u'支付其他与经营活动有关的现金', None),
                            (u'支付的其他与经营活动有关的现金', u'支付其他与经营活动有关的现金'),
                            (u'经营活动现金流出小计', None),
                            (u'经营活动产生的现金流量净额', None),
                            (u'收回投资收到的现金', None),
                            (u'取得投资收益收到的现金', None),
                            (u'取得投资收益所收到的现金', u'取得投资收益收到的现金'),
                            (u'处置固定资产、无形资产和其他长期资产收回的现金', None),
                            (u'处置子公司及其他营业单位收到的现金', None),
                            (u'购买子公司收到的现金净额', None),
                            (u'收到其他与投资活动有关的现金', None),
                            (u'收到的其他与投资活动有关的现金', u'收到其他与投资活动有关的现金'),
                            (u'投资活动现金流入小计', None),
                            (u'购建固定资产、无形资产和其他长期资产支付的现金', None),
                            (u'投资支付的现金', None),
                            (u'质押贷款净增加额', None),
                            (u'取得子公司流出的现金净额', u'取得子公司及处置子公司流出的现金净额'),
                            (u'取得子公司及其他营业单位支付的现金净额', u'取得子公司及处置子公司流出的现金净额'),
                            (u'取得子公司及处置子公司流出的现金净额', None),
                            (u'支付其他与投资活动有关的现金', None),
                            (u'投资活动现金流出小计', None),
                            (u'投资活动产生的现金流量净额', None),
                            (u'吸收投资收到的现金', None),
                            (u'取得借款收到的现金', None),
                            (u'取得借款所收到的现金', u'取得借款收到的现金'),
                            (u'发行债券收到的现金', None),
                            (u'收到其他与筹资活动有关的现金', u'收到其他与筹资活动有关的现金'),
                            (u'收到的其他与筹资活动有关的现金', None),
                            (u'筹资活动现金流入小计', None),
                            (u'偿还债务支付的现金', None),
                            (u'偿还债务所支付的现金', u'偿还债务支付的现金'),
                            (u'分配股利、利润或偿付利息支付的现金', None),
                            (u'分配股利、利润或偿付利息所支付的现金', u'分配股利、利润或偿付利息支付的现金'),
                            (u'支付其他与筹资活动有关的现金', None),
                            (u'支付的其他与筹资活动有关的现金', u'支付其他与筹资活动有关的现金'),
                            (u'筹资活动现金流出小计', None),
                            (u'筹资活动产生的现金流量净额', None),
                            (u'汇率变动对现金及现金等价物的影响', None),
                            (u'现金及现金等价物净减少额', None),
                            (u'期初现金及现金等价物余额', None),
                            (u'年初现金及现金等价物余额', u'期初现金及现金等价物余额'),
                            (u'期末现金及现金等价物余额', None),
                            (u'年末现金及现金等价物余额', u'期末现金及现金等价物余额'),
                           ),
                }