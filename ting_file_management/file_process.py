import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    if path_file in instance.queue:
        return
    txt = txt_importer(path_file)
    instance.enqueue(path_file)
    result = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(txt),
        "linhas_do_arquivo": txt,
    }
    print(result)


def remove(instance):
    if not instance.queue:
        sys.stdout.write("Não há elementos\n")
    else:
        result = instance.dequeue()
        print("Arquivo", result, "removido com sucesso")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
