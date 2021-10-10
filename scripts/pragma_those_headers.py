import os

HEADERS_ROOT_DIR = '../src/'


def get_header_files_paths(dir):
    headers_paths = []
    for root, subdirs, files in os.walk(dir):
        for file in files:
            if file.endswith('.h') or file.endswith('.hpp'):
                headers_paths.append(os.path.join(root, file))
    return headers_paths


def fix_headers(dir):
    for header_path in get_header_files_paths(dir):
        with open(header_path, 'r+') as header_file:
            source = header_file.read()
            header_file.seek(0)
            if not ("#pragma once" in source):
                source = "#pragma once\n" + source
                print('./' + header_path[len(HEADERS_ROOT_DIR):], 'fixed!')
                header_file.write(source)
                header_file.truncate()


fix_headers(HEADERS_ROOT_DIR)
