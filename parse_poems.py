import re
text_file = open('moore.txt', 'r', errors='ignore')
corpus = text_file.read().split('\n')
toc = corpus[0:corpus.index("POEMS:")]
titles = list(filter(lambda a: a != '', toc))[2:]
split_points = [] #these indicate where the poems split
for t in titles:
  indeces = [i for i, x in enumerate(corpus) if t.strip() in x]
  split_points.append(indeces[-1])

def clean_poem(poem):
  cleaned = ''
  for line in poem:
    clean_line = line.lower().replace('\xa0', '').strip()
    if clean_line != '':
      cleaned+=clean_line+' \n'
  return cleaned

for j in range(len(split_points)-1):
  start = split_points[j]
  stop = split_points[j+1]
  poem = clean_poem(corpus[start+1:stop])

  outfile = open('poems/'+re.sub(r'\W+', '', titles[j].lower())+'.txt', 'w')
  outfile.write(poem)
  outfile.close()
  print('poems/'+re.sub(r'\W+', '', titles[j].lower())+'.txt')


