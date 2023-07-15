from time import time #to record time
def typerror(promt):
    global inwords
    words=promt.split()
    errors = 0

    for i in range(len(inwords)):
        if i in (0,len(inwords)-1):
            if inwords[i]==words[i]:
                continue
            else:
                errors=errors+1
        else:
            if inwords[i]==words[i]:
                if(inwords[i+1]==words[i+1]) & (inwords[i-1]==words[i-1]):
                    continue
                else:
                    errors+=1
            else:
                error+=1
    return errors

# now to calculate the speed of typing words per minute
def speed(inprompt,stime,etime):
    global time
    global inwords

    inwords=inprompt.split()
    twords=len(inwords)
    speed=twords/time

    return speed
# calculate the total elapsed time
def elapsedtime(stime,etime):
    time=etime-stime
    return time
if __name__=='__main__':
    prompt="Track your progress with the free  program here at W3Schools.Log into your account, and start earning points!This is an optional feature. You can study W3Schools without using My Learning.."
    print("TYPE THIS :- ",prompt,"")
    input("press enter when you are ready to check your speed ")
    stime=time()
    inprompt=input()
    etime=time()
    time = round(elapsedtime(stime,etime),2)
    speed=speed(inprompt,stime,etime)
    error=typerror(prompt)

    print("total time elapsed : ",time,"seconds")
    print("your average typing speed was ",speed,"words per minute (w/m)")
    print("with the total of ",error,"errors")