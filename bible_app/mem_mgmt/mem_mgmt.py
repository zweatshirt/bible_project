import psutil


def mem_size(p: psutil.Process()):
    """returns memory usage of the app"""
    print(
        '* Memory usage of process ' + str(p.pid) +
        ' *\n\tBytes: {}\n\tMB: {}\n\tGB: {}'
        .format(mem_bytes := p.memory_info().rss,
                megabytes := mem_bytes / (1000 ** 2),
                gigabytes := megabytes / 1000)
    )
