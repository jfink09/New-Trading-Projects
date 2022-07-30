import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn
from scipy.stats import linregress

QQQ = yf.download('QQQ',start='2021-01-01',end='2021-12-31',interval='1d')

ATVI = yf.download('ATVI',start='2021-01-01',end='2021-12-31',interval='1d')
ADBE = yf.download('ADBE',start='2021-01-01',end='2021-12-31',interval='1d')
ADP = yf.download('ADP',start='2021-01-01',end='2021-12-31',interval='1d')
ABNB = yf.download('ABNB',start='2021-01-01',end='2021-12-31',interval='1d')
ALGN = yf.download('ALGN',start='2021-01-01',end='2021-12-31',interval='1d')
GOOGL = yf.download('GOOGL',start='2021-01-01',end='2021-12-31',interval='1d')
GOOG = yf.download('GOOG',start='2021-01-01',end='2021-12-31',interval='1d')
AMZN = yf.download('AMZN',start='2021-01-01',end='2021-12-31',interval='1d')
AMD = yf.download('AMD',start='2021-01-01',end='2021-12-31',interval='1d')
AEP = yf.download('AEP',start='2021-01-01',end='2021-12-31',interval='1d')
AMGN = yf.download('AMGN',start='2021-01-01',end='2021-12-31',interval='1d')
ADI = yf.download('ADI',start='2021-01-01',end='2021-12-31',interval='1d')
ANSS = yf.download('ANSS',start='2021-01-01',end='2021-12-31',interval='1d')
AAPL = yf.download('AAPL',start='2021-01-01',end='2021-12-31',interval='1d')
AMAT = yf.download('AMAT',start='2021-01-01',end='2021-12-31',interval='1d')
ASML = yf.download('ASML',start='2021-01-01',end='2021-12-31',interval='1d')
AZN = yf.download('AZN',start='2021-01-01',end='2021-12-31',interval='1d')
TEAM = yf.download('TEAM',start='2021-01-01',end='2021-12-31',interval='1d')
ADSK = yf.download('ADSK',start='2021-01-01',end='2021-12-31',interval='1d')
BIDU = yf.download('BIDU',start='2021-01-01',end='2021-12-31',interval='1d')
#BIID = yf.download('BIID',start='2021-01-01',end='2021-12-31',interval='1d')
BKNG = yf.download('BKNG',start='2021-01-01',end='2021-12-31',interval='1d')
AVGO = yf.download('AVGO',start='2021-01-01',end='2021-12-31',interval='1d')
CDNS = yf.download('CDNS',start='2021-01-01',end='2021-12-31',interval='1d')
CHTR = yf.download('CHTR',start='2021-01-01',end='2021-12-31',interval='1d')
CTAS = yf.download('CTAS',start='2021-01-01',end='2021-12-31',interval='1d')
CSCO = yf.download('CSCO',start='2021-01-01',end='2021-12-31',interval='1d')
CTSH = yf.download('CTSH',start='2021-01-01',end='2021-12-31',interval='1d')
CMCSA = yf.download('CMCSA',start='2021-01-01',end='2021-12-31',interval='1d')
#CEG = yf.download('CEG',start='2021-01-01',end='2021-12-31',interval='1d')
CPRT = yf.download('CPRT',start='2021-01-01',end='2021-12-31',interval='1d')
COST = yf.download('COST',start='2021-01-01',end='2021-12-31',interval='1d')
CRWD = yf.download('CRWD',start='2021-01-01',end='2021-12-31',interval='1d')
CSX = yf.download('CSX',start='2021-01-01',end='2021-12-31',interval='1d')
DDOG = yf.download('DDOG',start='2021-01-01',end='2021-12-31',interval='1d')
DXCM = yf.download('DXCM',start='2021-01-01',end='2021-12-31',interval='1d')
DOCU = yf.download('DOCU',start='2021-01-01',end='2021-12-31',interval='1d')
DLTR = yf.download('DLTR',start='2021-01-01',end='2021-12-31',interval='1d')
EBAY = yf.download('EBAY',start='2021-01-01',end='2021-12-31',interval='1d')
EA = yf.download('EA',start='2021-01-01',end='2021-12-31',interval='1d')
EXC = yf.download('EXC',start='2021-01-01',end='2021-12-31',interval='1d')
FAST = yf.download('FAST',start='2021-01-01',end='2021-12-31',interval='1d')
FISV = yf.download('FISV',start='2021-01-01',end='2021-12-31',interval='1d')
FTNT = yf.download('FTNT',start='2021-01-01',end='2021-12-31',interval='1d')
GILD = yf.download('GILD',start='2021-01-01',end='2021-12-31',interval='1d')
HON = yf.download('HON',start='2021-01-01',end='2021-12-31',interval='1d')
IDXX = yf.download('IDXX',start='2021-01-01',end='2021-12-31',interval='1d')
ILMN = yf.download('ILMN',start='2021-01-01',end='2021-12-31',interval='1d')
INTC = yf.download('INTC',start='2021-01-01',end='2021-12-31',interval='1d')
INTU = yf.download('INTU',start='2021-01-01',end='2021-12-31',interval='1d')
ISRG = yf.download('ISRG',start='2021-01-01',end='2021-12-31',interval='1d')
JD = yf.download('JD',start='2021-01-01',end='2021-12-31',interval='1d')
KDP = yf.download('KDP',start='2021-01-01',end='2021-12-31',interval='1d')
KLAC = yf.download('KLAC',start='2021-01-01',end='2021-12-31',interval='1d')
KHC = yf.download('KHC',start='2021-01-01',end='2021-12-31',interval='1d')
LRCX = yf.download('LRCX',start='2021-01-01',end='2021-12-31',interval='1d')
LCID = yf.download('LCID',start='2021-01-01',end='2021-12-31',interval='1d')
LULU = yf.download('LULU',start='2021-01-01',end='2021-12-31',interval='1d')
MAR = yf.download('MAR',start='2021-01-01',end='2021-12-31',interval='1d')
MRVL = yf.download('MRVL',start='2021-01-01',end='2021-12-31',interval='1d')
MTCH = yf.download('MTCH',start='2021-01-01',end='2021-12-31',interval='1d')
MELI = yf.download('MELI',start='2021-01-01',end='2021-12-31',interval='1d')
META = yf.download('META',start='2021-01-01',end='2021-12-31',interval='1d')
MCHP = yf.download('MCHP',start='2021-01-01',end='2021-12-31',interval='1d')
MU = yf.download('MU',start='2021-01-01',end='2021-12-31',interval='1d')
MSFT = yf.download('MSFT',start='2021-01-01',end='2021-12-31',interval='1d')
MRNA = yf.download('MRNA',start='2021-01-01',end='2021-12-31',interval='1d')
MDLZ = yf.download('MDLZ',start='2021-01-01',end='2021-12-31',interval='1d')
MNST = yf.download('MNST',start='2021-01-01',end='2021-12-31',interval='1d')
NTES = yf.download('NTES',start='2021-01-01',end='2021-12-31',interval='1d')
NFLX = yf.download('NFLX',start='2021-01-01',end='2021-12-31',interval='1d')
NVDA = yf.download('NVDA',start='2021-01-01',end='2021-12-31',interval='1d')
NXPI = yf.download('NXPI',start='2021-01-01',end='2021-12-31',interval='1d')
ORLY = yf.download('ORLY',start='2021-01-01',end='2021-12-31',interval='1d')
OKTA = yf.download('OKTA',start='2021-01-01',end='2021-12-31',interval='1d')
ODFL = yf.download('ODFL',start='2021-01-01',end='2021-12-31',interval='1d')
PCAR = yf.download('PCAR',start='2021-01-01',end='2021-12-31',interval='1d')
PANW = yf.download('PANW',start='2021-01-01',end='2021-12-31',interval='1d')
PAYX = yf.download('PAYX',start='2021-01-01',end='2021-12-31',interval='1d')
PYPL = yf.download('PYPL',start='2021-01-01',end='2021-12-31',interval='1d')
PEP = yf.download('PEP',start='2021-01-01',end='2021-12-31',interval='1d')
PDD = yf.download('PDD',start='2021-01-01',end='2021-12-31',interval='1d')
QCOM = yf.download('QCOM',start='2021-01-01',end='2021-12-31',interval='1d')
REGN = yf.download('REGN',start='2021-01-01',end='2021-12-31',interval='1d')
ROST = yf.download('ROST',start='2021-01-01',end='2021-12-31',interval='1d')
SGEN = yf.download('SGEN',start='2021-01-01',end='2021-12-31',interval='1d')
SIRI = yf.download('SIRI',start='2021-01-01',end='2021-12-31',interval='1d')
SWKS = yf.download('SWKS',start='2021-01-01',end='2021-12-31',interval='1d')
SPLK = yf.download('SPLK',start='2021-01-01',end='2021-12-31',interval='1d')
SBUX = yf.download('SBUX',start='2021-01-01',end='2021-12-31',interval='1d')
SNPS = yf.download('SNPS',start='2021-01-01',end='2021-12-31',interval='1d')
TMUS = yf.download('TMUS',start='2021-01-01',end='2021-12-31',interval='1d')
TSLA = yf.download('TSLA',start='2021-01-01',end='2021-12-31',interval='1d')
TXN = yf.download('TXN',start='2021-01-01',end='2021-12-31',interval='1d')
VRSN = yf.download('VRSN',start='2021-01-01',end='2021-12-31',interval='1d')
VRSK = yf.download('VRSK',start='2021-01-01',end='2021-12-31',interval='1d')
VRTX = yf.download('VRTX',start='2021-01-01',end='2021-12-31',interval='1d')
WBA = yf.download('WBA',start='2021-01-01',end='2021-12-31',interval='1d')
WDAY = yf.download('WDAY',start='2021-01-01',end='2021-12-31',interval='1d')
XEL = yf.download('XEL',start='2021-01-01',end='2021-12-31',interval='1d')
ZM = yf.download('ZM',start='2021-01-01',end='2021-12-31',interval='1d')
ZS = yf.download('ZS',start='2021-01-01',end='2021-12-31',interval='1d')

