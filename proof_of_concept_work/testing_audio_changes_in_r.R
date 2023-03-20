# Set up ####
## General ====
setwd("F:\\UNE\\COSC591")
library(tuneR)
library(signal)
library(audio)
## Read Data ====
beep <- readWave("../data/beep.wav")

## global parameters ====
selected_ear="right"
selected_delay = 0.02 #seconds to delay
selected_volume = 0.80 #the proportion to lower sound by (0.75 = 75% of normal volume)

# Functions to change audio #### 
change_delay <- function(sound_adjusted, ear="right",delay=1){
  new_samples <- round(sound_adjusted@samp.rate*delay)
  if(ear == "right"){
    sound_adjusted@right <<- c(rep(0,new_samples),sound_adjusted@left[1:(length(sound_adjusted@left)-(new_samples))])
    return("shitty function finished")
  }else if(ear == "left"){
    sound_adjusted@left <<- c(rep(0,new_samples),sound_adjusted@right[1:(length(sound_adjusted@right)-(new_samples))])
    return("shitty function finished")
  }
}

change_volume <- function(sound_adjusted, ear= "right"){
  if(ear=="right"){
    sound_adjusted@right <<- sound_adjusted@right*selected_volume
    return("shitty function finished")
  }else if(ear == "left"){
    sound_adjusted@left <<- sound_adjusted@left*selected_volume
    return("shitty function finished")
  }
}


