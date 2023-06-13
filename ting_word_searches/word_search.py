from ting_file_management.file_management import txt_importer


def exists_word(word, instance):
    word = word.lower()
    result = []

    for file_name in instance.queue:
        txt = txt_importer(file_name)
        occurrences = [
            {"linha": line_num + 1}
            for line_num, line in enumerate(txt)
            if word in line.lower()]
        if occurrences:
            result.append(
                {
                    "palavra": word,
                    "arquivo": file_name,
                    "ocorrencias": occurrences
                })
    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
