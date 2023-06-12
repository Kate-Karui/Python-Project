import random
import time

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def wordlist():
  global words
  words = ('coherent,please,greet,awake,flood,worry,recognise,moldy,space,consist,abhorrent,little,load,transport,group,tiresome,spy,fail,string,aloof,decide,numberless,pink,occur,zinc,calendar,look,skin,selfish,sugar,trousers,chance,faint,paint,squeamish,snails,visitor,close,refuse,lackadaisical,possess,hurry,bare,robin,pastoral,rush,nauseating,cheat,greasy,female,wide,detail,splendid,flight,dangerous,expert,unbiased,elated,spell,plant,flavor,purring,fanatical,color,cabbage,hollow,rich,innocent,rake,young,heady,rightful,vague,ground,well-groomed,weak,simple,flawless,cast,coat,scientific,shirt,fierce,hushed,soda,deranged,bone,icicle,fire,clever,eminent,kiss,gruesome,nest,condition,real,rabbit,trade,troubled,ill-fated,thoughtful,walk,axiomatic,grain,regular,remember,can,nondescript,aunt,craven,chicken,narrow,huge,parched,sweet,statement,snail,zebra,hapless,need,abashed,cute,average,peck,help,bake,direction,fixed,rough,attend,dogs,aboriginal,white,behavior,tooth,flame,shaggy,lace,gifted,general,disapprove,aftermath,periodic,skip,observe,unequaled,raspy,machine,fuel,volleyball,wobble,jolly,marble,elastic,uninterested,shock,event,necessary,admit,carve,shame,bells,quince,bent,many,same,scold,preach,fence,entertain,loose,quiver,colour,cooperative,useless,uttermost,ill,barbarous,spotty,reflect,concern,secretary,zany,unnatural,nappy,disagreeable,count,probable,range,abrupt,nonchalant,donkey,leather,mass,kitty,snakes,minister,fascinated,double,rot,funny,robust,camera,table,joyous,risk,industry,match,melodic,bounce,dear,smile,vivacious,cool,bleach,roll,tongue,thick,seal,impartial,strong,amusing,obeisant,old-fashioned,victorious,overconfident,exchange,squash,meal,exclusive,disgusted,frantic,replace,noise,resonant,awful,domineering,beef,eight,van,marvelous,pour,dislike,remain,scintillating,shape,thankful,jaded,plastic,knowing,weary,park,note,engine,maddening,existence,tie,amuck,home,bath,slimy,jewel,guiltless,tin,crowd,rail,judge,brainy,rainy,jump,crown,monkey,full,muddled,plan,sign,market,petite,available,horrible,ladybug,team,unhealthy,eye,obsolete,borrow,decorate,prevent,join,consider,sudden,fog,actually,adjustment,peace,uncovered,mark,shocking,substance,room,modern,shiny,grab,skillful,excited,doubt,sleet,frequent,silent,questionable,example,snake,substantial,sock,discover,ten,exotic,warlike,truthful,mind,fragile,fantastic,fair,meaty,stimulating,turn,fertile,representative,accidental,juice,knee,endurable,warn,sassy,past,homeless,system,art,receptive,boil,tree,well-to-do,nasty,wrist,coal,chase,crayon,own,governor,bathe,hilarious,fang,imaginary,intelligent,pricey,unusual,destruction,likeable,easy,organic,wide-eyed,cough,afraid,proud,agreeable,whirl,tacit,found,mere,mend,love,teaching,gorgeous,trot,one,doctor,ritzy,girl,flap,clumsy,great,last,fabulous,enchanting,launch,crow,confuse,trip,highfalutin,button,elfin,glue,two,lucky,fuzzy,jog,scarf,fireman,legs,sparkle,abundant,wrathful,river,reject,famous,sponge,irate,sweater,extra-large,pray,penitent,deadpan,teeny,kettle,earn,temper,spot,hall,loss,scale,volatile,ready,homely,lip,offend,harmonious,memory,collar,exist,tawdry,contain,multiply,instinctive,jail,scissors,pocket,ad hoc,glamorous,miss,beneficial,knotty,calm,divergent,iron,wave,treatment,flowers,coordinated,curvy,fowl,repeat,lake,insidious,downtown,tense,squirrel,tired,placid,flash,design,lush,next,fish,ambitious,feeling,left,black,reach,attract,preserve,class,tow,rejoice,functional,alleged,present,elbow,abject,scarce,bomb,stingy,hate,false,limping,pump,upset,desire,interesting,lick,secretive,opposite,settle,beam,scratch,depressed,celery,harbor,current,baseball,chivalrous,shy,save,miniature,foot,receipt,red,giraffe,change,accurate,thrill,eager,brush,glorious,harmony,hard-to-find,superficial,poised,request,changeable,coil,screeching,nod,friendly,silky,sink,wet,smelly,panicky,clean,blushing,fall,guttural,separate,half,naive,chief,spoon,protest,terrify,wise,educate,enthusiastic,release,telephone,common,nation,ripe,arrive,unwieldy,handle,infamous,curve,drum,used,hesitant,worm,thinkable,thought,tiny,admire,incredible,introduce,grey,watery,mellow,energetic,alarm,society,cup,observant,angry,alluring,vessel,lazy,bang,weigh,large,children,rambunctious,tendency,depend,powder,peaceful,giddy,song,cows,disastrous,place,pause,direful,steep,prick,teeny-tiny,hole,nerve,cats,terrible,prepare,tight,tick,hair,polite,macho,mixed,jobless,sky,alive,statuesque,tasteful,structure,puzzled,curly,steam,rescue,telling,four,yarn,carry,public,bustling,duck,inexpensive,friction,delightful,chew,attractive,delay,clear,momentous,wing,meek,quill,want,partner,learned,thoughtless,suspend,act,parsimonious,cagey,brawny,horses,bow,reminiscent,equable,drop,faulty,railway,gusty,spurious,rustic,ghost,poke,lonely,ice,umbrella,oval,theory,show,sophisticated,deep,plantation,snotty,murder,mundane,lively,dirt,handsomely,country,minute,maid,vase,sisters,crabby,sand,yam,invincible,threatening,acceptable,squalid,drown,imported,versed,romantic,unable,bag,solid,flock,jar,blood,stupendous,arrogant,pet,flowery,wire,weight,promise,oranges,fearless,cave,town,ski,punish,unlock,report,babies,exercise,correct,insect,remind,early,daily,stomach,ragged,tested,clap,first,increase,hover,curtain,imperfect,toe,numerous,needy,mean,melted,grass,corn,dull,adhesive,clam,breakable,lamentable,stone,land,humor,married,vanish,vest,exultant,queue,political,round,license,race,wail,repulsive,lacking,stamp,scrape,quickest,subtract,amuse,fax,enter,wreck,noxious,parallel,obese,bottle,program,ruin,elderly,rat,object,natural,type,rock,miscreant,hissing,story,lethal,irritating,fluttering,determined,brass,quick,annoy,lovely,old,freezing,cent,pin,obtainable,combative,basin,irritate,paper,sick,remove,caring,peep,girls,sea,complain,degree,defeated,flippant,colossal,bless,reply,liquid,appreciate,finger,haircut,bored,dinner,ugliest,verse,channel,route,name,growth,roasted,sincere,impulse,obnoxious,juicy,perfect,pointless,blow,strap,hanging,heap,voyage,null,blush,milky,develop,swim,overwrought,malicious,plot,paddle,station,play,hill,three,obtain,wandering,grumpy,youthful,boat,explode,material,week,ludicrous,slip,profit,incandescent,cross,giants,soggy,deafening,gold,equal,sort,friends,wrap,wren,hang,erratic,tank,pull,sticks,toothpaste,seed,stroke,dust,boy,fear,voice,encouraging,charming,strengthen,slippery,enchanted,discreet,lame,grandmother,untidy,swing,stupid,military,bouncy,crazy,ink,credit,poor,scribble,steady,camp,dam,piquant,gabby,airport,afternoon,orange,smoke,nice,conscious,greedy,playground,disillusioned,keen,cheerful,bulb,return,thing,sordid,mine,action,dynamic,thundering,inform,resolute,abounding,apathetic,riddle,invent,ill-informed,imagine,time,abstracted,pick,sprout,religion,courageous,mint,delicious,cuddly,comb,employ,animated,meeting,government,support,icy,shiver,cherries,letter,pleasant,wanting,needle,internal,dependent,dry,abiding,bear,moon,poison,wax,discussion,tub,economic,holistic,food,cheap,arch,salt,rings,nervous,visit,venomous,woman,bore,grateful,foamy,annoying,eyes,taste,abnormal,winter,jelly,pigs,manage,position,spark,zoom,delirious,creator,tasty,godly,file,unbecoming,colorful,rabid,beg,gleaming,step,absorbed,excuse,coach,psychedelic,valuable,incompetent,share,yummy,grubby,wall').split(',')
  print(random.choice(words))

def username():
  name = input("What is your name?: ")
  print("Hello " + name + ",", "are you able to guess the word?")
  
def guesswords():
  guess = input("Guess a letter: ")
  if guess in words:
      print("Correct!")
  else:
      print("Wrong!")
      
def functions():
  username()
  wordlist()
  guesswords()
  
functions()
