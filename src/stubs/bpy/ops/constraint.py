import sys
import typing


def childof_clear_inverse(constraint: str = "",
                          owner: typing.Union[int, str] = 'OBJECT'):
    '''Clear inverse correction for ChildOf constraint 

    :param constraint: Constraint, Name of the constraint to edit 
    :type constraint: str
    :param owner: Owner, The owner of this constraintOBJECT Object, Edit a constraint on the active object.BONE Bone, Edit a constraint on the active bone. 
    :type owner: typing.Union[int, str]
    '''

    pass


def childof_set_inverse(constraint: str = "",
                        owner: typing.Union[int, str] = 'OBJECT'):
    '''Set inverse correction for ChildOf constraint 

    :param constraint: Constraint, Name of the constraint to edit 
    :type constraint: str
    :param owner: Owner, The owner of this constraintOBJECT Object, Edit a constraint on the active object.BONE Bone, Edit a constraint on the active bone. 
    :type owner: typing.Union[int, str]
    '''

    pass


def delete():
    '''Remove constraint from constraint stack 

    '''

    pass


def followpath_path_animate(constraint: str = "",
                            owner: typing.Union[int, str] = 'OBJECT',
                            frame_start: int = 1,
                            length: int = 100):
    '''Add default animation for path used by constraint if it isn’t animated already 

    :param constraint: Constraint, Name of the constraint to edit 
    :type constraint: str
    :param owner: Owner, The owner of this constraintOBJECT Object, Edit a constraint on the active object.BONE Bone, Edit a constraint on the active bone. 
    :type owner: typing.Union[int, str]
    :param frame_start: Start Frame, First frame of path animation 
    :type frame_start: int
    :param length: Length, Number of frames that path animation should take 
    :type length: int
    '''

    pass


def limitdistance_reset(constraint: str = "",
                        owner: typing.Union[int, str] = 'OBJECT'):
    '''Reset limiting distance for Limit Distance Constraint 

    :param constraint: Constraint, Name of the constraint to edit 
    :type constraint: str
    :param owner: Owner, The owner of this constraintOBJECT Object, Edit a constraint on the active object.BONE Bone, Edit a constraint on the active bone. 
    :type owner: typing.Union[int, str]
    '''

    pass


def move_down(constraint: str = "", owner: typing.Union[int, str] = 'OBJECT'):
    '''Move constraint down in constraint stack 

    :param constraint: Constraint, Name of the constraint to edit 
    :type constraint: str
    :param owner: Owner, The owner of this constraintOBJECT Object, Edit a constraint on the active object.BONE Bone, Edit a constraint on the active bone. 
    :type owner: typing.Union[int, str]
    '''

    pass


def move_up(constraint: str = "", owner: typing.Union[int, str] = 'OBJECT'):
    '''Move constraint up in constraint stack 

    :param constraint: Constraint, Name of the constraint to edit 
    :type constraint: str
    :param owner: Owner, The owner of this constraintOBJECT Object, Edit a constraint on the active object.BONE Bone, Edit a constraint on the active bone. 
    :type owner: typing.Union[int, str]
    '''

    pass


def objectsolver_clear_inverse(constraint: str = "",
                               owner: typing.Union[int, str] = 'OBJECT'):
    '''Clear inverse correction for ObjectSolver constraint 

    :param constraint: Constraint, Name of the constraint to edit 
    :type constraint: str
    :param owner: Owner, The owner of this constraintOBJECT Object, Edit a constraint on the active object.BONE Bone, Edit a constraint on the active bone. 
    :type owner: typing.Union[int, str]
    '''

    pass


def objectsolver_set_inverse(constraint: str = "",
                             owner: typing.Union[int, str] = 'OBJECT'):
    '''Set inverse correction for ObjectSolver constraint 

    :param constraint: Constraint, Name of the constraint to edit 
    :type constraint: str
    :param owner: Owner, The owner of this constraintOBJECT Object, Edit a constraint on the active object.BONE Bone, Edit a constraint on the active bone. 
    :type owner: typing.Union[int, str]
    '''

    pass


def stretchto_reset(constraint: str = "",
                    owner: typing.Union[int, str] = 'OBJECT'):
    '''Reset original length of bone for Stretch To Constraint 

    :param constraint: Constraint, Name of the constraint to edit 
    :type constraint: str
    :param owner: Owner, The owner of this constraintOBJECT Object, Edit a constraint on the active object.BONE Bone, Edit a constraint on the active bone. 
    :type owner: typing.Union[int, str]
    '''

    pass