QQQ.to_csv('qqq.csv')
ATVI.to_csv('ATVI.csv')
ADBE.to_csv('ADBE.csv')
ADP.to_csv('ADP.csv')
ABNB.to_csv('ABNB.csv')
ALGN.to_csv('ALGN.csv')
GOOGL.to_csv('GOOGL.csv')
GOOG.to_csv('GOOG.csv')
AMZN.to_csv('AMZN.csv')
AMD.to_csv('AMD.csv')
AEP.to_csv('AEP.csv')
AMGN.to_csv('AMGN.csv')
ADI.to_csv('ADI.csv')
ANSS.to_csv('ANSS.csv')
AAPL.to_csv('AAPL.csv')
AMAT.to_csv('AMAT.csv')
ASML.to_csv('ASML.csv')
AZN.to_csv('AZN.csv')
TEAM.to_csv('TEAM.csv')
ADSK.to_csv('ADSK.csv')
BIDU.to_csv('BIDU.csv')
#BIID.to_csv('BIID.csv')
BKNG.to_csv('BKNG.csv')
AVGO.to_csv('AVGO.csv')
CDNS.to_csv('CDNS.csv')
CHTR.to_csv('CHTR.csv')
CTAS.to_csv('CTAS.csv')
CSCO.to_csv('CSCO.csv')
CTSH.to_csv('CTSH.csv')
CMCSA.to_csv('CMCSA.csv')
#CEG.to_csv('CEG.csv')
CPRT.to_csv('CPRT.csv')
COST.to_csv('COST.csv')
CRWD.to_csv('CRWD.csv')
CSX.to_csv('CSX.csv')
DDOG.to_csv('DDOG.csv')
DXCM.to_csv('DXCM.csv')
DOCU.to_csv('DOCU.csv')
DLTR.to_csv('DLTR.csv')
EBAY.to_csv('EBAY.csv')
EA.to_csv('EA.csv')
EXC.to_csv('EXC.csv')
FAST.to_csv('FAST.csv')
FISV.to_csv('FISV.csv')
FTNT.to_csv('FTNT.csv')
GILD.to_csv('GILD.csv')
HON.to_csv('HON.csv')
IDXX.to_csv('IDXX.csv')
ILMN.to_csv('ILMN.csv')
INTC.to_csv('INTC.csv')
INTU.to_csv('INTU.csv')
ISRG.to_csv('ISRG.csv')
JD.to_csv('JD.csv')
KDP.to_csv('KDP.csv')
KLAC.to_csv('KLAC.csv')
KHC.to_csv('KHC.csv')
LRCX.to_csv('LRCX.csv')
LCID.to_csv('LCID.csv')
LULU.to_csv('LULU.csv')
MAR.to_csv('MAR.csv')
MRVL.to_csv('MRVL.csv')
MTCH.to_csv('MTCH.csv')
MELI.to_csv('MELI.csv')
META.to_csv('META.csv')
MCHP.to_csv('MCHP.csv')
MU.to_csv('MU.csv')
MSFT.to_csv('MSFT.csv')
MRNA.to_csv('MRNA.csv')
MDLZ.to_csv('MDLZ.csv')
MNST.to_csv('MNST.csv')
NTES.to_csv('NTES.csv')
NFLX.to_csv('NFLX.csv')
NVDA.to_csv('NVDA.csv')
NXPI.to_csv('NXPI.csv')
ORLY.to_csv('ORLY.csv')
OKTA.to_csv('OKTA.csv')
ODFL.to_csv('ODFL.csv')
PCAR.to_csv('PCAR.csv')
PANW.to_csv('PANW.csv')
PAYX.to_csv('PAYX.csv')
PYPL.to_csv('PYPL.csv')
PEP.to_csv('PEP.csv')
PDD.to_csv('PDD.csv')
QCOM.to_csv('QCOM.csv')
REGN.to_csv('REGN.csv')
ROST.to_csv('ROST.csv')
SGEN.to_csv('SGEN.csv')
SIRI.to_csv('SIRI.csv')
SWKS.to_csv('SWKS.csv')
SPLK.to_csv('SPLK.csv')
SBUX.to_csv('SBUX.csv')
SNPS.to_csv('SNPS.csv')
TMUS.to_csv('TMUS.csv')
TSLA.to_csv('TSLA.csv')
TXN.to_csv('TXN.csv')
VRSN.to_csv('VRSN.csv')
VRSK.to_csv('VRSK.csv')
VRTX.to_csv('VRTX.csv')
WBA.to_csv('WBA.csv')
WDAY.to_csv('WDAY.csv')
XEL.to_csv('XEL.csv')
ZM.to_csv('ZM.csv')
ZS.to_csv('ZS.csv')

