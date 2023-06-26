parent1 = type("Parent1", (), {"a": "some_attr"})
parent2 = type("Parent2", (), {"b": "some_attr"})
child = type("Child", (parent1, parent2), {"c": "some_attr"})
