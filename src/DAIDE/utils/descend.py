

# def get_leaf_descendents(class_):
#     leaf_descendants = []
#     for descendent in class_.__subclasses__():
#         leaf_descendants.append(descendent)
#         leaf_descendants = leaf_descendants + get_leaf_descendents(descendent)

#     return leaf_descendants

# if __name__ == "__main__":
#     from DAIDE.syntax.daide_object import DAIDE_OBJECT
#     print(get_leaf_descendents(DAIDE_OBJECT))