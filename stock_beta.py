# Import libraries
import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn
from scipy.stats import linregress

# Download the stock data from Yahoo! Finance
SPY = yf.download('SPY',start='2021-01-01',end='2021-12-31',interval='1d')
IT = yf.download('IT',start='2021-01-01',end='2021-12-31',interval='1d')
FTNT = yf.download('FTNT',start='2021-01-01',end='2021-12-31',interval='1d')
NVDA = yf.download('NVDA',start='2021-01-01',end='2021-12-31',interval='1d')
NUE = yf.download('NUE',start='2021-01-01',end='2021-12-31',interval='1d')
FANG = yf.download('FANG',start='2021-01-01',end='2021-12-31',interval='1d')
MRO = yf.download('MRO',start='2021-01-01',end='2021-12-31',interval='1d')
F = yf.download('F',start='2021-01-01',end='2021-12-31',interval='1d')
DVN = yf.download('DVN',start='2021-01-01',end='2021-12-31',interval='1d')
UPST = yf.download('UPST',start='2021-01-01',end='2021-12-31',interval='1d')
MRNA = yf.download('MRNA',start='2021-01-01',end='2021-12-31',interval='1d')
VRTV = yf.download('VRTV',start='2021-01-01',end='2021-12-31',interval='1d')
CAR = yf.download('CAR',start='2021-01-01',end='2021-12-31',interval='1d')
PRTA = yf.download('PRTA',start='2021-01-01',end='2021-12-31',interval='1d')
AMEH = yf.download('AMEH',start='2021-01-01',end='2021-12-31',interval='1d')
OAS = yf.download('OAS',start='2021-01-01',end='2021-12-31',interval='1d')
DDS = yf.download('DDS',start='2021-01-01',end='2021-12-31',interval='1d')
CUBI = yf.download('CUBI',start='2021-01-01',end='2021-12-31',interval='1d')
CPE = yf.download('CPE',start='2021-01-01',end='2021-12-31',interval='1d')
IDT = yf.download('IDT',start='2021-01-01',end='2021-12-31',interval='1d')
BNTX = yf.download('BNTX',start='2021-01-01',end='2021-12-31',interval='1d')

# Save each stock data into a CSV file
SPY.to_csv('spy.csv')
IT.to_csv('it.csv')
FTNT.to_csv('ftnt.csv')
NVDA.to_csv('nvda.csv')
NUE.to_csv('nue.csv')
FANG.to_csv('fang.csv')
MRO.to_csv('mro.csv')
F.to_csv('f.csv')
DVN.to_csv('dvn.csv')
UPST.to_csv('upst.csv')
MRNA.to_csv('mrna.csv')
VRTV.to_csv('vrtv.csv')
CAR.to_csv('car.csv')
PRTA.to_csv('prta.csv')
AMEH.to_csv('ameh.csv')
OAS.to_csv('oas.csv')
DDS.to_csv('dds.csv')
CUBI.to_csv('cubi.csv')
CPE.to_csv('cpe.csv')
IDT.to_csv('idt.csv')
BNTX.to_csv('bntx.csv')

# Read each CSV file and calculate the percent changes between each day for beta values and correlations
# In the plot code, the first value of each percent change is deleted since it will read NaN due to not having a number before it to calculate a value
IT = pd.read_csv('it.csv'); IT['pct'] = IT['Close'].pct_change()
FTNT = pd.read_csv('ftnt.csv'); FTNT['pct'] = FTNT['Close'].pct_change()
NVDA = pd.read_csv('nvda.csv'); NVDA['pct'] = NVDA['Close'].pct_change()
NUE = pd.read_csv('nue.csv'); NUE['pct'] = NUE['Close'].pct_change()
FANG = pd.read_csv('fang.csv'); FANG['pct'] = FANG['Close'].pct_change()
MRO = pd.read_csv('mro.csv'); MRO['pct'] = MRO['Close'].pct_change()
F = pd.read_csv('f.csv'); F['pct'] = F['Close'].pct_change()
DVN = pd.read_csv('dvn.csv'); DVN['pct'] = DVN['Close'].pct_change()
UPST = pd.read_csv('upst.csv'); UPST['pct'] = UPST['Close'].pct_change()
MRNA = pd.read_csv('mrna.csv'); MRNA['pct'] = MRNA['Close'].pct_change()
VRTV = pd.read_csv('vrtv.csv'); VRTV['pct'] = VRTV['Close'].pct_change()
CAR = pd.read_csv('car.csv'); CAR['pct'] = CAR['Close'].pct_change()
PRTA = pd.read_csv('prta.csv'); PRTA['pct'] = PRTA['Close'].pct_change()
AMEH = pd.read_csv('ameh.csv'); AMEH['pct'] = AMEH['Close'].pct_change()
OAS = pd.read_csv('oas.csv'); OAS['pct'] = OAS['Close'].pct_change()
DDS = pd.read_csv('dds.csv'); DDS['pct'] = DDS['Close'].pct_change()
CUBI = pd.read_csv('cubi.csv'); CUBI['pct'] = CUBI['Close'].pct_change()
CPE = pd.read_csv('cpe.csv'); CPE['pct'] = CPE['Close'].pct_change()
IDT = pd.read_csv('idt.csv'); IDT['pct'] = IDT['Close'].pct_change()
BNTX = pd.read_csv('bntx.csv'); BNTX['pct'] = BNTX['Close'].pct_change()
SPY = pd.read_csv('spy.csv'); SPY['pct'] = SPY['Close'].pct_change()

