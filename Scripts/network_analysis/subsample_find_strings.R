

subsample <- list()
for(i in 1:4){
  subsample[[i]]<- emb_df[fit2$cluster==i,-1]
}


sub<-rownames(subsample[[1]])
gsub("\"","",sub, fixed = TRUE )



subset1<- subset(emb_df, rownames(emb_df) %in% rownames(subsample[[1]]))
subset2<- subset(emb_df, rownames(emb_df) %in% rownames(subsample[[2]]))
subset3<- subset(emb_df, rownames(emb_df) %in% rownames(subsample[[3]]))
subset4<- subset(emb_df, rownames(emb_df) %in% rownames(subsample[[4]]))

Net<-read.csv("NetworkAnalysis1.csv")
head(Net)

Group1<-as.data.frame(unique(Net[Net$Celebrity %in% subset1$X, "Celebrity"]))
Group2<-as.data.frame(unique(Net[Net$Celebrity %in% subset2$X, "Celebrity"]))
Group3<-as.data.frame(unique(Net[Net$Celebrity %in% subset3$X, "Celebrity"]))
Group4<-as.data.frame(unique(Net[Net$Celebrity %in% subset4$X, "Celebrity"]))





write.csv(Group1, file = "Output/Group1.csv")
write.csv(Group2, file = "Output/Group2.csv")
write.csv(Group3, file = "Output/Group3.csv")
write.csv(Group4, file = "Output/Group4.csv")
