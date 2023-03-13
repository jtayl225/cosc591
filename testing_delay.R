setwd("F:\\UNE\\COSC591")
install.packages("tuneR")
library(tuneR)

test_beep <- readWave("beep.wav")
play(test_beep)

delay_audio <- function(sound=test_beep, ear="right",delay=1){
  new_samples <- round(sound@samp.rate*delay)
  if(ear == "right"){
    return(c(rep(0,new_samples),test_beep@left[1:(length(test_beep@left)-(new_samples))]))
  }else if(ear == "left"){
    return(c(rep(0,new_samples),test_beep@right[1:(length(test_beep@right)-(new_samples))]))
  }
}
test_beep_adjusted <- test_beep
test_beep_adjusted@left <- delay_audio(ear="left",delay=0.01)

play(test_beep_adjusted)
