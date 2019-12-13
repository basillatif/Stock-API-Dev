stockdat = read.csv("/Users/RebeccaFang/Desktop/Stock-API-Dev/AMZN_data.csv")

plot(stockdat$Date,stockdat$Adj..Close, ylab="Price",xlab="Date")
real1<-lines(stockdat$Date,stockdat$Adj..Close,col="blue",type="l")
real2<-lines(stockdat$Date,stockdat$Adj..Open,col= "red",type = "l",lwd=.5)


library(quantmod)
library(xts)
library(rvest)
library(tidyverse)
library(stringr)
library(forcats)
library(lubridate)
library(plotly)
library(corrplot)
library(dplyr)
library(PerformanceAnalytics)


getSymbols("AMZN",from="2012-11-01",to="2016-12-31")
AMZN_log_returns<-AMZN%>%Ad()%>%dailyReturn(type='log')
AMZN_mean_log<-mean(AMZN_log_returns)
mean_log<-round(AMZN_mean_log,4)
AMZN_sd_Log<-sd(AMZN_log_returns)
sd_log<-round(AMZN_sd_Log,4)
graphic1<-data.frame(mean_log,sd_log)

rownames(graphic1)<-c("AMZN")
colnames(graphic1)<-c("Mean_Log_Return", "Sd_Log_Return")

xlab<-list(title="Reward",titlefont=F)
ylab<-list(title="Risk", titlefont=F)

plot_ly(x=graphic1[,1],y=graphic1[,2],text=rownames(graphic1),type='scatter',mode="markers",marker=list(color=c("black","blue","red","grey","green")))%>%layout(title="Risk v Reward",xaxis=xlab,yaxis=ylab)


AMZN%>%Ad()%>%chartSeries()
AMZN%>%chartSeries(TA='addBBands();addBBands(draw="p");addVo();addMACD()',subset='2016')

probs<-c(0.005,0.025,0.25,0.5,0.75,0.975,0.995)

AMZN_dist<-AMZN_log_returns%>%quantile(probs=probs,na.rm=TRUE)
AMZN_mean<-mean(AMZN_log_returns,na.rm=TRUE)
AMZN_sd<-sd(AMZN_log_returns,na.rm=TRUE)


AMZN_mean%>%exp() 




#random walk: Rooted in past performance is not an indicator of future results. Price fluctuations can not be predicted with accuracy

mu<-AMZN_mean_log
sig<-AMZN_sd_Log
testsim<-rep(NA,250*1)


#generate random daily exponent increase rate using AMZN's mean and sd log returns

#one year 250 trading days, simulate for 4 years 
# 4*250 trading days

price<-rep(NA,250*1)

#most recent price
price[1]<-as.numeric(AMZN$AMZN.Adjusted[length(AMZN$AMZN.Adjusted),])

#start simulating prices

for(i in 2:length(testsim)){
  price[i]<-price[i-1]*exp(rnorm(1,mu,sig))
}

random_data<-cbind(price,1:(250*1))
colnames(random_data)<-c("Price","Day")
random_data<-as.data.frame(random_data)

random_data%>%ggplot(aes(Day,Price))+geom_line()+labs(title="AMZNe (AMZN) price simulation for 2017")+theme_bw()
#monte carlo simulation: incredibly useful forecasting tool to predict outcomes of events with many random variables


N<-500
mc_matrix<-matrix(nrow=250*1,ncol=N)
mc_matrix[1,1]<-as.numeric(AMZN$AMZN.Adjusted[length(AMZN$AMZN.Adjusted),])

for(j in 1:ncol(mc_matrix)){
  mc_matrix[1,j]<-as.numeric(AMZN$AMZN.Adjusted[length(AMZN$AMZN.Adjusted),])
  for(i in 2:nrow(mc_matrix)){
    mc_matrix[i,j]<-mc_matrix[i-1,j]*exp(rnorm(1,mu,sig))
  }
}

name<-str_c("Sim ",seq(1,500))
name<-c("Day",name)

final_mat<-cbind(1:(250*1),mc_matrix)
final_mat<-as.tibble(final_mat)
colnames(final_mat)<-name

dim(final_mat) 

final_mat%>%gather("Simulation","Price",2:501)%>%ggplot(aes(x=Day,y=Price,Group=Simulation))+geom_line(alpha=0.2)+labs(title="AMZNe Stock (AMZN): 500 Monte Carlo Simulations for 2017")+theme_bw()

#is it likely? Check the confidence interval

final_mat[250*1,-1]%>%as.numeric()%>%quantile(probs=probs)

#/////////////////
library(quantmod)
library(xts)
library(rvest)
library(tidyverse)
library(stringr)
library(forcats)
library(lubridate)
library(plotly)
library(corrplot)
library(dplyr)
library(PerformanceAnalytics)
getSymbols("AMZN",from="2017-01-01",to="2017-12-31")
AMZN_log_returns1<-AMZN%>%Ad()%>%dailyReturn(type='log')
AMZN_mean_log1<-mean(AMZN_log_returns1)
mean_log1<-round(AMZN_mean_log1,4)
AMZN_sd_Log1<-sd(AMZN_log_returns1)
sd_log1<-round(AMZN_sd_Log1,4)
graphic2<-data.frame(mean_log1,sd_log1)
rownames(graphic2)<-c("AMZN")
colnames(graphic2)<-c("Mean_Log_Return1", "Sd_Log_Return1")

xlab<-list(title="Reward",titlefont=F)
ylab<-list(title="Risk", titlefont=F)

plot_ly(x=graphic2[,1],y=graphic2[,2],text=rownames(graphic2),type='scatter',mode="markers",marker=list(color=c("black","blue","red","grey","green")))%>%layout(title="Risk v Reward",xaxis=xlab,yaxis=ylab)

AMZN%>%Ad()%>%chartSeries()
AMZN%>%chartSeries(TA='addBBands();addBBands(draw="p");addVo();addMACD()',subset='2017')

probs<-c(0.005,0.025,0.25,0.5,0.75,0.975,0.995)

AMZN_dist1<-AMZN_log_returns1%>%quantile(probs=probs,na.rm=TRUE)
AMZN_mean1<-mean(AMZN_log_returns1,na.rm=TRUE)
AMZN_sd1<-sd(AMZN_log_returns1,na.rm=TRUE)


AMZN_mean1%>%exp() 

#random_data1<-getSymbols("AMZN2",from="2017-01-01",to="2017-12-31")
#random_data1%>%ggplot(aes(Day,Price))+geom_line()+labs(title="AMZNe (AMZN1) real price for 2017")+theme_bw()