#A multi-clipborad program
text={'agree':"""yes, i agree. That sounds fine to me.""",
      'busy':"""sorrt, we can do this later this week or next week""",
      'upsell':"""would you consider mking this a monthly donation"""}
import sys,pyperclip
if len(sys.argv)<2:
    print('Usage:python multi_clipboardAutomaticMessages.py [keyphrase] -copy phrase text')
    sys.exit()
keyphrase=sys.argv[1]  #first command line arg is the key phrase

if keyphrase in text:
    pyperclip.copy(text[keyphrase])
    print('Text for' + keyphrase + 'copied to clipbord')
else:
    print("There is notext for " )