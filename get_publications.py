#!/usr/bin/env python
import feedparser

topics = ['gravitational waves',
          'gravitational wave',
          'gravitational-wave',
          'GWs',
          'GW',
          'LIGO',
          'LISA',
          'pulsar timing arrays',
          'pulsar timing array',
          'PTAs',
          'PTA',
          'numerical relativity',
          ]

topics = ['all:%22' + topic.replace(' ', '+') + '%22' for topic in topics]
topics = '%28' + '+OR+'.join(topics) + '%29'

with open('names.txt', 'r') as file:
    names = [line.strip() for line in file.readlines()]

allnames = []

for name in names:
    allnames.append(name)
    subnames = name.split(' ')
    if len(subnames) > 2: allnames.append(subnames[0] + ' ' + subnames[-1])
    subnames = [subname[0] + '.' for subname in subnames[:-1]] + [subnames[-1]]
    allnames.append(' '.join(subnames))
    if len(subnames) > 2: allnames.append(subnames[0] + ' ' + subnames[-1])

urlnames = ['au:%22' + name.replace(' ', '+') + '%22' for name in allnames]
urlnames = '%28' + '+OR+'.join(urlnames) + '%29'

file = open('publications.md', 'w')
file.write('# Publications\n\n')
file.write('A selection of recent publications by CamGW members.\n\n')

print('Fetching publications...')

for year in ['2026', '2025', '2024', '2023']:
    file.write('## ' + year + '\n\n')
    query = str('https://export.arxiv.org/api/query?'
                + 'search_query=submittedDate:['
                + year + '01010000+TO+' + year + '12312359]'
                + '+AND+' + topics + '+AND+' + urlnames
                + '&max_results=1000')
    print('Querying arXiv for publications from ' + year + '...')
    feed = feedparser.parse(query)

    if len(feed.entries) == 0: continue

    if feed.entries[0].title == 'Error':
        print('Error fetching data from arXiv API: ' + feed.entries[0].summary)
        break

    print('Found ' + str(len(feed.entries)) + ' publications')
    print('Writing to file...')

    entries, _ = zip(*sorted(zip(feed.entries,
                                 [entry.id for entry in feed.entries]),
                             reverse=True,
                             key=lambda x: x[1]))

    papers = []
    collaboration_papers = []

    for entry in entries:
        authors = [author['name'] for author in entry.authors]

        if len(list(set(authors) & set(allnames))) == 0: continue

        try:
            link = 'https://doi.org/' + entry.arxiv_doi
        except AttributeError:
            link = entry.id

        if any(collab in authors[0]
               for collab in ['LIGO', 'Virgo', 'KAGRA', 'LVK']):
            collaborations = authors[0]
            for author in authors[1:]:
                if 'Collaboration' in author:
                    collaborations = collaborations + ', ' + author
                else:
                    break
            incauthors = list()
            for author in authors:
                if author in allnames:
                    incauthors.append('**' + author + '**')
            if len(incauthors) > 1:
                incauthors[-1] = 'and ' + incauthors[-1]
            authors = str(collaborations
                          + ' (inc. ' + ', '.join(incauthors) + ')')
            collaboration_papers.append(
                '{0}, [*{1}*]({2}), arXiv:{3} [{4}]\n'.format(
                    authors, entry.title, link, entry.id.split('/')[-1][:-2],
                    entry.arxiv_primary_category['term']))

        elif 'LIGO' in ', '.join(authors):
            incauthors = list()
            for author in authors[1:]:
                if author in allnames:
                    incauthors.append('**' + author + '**')
            if len(incauthors) > 1:
                incauthors[-1] = 'and ' + incauthors[-1]
            if authors[0] in allnames:
                authors[0] = '**' + authors[0] + '**'
            authors[0] = authors[0] + ' *et al.*'
            if len(incauthors) == 0:
                authors = str(authors[0])
            else:
                authors = str(authors[0]
                              + ' (inc. ' + ', '.join(incauthors) + ')')
            collaboration_papers.append(
                '{0}, [*{1}*]({2}), arXiv:{3} [{4}]\n'.format(
                    authors, entry.title, link, entry.id.split('/')[-1][:-2],
                    entry.arxiv_primary_category['term']))

        elif len(authors) <= 10:
            for author in authors:
                if author in allnames:
                    authors[authors.index(author)] = '**' + author + '**'
            if len(authors) > 1:
                authors[-1] = 'and ' + authors[-1]
            authors = ', '.join(authors)
            papers.append(
                '{0}, [*{1}*]({2}), arXiv:{3} [{4}]\n'.format(
                    authors, entry.title, link, entry.id.split('/')[-1][:-2],
                    entry.arxiv_primary_category['term']))

        else:
            incauthors = list()
            for author in authors[1:]:
                if author in allnames:
                    incauthors.append('**' + author + '**')
            if len(incauthors) > 1:
                incauthors[-1] = 'and ' + incauthors[-1]
            if authors[0] in allnames:
                authors[0] = '**' + authors[0] + '**'
            authors[0] = authors[0] + ' *et al.*'
            if len(incauthors) == 0:
                authors = str(authors[0])
            else:
                authors = str(authors[0]
                              + ' (inc. ' + ', '.join(incauthors) + ')')
            papers.append(
                '{0}, [*{1}*]({2}), arXiv:{3} [{4}]\n'.format(
                    authors, entry.title, link, entry.id.split('/')[-1][:-2],
                    entry.arxiv_primary_category['term']))

    for i, paper in enumerate(papers):
        file.write('{}. '.format(i+1) + paper)
    file.write('\n')

    if len(collaboration_papers) > 0:
        file.write('##### LVK Collaboration Papers\n')
        for i, paper in enumerate(collaboration_papers):
            file.write('{}. '.format(i+1) + paper)
        file.write('\n')

file.write('[Back to Home](index.html)\n')
file.close()
