library(tm)

INDIR <- "../../data/"
OUTDIR <- INDIR


read_data <- function(fname=paste(INDIR, "jarchiven.csv", sep='/')) {
  x <- read.csv(fname, as.is=T)
  ds <- DataframeSource(x[,'clue',drop=F])
  corp <- Corpus(ds)
  corp <- tm_map(corp, stripWhitespace)
  corp <- tm_map(corp, tolower)
  corp <- tm_map(corp, removeWords, stopwords("english"))
  list(df=x, corp=corp)
}

do_kmeans <- function(corp, n=40) {
  #TODO: figure out how to force algo into using more evenly sized clusters.
  
  dtm <- DocumentTermMatrix(corp)
  kmeans(dtm, n)
}

write_data <- function(df, fname=paste(OUTDIR, "jarchiven-clustered.csv", sep='/')) {
  write.csv(df, fname, row.names=F)
}

#TODO: function to take kmeans output and assign cluster number back to original document.
main <- function(debug=F) {
  dat <- read_data()
  
  km <- do_kmeans(dat$corp)
  dat$df$cluster <- km$cluster

  write_data(dat$df)

  if(debug) return(list(df=dat$df, km=km))
}

main()
