from ragnarok_expedition_pet import Gene, Part
from ragnarok_expedition_pet.services import gene_list


class TacticService:
    def __init__(self):

        self.__genes = {}

        for gene in gene_list:
            self.__genes[gene.name] = gene

    def search(self, gene_name):
        gene = self.__genes.get(gene_name)

        return gene if gene is not None else "Not found"
