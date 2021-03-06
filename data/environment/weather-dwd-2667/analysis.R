#
# This is a GNU R script for analysis and visualization
# of historic weather data in this folder.
# 

# import dependencies
require(zoo)
require(ggplot2)
require(splines)
require(MASS)

weather.df <- read.csv("./weather-dwd-2667.csv")
colnames(weather.df) <- c("datum", "qual", "bedeckung", "relfeuchte",
                           "dampfdruck", "ltemp", "ldruck", "wges", "temp_boden",
                           "ltemp_min", "ltemp_max", "wind_max", "ndschlag_typ",
                           "ndschlag_hoehe", "sonne", "schnee")
weather.df$datum <- as.Date(as.character(weather.df$datum), format="%Y%m%d")

# eleminate empty values
weather.df$bedeckung[weather.df$bedeckung == -999.0] <- NA
weather.df$relfeuchte[weather.df$relfeuchte == -999.0] <- NA
weather.df$dampfdruck[weather.df$dampfdruck == -999.0] <- NA
weather.df$ltemp[weather.df$ltemp == -999.0] <- NA
weather.df$ldruck[weather.df$ldruck == -999.0] <- NA
weather.df$wges[weather.df$wges == -999.0] <- NA
weather.df$temp_boden[weather.df$temp_boden == -999.0] <- NA
weather.df$ltemp_min[weather.df$ltemp_min == -999.0] <- NA
weather.df$ltemp_max[weather.df$ltemp_max == -999.0] <- NA
weather.df$wind_max[weather.df$wind_max == -999.0] <- NA
weather.df$ndschlag_typ[weather.df$ndschlag_typ == -999.0] <- NA
weather.df$ndschlag_hoehe[weather.df$ndschlag_hoehe == -999.0] <- NA
weather.df$sonne[weather.df$sonne == -999.0] <- NA
weather.df$schnee[weather.df$schnee == -999.0] <- NA

# create temperature time series using zoo package (for whatever reason)
weather.ltemp.zoo <- with(weather.df, zoo(ltemp, order.by = weather.df$datum))

# create temperature time series as ts object and analyse
weather.ltemp.ts <- ts(weather.df$ltemp, frequency=365, start=c(1957, 243))
ltemp.decomp <- decompose(weather.ltemp.ts)
plot(ltemp.decomp$trend)
ltemp.decomp.trend.df <- as.data.frame(matrix(ltemp.decomp$trend))
ltemp.decomp.trend.df$datum <- weather.df$datum
ggplot(data=ltemp.decomp.trend.df, aes(x=datum, y = V1)) +
  geom_line(weight=0.2) +
  geom_smooth(method="lm", formula = y ~ ns(x,5), size=0.5) +
  ggtitle("Air temperature trend") +
  xlab("Date") +
  ylab("Temperature (°C)")

# Time series plot of air temperature
ggplot(weather.df, aes(datum, ltemp)) + geom_line(size=0.2) + geom_smooth() + ggtitle("Air temperature Cologne/Bonn 1957 - 2013") + xlab("Date") + ylab("Temperature (°C)")

# Time series plot of ground temperature
ggplot(weather.df, aes(datum, temp_boden)) + geom_line(size=0.2) + geom_smooth() + ggtitle("Air temperature Cologne/Bonn 1957 - 2013") + xlab("Date") + ylab("Temperature (°C)")

# Time series plot of precipitation
ggplot(weather.df, aes(datum, ndschlag_hoehe)) + geom_line(size=0.2) + geom_smooth() + ggtitle("Precipitation Cologne/Bonn 1957 - 2013") + xlab("Date") + ylab("Precipitation (mm)")

# Time series plot of avg. wind speed
ggplot(weather.df, aes(datum, wges)) + geom_line(size=0.2) + geom_smooth() + ggtitle("Average daily wind speed Cologne/Bonn 1957 - 2013") + xlab("Date") + ylab("Speed (m/sec)")

# Time series plot of max wind speed
ggplot(weather.df, aes(datum, wind_max)) + geom_line(size=0.2) + geom_smooth() + ggtitle("Maximum daily wind speed Cologne/Bonn 1957 - 2013") + xlab("Date") + ylab("Speed (m/sec)")

# Time series plot of air pressure
ggplot(weather.df, aes(datum, ldruck)) + geom_line(size=0.2) + geom_smooth() + ggtitle("Average daily air pressure Cologne/Bonn 1957 - 2013") + xlab("Date") + ylab("Pressure (hpa)")

# Time series plot of cloudyness
ggplot(weather.df, aes(datum, bedeckung)) + geom_line(size=0.2) + geom_smooth() + ggtitle("Average daily cloud coverage Cologne/Bonn 1957 - 2013") + xlab("Date") + ylab("Coverage")

# Time series plot of relative humidity
ggplot(weather.df, aes(datum, relfeuchte)) + geom_line(size=0.2) + geom_smooth() + ggtitle("Average daily relative humidity Cologne/Bonn 1957 - 2013") + xlab("Date") + ylab("Relative humidity (%)")

# Scatter plots
ggplot(weather.df, aes(x=ltemp, y=temp_boden)) + geom_point(size=0.6, position="jitter") + ggtitle("Air temperature vs. ground temperature")
ggplot(weather.df, aes(x=ltemp, y=bedeckung)) + geom_point(size=0.6, position="jitter") + ggtitle("Air temperature vs. cloud coverage")
ggplot(weather.df, aes(x=ltemp, y=relfeuchte)) + geom_point(size=0.6, position="jitter") + ggtitle("Air temperature vs. cloud coverage")
ggplot(weather.df, aes(x=ltemp, y=ldruck)) + geom_point(size=0.6, position="jitter") + ggtitle("Air temperature vs. air pressure")
ggplot(weather.df, aes(x=ltemp, y=wges)) + geom_point(size=0.6, position="jitter") + ggtitle("Air temperature vs. wind speed")
ggplot(weather.df, aes(x=ltemp, y=ndschlag_hoehe)) + geom_point(size=0.6, position="jitter") + ggtitle("Air temperature vs. precipitation")


