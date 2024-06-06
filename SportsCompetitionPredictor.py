# solver for Sports Analytics project


#first is weighted the most. It is the true head to head prediction.
#(Percent chance a wins + percent chance B looses)/(percent chance a wins + percent chance B looses)+(Percent chance B wins + percent chance a looses)
def head2heada(pctwa, pctwb):
    pa = (pctwa+(1000-pctwb))/((pctwa+(1000-pctwb))+(pctwb+(1000-pctwa)))
    return pa
def head2headb(pctwa,pctwb):
    pb = (pctwb+(1000-pctwa))/((pctwb+(1000-pctwa))+(pctwa+(1000-pctwb)))
    return pb


#uses the head 2 head percentages (calculated above) calculated above and weighs them 60%, weighs the last 5 winning percentage 30% and the "true" head 2 head record is weighed 10%
def win(pb,last5win, h2h):
    last5win = last5win/1000
    h2h = h2h/1000
    winpct = ((pb*60)+(last5win*30)+(h2h*10))/100
    return winpct


#Calculates the "implied odds"
def vegasodds(odds): 
    if odds>0:
        odds = 100/(odds+100)
    elif odds<0:
        odds = odds*-1
        odds = odds/(odds+100)
    return odds


#determines if my model's prediction beats vegas odds by enough to be considered a good bet.
def goodbet(odds, p):
    if p-odds>.2:
        return True
    else: return False


#user inputs
pctwa = int(input("Team A win pct"))
pctwb = int(input("Team B win pct"))
last5a = int(input("team A win pct over their last 5 games"))
last5b = int(input("team B win pct over their last 5 games"))
h2ha = int(input("head to win pct for team A"))
h2hb = int(input("head to win pct for team B"))
oddsa = int(input("odds for team A"))
oddsb = int(input("odds for team B"))

#calls function for percent change A/B wins and returns data
pa = head2heada(pctwa, pctwb)
pb = head2headb(pctwa,pctwb)
print ("p of a:" + str(pa))
print ("p of b:" + str(pb))

#calls function for the improved model accounting for winning/loosing streaks and teams history against eachother
ourwina = win(pa,last5a, h2ha)
ourwinb = win(pb,last5b, h2hb)
#returns data
print("weighting recent scores and head to head, the winning odds for team a is:" + str(ourwina))
print("weighting recent scores and head to head, the winning odds for team b is:" + str(ourwinb))

#returns vegas data
voddsa = vegasodds(oddsa)
voddsb = vegasodds(oddsb)
print("vegas's implied odds for team a"+ str(voddsa))
print("vegas's implied odds for team b"+ str(voddsb))

#tells user if bet is good/bad
if goodbet(voddsa,ourwina)== True:
    print("it is a good bet to bet on team A")
if goodbet(voddsb,ourwinb)== True:
    print("it is a good bet to bet on team B")
