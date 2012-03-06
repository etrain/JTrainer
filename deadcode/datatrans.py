from csv import DictWriter
import sys, json, codecs

def main():
  fieldnames = ['correct_response','game','value','category','clue']
  of = codecs.open(sys.argv[2], 'wb', 'utf-8')
  o = DictWriter(of, fieldnames)
  i = json.loads(open(sys.argv[1]).read())

  o.writerow(dict([(k,k) for k in fieldnames]))
  for q in i:
    try:
      o.writerow(q)
    except Exception, e:
      continue

  of.close()


if __name__ == "__main__":
  main()
