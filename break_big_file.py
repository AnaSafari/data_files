chunk_size = 160000
def write_chunk(part, lines):
    with open('C:/Users/anahita.safari/Downloads/kccfc/splitted/NFL_Chiefs_20170701_'+ str(part) +'.csv', 'w') as f_out:
        f_out.write(header)
        f_out.writelines(lines)
with open("C:/Users/anahita.safari/Downloads/kccfc/NFL_Chiefs_20170701_20210824.tsv", "r", encoding='utf-8') as f:
    count = 0
    header = f.readline()
    lines = []
    for line in f:
        count += 1
        lines.append(line)
        if count % chunk_size == 0:
            write_chunk(count // chunk_size, lines)
            lines = []
    # write remainder
    if len(lines) > 0:
        write_chunk((count // chunk_size) + 1, lines)