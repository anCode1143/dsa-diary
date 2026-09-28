class Solution:
    def findAllRecipes(self, recipes: list[str], ingredients: list[list[str]], supplies: list[str]) -> list[str]:
        canMake = set(supplies)
        cantMake = set()
        recipesMap = {recipe : i for i, recipe in enumerate(recipes)}
        def canCreate(recipeIdx, dependent):
            if recipes[recipeIdx] in dependent:
                return False
            dependent.add(recipes[recipeIdx])
            for ingredient in ingredients[recipeIdx]:
                if ingredient in canMake:
                    continue
                if ingredient in cantMake or ingredient not in recipesMap:
                    return False
                else:
                    ingredientIdx = recipesMap[ingredient]
                    if not canCreate(ingredientIdx, dependent):
                        cantMake.add(recipes[recipeIdx])
                        return False
                    canMake.add(ingredient)
            canMake.add(recipes[recipeIdx])
            return True
        answer = []
        for recipeIdx in range(len(recipes)):
            if canCreate(recipeIdx, set()):
                answer.append(recipes[recipeIdx])
        return answer