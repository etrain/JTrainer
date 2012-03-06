import json, sys

x = json.loads(open(sys.argv[1]).read())
x = filter(lambda f: all(f.get(x) is not None for x in ['category','correct_response','game','clue','value']), x)

print json.dumps([{"model":"jflashcards.Clue","pk":i,"fields":r} for i,r in enumerate(x)])
