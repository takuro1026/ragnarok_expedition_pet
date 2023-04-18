from ragnarok_expedition_pet import Gene, Part
from ragnarok_expedition_pet.models.gene import Level
from ragnarok_expedition_pet.models.polly import Polly
from ragnarok_expedition_pet.models.result import Result
from ragnarok_expedition_pet.services import gene_list
from itertools import product
from collections import Counter


class TacticService:
    def __init__(self):

        self.__genes = {}

        for gene in gene_list:
            self.__genes[gene.name] = gene

    def find_combination(self, first_polly: Polly, second_polly: Polly):
        heads = self.find_advanced_match(first_polly.head, second_polly.head)
        bodies = self.find_advanced_match(first_polly.body, second_polly.body)
        around = self.find_advanced_match(first_polly.around, second_polly.around)

        max_weight = 0
        best_combination = None
        best_potential_match = None
        for components in product(heads, bodies, around):
            combination = Polly(components[0], components[1], components[2])
            weight, potential_polly = self.find_final_match(combination)

            if weight > max_weight:
                max_weight = weight
                best_combination = combination
                best_potential_match = potential_polly

        return Result(
            best_polly=best_combination,
            weight=max_weight,
            best_potential_match=best_potential_match
        )

    def find_advanced_match(self, gene_str1, gene_str2):
        gene1: Gene = self.__genes.get(gene_str1)
        gene2: Gene = self.__genes.get(gene_str2)

        result = []
        if gene1.get_level() == Level.ADVANCED:
            result.append(gene1.name)

        if gene2.get_level() == Level.ADVANCED:
            result.append(gene2.name)

        if len(result) != 0:
            result = list(set(result))
        elif gene1.get_level() == Level.BASIC and gene2.get_level() == Level.BASIC:
            result = list(set(gene1.parent).intersection(gene2.parent))

        return result

    def find_final_match(self, polly: Polly):
        head_gene_related = self.__genes.get(polly.head).parent
        body_gene_related = self.__genes.get(polly.body).parent
        around_gene_related = self.__genes.get(polly.around).parent

        result = dict(Counter(head_gene_related + body_gene_related + around_gene_related))

        weight = 2
        potential_polly = []
        for key in result:
            if weight < result[key]:
                weight = result[key]
                potential_polly.clear()
                potential_polly.append(key)
            elif weight == result[key]:
                potential_polly.append(key)

        final_weight = pow(10, weight) * len(potential_polly)

        return final_weight, potential_polly

    def search(self, gene_name):
        gene = self.__genes.get(gene_name)

        return gene if gene is not None else "Not found"
