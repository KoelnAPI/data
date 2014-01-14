# Some analysis of employment data

# import dependencies
require(zoo)
require(ggplot2)
require(splines)
require(MASS)

unemployed.df <- read.csv("13211-03ir.csv")
unemployed.df$datum <- as.Date(as.character(unemployed.df$datum), format="%Y-%m-%d")

# create temperature time series using zoo package (for whatever reason)
unemployed.gesamt.zoo <- with(unemployed.df, zoo(gesamt, order.by = unemployed.df$datum))

# create temperature time series as ts object and analyse
unemployed.gesamt.ts <- ts(unemployed.df$gesamt, frequency=30, start=c(2000, 31))
gesamt.decomp <- decompose(unemployed.gesamt.ts)
plot(gesamt.decomp$trend)
gesamt.decomp.trend.df <- as.data.frame(matrix(gesamt.decomp$trend))
gesamt.decomp.trend.df$datum <- unemployed.df$datum
ggplot(data=gesamt.decomp.trend.df, aes(x=datum, y = V1)) +
  geom_line(weight=0.2) +
  ggtitle("Unemployment trend for Cologne (without seasonal effects)") +
  xlab("Date") +
  ylim(0, max(gesamt.decomp.trend.df$V1, na.rm=TRUE) + 500) +
  ylab("People unemployed")

# Time series plot of "gesamt"
ggplot(unemployed.df, aes(datum, gesamt)) + geom_line(size=0.2) + geom_smooth() + ggtitle("Unemployment data for Cologne") + xlab("Date") + ylab("Unemployed people")

# Time series plot of "maennlich"
ggplot(unemployed.df, aes(datum, maennlich)) + geom_line(size=0.2) + geom_smooth() + ggtitle("Unemployment data for Cologne - male") + xlab("Date") + ylab("Unemployed people")

# Time series plot of "weiblich"
ggplot(unemployed.df, aes(datum, weiblich)) + geom_line(size=0.2) + geom_smooth() + ggtitle("Unemployment data for Cologne - female") + xlab("Date") + ylab("Unemployed people")

# maennlich and weiblich
ggplot(unemployed.df, aes(datum)) +
  geom_line(aes(y=maennlich), color="blue") +
  geom_line(aes(y=weiblich), color="red") + 
  ggtitle("Unemployment data for Cologne - male and female") +
  xlab("Date") +
  ylab("Unemployed people")