# Plot for beta values, correlations, and linear regressions

#################################################################################

it_pct = IT['pct'].to_numpy(); it_pct = np.delete(it_pct,0)
spy_pct = SPY['pct'].to_numpy(); spy_pct = np.delete(spy_pct,0)

plt.plot(spy_pct,it_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")
plt.title("IT vs. SPY")

slope, intercept, r_value, p_value, std_err = linregress(spy_pct,it_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#################################################################################

ftnt_pct = FTNT['pct'].to_numpy(); ftnt_pct = np.delete(ftnt_pct,0)
spy_pct = SPY['pct'].to_numpy(); spy_pct = np.delete(spy_pct,0)

plt.plot(spy_pct,ftnt_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")
plt.title("FTNT vs. SPY")

slope, intercept, r_value, p_value, std_err = linregress(spy_pct,ftnt_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()



#################################################################################

nvda_pct = NVDA['pct'].to_numpy(); nvda_pct = np.delete(nvda_pct,0)
spy_pct = SPY['pct'].to_numpy(); spy_pct = np.delete(spy_pct,0)

plt.plot(spy_pct,nvda_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")
plt.title("NVDA vs. SPY")

slope, intercept, r_value, p_value, std_err = linregress(spy_pct,nvda_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()


#################################################################################

nue_pct = NUE['pct'].to_numpy(); nue_pct = np.delete(nue_pct,0)
spy_pct = SPY['pct'].to_numpy(); spy_pct = np.delete(spy_pct,0)

plt.plot(spy_pct,nue_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")
plt.title("NUE vs. SPY")

slope, intercept, r_value, p_value, std_err = linregress(spy_pct,nue_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()



#################################################################################

fang_pct = FANG['pct'].to_numpy(); fang_pct = np.delete(fang_pct,0)
spy_pct = SPY['pct'].to_numpy(); spy_pct = np.delete(spy_pct,0)

plt.plot(spy_pct,fang_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")
plt.title("FANG vs. SPY")

slope, intercept, r_value, p_value, std_err = linregress(spy_pct,fang_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#################################################################################

mro_pct = MRO['pct'].to_numpy(); mro_pct = np.delete(mro_pct,0)
spy_pct = SPY['pct'].to_numpy(); spy_pct = np.delete(spy_pct,0)

plt.plot(spy_pct,mro_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")
plt.title("MRO vs. SPY")

slope, intercept, r_value, p_value, std_err = linregress(spy_pct,mro_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#################################################################################

f_pct = F['pct'].to_numpy(); f_pct = np.delete(f_pct,0)
spy_pct = SPY['pct'].to_numpy(); spy_pct = np.delete(spy_pct,0)

plt.plot(spy_pct,f_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")
plt.title("F vs. SPY")

slope, intercept, r_value, p_value, std_err = linregress(spy_pct,f_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#################################################################################

dvn_pct = DVN['pct'].to_numpy(); dvn_pct = np.delete(dvn_pct,0)
spy_pct = SPY['pct'].to_numpy(); spy_pct = np.delete(spy_pct,0)

plt.plot(spy_pct,dvn_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")
plt.title("DVN vs. SPY")

slope, intercept, r_value, p_value, std_err = linregress(spy_pct,dvn_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#################################################################################

upst_pct = UPST['pct'].to_numpy(); upst_pct = np.delete(upst_pct,0)
spy_pct = SPY['pct'].to_numpy(); spy_pct = np.delete(spy_pct,0)

plt.plot(spy_pct,upst_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")
plt.title("UPST vs. SPY")

slope, intercept, r_value, p_value, std_err = linregress(spy_pct,upst_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#################################################################################

mrna_pct = MRNA['pct'].to_numpy(); mrna_pct = np.delete(mrna_pct,0)
spy_pct = SPY['pct'].to_numpy(); spy_pct = np.delete(spy_pct,0)

plt.plot(spy_pct,mrna_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")
plt.title("MRNA vs. SPY")

slope, intercept, r_value, p_value, std_err = linregress(spy_pct,mrna_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#################################################################################

vrtv_pct = VRTV['pct'].to_numpy(); vrtv_pct = np.delete(vrtv_pct,0)
spy_pct = SPY['pct'].to_numpy(); spy_pct = np.delete(spy_pct,0)

plt.plot(spy_pct,vrtv_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")
plt.title("VRTV vs. SPY")

slope, intercept, r_value, p_value, std_err = linregress(spy_pct,vrtv_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#################################################################################

car_pct = CAR['pct'].to_numpy(); car_pct = np.delete(car_pct,0)
spy_pct = SPY['pct'].to_numpy(); spy_pct = np.delete(spy_pct,0)

plt.plot(spy_pct,car_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")
plt.title("CAR vs. SPY")

slope, intercept, r_value, p_value, std_err = linregress(spy_pct,car_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#################################################################################

prta_pct = PRTA['pct'].to_numpy(); prta_pct = np.delete(prta_pct,0)
spy_pct = SPY['pct'].to_numpy(); spy_pct = np.delete(spy_pct,0)

plt.plot(spy_pct,prta_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")
plt.title("PRTA vs. SPY")

slope, intercept, r_value, p_value, std_err = linregress(spy_pct,prta_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#################################################################################

ameh_pct = AMEH['pct'].to_numpy(); ameh_pct = np.delete(ameh_pct,0)
spy_pct = SPY['pct'].to_numpy(); spy_pct = np.delete(spy_pct,0)

plt.plot(spy_pct,ameh_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")
plt.title("AMEH vs. SPY")

slope, intercept, r_value, p_value, std_err = linregress(spy_pct,ameh_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#################################################################################

oas_pct = OAS['pct'].to_numpy(); oas_pct = np.delete(oas_pct,0)
spy_pct = SPY['pct'].to_numpy(); spy_pct = np.delete(spy_pct,0)

plt.plot(spy_pct,oas_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")
plt.title("OAS vs. SPY")

slope, intercept, r_value, p_value, std_err = linregress(spy_pct,oas_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#################################################################################

dds_pct = DDS['pct'].to_numpy(); dds_pct = np.delete(dds_pct,0)
spy_pct = SPY['pct'].to_numpy(); spy_pct = np.delete(spy_pct,0)

plt.plot(spy_pct,dds_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")
plt.title("DDS vs. SPY")

slope, intercept, r_value, p_value, std_err = linregress(spy_pct,dds_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#################################################################################

cubi_pct = CUBI['pct'].to_numpy(); cubi_pct = np.delete(cubi_pct,0)
spy_pct = SPY['pct'].to_numpy(); spy_pct = np.delete(spy_pct,0)

plt.plot(spy_pct,cubi_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")
plt.title("CUBI vs. SPY")

slope, intercept, r_value, p_value, std_err = linregress(spy_pct,cubi_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#################################################################################

cpe_pct = CPE['pct'].to_numpy(); cpe_pct = np.delete(cpe_pct,0)
spy_pct = SPY['pct'].to_numpy(); spy_pct = np.delete(spy_pct,0)

plt.plot(spy_pct,cpe_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")
plt.title("CPE vs. SPY")

slope, intercept, r_value, p_value, std_err = linregress(spy_pct,cpe_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#################################################################################

idt_pct = IDT['pct'].to_numpy(); idt_pct = np.delete(idt_pct,0)
spy_pct = SPY['pct'].to_numpy(); spy_pct = np.delete(spy_pct,0)

plt.plot(spy_pct,idt_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")
plt.title("IDT vs. SPY")

slope, intercept, r_value, p_value, std_err = linregress(spy_pct,idt_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

#################################################################################

bntx_pct = BNTX['pct'].to_numpy(); bntx_pct = np.delete(bntx_pct,0)
spy_pct = SPY['pct'].to_numpy(); spy_pct = np.delete(spy_pct,0)

plt.plot(spy_pct,bntx_pct,'.')
plt.grid(True)
plt.xlabel("dS/S")
plt.ylabel("dE/E")
plt.title("BNTX vs. SPY")

slope, intercept, r_value, p_value, std_err = linregress(spy_pct,bntx_pct)
print('beta = ',slope)
print('correlation = ', r_value)
beta = slope
x = np.linspace(-0.1,0.1)
y = slope*x + intercept
plt.plot(x,y,'k')
plt.show()

# Create a heatmap to show how stocks correlate with each other and with the S&P500
data = [SPY['pct'],IT['pct'],FTNT['pct'],NVDA['pct'],NUE['pct'],FANG['pct'],MRO['pct'],F['pct'],DVN['pct'],
        UPST['pct'],MRNA['pct'],VRTV['pct'],CAR['pct'],PRTA['pct'],AMEH['pct'],OAS['pct'],DDS['pct'],CUBI['pct'],
        CPE['pct'],IDT['pct'],BNTX['pct']]
headers = ['SPY','IT','FTNT','NVDA','NUE','FANG','MRO','F','DVN','UPST','MRNA',
           'VRTV','CAR','PRTA','AMEH','OAS','DDS','CUBI','CPE','IDT','BNTX']

pct_frame = pd.concat(data,axis=1,keys=headers)
corr_frame = pct_frame.corr()
print(corr_frame)

seaborn.heatmap(corr_frame,cmap="RdYlGn")
plt.show()
