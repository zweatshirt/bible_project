import psutil


def mem_size(p: psutil.Process()):
    """returns memory usage of the app"""
    print(
        '* Memory usage of process ' + str(p.pid) +
        ' *\n\tBytes: {}\n\tMB: {}\n\tGB: {}'
        .format(mem_bytes := p.memory_info().rss,
                megabytes := mem_bytes / (2 ** 20),
                gigabytes := mem_bytes / (2 ** 30)
    )