QQQ = pd.read_csv('QQQ.csv'); QQQ['pct'] = QQQ['Close'].pct_change()
ATVI = pd.read_csv('ATVI.csv'); ATVI['pct'] = ATVI['Close'].pct_change()
ADBE = pd.read_csv('ADBE.csv'); ADBE['pct'] = ADBE['Close'].pct_change()
ADP = pd.read_csv('ADP.csv'); ADP['pct'] = ADP['Close'].pct_change()
ABNB = pd.read_csv('ABNB.csv'); ABNB['pct'] = ABNB['Close'].pct_change()
ALGN = pd.read_csv('ALGN.csv'); ALGN['pct'] = ALGN['Close'].pct_change()
GOOGL = pd.read_csv('GOOGL.csv'); GOOGL['pct'] = GOOGL['Close'].pct_change()
GOOG = pd.read_csv('GOOG.csv'); GOOG['pct'] = GOOG['Close'].pct_change()
AMZN = pd.read_csv('AMZN.csv'); AMZN['pct'] = AMZN['Close'].pct_change()
AMD = pd.read_csv('AMD.csv'); AMD['pct'] = AMD['Close'].pct_change()
AEP = pd.read_csv('AEP.csv'); AEP['pct'] = AEP['Close'].pct_change()
AMGN = pd.read_csv('AMGN.csv'); AMGN['pct'] = AMGN['Close'].pct_change()
ADI = pd.read_csv('ADI.csv'); ADI['pct'] = ADI['Close'].pct_change()
ANSS = pd.read_csv('ANSS.csv'); ANSS['pct'] = ANSS['Close'].pct_change()
AAPL = pd.read_csv('AAPL.csv'); AAPL['pct'] = AAPL['Close'].pct_change()
AMAT = pd.read_csv('AMAT.csv'); AMAT['pct'] = AMAT['Close'].pct_change()
ASML = pd.read_csv('ASML.csv'); ASML['pct'] = ASML['Close'].pct_change()
AZN = pd.read_csv('AZN.csv'); AZN['pct'] = AZN['Close'].pct_change()
TEAM = pd.read_csv('TEAM.csv'); TEAM['pct'] = TEAM['Close'].pct_change()
ADSK = pd.read_csv('ADSK.csv'); ADSK['pct'] = ADSK['Close'].pct_change()
BIDU = pd.read_csv('BIDU.csv'); BIDU['pct'] = BIDU['Close'].pct_change()
BKNG = pd.read_csv('BKNG.csv'); BKNG['pct'] = BKNG['Close'].pct_change()
AVGO = pd.read_csv('AVGO.csv'); AVGO['pct'] = AVGO['Close'].pct_change()
CDNS = pd.read_csv('CDNS.csv'); CDNS['pct'] = CDNS['Close'].pct_change()
CHTR = pd.read_csv('CHTR.csv'); CHTR['pct'] = CHTR['Close'].pct_change()
CTAS = pd.read_csv('CTAS.csv'); CTAS['pct'] = CTAS['Close'].pct_change()
CSCO = pd.read_csv('CSCO.csv'); CSCO['pct'] = CSCO['Close'].pct_change()
CTSH = pd.read_csv('CTSH.csv'); CTSH['pct'] = CTSH['Close'].pct_change()
CMCSA = pd.read_csv('CMCSA.csv'); CMCSA['pct'] = CMCSA['Close'].pct_change()
CPRT = pd.read_csv('CPRT.csv'); CPRT['pct'] = CPRT['Close'].pct_change()
COST = pd.read_csv('COST.csv'); COST['pct'] = COST['Close'].pct_change()
CRWD = pd.read_csv('CRWD.csv'); CRWD['pct'] = CRWD['Close'].pct_change()
CSX = pd.read_csv('CSX.csv'); CSX['pct'] = CSX['Close'].pct_change()
DDOG = pd.read_csv('DDOG.csv'); DDOG['pct'] = DDOG['Close'].pct_change()
DXCM = pd.read_csv('DXCM.csv'); DXCM['pct'] = DXCM['Close'].pct_change()
DOCU = pd.read_csv('DOCU.csv'); DOCU['pct'] = DOCU['Close'].pct_change()
DLTR = pd.read_csv('DLTR.csv'); DLTR['pct'] = DLTR['Close'].pct_change()
EBAY = pd.read_csv('EBAY.csv'); EBAY['pct'] = EBAY['Close'].pct_change()
EA = pd.read_csv('EA.csv'); EA['pct'] = EA['Close'].pct_change()
EXC = pd.read_csv('EXC.csv'); EXC['pct'] = EXC['Close'].pct_change()
FAST = pd.read_csv('FAST.csv'); FAST['pct'] = FAST['Close'].pct_change()
FISV = pd.read_csv('FISV.csv'); FISV['pct'] = FISV['Close'].pct_change()
FTNT = pd.read_csv('FTNT.csv'); FTNT['pct'] = FTNT['Close'].pct_change()
GILD = pd.read_csv('GILD.csv'); GILD['pct'] = GILD['Close'].pct_change()
HON = pd.read_csv('HON.csv'); HON['pct'] = HON['Close'].pct_change()
IDXX = pd.read_csv('IDXX.csv'); IDXX['pct'] = IDXX['Close'].pct_change()
ILMN = pd.read_csv('ILMN.csv'); ILMN['pct'] = ILMN['Close'].pct_change()
INTC = pd.read_csv('INTC.csv'); INTC['pct'] = INTC['Close'].pct_change()
INTU = pd.read_csv('INTU.csv'); INTU['pct'] = INTU['Close'].pct_change()
ISRG = pd.read_csv('ISRG.csv'); ISRG['pct'] = ISRG['Close'].pct_change()
JD = pd.read_csv('JD.csv'); JD['pct'] = JD['Close'].pct_change()
KDP = pd.read_csv('KDP.csv'); KDP['pct'] = KDP['Close'].pct_change()
KLAC = pd.read_csv('KLAC.csv'); KLAC['pct'] = KLAC['Close'].pct_change()
KHC = pd.read_csv('KHC.csv'); KHC['pct'] = KHC['Close'].pct_change()
LRCX = pd.read_csv('LRCX.csv'); LRCX['pct'] = LRCX['Close'].pct_change()
LCID = pd.read_csv('LCID.csv'); LCID['pct'] = LCID['Close'].pct_change()
LULU = pd.read_csv('LULU.csv'); LULU['pct'] = LULU['Close'].pct_change()
MAR = pd.read_csv('MAR.csv'); MAR['pct'] = MAR['Close'].pct_change()
MRVL = pd.read_csv('MRVL.csv'); MRVL['pct'] = MRVL['Close'].pct_change()
MTCH = pd.read_csv('MTCH.csv'); MTCH['pct'] = MTCH['Close'].pct_change()
MELI = pd.read_csv('MELI.csv'); MELI['pct'] = MELI['Close'].pct_change()
META = pd.read_csv('META.csv'); META['pct'] = META['Close'].pct_change()
MCHP = pd.read_csv('MCHP.csv'); MCHP['pct'] = MCHP['Close'].pct_change()
MU = pd.read_csv('MU.csv'); MU['pct'] = MU['Close'].pct_change()
MSFT = pd.read_csv('MSFT.csv'); MSFT['pct'] = MSFT['Close'].pct_change()
MRNA = pd.read_csv('MRNA.csv'); MRNA['pct'] = MRNA['Close'].pct_change()
MDLZ = pd.read_csv('MDLZ.csv'); MDLZ['pct'] = MDLZ['Close'].pct_change()
MNST = pd.read_csv('MNST.csv'); MNST['pct'] = MNST['Close'].pct_change()
NTES = pd.read_csv('NTES.csv'); NTES['pct'] = NTES['Close'].pct_change()
NFLX = pd.read_csv('NFLX.csv'); NFLX['pct'] = NFLX['Close'].pct_change()
NVDA = pd.read_csv('NVDA.csv'); NVDA['pct'] = NVDA['Close'].pct_change()
NXPI = pd.read_csv('NXPI.csv'); NXPI['pct'] = NXPI['Close'].pct_change()
ORLY = pd.read_csv('ORLY.csv'); ORLY['pct'] = ORLY['Close'].pct_change()
OKTA = pd.read_csv('OKTA.csv'); OKTA['pct'] = OKTA['Close'].pct_change()
ODFL = pd.read_csv('ODFL.csv'); ODFL['pct'] = ODFL['Close'].pct_change()
PCAR = pd.read_csv('PCAR.csv'); PCAR['pct'] = PCAR['Close'].pct_change()
PANW = pd.read_csv('PANW.csv'); PANW['pct'] = PANW['Close'].pct_change()
PAYX = pd.read_csv('PAYX.csv'); PAYX['pct'] = PAYX['Close'].pct_change()
PYPL = pd.read_csv('PYPL.csv'); PYPL['pct'] = PYPL['Close'].pct_change()
PEP = pd.read_csv('PEP.csv'); PEP['pct'] = PEP['Close'].pct_change()
PDD = pd.read_csv('PDD.csv'); PDD['pct'] = PDD['Close'].pct_change()
QCOM = pd.read_csv('QCOM.csv'); QCOM['pct'] = QCOM['Close'].pct_change()
REGN = pd.read_csv('REGN.csv'); REGN['pct'] = REGN['Close'].pct_change()
ROST = pd.read_csv('ROST.csv'); ROST['pct'] = ROST['Close'].pct_change()
SGEN = pd.read_csv('SGEN.csv'); SGEN['pct'] = SGEN['Close'].pct_change()
SIRI = pd.read_csv('SIRI.csv'); SIRI['pct'] = SIRI['Close'].pct_change()
SWKS = pd.read_csv('SWKS.csv'); SWKS['pct'] = SWKS['Close'].pct_change()
SPLK = pd.read_csv('SPLK.csv'); SPLK['pct'] = SPLK['Close'].pct_change()
SBUX = pd.read_csv('SBUX.csv'); SBUX['pct'] = SBUX['Close'].pct_change()
SNPS = pd.read_csv('SNPS.csv'); SNPS['pct'] = SNPS['Close'].pct_change()
TMUS = pd.read_csv('TMUS.csv'); TMUS['pct'] = TMUS['Close'].pct_change()
TSLA = pd.read_csv('TSLA.csv'); TSLA['pct'] = TSLA['Close'].pct_change()
TXN = pd.read_csv('TXN.csv'); TXN['pct'] = TXN['Close'].pct_change()
VRSN = pd.read_csv('VRSN.csv'); VRSN['pct'] = VRSN['Close'].pct_change()
VRSK = pd.read_csv('VRSK.csv'); VRSK['pct'] = VRSK['Close'].pct_change()
VRTX = pd.read_csv('VRTX.csv'); VRTX['pct'] = VRTX['Close'].pct_change()
WBA = pd.read_csv('WBA.csv'); WBA['pct'] = WBA['Close'].pct_change()
WDAY = pd.read_csv('WDAY.csv'); WDAY['pct'] = WDAY['Close'].pct_change()
XEL = pd.read_csv('XEL.csv'); XEL['pct'] = XEL['Close'].pct_change()
ZM = pd.read_csv('ZM.csv'); ZM['pct'] = ZM['Close'].pct_change()
ZS = pd.read_csv('ZS.csv'); ZS['pct'] = ZS['Close'].pct_change()

