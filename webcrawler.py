import os

#each website is a different project

def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating folder' + directory)
        os.makedirs(directory)

#create queue and crawled files

def create_data_files(project_name,base_url):
    queue = project_name + '/queue.txt'
    crawled =  project_name + '/crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled,'')

#create a new file

def write_file(path,data):
    f = open(path,'w')
    f.write(data)
    f.close()

# add data onto a existing file

def append_to_file(path,data):
    with open(path,'a',encoding = 'latin-1') as file:
        file.write(data + '\n')

# delete the content on file

def delete_file_content(path):
    with open(path,'w'):
        pass

# file conversion to set items

def file_to_set(file_name):
    results = set()
    with open(file_name,'r') as f:
        for line in f:
            results.add(line.replace('\n',''))
    return results

#set conversion to file

def set_to_file(links,file):
    delete_file_content(file)
    for link in sorted(links):
        append_to_file(file, link)