ATVI_pct = ATVI['pct'].to_numpy(); ATVI_pct = np.delete(ATVI_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,ATVI_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,ATVI_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

ADBE_pct = ADBE['pct'].to_numpy(); ADBE_pct = np.delete(ADBE_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,ADBE_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,ADBE_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

ADP_pct = ADP['pct'].to_numpy(); ADP_pct = np.delete(ADP_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,ADP_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,ADP_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

ABNB_pct = ABNB['pct'].to_numpy(); ABNB_pct = np.delete(ABNB_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,ABNB_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,ABNB_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

ALGN_pct = ALGN['pct'].to_numpy(); ALGN_pct = np.delete(ALGN_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,ALGN_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,ALGN_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

GOOGL_pct = GOOGL['pct'].to_numpy(); GOOGL_pct = np.delete(GOOGL_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,GOOGL_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,GOOGL_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

AAPL_pct = AAPL['pct'].to_numpy(); AAPL_pct = np.delete(AAPL_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,AAPL_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,AAPL_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

GOOG_pct = GOOG['pct'].to_numpy(); GOOG_pct = np.delete(GOOG_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,GOOG_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,GOOG_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

AMZN_pct = AMZN['pct'].to_numpy(); AMZN_pct = np.delete(AMZN_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,AMZN_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,AMZN_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

AMD_pct = AMD['pct'].to_numpy(); AMD_pct = np.delete(AMD_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,AMD_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,AMD_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

AEP_pct = AEP['pct'].to_numpy(); AEP_pct = np.delete(AEP_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,AEP_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,AEP_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

AMGN_pct = AMGN['pct'].to_numpy(); AMGN_pct = np.delete(AMGN_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,AMGN_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,AMGN_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

ADI_pct = ADI['pct'].to_numpy(); ADI_pct = np.delete(ADI_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,ADI_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,ADI_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

ANSS_pct = ANSS['pct'].to_numpy(); ANSS_pct = np.delete(ANSS_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,ANSS_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,ANSS_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

AAPL_pct = AAPL['pct'].to_numpy(); AAPL_pct = np.delete(AAPL_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,AAPL_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,AAPL_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

AMAT_pct = AMAT['pct'].to_numpy(); AMAT_pct = np.delete(AMAT_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,AMAT_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,AMAT_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

ASML_pct = ASML['pct'].to_numpy(); ASML_pct = np.delete(ASML_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,ASML_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,ASML_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

AZN_pct = AZN['pct'].to_numpy(); AZN_pct = np.delete(AZN_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,AZN_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,AZN_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

TEAM_pct = TEAM['pct'].to_numpy(); TEAM_pct = np.delete(TEAM_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,TEAM_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,TEAM_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

ADSK_pct = ADSK['pct'].to_numpy(); ADSK_pct = np.delete(ADSK_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,ADSK_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,ADSK_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

BIDU_pct = BIDU['pct'].to_numpy(); BIDU_pct = np.delete(BIDU_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,BIDU_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,BIDU_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

BKNG_pct = BKNG['pct'].to_numpy(); BKNG_pct = np.delete(BKNG_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,BKNG_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,BKNG_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

AVGO_pct = AVGO['pct'].to_numpy(); AVGO_pct = np.delete(AVGO_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,AZN_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,AVGO_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

CDNS_pct = CDNS['pct'].to_numpy(); CDNS_pct = np.delete(CDNS_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,CDNS_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,CDNS_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

CHTR_pct = CHTR['pct'].to_numpy(); CHTR_pct = np.delete(CHTR_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,CHTR_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,CHTR_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

CTAS_pct = CTAS['pct'].to_numpy(); CTAS_pct = np.delete(CTAS_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,CTAS_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,CTAS_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

CSCO_pct = CSCO['pct'].to_numpy(); CSCO_pct = np.delete(CSCO_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,CSCO_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,CSCO_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

CTSH_pct = CTSH['pct'].to_numpy(); CTSH_pct = np.delete(CTSH_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,CTSH_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,CTSH_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

CMCSA_pct = CMCSA['pct'].to_numpy(); CMCSA_pct = np.delete(CMCSA_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,CMCSA_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,CMCSA_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

CPRT_pct = CPRT['pct'].to_numpy(); CPRT_pct = np.delete(CPRT_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,CPRT_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,CPRT_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

COST_pct = COST['pct'].to_numpy(); COST_pct = np.delete(COST_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,CMCSA_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,COST_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

CRWD_pct = CRWD['pct'].to_numpy(); CRWD_pct = np.delete(CRWD_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,CRWD_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,CRWD_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

CSX_pct = CSX['pct'].to_numpy(); CSX_pct = np.delete(CSX_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,CSX_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,CSX_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

DDOG_pct = DDOG['pct'].to_numpy(); DDOG_pct = np.delete(DDOG_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,DDOG_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,DDOG_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

DXCM_pct = DXCM['pct'].to_numpy(); DXCM_pct = np.delete(DXCM_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,DXCM_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,DXCM_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

DOCU_pct = DOCU['pct'].to_numpy(); DOCU_pct = np.delete(DOCU_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,DOCU_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,DOCU_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

DLTR_pct = DLTR['pct'].to_numpy(); DLTR_pct = np.delete(DLTR_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,DLTR_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,DLTR_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

EBAY_pct = EBAY['pct'].to_numpy(); EBAY_pct = np.delete(EBAY_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,EBAY_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,EBAY_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

EA_pct = EA['pct'].to_numpy(); EA_pct = np.delete(EA_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,EA_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,EA_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

EXC_pct = EXC['pct'].to_numpy(); EXC_pct = np.delete(EXC_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,EXC_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,EXC_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

FAST_pct = FAST['pct'].to_numpy(); FAST_pct = np.delete(FAST_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,FAST_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,FAST_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

FISV_pct = FISV['pct'].to_numpy(); FISV_pct = np.delete(FISV_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,FISV_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,FISV_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

FTNT_pct = FTNT['pct'].to_numpy(); FTNT_pct = np.delete(FTNT_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,FTNT_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,FTNT_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

GILD_pct = GILD['pct'].to_numpy(); GILD_pct = np.delete(GILD_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,GILD_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,GILD_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

HON_pct = HON['pct'].to_numpy(); HON_pct = np.delete(HON_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,HON_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,HON_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

IDXX_pct = IDXX['pct'].to_numpy(); IDXX_pct = np.delete(IDXX_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,IDXX_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,IDXX_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

ILMN_pct = ILMN['pct'].to_numpy(); ILMN_pct = np.delete(ILMN_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,ILMN_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,ILMN_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

INTC_pct = INTC['pct'].to_numpy(); INTC_pct = np.delete(INTC_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,INTC_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,INTC_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

INTU_pct = INTU['pct'].to_numpy(); INTU_pct = np.delete(INTU_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,INTU_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,INTU_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

ISRG_pct = ISRG['pct'].to_numpy(); ISRG_pct = np.delete(ISRG_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,ISRG_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,ISRG_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

JD_pct = JD['pct'].to_numpy(); JD_pct = np.delete(JD_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,JD_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,JD_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

KDP_pct = KDP['pct'].to_numpy(); KDP_pct = np.delete(KDP_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,KDP_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,KDP_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

ISRG_pct = ISRG['pct'].to_numpy(); ISRG_pct = np.delete(ISRG_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,ISRG_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,ISRG_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

KLAC_pct = KLAC['pct'].to_numpy(); KLAC_pct = np.delete(KLAC_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,KLAC_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,KLAC_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

KHC_pct = KHC['pct'].to_numpy(); KHC_pct = np.delete(KHC_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,KHC_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,KHC_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

LRCX_pct = LRCX['pct'].to_numpy(); LRCX_pct = np.delete(LRCX_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,LRCX_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,LRCX_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

LCID_pct = LCID['pct'].to_numpy(); LCID_pct = np.delete(LCID_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,LCID_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,LCID_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

LULU_pct = LULU['pct'].to_numpy(); LULU_pct = np.delete(LULU_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,LULU_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,LULU_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

MAR_pct = MAR['pct'].to_numpy(); MAR_pct = np.delete(MAR_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,MAR_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,MAR_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

MRVL_pct = MRVL['pct'].to_numpy(); MRVL_pct = np.delete(MRVL_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,MRVL_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,MRVL_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

MTCH_pct = MTCH['pct'].to_numpy(); MTCH_pct = np.delete(MTCH_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,MTCH_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,MTCH_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

MELI_pct = MELI['pct'].to_numpy(); MELI_pct = np.delete(MELI_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,MELI_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,MELI_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

META_pct = META['pct'].to_numpy(); META_pct = np.delete(META_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,META_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,META_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

MCHP_pct = MCHP['pct'].to_numpy(); MCHP_pct = np.delete(MCHP_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,MCHP_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,MCHP_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

MU_pct = MU['pct'].to_numpy(); MU_pct = np.delete(MU_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,MU_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,MU_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

MSFT_pct = MSFT['pct'].to_numpy(); MSFT_pct = np.delete(MSFT_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,MSFT_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,MSFT_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

MRNA_pct = MRNA['pct'].to_numpy(); MRNA_pct = np.delete(MRNA_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,MRNA_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,MRNA_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

MDLZ_pct = MDLZ['pct'].to_numpy(); MDLZ_pct = np.delete(MDLZ_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,MDLZ_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,MDLZ_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

MNST_pct = MNST['pct'].to_numpy(); MNST_pct = np.delete(MNST_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,MNST_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,MNST_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

NTES_pct = NTES['pct'].to_numpy(); NTES_pct = np.delete(NTES_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,NTES_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,NTES_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

NFLX_pct = NFLX['pct'].to_numpy(); NFLX_pct = np.delete(NFLX_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,NFLX_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,NFLX_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

NVDA_pct = NVDA['pct'].to_numpy(); NVDA_pct = np.delete(NVDA_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,NVDA_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,NVDA_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

NXPI_pct = NXPI['pct'].to_numpy(); NXPI_pct = np.delete(NXPI_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,NXPI_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,NXPI_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

ORLY_pct = ORLY['pct'].to_numpy(); ORLY_pct = np.delete(ORLY_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,ORLY_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,ORLY_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

OKTA_pct = OKTA['pct'].to_numpy(); OKTA_pct = np.delete(OKTA_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,OKTA_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,OKTA_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

ODFL_pct = ODFL['pct'].to_numpy(); ODFL_pct = np.delete(ODFL_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,ODFL_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,ODFL_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

PCAR_pct = PCAR['pct'].to_numpy(); PCAR_pct = np.delete(PCAR_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,PCAR_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,PCAR_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

PANW_pct = PANW['pct'].to_numpy(); PANW_pct = np.delete(PANW_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,PANW_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,PANW_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

PAYX_pct = PAYX['pct'].to_numpy(); PAYX_pct = np.delete(PAYX_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,PAYX_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,PAYX_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

PYPL_pct = PYPL['pct'].to_numpy(); PYPL_pct = np.delete(PYPL_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,PYPL_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,PYPL_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

PEP_pct = PEP['pct'].to_numpy(); PEP_pct = np.delete(PEP_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,PEP_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,PEP_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

PDD_pct = PDD['pct'].to_numpy(); PDD_pct = np.delete(PDD_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,PDD_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,PDD_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

QCOM_pct = QCOM['pct'].to_numpy(); QCOM_pct = np.delete(QCOM_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,QCOM_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,QCOM_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

ROST_pct = ROST['pct'].to_numpy(); ROST_pct = np.delete(ROST_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,ROST_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,ROST_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

SGEN_pct = SGEN['pct'].to_numpy(); SGEN_pct = np.delete(SGEN_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,SGEN_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,SGEN_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

SIRI_pct = SIRI['pct'].to_numpy(); SIRI_pct = np.delete(SIRI_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,SIRI_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,SIRI_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

SWKS_pct = SWKS['pct'].to_numpy(); SWKS_pct = np.delete(SWKS_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,SWKS_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,SWKS_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

SPLK_pct = SPLK['pct'].to_numpy(); SPLK_pct = np.delete(SPLK_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,SPLK_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,SPLK_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

SBUX_pct = SBUX['pct'].to_numpy(); SBUX_pct = np.delete(SBUX_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,SBUX_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,SBUX_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

SNPS_pct = SNPS['pct'].to_numpy(); SNPS_pct = np.delete(SNPS_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,SNPS_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,SNPS_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

TMUS_pct = TMUS['pct'].to_numpy(); TMUS_pct = np.delete(TMUS_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,TMUS_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,TMUS_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

TSLA_pct = TSLA['pct'].to_numpy(); TSLA_pct = np.delete(TSLA_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,TSLA_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,TSLA_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

TXN_pct = TXN['pct'].to_numpy(); TXN_pct = np.delete(TXN_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,TXN_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,TXN_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

VRSN_pct = VRSN['pct'].to_numpy(); VRSN_pct = np.delete(VRSN_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,VRSN_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,VRSN_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

VRSK_pct = VRSK['pct'].to_numpy(); VRSK_pct = np.delete(VRSK_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,VRSK_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,VRSK_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

VRTX_pct = VRTX['pct'].to_numpy(); VRTX_pct = np.delete(VRTX_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,VRTX_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,VRTX_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

WBA_pct = WBA['pct'].to_numpy(); WBA_pct = np.delete(WBA_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,WBA_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,WBA_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

WDAY_pct = WDAY['pct'].to_numpy(); WDAY_pct = np.delete(WDAY_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,WDAY_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,WDAY_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

XEL_pct = XEL['pct'].to_numpy(); XEL_pct = np.delete(XEL_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,XEL_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,XEL_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

ZM_pct = ZM['pct'].to_numpy(); ZM_pct = np.delete(ZM_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,ZM_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,ZM_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#############################################################################

ZS_pct = ZS['pct'].to_numpy(); ZS_pct = np.delete(ZS_pct,0)
QQQ_pct = QQQ['pct'].to_numpy(); QQQ_pct = np.delete(QQQ_pct,0)

plt.plot(QQQ_pct,ZS_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")

slope, intercept, r_value, p_value, std_err = linregress(QQQ_pct,ZS_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

data = [QQQ['pct'],
ATVI['pct'],
ADBE['pct'],
ADP['pct'],
ABNB['pct'],
ALGN['pct'],
GOOGL['pct'],
GOOG['pct'],
AMZN['pct'],
AMD['pct'],
AEP['pct'],
AMGN['pct'],
ADI['pct'],
ANSS['pct'],
AAPL['pct'],
AMAT['pct'],
ASML['pct'],
AZN['pct'],
TEAM['pct'],
ADSK['pct'],
BIDU['pct'],
BKNG['pct'],
AVGO['pct'],
CDNS['pct'],
CHTR['pct'],
CTAS['pct'],
CSCO['pct'],
CTSH['pct'],
CMCSA['pct'],
CPRT['pct'],
COST['pct'],
CRWD['pct'],
CSX['pct'],
DDOG['pct'],
DXCM['pct'],
DOCU['pct'],
DLTR['pct'],
EBAY['pct'],
EA['pct'],
EXC['pct'],
FAST['pct'],
FISV['pct'],
FTNT['pct'],
GILD['pct'],
HON['pct'],
IDXX['pct'],
ILMN['pct'],
INTC['pct'],
INTU['pct'],
ISRG['pct'],
JD['pct'],
KDP['pct'],
KLAC['pct'],
KHC['pct'],
LRCX['pct'],
LCID['pct'],
LULU['pct'],
MAR['pct'],
MRVL['pct'],
MTCH['pct'],
MELI['pct'],
META['pct'],
MCHP['pct'],
MU['pct'],
MSFT['pct'],
MRNA['pct'],
MDLZ['pct'],
MNST['pct'],
NTES['pct'],
NFLX['pct'],
NVDA['pct'],
NXPI['pct'],
ORLY['pct'],
OKTA['pct'],
ODFL['pct'],
PCAR['pct'],
PANW['pct'],
PAYX['pct'],
PYPL['pct'],
PEP['pct'],
PDD['pct'],
QCOM['pct'],
REGN['pct'],
ROST['pct'],
SGEN['pct'],
SIRI['pct'],
SWKS['pct'],
SPLK['pct'],
SBUX['pct'],
SNPS['pct'],
TMUS['pct'],
TSLA['pct'],
TXN['pct'],
VRSN['pct'],
VRSK['pct'],
VRTX['pct'],
WBA['pct'],
WDAY['pct'],
XEL['pct'],
ZM['pct'],
ZS['pct']]

headers = ['QQQ',
'ATVI',
'ADBE',
'ADP',
'ABNB',
'ALGN',
'GOOGL',
'GOOG',
'AMZN',
'AMD',
'AEP',
'AMGN',
'ADI',
'ANSS',
'AAPL',
'AMAT',
'ASML ',
'AZN ',
'TEAM',
'ADSK',
'BIDU',
'BKNG' ,
'AVGO' ,
'CDNS',
'CHTR',
'CTAS',
'CSCO',
'CTSH',
'CMCSA',
'CPRT',
'COST',
'CRWD',
'CSX',
'DDOG',
'DXCM',
'DOCU',
'DLTR',
'EBAY',
'EA',
'EXC',
'FAST',
'FISV',
'FTNT',
'GILD',
'HON',
'IDXX',
'ILMN',
'INTC',
'INTU',
'ISRG',
'JD',
'KDP',
'KLAC',
'KHC',
'LRCX',
'LCID',
'LULU',
'MAR',
'MRVL',
'MTCH',
'MELI',
'META',
'MCHP',
'MU',
'MSFT',
'MRNA',
'MDLZ',
'MNST',
'NTES',
'NFLX',
'NVDA',
'NXPI',
'ORLY',
'OKTA',
'ODFL',
'PCAR',
'PANW',
'PAYX',
'PYPL',
'PEP',
'PDD',
'QCOM',
'REGN',
'ROST',
'SGEN',
'SIRI',
'SWKS',
'SPLK',
'SBUX',
'SNPS',
'TMUS',
'TSLA',
'TXN',
'VRSN',
'VRSK',
'VRTX',
'WBA',
'WDAY',
'XEL',
'ZM',
'ZS']

pct_frame = pd.concat(data,axis=1,keys=headers)
corr_frame = pct_frame.corr()
print(corr_frame)

seaborn.heatmap(corr_frame,cmap="RdYlGn",xticklabels=1,yticklabels=1)
plt.xticks(fontsize=3)
plt.yticks(fontsize=3)
plt.show()
