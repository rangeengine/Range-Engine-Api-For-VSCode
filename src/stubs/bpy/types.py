import sys
import typing
import mathutils
import bpy


class Action:
    '''A collection of F-Curves for animation '''

    fcurves: typing.List['FCurve'] = None
    '''The individual F-Curves that make up the action 

    :type: typing.List['FCurve']
    '''

    frame_range: float = None
    '''The final frame range of all F-Curves within this action 

    :type: float
    '''

    groups: typing.List['ActionGroup'] = None
    '''Convenient groupings of F-Curves 

    :type: typing.List['ActionGroup']
    '''

    id_root: typing.Union[int, str] = None
    '''Type of ID block that action can be used on - DO NOT CHANGE UNLESS YOU KNOW WHAT YOU ARE DOING 

    :type: typing.Union[int, str]
    '''

    pose_markers: typing.List['ActionPoseMarkers'] = None
    '''Markers specific to this action, for labeling poses 

    :type: typing.List['ActionPoseMarkers']
    '''


class ActionActuator:
    '''Actuator to control the object movement '''

    action: 'Action' = None
    '''

    :type: 'Action'
    '''

    apply_to_children: bool = None
    '''Update Action on all children Objects as well 

    :type: bool
    '''

    blend_mode: typing.Union[int, str] = None
    '''How this layer is blended with previous layers 

    :type: typing.Union[int, str]
    '''

    frame_blend_in: int = None
    '''Number of frames of motion blending 

    :type: int
    '''

    frame_end: float = None
    '''

    :type: float
    '''

    frame_property: str = None
    '''Assign the action’s current frame number to this property 

    :type: str
    '''

    frame_start: float = None
    '''

    :type: float
    '''

    layer: int = None
    '''The animation layer to play the action on 

    :type: int
    '''

    layer_weight: float = None
    '''How much of the previous layer to blend into this one 

    :type: float
    '''

    play_mode: typing.Union[int, str] = None
    '''Action playback type 

    :type: typing.Union[int, str]
    '''

    priority: int = None
    '''Execution priority - lower numbers will override actions with higher numbers (with 2 or more actions at once, the overriding channels must be lower in the stack) 

    :type: int
    '''

    property: str = None
    '''Use this property to define the Action position 

    :type: str
    '''

    use_additive: bool = None
    '''Action is added to the current loc/rot/scale in global or local coordinate according to Local flag 

    :type: bool
    '''

    use_continue_last_frame: bool = None
    '''Restore last frame when switching on/off, otherwise play from the start each time 

    :type: bool
    '''

    use_force: bool = None
    '''Apply Action as a global or local force depending on the local option (dynamic objects only) 

    :type: bool
    '''

    use_local: bool = None
    '''Let the Action act in local coordinates, used in Force and Add mode 

    :type: bool
    '''


class ActionConstraint:
    '''Map an action to the transform axes of a bone '''

    action: 'Action' = None
    '''The constraining action 

    :type: 'Action'
    '''

    frame_end: int = None
    '''Last frame of the Action to use 

    :type: int
    '''

    frame_start: int = None
    '''First frame of the Action to use 

    :type: int
    '''

    max: float = None
    '''Maximum value for target channel range 

    :type: float
    '''

    min: float = None
    '''Minimum value for target channel range 

    :type: float
    '''

    subtarget: str = None
    '''

    :type: str
    '''

    target: 'Object' = None
    '''Target Object 

    :type: 'Object'
    '''

    transform_channel: typing.Union[int, str] = None
    '''Transformation channel from the target that is used to key the Action 

    :type: typing.Union[int, str]
    '''

    use_bone_object_action: bool = None
    '''Bones only: apply the object’s transformation channels of the action to the constrained bone, instead of bone’s channels 

    :type: bool
    '''


class ActionFCurves:
    '''Collection of action F-Curves '''

    def new(self, data_path: str, index: int = 0,
            action_group: str = "") -> 'FCurve':
        '''Add an F-Curve to the action 

        :param data_path: Data Path, F-Curve data path to use 
        :type data_path: str
        :param index: Index, Array index 
        :type index: int
        :param action_group: Action Group, Acton group to add this F-Curve into 
        :type action_group: str
        :rtype: 'FCurve'
        :return:  Newly created F-Curve 
        '''
        pass

    def find(self, data_path: str, index: int = 0) -> 'FCurve':
        '''Find an F-Curve. Note that this function performs a linear scan of all F-Curves in the action. 

        :param data_path: Data Path, F-Curve data path 
        :type data_path: str
        :param index: Index, Array index 
        :type index: int
        :rtype: 'FCurve'
        :return:  The found F-Curve, or None if it doesn’t exist 
        '''
        pass

    def remove(self, fcurve: 'FCurve'):
        '''Remove action group 

        :param fcurve: F-Curve to remove 
        :type fcurve: 'FCurve'
        '''
        pass


class ActionGroup:
    '''Groups of F-Curves '''

    channels: typing.List['FCurve'] = None
    '''F-Curves in this group 

    :type: typing.List['FCurve']
    '''

    color_set: typing.Union[int, str] = None
    '''Custom color set to use 

    :type: typing.Union[int, str]
    '''

    colors: 'ThemeBoneColorSet' = None
    '''Copy of the colors associated with the group’s color set 

    :type: 'ThemeBoneColorSet'
    '''

    is_custom_color_set: bool = None
    '''Color set is user-defined instead of a fixed theme color set 

    :type: bool
    '''

    lock: bool = None
    '''Action group is locked 

    :type: bool
    '''

    name: str = None
    '''

    :type: str
    '''

    select: bool = None
    '''Action group is selected 

    :type: bool
    '''

    show_expanded: bool = None
    '''Action group is expanded 

    :type: bool
    '''


class ActionGroups:
    '''Collection of action groups '''

    def new(self, name: str) -> 'ActionGroup':
        '''Create a new action group and add it to the action 

        :param name: New name for the action group 
        :type name: str
        :rtype: 'ActionGroup'
        :return:  Newly created action group 
        '''
        pass

    def remove(self, action_group: 'ActionGroup'):
        '''Remove action group 

        :param action_group: Action group to remove 
        :type action_group: 'ActionGroup'
        '''
        pass


class ActionPoseMarkers:
    '''Collection of timeline markers '''

    active: 'TimelineMarker' = None
    '''Active pose marker for this action 

    :type: 'TimelineMarker'
    '''

    active_index: int = None
    '''Index of active pose marker 

    :type: int
    '''

    def new(self, name: str) -> 'TimelineMarker':
        '''Add a pose marker to the action 

        :param name: New name for the marker (not unique) 
        :type name: str
        :rtype: 'TimelineMarker'
        :return:  Newly created marker 
        '''
        pass

    def remove(self, marker: 'TimelineMarker'):
        '''Remove a timeline marker 

        :param marker: Timeline marker to remove 
        :type marker: 'TimelineMarker'
        '''
        pass


class Actuator:
    '''Actuator to apply actions in the game engine '''

    active: bool = None
    '''Set the active state of the actuator 

    :type: bool
    '''

    name: str = None
    '''

    :type: str
    '''

    pin: bool = None
    '''Display when not linked to a visible states controller 

    :type: bool
    '''

    show_expanded: bool = None
    '''Set actuator expanded in the user interface 

    :type: bool
    '''

    type: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    def link(self, controller: 'Controller'):
        '''Link the actuator to a controller 

        :param controller: Controller to link to 
        :type controller: 'Controller'
        '''
        pass

    def unlink(self, controller: 'Controller'):
        '''Unlink the actuator from a controller 

        :param controller: Controller to unlink from 
        :type controller: 'Controller'
        '''
        pass


class ActuatorSensor:
    '''Sensor to detect state modifications of actuators '''

    actuator: str = None
    '''Actuator name, actuator active state modifications will be detected 

    :type: str
    '''


class AddSequence:
    '''Add Sequence '''

    input_1: 'Sequence' = None
    '''First input for the effect strip 

    :type: 'Sequence'
    '''

    input_2: 'Sequence' = None
    '''Second input for the effect strip 

    :type: 'Sequence'
    '''

    input_count: int = None
    '''

    :type: int
    '''


class Addon:
    '''Python add-ons to be loaded automatically '''

    module: str = None
    '''Module name 

    :type: str
    '''

    preferences: 'AddonPreferences' = None
    '''

    :type: 'AddonPreferences'
    '''


class AddonPreferences:
    bl_idname: str = None
    '''

    :type: str
    '''


class Addons:
    '''Collection of add-ons '''

    pass


class AdjustmentSequence:
    '''Sequence strip to perform filter adjustments to layers below '''

    animation_offset_end: int = None
    '''Animation end offset (trim end) 

    :type: int
    '''

    animation_offset_start: int = None
    '''Animation start offset (trim start) 

    :type: int
    '''

    input_count: int = None
    '''

    :type: int
    '''


class AlembicObjectPath:
    '''Path of an object inside of an Alembic archive '''

    path: str = None
    '''Object path 

    :type: str
    '''


class AlembicObjectPaths:
    '''Collection of object paths '''

    pass


class AlphaOverSequence:
    '''Alpha Over Sequence '''

    input_1: 'Sequence' = None
    '''First input for the effect strip 

    :type: 'Sequence'
    '''

    input_2: 'Sequence' = None
    '''Second input for the effect strip 

    :type: 'Sequence'
    '''

    input_count: int = None
    '''

    :type: int
    '''


class AlphaUnderSequence:
    '''Alpha Under Sequence '''

    input_1: 'Sequence' = None
    '''First input for the effect strip 

    :type: 'Sequence'
    '''

    input_2: 'Sequence' = None
    '''Second input for the effect strip 

    :type: 'Sequence'
    '''

    input_count: int = None
    '''

    :type: int
    '''


class AlwaysSensor:
    '''Sensor to generate continuous pulses '''

    pass


class AndController:
    '''Controller passing on events based on a logical AND operation '''

    pass


class AnimData:
    '''Animation data for data-block '''

    action: 'Action' = None
    '''Active Action for this data-block 

    :type: 'Action'
    '''

    action_blend_type: typing.Union[int, str] = None
    '''Method used for combining Active Action’s result with result of NLA stack 

    :type: typing.Union[int, str]
    '''

    action_extrapolation: typing.Union[int, str] = None
    '''Action to take for gaps past the Active Action’s range (when evaluating with NLA) 

    :type: typing.Union[int, str]
    '''

    action_influence: float = None
    '''Amount the Active Action contributes to the result of the NLA stack 

    :type: float
    '''

    drivers: typing.List['FCurve'] = None
    '''The Drivers/Expressions for this data-block 

    :type: typing.List['FCurve']
    '''

    nla_tracks: typing.List['NlaTrack'] = None
    '''NLA Tracks (i.e. Animation Layers) 

    :type: typing.List['NlaTrack']
    '''

    use_nla: bool = None
    '''NLA stack is evaluated when evaluating this block 

    :type: bool
    '''

    use_tweak_mode: bool = None
    '''Whether to enable or disable tweak mode in NLA 

    :type: bool
    '''


class AnimDataDrivers:
    '''Collection of Driver F-Curves '''

    def from_existing(self, src_driver: 'FCurve' = None) -> 'FCurve':
        '''Add a new driver given an existing one 

        :param src_driver: Existing Driver F-Curve to use as template for a new one 
        :type src_driver: 'FCurve'
        :rtype: 'FCurve'
        :return:  New Driver F-Curve 
        '''
        pass

    def find(self, data_path: str, index: int = 0) -> 'FCurve':
        '''Find a driver F-Curve. Note that this function performs a linear scan of all driver F-Curves. 

        :param data_path: Data Path, F-Curve data path 
        :type data_path: str
        :param index: Index, Array index 
        :type index: int
        :rtype: 'FCurve'
        :return:  The found F-Curve, or None if it doesn’t exist 
        '''
        pass


class AnimViz:
    '''Settings for the visualization of motion '''

    motion_path: 'AnimVizMotionPaths' = None
    '''Motion Path settings for visualization 

    :type: 'AnimVizMotionPaths'
    '''

    onion_skin_frames: 'AnimVizOnionSkinning' = None
    '''Onion Skinning (ghosting) settings for visualization 

    :type: 'AnimVizOnionSkinning'
    '''


class AnimVizMotionPaths:
    '''Motion Path settings for animation visualization '''

    bake_location: typing.Union[int, str] = None
    '''When calculating Bone Paths, use Head or Tips 

    :type: typing.Union[int, str]
    '''

    frame_after: int = None
    '''Number of frames to show after the current frame (only for ‘Around Current Frame’ Onion-skinning method) 

    :type: int
    '''

    frame_before: int = None
    '''Number of frames to show before the current frame (only for ‘Around Current Frame’ Onion-skinning method) 

    :type: int
    '''

    frame_end: int = None
    '''End frame of range of paths to display/calculate (not for ‘Around Current Frame’ Onion-skinning method) 

    :type: int
    '''

    frame_start: int = None
    '''Starting frame of range of paths to display/calculate (not for ‘Around Current Frame’ Onion-skinning method) 

    :type: int
    '''

    frame_step: int = None
    '''Number of frames between paths shown (not for ‘On Keyframes’ Onion-skinning method) 

    :type: int
    '''

    show_frame_numbers: bool = None
    '''Show frame numbers on Motion Paths 

    :type: bool
    '''

    show_keyframe_action_all: bool = None
    '''For bone motion paths, search whole Action for keyframes instead of in group with matching name only (is slower) 

    :type: bool
    '''

    show_keyframe_highlight: bool = None
    '''Emphasize position of keyframes on Motion Paths 

    :type: bool
    '''

    show_keyframe_numbers: bool = None
    '''Show frame numbers of Keyframes on Motion Paths 

    :type: bool
    '''

    type: typing.Union[int, str] = None
    '''Type of range to show for Motion Paths 

    :type: typing.Union[int, str]
    '''


class AnimVizOnionSkinning:
    '''Onion Skinning settings for animation visualization '''

    frame_after: int = None
    '''Number of frames to show after the current frame (only for ‘Around Current Frame’ Onion-skinning method) 

    :type: int
    '''

    frame_before: int = None
    '''Number of frames to show before the current frame (only for ‘Around Current Frame’ Onion-skinning method) 

    :type: int
    '''

    frame_end: int = None
    '''End frame of range of Ghosts to display (not for ‘Around Current Frame’ Onion-skinning method) 

    :type: int
    '''

    frame_start: int = None
    '''Starting frame of range of Ghosts to display (not for ‘Around Current Frame’ Onion-skinning method) 

    :type: int
    '''

    frame_step: int = None
    '''Number of frames between ghosts shown (not for ‘On Keyframes’ Onion-skinning method) 

    :type: int
    '''

    show_only_selected: bool = None
    '''For Pose-Mode drawing, only draw ghosts for selected bones 

    :type: bool
    '''

    type: typing.Union[int, str] = None
    '''Method used for determining what ghosts get drawn 

    :type: typing.Union[int, str]
    '''


class AnyType:
    '''RNA type used for pointers to any possible data '''

    pass


class Area:
    '''Area in a subdivided screen, containing an editor '''

    height: int = None
    '''Area height 

    :type: int
    '''

    regions: typing.List['Region'] = None
    '''Regions this area is subdivided in 

    :type: typing.List['Region']
    '''

    show_menus: bool = None
    '''Show menus in the header 

    :type: bool
    '''

    spaces: typing.List['Space'] = None
    '''Spaces contained in this area, the first being the active space (NOTE: Useful for example to restore a previously used 3D view space in a certain area to get the old view orientation) 

    :type: typing.List['Space']
    '''

    type: typing.Union[int, str] = None
    '''Current editor type for this area 

    :type: typing.Union[int, str]
    '''

    width: int = None
    '''Area width 

    :type: int
    '''

    x: int = None
    '''The window relative vertical location of the area 

    :type: int
    '''

    y: int = None
    '''The window relative horizontal location of the area 

    :type: int
    '''

    def tag_redraw(self, ):
        '''tag_redraw 

        '''
        pass

    def header_text_set(self, text: str = ""):
        '''Set the header text 

        :param text: Text, New string for the header, no argument clears the text 
        :type text: str
        '''
        pass


class AreaLamp:
    '''Directional area lamp '''

    compression_threshold: float = None
    '''Deep shadow map compression threshold 

    :type: float
    '''

    gamma: float = None
    '''Light gamma correction value 

    :type: float
    '''

    ge_shadow_buffer_type: typing.Union[int, str] = None
    '''The shadow mapping algorithm used 

    :type: typing.Union[int, str]
    '''

    shadow_adaptive_threshold: float = None
    '''Threshold for Adaptive Sampling (Raytraced shadows) 

    :type: float
    '''

    shadow_buffer_bias: float = None
    '''Shadow buffer sampling bias 

    :type: float
    '''

    shadow_buffer_bleed_bias: float = None
    '''Bias for reducing light-bleed on variance shadow maps 

    :type: float
    '''

    shadow_buffer_clip_end: float = None
    '''Shadow map clip end, beyond which objects will not generate shadows 

    :type: float
    '''

    shadow_buffer_clip_start: float = None
    '''Shadow map clip start, below which objects will not generate shadows 

    :type: float
    '''

    shadow_buffer_samples: int = None
    '''Number of shadow buffer samples 

    :type: int
    '''

    shadow_buffer_size: int = None
    '''Resolution of the shadow buffer, higher values give crisper shadows but use more memory 

    :type: int
    '''

    shadow_buffer_soft: float = None
    '''Size of shadow buffer sampling area 

    :type: float
    '''

    shadow_buffer_type: typing.Union[int, str] = None
    '''Type of shadow buffer 

    :type: typing.Union[int, str]
    '''

    shadow_color: float = None
    '''Color of shadows cast by the lamp 

    :type: float
    '''

    shadow_filter_type: typing.Union[int, str] = None
    '''Type of shadow filter (Buffer Shadows) 

    :type: typing.Union[int, str]
    '''

    shadow_method: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    shadow_ray_sample_method: typing.Union[int, str] = None
    '''Method for generating shadow samples: Adaptive QMC is fastest, Constant QMC is less noisy but slower 

    :type: typing.Union[int, str]
    '''

    shadow_ray_samples_x: int = None
    '''Number of samples taken extra (samples x samples) 

    :type: int
    '''

    shadow_ray_samples_y: int = None
    '''Number of samples taken extra (samples x samples) 

    :type: int
    '''

    shadow_sample_buffers: typing.Union[int, str] = None
    '''Number of shadow buffers to render for better AA, this increases memory usage 

    :type: typing.Union[int, str]
    '''

    shadow_soft_size: float = None
    '''Light size for ray shadow sampling (Raytraced shadows) 

    :type: float
    '''

    shape: typing.Union[int, str] = None
    '''Shape of the area lamp 

    :type: typing.Union[int, str]
    '''

    size: float = None
    '''Size of the area of the area Lamp, X direction size for Rectangle shapes 

    :type: float
    '''

    size_y: float = None
    '''Size of the area of the area Lamp in the Y direction for Rectangle shapes 

    :type: float
    '''

    use_auto_clip_end: bool = None
    '''Automatic calculation of clipping-end, based on visible vertices 

    :type: bool
    '''

    use_auto_clip_start: bool = None
    '''Automatic calculation of clipping-start, based on visible vertices 

    :type: bool
    '''

    use_dither: bool = None
    '''Use 2x2 dithering for sampling (Constant Jittered sampling) 

    :type: bool
    '''

    use_jitter: bool = None
    '''Use noise for sampling (Constant Jittered sampling) 

    :type: bool
    '''

    use_only_shadow: bool = None
    '''Cast shadows only, without illuminating objects 

    :type: bool
    '''

    use_shadow: bool = None
    '''

    :type: bool
    '''

    use_shadow_layer: bool = None
    '''Objects on the same layers only cast shadows 

    :type: bool
    '''

    use_umbra: bool = None
    '''Emphasize parts that are fully shadowed (Constant Jittered sampling) 

    :type: bool
    '''


class AreaSpaces:
    '''Collection of spaces '''

    active: 'Space' = None
    '''Space currently being displayed in this area 

    :type: 'Space'
    '''


class Armature:
    '''Armature data-block containing a hierarchy of bones, usually used for rigging characters '''

    animation_data: 'AnimData' = None
    '''Animation data for this data-block 

    :type: 'AnimData'
    '''

    bones: typing.List['Bone'] = None
    '''

    :type: typing.List['Bone']
    '''

    deform_method: typing.Union[int, str] = None
    '''Vertex Deformer Method (Game Engine only) 

    :type: typing.Union[int, str]
    '''

    draw_type: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    edit_bones: typing.List['ArmatureEditBones'] = None
    '''

    :type: typing.List['ArmatureEditBones']
    '''

    ghost_frame_end: int = None
    '''End frame of range of Ghosts to display (not for ‘Around Current Frame’ Onion-skinning method) 

    :type: int
    '''

    ghost_frame_start: int = None
    '''Starting frame of range of Ghosts to display (not for ‘Around Current Frame’ Onion-skinning method) 

    :type: int
    '''

    ghost_size: int = None
    '''Frame step for Ghosts (not for ‘On Keyframes’ Onion-skinning method) 

    :type: int
    '''

    ghost_step: int = None
    '''Number of frame steps on either side of current frame to show as ghosts (only for ‘Around Current Frame’ Onion-skinning method) 

    :type: int
    '''

    ghost_type: typing.Union[int, str] = None
    '''Method of Onion-skinning for active Action 

    :type: typing.Union[int, str]
    '''

    is_editmode: bool = None
    '''True when used in editmode 

    :type: bool
    '''

    layers: bool = None
    '''Armature layer visibility 

    :type: bool
    '''

    layers_protected: bool = None
    '''Protected layers in Proxy Instances are restored to Proxy settings on file reload and undo 

    :type: bool
    '''

    pose_position: typing.Union[int, str] = None
    '''Show armature in binding pose or final posed state 

    :type: typing.Union[int, str]
    '''

    show_axes: bool = None
    '''Draw bone axes 

    :type: bool
    '''

    show_bone_custom_shapes: bool = None
    '''Draw bones with their custom shapes 

    :type: bool
    '''

    show_group_colors: bool = None
    '''Draw bone group colors 

    :type: bool
    '''

    show_names: bool = None
    '''Draw bone names 

    :type: bool
    '''

    show_only_ghost_selected: bool = None
    '''

    :type: bool
    '''

    use_auto_ik: bool = None
    '''Add temporary IK constraints while grabbing bones in Pose Mode 

    :type: bool
    '''

    use_deform_delay: bool = None
    '''Don’t deform children when manipulating bones in Pose Mode 

    :type: bool
    '''

    use_mirror_x: bool = None
    '''Apply changes to matching bone on opposite side of X-Axis 

    :type: bool
    '''

    def transform(self, matrix: float):
        '''Transform armature bones by a matrix 

        :param matrix: Matrix 
        :type matrix: float
        '''
        pass


class ArmatureActuator:
    bone: str = None
    '''Bone on which the constraint is defined 

    :type: str
    '''

    constraint: str = None
    '''Name of the constraint to control 

    :type: str
    '''

    influence: float = None
    '''Influence of this constraint 

    :type: float
    '''

    mode: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    secondary_target: 'Object' = None
    '''Set this object as the secondary target of the constraint (only IK polar target at the moment) 

    :type: 'Object'
    '''

    target: 'Object' = None
    '''Set this object as the target of the constraint 

    :type: 'Object'
    '''

    weight: float = None
    '''Weight of this constraint 

    :type: float
    '''


class ArmatureBones:
    '''Collection of armature bones '''

    active: 'Bone' = None
    '''Armature’s active bone 

    :type: 'Bone'
    '''


class ArmatureEditBones:
    '''Collection of armature edit bones '''

    active: 'EditBone' = None
    '''Armatures active edit bone 

    :type: 'EditBone'
    '''

    def new(self, name: str) -> 'EditBone':
        '''Add a new bone 

        :param name: New name for the bone 
        :type name: str
        :rtype: 'EditBone'
        :return:  Newly created edit bone 
        '''
        pass

    def remove(self, bone: 'EditBone'):
        '''Remove an existing bone from the armature 

        :param bone: EditBone to remove 
        :type bone: 'EditBone'
        '''
        pass


class ArmatureModifier:
    '''Armature deformation modifier '''

    invert_vertex_group: bool = None
    '''Invert vertex group influence 

    :type: bool
    '''

    object: 'Object' = None
    '''Armature object to deform with 

    :type: 'Object'
    '''

    use_bone_envelopes: bool = None
    '''Bind Bone envelopes to armature modifier 

    :type: bool
    '''

    use_deform_preserve_volume: bool = None
    '''Deform rotation interpolation with quaternions 

    :type: bool
    '''

    use_multi_modifier: bool = None
    '''Use same input as previous modifier, and mix results using overall vgroup 

    :type: bool
    '''

    use_vertex_groups: bool = None
    '''Bind vertex groups to armature modifier 

    :type: bool
    '''

    vertex_group: str = None
    '''Name of Vertex Group which determines influence of modifier per point 

    :type: str
    '''


class ArmatureSensor:
    '''Sensor to detect values and changes in values of IK solver '''

    bone: str = None
    '''Identify the bone to check value from 

    :type: str
    '''

    constraint: str = None
    '''Identify the bone constraint to check value from 

    :type: str
    '''

    test_type: typing.Union[int, str] = None
    '''Type of value and test 

    :type: typing.Union[int, str]
    '''

    value: float = None
    '''Value to be used in comparison 

    :type: float
    '''


class ArrayModifier:
    '''Array duplication modifier '''

    constant_offset_displace: float = None
    '''Value for the distance between arrayed items 

    :type: float
    '''

    count: int = None
    '''Number of duplicates to make 

    :type: int
    '''

    curve: 'Object' = None
    '''Curve object to fit array length to 

    :type: 'Object'
    '''

    end_cap: 'Object' = None
    '''Mesh object to use as an end cap 

    :type: 'Object'
    '''

    fit_length: float = None
    '''Length to fit array within 

    :type: float
    '''

    fit_type: typing.Union[int, str] = None
    '''Array length calculation method 

    :type: typing.Union[int, str]
    '''

    merge_threshold: float = None
    '''Limit below which to merge vertices 

    :type: float
    '''

    offset_object: 'Object' = None
    '''Use the location and rotation of another object to determine the distance and rotational change between arrayed items 

    :type: 'Object'
    '''

    relative_offset_displace: float = None
    '''The size of the geometry will determine the distance between arrayed items 

    :type: float
    '''

    start_cap: 'Object' = None
    '''Mesh object to use as a start cap 

    :type: 'Object'
    '''

    use_constant_offset: bool = None
    '''Add a constant offset 

    :type: bool
    '''

    use_merge_vertices: bool = None
    '''Merge vertices in adjacent duplicates 

    :type: bool
    '''

    use_merge_vertices_cap: bool = None
    '''Merge vertices in first and last duplicates 

    :type: bool
    '''

    use_object_offset: bool = None
    '''Add another object’s transformation to the total offset 

    :type: bool
    '''

    use_relative_offset: bool = None
    '''Add an offset relative to the object’s bounding box 

    :type: bool
    '''


class Available:
    pass


class BackgroundImage:
    '''Image and settings for display in the 3D View background '''

    clip: 'MovieClip' = None
    '''Movie clip displayed and edited in this space 

    :type: 'MovieClip'
    '''

    clip_user: 'MovieClipUser' = None
    '''Parameters defining which frame of the movie clip is displayed 

    :type: 'MovieClipUser'
    '''

    draw_depth: typing.Union[int, str] = None
    '''Draw under or over everything 

    :type: typing.Union[int, str]
    '''

    frame_method: typing.Union[int, str] = None
    '''How the image fits in the camera frame 

    :type: typing.Union[int, str]
    '''

    image: 'Image' = None
    '''Image displayed and edited in this space 

    :type: 'Image'
    '''

    image_user: 'ImageUser' = None
    '''Parameters defining which layer, pass and frame of the image is displayed 

    :type: 'ImageUser'
    '''

    offset_x: float = None
    '''Offset image horizontally from the world origin 

    :type: float
    '''

    offset_y: float = None
    '''Offset image vertically from the world origin 

    :type: float
    '''

    opacity: float = None
    '''Image opacity to blend the image against the background color 

    :type: float
    '''

    rotation: float = None
    '''Rotation for the background image (ortho view only) 

    :type: float
    '''

    show_background_image: bool = None
    '''Show this image as background 

    :type: bool
    '''

    show_expanded: bool = None
    '''Show the expanded in the user interface 

    :type: bool
    '''

    show_on_foreground: bool = None
    '''Show this image in front of objects in viewport 

    :type: bool
    '''

    size: float = None
    '''Size of the background image (ortho view only) 

    :type: float
    '''

    source: typing.Union[int, str] = None
    '''Data source used for background 

    :type: typing.Union[int, str]
    '''

    use_camera_clip: bool = None
    '''Use movie clip from active scene camera 

    :type: bool
    '''

    use_flip_x: bool = None
    '''Flip the background image horizontally 

    :type: bool
    '''

    use_flip_y: bool = None
    '''Flip the background image vertically 

    :type: bool
    '''

    view_axis: typing.Union[int, str] = None
    '''The axis to display the image on 

    :type: typing.Union[int, str]
    '''


class BackgroundImages:
    '''Collection of background images '''

    def new(self, ) -> 'BackgroundImage':
        '''Add new background image 

        :rtype: 'BackgroundImage'
        :return:  Image displayed as viewport background 
        '''
        pass

    def remove(self, image: 'BackgroundImage'):
        '''Remove background image 

        :param image: Image displayed as viewport background 
        :type image: 'BackgroundImage'
        '''
        pass

    def clear(self, ):
        '''Remove all background images 

        '''
        pass


class BakePixel:
    du_dx: float = None
    '''

    :type: float
    '''

    du_dy: float = None
    '''

    :type: float
    '''

    dv_dx: float = None
    '''

    :type: float
    '''

    dv_dy: float = None
    '''

    :type: float
    '''

    next: 'BakePixel' = None
    '''

    :type: 'BakePixel'
    '''

    object_id: int = None
    '''

    :type: int
    '''

    primitive_id: int = None
    '''

    :type: int
    '''

    uv: float = None
    '''

    :type: float
    '''


class BakeSettings:
    '''Bake data for a Scene data-block '''

    cage_extrusion: float = None
    '''Distance to use for the inward ray cast when using selected to active 

    :type: float
    '''

    cage_object: str = None
    '''Object to use as cage instead of calculating the cage from the active object with cage extrusion 

    :type: str
    '''

    filepath: str = None
    '''Image filepath to use when saving externally 

    :type: str
    '''

    height: int = None
    '''Vertical dimension of the baking map 

    :type: int
    '''

    image_settings: 'ImageFormatSettings' = None
    '''

    :type: 'ImageFormatSettings'
    '''

    margin: int = None
    '''Extends the baked result as a post process filter 

    :type: int
    '''

    normal_b: typing.Union[int, str] = None
    '''Axis to bake in blue channel 

    :type: typing.Union[int, str]
    '''

    normal_g: typing.Union[int, str] = None
    '''Axis to bake in green channel 

    :type: typing.Union[int, str]
    '''

    normal_r: typing.Union[int, str] = None
    '''Axis to bake in red channel 

    :type: typing.Union[int, str]
    '''

    normal_space: typing.Union[int, str] = None
    '''Choose normal space for baking 

    :type: typing.Union[int, str]
    '''

    pass_filter: typing.Set[typing.Union[int, str]] = None
    '''Passes to include in the active baking pass 

    :type: typing.Set[typing.Union[int, str]]
    '''

    save_mode: typing.Union[int, str] = None
    '''Choose how to save the baking map 

    :type: typing.Union[int, str]
    '''

    use_automatic_name: bool = None
    '''Automatically name the output file with the pass type (external only) 

    :type: bool
    '''

    use_cage: bool = None
    '''Cast rays to active object from a cage 

    :type: bool
    '''

    use_clear: bool = None
    '''Clear Images before baking (internal only) 

    :type: bool
    '''

    use_pass_ambient_occlusion: bool = None
    '''Add ambient occlusion contribution 

    :type: bool
    '''

    use_pass_color: bool = None
    '''Color the pass 

    :type: bool
    '''

    use_pass_diffuse: bool = None
    '''Add diffuse contribution 

    :type: bool
    '''

    use_pass_direct: bool = None
    '''Add direct lighting contribution 

    :type: bool
    '''

    use_pass_emit: bool = None
    '''Add emission contribution 

    :type: bool
    '''

    use_pass_glossy: bool = None
    '''Add glossy contribution 

    :type: bool
    '''

    use_pass_indirect: bool = None
    '''Add indirect lighting contribution 

    :type: bool
    '''

    use_pass_subsurface: bool = None
    '''Add subsurface contribution 

    :type: bool
    '''

    use_pass_transmission: bool = None
    '''Add transmission contribution 

    :type: bool
    '''

    use_selected_to_active: bool = None
    '''Bake shading on the surface of selected objects to the active object 

    :type: bool
    '''

    use_split_materials: bool = None
    '''Split external images per material (external only) 

    :type: bool
    '''

    width: int = None
    '''Horizontal dimension of the baking map 

    :type: int
    '''


class BevelModifier:
    '''Bevel modifier to make edges and vertices more rounded '''

    angle_limit: float = None
    '''Angle above which to bevel edges 

    :type: float
    '''

    edge_weight_method: typing.Union[int, str] = None
    '''What edge weight to use for weighting a vertex 

    :type: typing.Union[int, str]
    '''

    limit_method: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    loop_slide: bool = None
    '''Prefer sliding along edges to having even widths 

    :type: bool
    '''

    material: int = None
    '''Material index of generated faces, -1 for automatic 

    :type: int
    '''

    offset_type: typing.Union[int, str] = None
    '''What distance Width measures 

    :type: typing.Union[int, str]
    '''

    profile: float = None
    '''The profile shape (0.5 = round) 

    :type: float
    '''

    segments: int = None
    '''Number of segments for round edges/verts 

    :type: int
    '''

    use_clamp_overlap: bool = None
    '''Clamp the width to avoid overlap 

    :type: bool
    '''

    use_only_vertices: bool = None
    '''Bevel verts/corners, not edges 

    :type: bool
    '''

    vertex_group: str = None
    '''Vertex group name 

    :type: str
    '''

    width: float = None
    '''Bevel value/amount 

    :type: float
    '''


class BezierSplinePoint:
    '''Bezier curve point with two handles '''

    co: float = None
    '''Coordinates of the control point 

    :type: float
    '''

    handle_left: float = None
    '''Coordinates of the first handle 

    :type: float
    '''

    handle_left_type: typing.Union[int, str] = None
    '''Handle types 

    :type: typing.Union[int, str]
    '''

    handle_right: float = None
    '''Coordinates of the second handle 

    :type: float
    '''

    handle_right_type: typing.Union[int, str] = None
    '''Handle types 

    :type: typing.Union[int, str]
    '''

    hide: bool = None
    '''Visibility status 

    :type: bool
    '''

    radius: float = None
    '''Radius for beveling 

    :type: float
    '''

    select_control_point: bool = None
    '''Control point selection status 

    :type: bool
    '''

    select_left_handle: bool = None
    '''Handle 1 selection status 

    :type: bool
    '''

    select_right_handle: bool = None
    '''Handle 2 selection status 

    :type: bool
    '''

    tilt: float = None
    '''Tilt in 3D View 

    :type: float
    '''

    weight_softbody: float = None
    '''Softbody goal weight 

    :type: float
    '''


class BlendData:
    '''Main data structure representing a .blend file and all its data-blocks '''

    actions: typing.List['Action'] = None
    '''Action data-blocks 

    :type: typing.List['Action']
    '''

    armatures: typing.List['BlendDataArmatures'] = None
    '''Armature data-blocks 

    :type: typing.List['BlendDataArmatures']
    '''

    brushes: typing.List['BlendDataBrushes'] = None
    '''Brush data-blocks 

    :type: typing.List['BlendDataBrushes']
    '''

    cache_files: typing.List['CacheFile'] = None
    '''Cache Files data-blocks 

    :type: typing.List['CacheFile']
    '''

    cameras: typing.List['Camera'] = None
    '''Camera data-blocks 

    :type: typing.List['Camera']
    '''

    curves: typing.List['Curve'] = None
    '''Curve data-blocks 

    :type: typing.List['Curve']
    '''

    filepath: str = None
    '''Path to the .blend file 

    :type: str
    '''

    fonts: typing.List['VectorFont'] = None
    '''Vector font data-blocks 

    :type: typing.List['VectorFont']
    '''

    grease_pencil: typing.List['BlendDataGreasePencils'] = None
    '''Grease Pencil data-blocks 

    :type: typing.List['BlendDataGreasePencils']
    '''

    groups: typing.List['Group'] = None
    '''Group data-blocks 

    :type: typing.List['Group']
    '''

    images: typing.List['BlendDataImages'] = None
    '''Image data-blocks 

    :type: typing.List['BlendDataImages']
    '''

    is_dirty: bool = None
    '''Have recent edits been saved to disk 

    :type: bool
    '''

    is_saved: bool = None
    '''Has the current session been saved to disk as a .blend file 

    :type: bool
    '''

    lamps: typing.List['Lamp'] = None
    '''Lamp data-blocks 

    :type: typing.List['Lamp']
    '''

    lattices: typing.List['BlendDataLattices'] = None
    '''Lattice data-blocks 

    :type: typing.List['BlendDataLattices']
    '''

    libraries: typing.List['BlendDataLibraries'] = None
    '''Library data-blocks 

    :type: typing.List['BlendDataLibraries']
    '''

    linestyles: typing.List['BlendDataLineStyles'] = None
    '''Line Style data-blocks 

    :type: typing.List['BlendDataLineStyles']
    '''

    masks: typing.List['BlendDataMasks'] = None
    '''Masks data-blocks 

    :type: typing.List['BlendDataMasks']
    '''

    materials: typing.List['Material'] = None
    '''Material data-blocks 

    :type: typing.List['Material']
    '''

    meshes: typing.List['Mesh'] = None
    '''Mesh data-blocks 

    :type: typing.List['Mesh']
    '''

    metaballs: typing.List['BlendDataMetaBalls'] = None
    '''Metaball data-blocks 

    :type: typing.List['BlendDataMetaBalls']
    '''

    movieclips: typing.List['MovieClip'] = None
    '''Movie Clip data-blocks 

    :type: typing.List['MovieClip']
    '''

    node_groups: typing.List['BlendDataNodeTrees'] = None
    '''Node group data-blocks 

    :type: typing.List['BlendDataNodeTrees']
    '''

    objects: typing.List['Object'] = None
    '''Object data-blocks 

    :type: typing.List['Object']
    '''

    paint_curves: typing.List['PaintCurve'] = None
    '''Paint Curves data-blocks 

    :type: typing.List['PaintCurve']
    '''

    palettes: typing.List['Palette'] = None
    '''Palette data-blocks 

    :type: typing.List['Palette']
    '''

    particles: typing.List['BlendDataParticles'] = None
    '''Particle data-blocks 

    :type: typing.List['BlendDataParticles']
    '''

    scenes: typing.List['BlendDataScenes'] = None
    '''Scene data-blocks 

    :type: typing.List['BlendDataScenes']
    '''

    screens: typing.List['Screen'] = None
    '''Screen data-blocks 

    :type: typing.List['Screen']
    '''

    shape_keys: typing.List['Key'] = None
    '''Shape Key data-blocks 

    :type: typing.List['Key']
    '''

    sounds: typing.List['Sound'] = None
    '''Sound data-blocks 

    :type: typing.List['Sound']
    '''

    speakers: typing.List['BlendDataSpeakers'] = None
    '''Speaker data-blocks 

    :type: typing.List['BlendDataSpeakers']
    '''

    texts: typing.List['Text'] = None
    '''Text data-blocks 

    :type: typing.List['Text']
    '''

    textures: typing.List['Texture'] = None
    '''Texture data-blocks 

    :type: typing.List['Texture']
    '''

    use_autopack: bool = None
    '''Automatically pack all external data into .blend file 

    :type: bool
    '''

    version: int = None
    '''Version of Blender the .blend was saved with 

    :type: int
    '''

    window_managers: typing.List['WindowManager'] = None
    '''Window manager data-blocks 

    :type: typing.List['WindowManager']
    '''

    worlds: typing.List['BlendDataWorlds'] = None
    '''World data-blocks 

    :type: typing.List['BlendDataWorlds']
    '''

    def user_map(self, key_types: set, value_types: set) -> dict:
        '''For list of valid set members for key_types & value_types, see: bpy.types.KeyingSetPath.id_type. 

        :param subset: When passed, only these data-blocks and their users will be included as keys/values in the map. 
        :type subset: list
        :param key_types: Filter the keys mapped by ID types. 
        :type key_types: set
        :param value_types: Filter the values in the set by ID types. 
        :type value_types: set
        :rtype: dict
        :return:  dictionary of bpy.types.ID instances, with sets of ID’s as their values. 
        '''
        pass


class BlendDataActions:
    '''Collection of actions '''

    is_updated: bool = None
    '''

    :type: bool
    '''

    def new(self, name: str) -> 'Action':
        '''Add a new action to the main database 

        :param name: New name for the data-block 
        :type name: str
        :rtype: 'Action'
        :return:  New action data-block 
        '''
        pass

    def remove(self,
               action: 'Action',
               do_unlink: bool = True,
               do_id_user: bool = True,
               do_ui_user: bool = True):
        '''Remove a action from the current blendfile 

        :param action: Action to remove 
        :type action: 'Action'
        :param do_unlink: Unlink all usages of this action before deleting it 
        :type do_unlink: bool
        :param do_id_user: Decrement user counter of all datablocks used by this action 
        :type do_id_user: bool
        :param do_ui_user: Make sure interface does not reference this action 
        :type do_ui_user: bool
        '''
        pass

    def tag(self, value: bool):
        '''tag 

        :param value: Value 
        :type value: bool
        '''
        pass


class BlendDataArmatures:
    '''Collection of armatures '''

    is_updated: bool = None
    '''

    :type: bool
    '''

    def new(self, name: str) -> 'Armature':
        '''Add a new armature to the main database 

        :param name: New name for the data-block 
        :type name: str
        :rtype: 'Armature'
        :return:  New armature data-block 
        '''
        pass

    def remove(self,
               armature: 'Armature',
               do_unlink: bool = True,
               do_id_user: bool = True,
               do_ui_user: bool = True):
        '''Remove a armature from the current blendfile 

        :param armature: Armature to remove 
        :type armature: 'Armature'
        :param do_unlink: Unlink all usages of this armature before deleting it (WARNING: will also delete objects instancing that armature data) 
        :type do_unlink: bool
        :param do_id_user: Decrement user counter of all datablocks used by this armature data 
        :type do_id_user: bool
        :param do_ui_user: Make sure interface does not reference this armature data 
        :type do_ui_user: bool
        '''
        pass

    def tag(self, value: bool):
        '''tag 

        :param value: Value 
        :type value: bool
        '''
        pass


class BlendDataBrushes:
    '''Collection of brushes '''

    is_updated: bool = None
    '''

    :type: bool
    '''

    def new(self, name: str,
            mode: typing.Union[int, str] = 'TEXTURE_PAINT') -> 'Brush':
        '''Add a new brush to the main database 

        :param name: New name for the data-block 
        :type name: str
        :param mode: Paint Mode for the new brushOBJECT Object Mode.EDIT Edit Mode.POSE Pose Mode.SCULPT Sculpt Mode.VERTEX_PAINT Vertex Paint.WEIGHT_PAINT Weight Paint.TEXTURE_PAINT Texture Paint.PARTICLE_EDIT Particle Edit.GPENCIL_EDIT Edit Strokes, Edit Grease Pencil Strokes. 
        :type mode: typing.Union[int, str]
        :rtype: 'Brush'
        :return:  New brush data-block 
        '''
        pass

    def remove(self,
               brush: 'Brush',
               do_unlink: bool = True,
               do_id_user: bool = True,
               do_ui_user: bool = True):
        '''Remove a brush from the current blendfile 

        :param brush: Brush to remove 
        :type brush: 'Brush'
        :param do_unlink: Unlink all usages of this brush before deleting it 
        :type do_unlink: bool
        :param do_id_user: Decrement user counter of all datablocks used by this brush 
        :type do_id_user: bool
        :param do_ui_user: Make sure interface does not reference this brush 
        :type do_ui_user: bool
        '''
        pass

    def tag(self, value: bool):
        '''tag 

        :param value: Value 
        :type value: bool
        '''
        pass


class BlendDataCacheFiles:
    '''Collection of cache files '''

    is_updated: bool = None
    '''

    :type: bool
    '''

    def tag(self, value: bool):
        '''tag 

        :param value: Value 
        :type value: bool
        '''
        pass


class BlendDataCameras:
    '''Collection of cameras '''

    is_updated: bool = None
    '''

    :type: bool
    '''

    def new(self, name: str) -> 'Camera':
        '''Add a new camera to the main database 

        :param name: New name for the data-block 
        :type name: str
        :rtype: 'Camera'
        :return:  New camera data-block 
        '''
        pass

    def remove(self,
               camera: 'Camera',
               do_unlink: bool = True,
               do_id_user: bool = True,
               do_ui_user: bool = True):
        '''Remove a camera from the current blendfile 

        :param camera: Camera to remove 
        :type camera: 'Camera'
        :param do_unlink: Unlink all usages of this camera before deleting it (WARNING: will also delete objects instancing that camera data) 
        :type do_unlink: bool
        :param do_id_user: Decrement user counter of all datablocks used by this camera 
        :type do_id_user: bool
        :param do_ui_user: Make sure interface does not reference this camera 
        :type do_ui_user: bool
        '''
        pass

    def tag(self, value: bool):
        '''tag 

        :param value: Value 
        :type value: bool
        '''
        pass


class BlendDataCurves:
    '''Collection of curves '''

    is_updated: bool = None
    '''

    :type: bool
    '''

    def new(self, name: str, type: typing.Union[int, str]) -> 'Curve':
        '''Add a new curve to the main database 

        :param name: New name for the data-block 
        :type name: str
        :param type: Type, The type of curve to add 
        :type type: typing.Union[int, str]
        :rtype: 'Curve'
        :return:  New curve data-block 
        '''
        pass

    def remove(self,
               curve: 'Curve',
               do_unlink: bool = True,
               do_id_user: bool = True,
               do_ui_user: bool = True):
        '''Remove a curve from the current blendfile 

        :param curve: Curve to remove 
        :type curve: 'Curve'
        :param do_unlink: Unlink all usages of this curve before deleting it (WARNING: will also delete objects instancing that curve data) 
        :type do_unlink: bool
        :param do_id_user: Decrement user counter of all datablocks used by this curve data 
        :type do_id_user: bool
        :param do_ui_user: Make sure interface does not reference this curve data 
        :type do_ui_user: bool
        '''
        pass

    def tag(self, value: bool):
        '''tag 

        :param value: Value 
        :type value: bool
        '''
        pass


class BlendDataFonts:
    '''Collection of fonts '''

    is_updated: bool = None
    '''

    :type: bool
    '''

    def load(self, filepath: str,
             check_existing: bool = False) -> 'VectorFont':
        '''Load a new font into the main database 

        :param filepath: path of the font to load 
        :type filepath: str
        :param check_existing: Using existing data-block if this file is already loaded 
        :type check_existing: bool
        :rtype: 'VectorFont'
        :return:  New font data-block 
        '''
        pass

    def remove(self,
               vfont: 'VectorFont',
               do_unlink: bool = True,
               do_id_user: bool = True,
               do_ui_user: bool = True):
        '''Remove a font from the current blendfile 

        :param vfont: Font to remove 
        :type vfont: 'VectorFont'
        :param do_unlink: Unlink all usages of this font before deleting it 
        :type do_unlink: bool
        :param do_id_user: Decrement user counter of all datablocks used by this font 
        :type do_id_user: bool
        :param do_ui_user: Make sure interface does not reference this font 
        :type do_ui_user: bool
        '''
        pass

    def tag(self, value: bool):
        '''tag 

        :param value: Value 
        :type value: bool
        '''
        pass


class BlendDataGreasePencils:
    '''Collection of grease pencils '''

    is_updated: bool = None
    '''

    :type: bool
    '''

    def tag(self, value: bool):
        '''tag 

        :param value: Value 
        :type value: bool
        '''
        pass

    def remove(self,
               grease_pencil: 'GreasePencil',
               do_unlink: bool = True,
               do_id_user: bool = True,
               do_ui_user: bool = True):
        '''Remove a grease pencil instance from the current blendfile 

        :param grease_pencil: Grease Pencil to remove 
        :type grease_pencil: 'GreasePencil'
        :param do_unlink: Unlink all usages of this grease pencil before deleting it 
        :type do_unlink: bool
        :param do_id_user: Decrement user counter of all datablocks used by this grease pencil 
        :type do_id_user: bool
        :param do_ui_user: Make sure interface does not reference this grease pencil 
        :type do_ui_user: bool
        '''
        pass


class BlendDataGroups:
    '''Collection of groups '''

    is_updated: bool = None
    '''

    :type: bool
    '''

    def new(self, name: str) -> 'Group':
        '''Add a new group to the main database 

        :param name: New name for the data-block 
        :type name: str
        :rtype: 'Group'
        :return:  New group data-block 
        '''
        pass

    def remove(self,
               group: 'Group',
               do_unlink: bool = True,
               do_id_user: bool = True,
               do_ui_user: bool = True):
        '''Remove a group from the current blendfile 

        :param group: Group to remove 
        :type group: 'Group'
        :param do_unlink: Unlink all usages of this group before deleting it 
        :type do_unlink: bool
        :param do_id_user: Decrement user counter of all datablocks used by this group 
        :type do_id_user: bool
        :param do_ui_user: Make sure interface does not reference this group 
        :type do_ui_user: bool
        '''
        pass

    def tag(self, value: bool):
        '''tag 

        :param value: Value 
        :type value: bool
        '''
        pass


class BlendDataImages:
    '''Collection of images '''

    is_updated: bool = None
    '''

    :type: bool
    '''

    def new(self,
            name: str,
            width: int,
            height: int,
            alpha: bool = False,
            float_buffer: bool = False,
            stereo3d: bool = False) -> 'Image':
        '''Add a new image to the main database 

        :param name: New name for the data-block 
        :type name: str
        :param width: Width of the image 
        :type width: int
        :param height: Height of the image 
        :type height: int
        :param alpha: Alpha, Use alpha channel 
        :type alpha: bool
        :param float_buffer: Float Buffer, Create an image with floating point color 
        :type float_buffer: bool
        :param stereo3d: Stereo 3D, Create left and right views 
        :type stereo3d: bool
        :rtype: 'Image'
        :return:  New image data-block 
        '''
        pass

    def load(self, filepath: str, check_existing: bool = False) -> 'Image':
        '''Load a new image into the main database 

        :param filepath: path of the file to load 
        :type filepath: str
        :param check_existing: Using existing data-block if this file is already loaded 
        :type check_existing: bool
        :rtype: 'Image'
        :return:  New image data-block 
        '''
        pass

    def remove(self,
               image: 'Image',
               do_unlink: bool = True,
               do_id_user: bool = True,
               do_ui_user: bool = True):
        '''Remove an image from the current blendfile 

        :param image: Image to remove 
        :type image: 'Image'
        :param do_unlink: Unlink all usages of this image before deleting it 
        :type do_unlink: bool
        :param do_id_user: Decrement user counter of all datablocks used by this image 
        :type do_id_user: bool
        :param do_ui_user: Make sure interface does not reference this image 
        :type do_ui_user: bool
        '''
        pass

    def tag(self, value: bool):
        '''tag 

        :param value: Value 
        :type value: bool
        '''
        pass


class BlendDataLamps:
    '''Collection of lamps '''

    is_updated: bool = None
    '''

    :type: bool
    '''

    def new(self, name: str, type: typing.Union[int, str]) -> 'Lamp':
        '''Add a new lamp to the main database 

        :param name: New name for the data-block 
        :type name: str
        :param type: Type, The type of texture to addPOINT Point, Omnidirectional point light source.SUN Sun, Constant direction parallel ray light source.SPOT Spot, Directional cone light source.HEMI Hemi, 180 degree constant light source.AREA Area, Directional area light source. 
        :type type: typing.Union[int, str]
        :rtype: 'Lamp'
        :return:  New lamp data-block 
        '''
        pass

    def remove(self,
               lamp: 'Lamp',
               do_unlink: bool = True,
               do_id_user: bool = True,
               do_ui_user: bool = True):
        '''Remove a lamp from the current blendfile 

        :param lamp: Lamp to remove 
        :type lamp: 'Lamp'
        :param do_unlink: Unlink all usages of this lamp before deleting it (WARNING: will also delete objects instancing that lamp data) 
        :type do_unlink: bool
        :param do_id_user: Decrement user counter of all datablocks used by this lamp data 
        :type do_id_user: bool
        :param do_ui_user: Make sure interface does not reference this lamp data 
        :type do_ui_user: bool
        '''
        pass

    def tag(self, value: bool):
        '''tag 

        :param value: Value 
        :type value: bool
        '''
        pass


class BlendDataLattices:
    '''Collection of lattices '''

    is_updated: bool = None
    '''

    :type: bool
    '''

    def new(self, name: str) -> 'Lattice':
        '''Add a new lattice to the main database 

        :param name: New name for the data-block 
        :type name: str
        :rtype: 'Lattice'
        :return:  New lattices data-block 
        '''
        pass

    def remove(self,
               lattice: 'Lattice',
               do_unlink: bool = True,
               do_id_user: bool = True,
               do_ui_user: bool = True):
        '''Remove a lattice from the current blendfile 

        :param lattice: Lattice to remove 
        :type lattice: 'Lattice'
        :param do_unlink: Unlink all usages of this lattice before deleting it (WARNING: will also delete objects instancing that lattice data) 
        :type do_unlink: bool
        :param do_id_user: Decrement user counter of all datablocks used by this lattice data 
        :type do_id_user: bool
        :param do_ui_user: Make sure interface does not reference this lattice data 
        :type do_ui_user: bool
        '''
        pass

    def tag(self, value: bool):
        '''tag 

        :param value: Value 
        :type value: bool
        '''
        pass


class BlendDataLibraries:
    '''Collection of libraries '''

    is_updated: bool = None
    '''

    :type: bool
    '''

    def tag(self, value: bool):
        '''tag 

        :param value: Value 
        :type value: bool
        '''
        pass

    def load(self, filepath: str, link: bool = False, relative: bool = False):
        '''Returns a context manager which exposes 2 library objects on entering. Each object has attributes matching bpy.data which are lists of strings to be linked. 

        :param filepath: The path to a blend file. 
        :type filepath: str
        :param link: When False reference to the original file is lost. 
        :type link: bool
        :param relative: When True the path is stored relative to the open blend file. 
        :type relative: bool
        '''
        pass

    def write(self,
              filepath: str,
              datablocks: set,
              relative_remap: bool = False,
              fake_user: bool = False,
              compress: bool = False):
        '''Write data-blocks into a blend file. 

        :param filepath: The path to write the blend-file. 
        :type filepath: str
        :param datablocks: set of data-blocks (bpy.types.ID instances). 
        :type datablocks: set
        :param relative_remap: When True, remap the paths relative to the current blend-file. 
        :type relative_remap: bool
        :param fake_user: When True, data-blocks will be written with fake-user flag enabled. 
        :type fake_user: bool
        :param compress: When True, write a compressed blend file. 
        :type compress: bool
        '''
        pass


class BlendDataLineStyles:
    '''Collection of line styles '''

    is_updated: bool = None
    '''

    :type: bool
    '''

    def tag(self, value: bool):
        '''tag 

        :param value: Value 
        :type value: bool
        '''
        pass

    def new(self, name: str) -> 'FreestyleLineStyle':
        '''Add a new line style instance to the main database 

        :param name: New name for the data-block 
        :type name: str
        :rtype: 'FreestyleLineStyle'
        :return:  New line style data-block 
        '''
        pass

    def remove(self,
               linestyle: 'FreestyleLineStyle',
               do_unlink: bool = True,
               do_id_user: bool = True,
               do_ui_user: bool = True):
        '''Remove a line style instance from the current blendfile 

        :param linestyle: Line style to remove 
        :type linestyle: 'FreestyleLineStyle'
        :param do_unlink: Unlink all usages of this line style before deleting it 
        :type do_unlink: bool
        :param do_id_user: Decrement user counter of all datablocks used by this line style 
        :type do_id_user: bool
        :param do_ui_user: Make sure interface does not reference this line style 
        :type do_ui_user: bool
        '''
        pass


class BlendDataMasks:
    '''Collection of masks '''

    is_updated: bool = None
    '''

    :type: bool
    '''

    def tag(self, value: bool):
        '''tag 

        :param value: Value 
        :type value: bool
        '''
        pass

    def new(self, name: str = "") -> 'Mask':
        '''Add a new mask with a given name to the main database 

        :param name: Mask, Name of new mask data-block 
        :type name: str
        :rtype: 'Mask'
        :return:  New mask data-block 
        '''
        pass

    def remove(self,
               mask: 'Mask',
               do_unlink: bool = True,
               do_id_user: bool = True,
               do_ui_user: bool = True):
        '''Remove a masks from the current blendfile. 

        :param mask: Mask to remove 
        :type mask: 'Mask'
        :param do_unlink: Unlink all usages of this mask before deleting it 
        :type do_unlink: bool
        :param do_id_user: Decrement user counter of all datablocks used by this mask 
        :type do_id_user: bool
        :param do_ui_user: Make sure interface does not reference this mask 
        :type do_ui_user: bool
        '''
        pass


class BlendDataMaterials:
    '''Collection of materials '''

    is_updated: bool = None
    '''

    :type: bool
    '''

    def new(self, name: str) -> 'Material':
        '''Add a new material to the main database 

        :param name: New name for the data-block 
        :type name: str
        :rtype: 'Material'
        :return:  New material data-block 
        '''
        pass

    def remove(self,
               material: 'Material',
               do_unlink: bool = True,
               do_id_user: bool = True,
               do_ui_user: bool = True):
        '''Remove a material from the current blendfile 

        :param material: Material to remove 
        :type material: 'Material'
        :param do_unlink: Unlink all usages of this material before deleting it 
        :type do_unlink: bool
        :param do_id_user: Decrement user counter of all datablocks used by this material 
        :type do_id_user: bool
        :param do_ui_user: Make sure interface does not reference this material 
        :type do_ui_user: bool
        '''
        pass

    def tag(self, value: bool):
        '''tag 

        :param value: Value 
        :type value: bool
        '''
        pass


class BlendDataMeshes:
    '''Collection of meshes '''

    is_updated: bool = None
    '''

    :type: bool
    '''

    def new(self, name: str) -> 'Mesh':
        '''Add a new mesh to the main database 

        :param name: New name for the data-block 
        :type name: str
        :rtype: 'Mesh'
        :return:  New mesh data-block 
        '''
        pass

    def new_from_object(self,
                        scene: 'Scene',
                        object: 'Object',
                        apply_modifiers: bool,
                        settings: typing.Union[int, str],
                        calc_tessface: bool = True,
                        calc_undeformed: bool = False) -> 'Mesh':
        '''Add a new mesh created from object with modifiers applied 

        :param scene: Scene within which to evaluate modifiers 
        :type scene: 'Scene'
        :param object: Object to create mesh from 
        :type object: 'Object'
        :param apply_modifiers: Apply modifiers 
        :type apply_modifiers: bool
        :param settings: Modifier settings to applyPREVIEW Preview, Apply modifier preview settings.RENDER Render, Apply modifier render settings. 
        :type settings: typing.Union[int, str]
        :param calc_tessface: Calculate Tessellation, Calculate tessellation faces 
        :type calc_tessface: bool
        :param calc_undeformed: Calculate Undeformed, Calculate undeformed vertex coordinates 
        :type calc_undeformed: bool
        :rtype: 'Mesh'
        :return:  Mesh created from object, remove it if it is only used for export 
        '''
        pass

    def remove(self,
               mesh: 'Mesh',
               do_unlink: bool = True,
               do_id_user: bool = True,
               do_ui_user: bool = True):
        '''Remove a mesh from the current blendfile 

        :param mesh: Mesh to remove 
        :type mesh: 'Mesh'
        :param do_unlink: Unlink all usages of this mesh before deleting it (WARNING: will also delete objects instancing that mesh data) 
        :type do_unlink: bool
        :param do_id_user: Decrement user counter of all datablocks used by this mesh data 
        :type do_id_user: bool
        :param do_ui_user: Make sure interface does not reference this mesh data 
        :type do_ui_user: bool
        '''
        pass

    def tag(self, value: bool):
        '''tag 

        :param value: Value 
        :type value: bool
        '''
        pass


class BlendDataMetaBalls:
    '''Collection of metaballs '''

    is_updated: bool = None
    '''

    :type: bool
    '''

    def new(self, name: str) -> 'MetaBall':
        '''Add a new metaball to the main database 

        :param name: New name for the data-block 
        :type name: str
        :rtype: 'MetaBall'
        :return:  New metaball data-block 
        '''
        pass

    def remove(self,
               metaball: 'MetaBall',
               do_unlink: bool = True,
               do_id_user: bool = True,
               do_ui_user: bool = True):
        '''Remove a metaball from the current blendfile 

        :param metaball: Metaball to remove 
        :type metaball: 'MetaBall'
        :param do_unlink: Unlink all usages of this metaball before deleting it (WARNING: will also delete objects instancing that metaball data) 
        :type do_unlink: bool
        :param do_id_user: Decrement user counter of all datablocks used by this metaball data 
        :type do_id_user: bool
        :param do_ui_user: Make sure interface does not reference this metaball data 
        :type do_ui_user: bool
        '''
        pass

    def tag(self, value: bool):
        '''tag 

        :param value: Value 
        :type value: bool
        '''
        pass


class BlendDataMovieClips:
    '''Collection of movie clips '''

    is_updated: bool = None
    '''

    :type: bool
    '''

    def tag(self, value: bool):
        '''tag 

        :param value: Value 
        :type value: bool
        '''
        pass

    def remove(self,
               clip: 'MovieClip',
               do_unlink: bool = True,
               do_id_user: bool = True,
               do_ui_user: bool = True):
        '''Remove a movie clip from the current blendfile. 

        :param clip: Movie clip to remove 
        :type clip: 'MovieClip'
        :param do_unlink: Unlink all usages of this movie clip before deleting it 
        :type do_unlink: bool
        :param do_id_user: Decrement user counter of all datablocks used by this movie clip 
        :type do_id_user: bool
        :param do_ui_user: Make sure interface does not reference this movie clip 
        :type do_ui_user: bool
        '''
        pass

    def load(self, filepath: str, check_existing: bool = False) -> 'MovieClip':
        '''Add a new movie clip to the main database from a file (while check_existing is disabled for consistency with other load functions, behavior with multiple movie-clips using the same file may incorrectly generate proxies) 

        :param filepath: path for the data-block 
        :type filepath: str
        :param check_existing: Using existing data-block if this file is already loaded 
        :type check_existing: bool
        :rtype: 'MovieClip'
        :return:  New movie clip data-block 
        '''
        pass


class BlendDataNodeTrees:
    '''Collection of node trees '''

    is_updated: bool = None
    '''

    :type: bool
    '''

    def new(self, name: str, type: typing.Union[int, str]) -> 'NodeTree':
        '''Add a new node tree to the main database 

        :param name: New name for the data-block 
        :type name: str
        :param type: Type, The type of node_group to add 
        :type type: typing.Union[int, str]
        :rtype: 'NodeTree'
        :return:  New node tree data-block 
        '''
        pass

    def remove(self,
               tree: 'NodeTree',
               do_unlink: bool = True,
               do_id_user: bool = True,
               do_ui_user: bool = True):
        '''Remove a node tree from the current blendfile 

        :param tree: Node tree to remove 
        :type tree: 'NodeTree'
        :param do_unlink: Unlink all usages of this node tree before deleting it 
        :type do_unlink: bool
        :param do_id_user: Decrement user counter of all datablocks used by this node tree 
        :type do_id_user: bool
        :param do_ui_user: Make sure interface does not reference this node tree 
        :type do_ui_user: bool
        '''
        pass

    def tag(self, value: bool):
        '''tag 

        :param value: Value 
        :type value: bool
        '''
        pass


class BlendDataObjects:
    '''Collection of objects '''

    is_updated: bool = None
    '''

    :type: bool
    '''

    def new(self, name: str, object_data: 'ID') -> 'Object':
        '''Add a new object to the main database 

        :param name: New name for the data-block 
        :type name: str
        :param object_data: Object data or None for an empty object 
        :type object_data: 'ID'
        :rtype: 'Object'
        :return:  New object data-block 
        '''
        pass

    def remove(self,
               object: 'Object',
               do_unlink: bool = True,
               do_id_user: bool = True,
               do_ui_user: bool = True):
        '''Remove a object from the current blendfile 

        :param object: Object to remove 
        :type object: 'Object'
        :param do_unlink: Unlink all usages of this object before deleting it 
        :type do_unlink: bool
        :param do_id_user: Decrement user counter of all datablocks used by this object 
        :type do_id_user: bool
        :param do_ui_user: Make sure interface does not reference this object 
        :type do_ui_user: bool
        '''
        pass

    def tag(self, value: bool):
        '''tag 

        :param value: Value 
        :type value: bool
        '''
        pass


class BlendDataPaintCurves:
    '''Collection of paint curves '''

    is_updated: bool = None
    '''

    :type: bool
    '''

    def tag(self, value: bool):
        '''tag 

        :param value: Value 
        :type value: bool
        '''
        pass


class BlendDataPalettes:
    '''Collection of palettes '''

    is_updated: bool = None
    '''

    :type: bool
    '''

    def new(self, name: str) -> 'Palette':
        '''Add a new palette to the main database 

        :param name: New name for the data-block 
        :type name: str
        :rtype: 'Palette'
        :return:  New palette data-block 
        '''
        pass

    def remove(self,
               palette: 'Palette',
               do_unlink: bool = True,
               do_id_user: bool = True,
               do_ui_user: bool = True):
        '''Remove a palette from the current blendfile 

        :param palette: Palette to remove 
        :type palette: 'Palette'
        :param do_unlink: Unlink all usages of this palette before deleting it 
        :type do_unlink: bool
        :param do_id_user: Decrement user counter of all datablocks used by this palette 
        :type do_id_user: bool
        :param do_ui_user: Make sure interface does not reference this palette 
        :type do_ui_user: bool
        '''
        pass

    def tag(self, value: bool):
        '''tag 

        :param value: Value 
        :type value: bool
        '''
        pass


class BlendDataParticles:
    '''Collection of particle settings '''

    is_updated: bool = None
    '''

    :type: bool
    '''

    def new(self, name: str) -> 'ParticleSettings':
        '''Add a new particle settings instance to the main database 

        :param name: New name for the data-block 
        :type name: str
        :rtype: 'ParticleSettings'
        :return:  New particle settings data-block 
        '''
        pass

    def remove(self,
               particle: 'ParticleSettings',
               do_unlink: bool = True,
               do_id_user: bool = True,
               do_ui_user: bool = True):
        '''Remove a particle settings instance from the current blendfile 

        :param particle: Particle Settings to remove 
        :type particle: 'ParticleSettings'
        :param do_unlink: Unlink all usages of those particle settings before deleting them 
        :type do_unlink: bool
        :param do_id_user: Decrement user counter of all datablocks used by this particle settings 
        :type do_id_user: bool
        :param do_ui_user: Make sure interface does not reference this particle settings 
        :type do_ui_user: bool
        '''
        pass

    def tag(self, value: bool):
        '''tag 

        :param value: Value 
        :type value: bool
        '''
        pass


class BlendDataScenes:
    '''Collection of scenes '''

    is_updated: bool = None
    '''

    :type: bool
    '''

    def new(self, name: str) -> 'Scene':
        '''Add a new scene to the main database 

        :param name: New name for the data-block 
        :type name: str
        :rtype: 'Scene'
        :return:  New scene data-block 
        '''
        pass

    def remove(self, scene: 'Scene', do_unlink: bool = True):
        '''Remove a scene from the current blendfile 

        :param scene: Scene to remove 
        :type scene: 'Scene'
        :param do_unlink: Unlink all usages of this scene before deleting it 
        :type do_unlink: bool
        '''
        pass

    def tag(self, value: bool):
        '''tag 

        :param value: Value 
        :type value: bool
        '''
        pass


class BlendDataScreens:
    '''Collection of screens '''

    is_updated: bool = None
    '''

    :type: bool
    '''

    def tag(self, value: bool):
        '''tag 

        :param value: Value 
        :type value: bool
        '''
        pass


class BlendDataSounds:
    '''Collection of sounds '''

    is_updated: bool = None
    '''

    :type: bool
    '''

    def load(self, filepath: str, check_existing: bool = False) -> 'Sound':
        '''Add a new sound to the main database from a file 

        :param filepath: path for the data-block 
        :type filepath: str
        :param check_existing: Using existing data-block if this file is already loaded 
        :type check_existing: bool
        :rtype: 'Sound'
        :return:  New text data-block 
        '''
        pass

    def remove(self,
               sound: 'Sound',
               do_unlink: bool = True,
               do_id_user: bool = True,
               do_ui_user: bool = True):
        '''Remove a sound from the current blendfile 

        :param sound: Sound to remove 
        :type sound: 'Sound'
        :param do_unlink: Unlink all usages of this sound before deleting it 
        :type do_unlink: bool
        :param do_id_user: Decrement user counter of all datablocks used by this sound 
        :type do_id_user: bool
        :param do_ui_user: Make sure interface does not reference this sound 
        :type do_ui_user: bool
        '''
        pass

    def tag(self, value: bool):
        '''tag 

        :param value: Value 
        :type value: bool
        '''
        pass


class BlendDataSpeakers:
    '''Collection of speakers '''

    is_updated: bool = None
    '''

    :type: bool
    '''

    def new(self, name: str) -> 'Speaker':
        '''Add a new speaker to the main database 

        :param name: New name for the data-block 
        :type name: str
        :rtype: 'Speaker'
        :return:  New speaker data-block 
        '''
        pass

    def remove(self,
               speaker: 'Speaker',
               do_unlink: bool = True,
               do_id_user: bool = True,
               do_ui_user: bool = True):
        '''Remove a speaker from the current blendfile 

        :param speaker: Speaker to remove 
        :type speaker: 'Speaker'
        :param do_unlink: Unlink all usages of this speaker before deleting it (WARNING: will also delete objects instancing that speaker data) 
        :type do_unlink: bool
        :param do_id_user: Decrement user counter of all datablocks used by this speaker data 
        :type do_id_user: bool
        :param do_ui_user: Make sure interface does not reference this speaker data 
        :type do_ui_user: bool
        '''
        pass

    def tag(self, value: bool):
        '''tag 

        :param value: Value 
        :type value: bool
        '''
        pass


class BlendDataTexts:
    '''Collection of texts '''

    is_updated: bool = None
    '''

    :type: bool
    '''

    def new(self, name: str) -> 'Text':
        '''Add a new text to the main database 

        :param name: New name for the data-block 
        :type name: str
        :rtype: 'Text'
        :return:  New text data-block 
        '''
        pass

    def remove(self,
               text: 'Text',
               do_unlink: bool = True,
               do_id_user: bool = True,
               do_ui_user: bool = True):
        '''Remove a text from the current blendfile 

        :param text: Text to remove 
        :type text: 'Text'
        :param do_unlink: Unlink all usages of this text before deleting it 
        :type do_unlink: bool
        :param do_id_user: Decrement user counter of all datablocks used by this text 
        :type do_id_user: bool
        :param do_ui_user: Make sure interface does not reference this text 
        :type do_ui_user: bool
        '''
        pass

    def load(self, filepath: str, internal: bool = False) -> 'Text':
        '''Add a new text to the main database from a file 

        :param filepath: path for the data-block 
        :type filepath: str
        :param internal: Make internal, Make text file internal after loading 
        :type internal: bool
        :rtype: 'Text'
        :return:  New text data-block 
        '''
        pass

    def tag(self, value: bool):
        '''tag 

        :param value: Value 
        :type value: bool
        '''
        pass


class BlendDataTextures:
    '''Collection of groups '''

    is_updated: bool = None
    '''

    :type: bool
    '''

    def new(self, name: str, type: typing.Union[int, str]) -> 'Texture':
        '''Add a new texture to the main database 

        :param name: New name for the data-block 
        :type name: str
        :param type: Type, The type of texture to addNONE None.BLEND Blend, Procedural - create a ramp texture.CLOUDS Clouds, Procedural - create a cloud-like fractal noise texture.DISTORTED_NOISE Distorted Noise, Procedural - noise texture distorted by two noise algorithms.ENVIRONMENT_MAP Environment Map, Create a render of the environment mapped to a texture.IMAGE Image or Movie, Allow for images or movies to be used as textures.MAGIC Magic, Procedural - color texture based on trigonometric functions.MARBLE Marble, Procedural - marble-like noise texture with wave generated bands.MUSGRAVE Musgrave, Procedural - highly flexible fractal noise texture.NOISE Noise, Procedural - random noise, gives a different result every time, for every frame, for every pixel.OCEAN Ocean, Use a texture generated by an Ocean modifier.POINT_DENSITY Point Density.STUCCI Stucci, Procedural - create a fractal noise texture.VORONOI Voronoi, Procedural - create cell-like patterns based on Worley noise.VOXEL_DATA Voxel Data, Create a 3D texture based on volumetric data.WOOD Wood, Procedural - wave generated bands or rings, with optional noise. 
        :type type: typing.Union[int, str]
        :rtype: 'Texture'
        :return:  New texture data-block 
        '''
        pass

    def remove(self,
               texture: 'Texture',
               do_unlink: bool = True,
               do_id_user: bool = True,
               do_ui_user: bool = True):
        '''Remove a texture from the current blendfile 

        :param texture: Texture to remove 
        :type texture: 'Texture'
        :param do_unlink: Unlink all usages of this texture before deleting it 
        :type do_unlink: bool
        :param do_id_user: Decrement user counter of all datablocks used by this texture 
        :type do_id_user: bool
        :param do_ui_user: Make sure interface does not reference this texture 
        :type do_ui_user: bool
        '''
        pass

    def tag(self, value: bool):
        '''tag 

        :param value: Value 
        :type value: bool
        '''
        pass


class BlendDataWindowManagers:
    '''Collection of window managers '''

    is_updated: bool = None
    '''

    :type: bool
    '''

    def tag(self, value: bool):
        '''tag 

        :param value: Value 
        :type value: bool
        '''
        pass


class BlendDataWorlds:
    '''Collection of worlds '''

    is_updated: bool = None
    '''

    :type: bool
    '''

    def new(self, name: str) -> 'World':
        '''Add a new world to the main database 

        :param name: New name for the data-block 
        :type name: str
        :rtype: 'World'
        :return:  New world data-block 
        '''
        pass

    def remove(self,
               world: 'World',
               do_unlink: bool = True,
               do_id_user: bool = True,
               do_ui_user: bool = True):
        '''Remove a world from the current blendfile 

        :param world: World to remove 
        :type world: 'World'
        :param do_unlink: Unlink all usages of this world before deleting it 
        :type do_unlink: bool
        :param do_id_user: Decrement user counter of all datablocks used by this world 
        :type do_id_user: bool
        :param do_ui_user: Make sure interface does not reference this world 
        :type do_ui_user: bool
        '''
        pass

    def tag(self, value: bool):
        '''tag 

        :param value: Value 
        :type value: bool
        '''
        pass


class BlendTexture:
    '''Procedural color blending texture '''

    progression: typing.Union[int, str] = None
    '''Style of the color blending 

    :type: typing.Union[int, str]
    '''

    use_flip_axis: typing.Union[int, str] = None
    '''Flip the texture’s X and Y axis 

    :type: typing.Union[int, str]
    '''

    users_material = None
    '''Materials that use this texture (readonly) '''

    users_object_modifier = None
    '''Object modifiers that use this texture (readonly) '''


class BlenderRNA:
    '''Blender RNA structure definitions '''

    structs: typing.List['Struct'] = None
    '''

    :type: typing.List['Struct']
    '''


class BoidRule:
    name: str = None
    '''Boid rule name 

    :type: str
    '''

    type: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    use_in_air: bool = None
    '''Use rule when boid is flying 

    :type: bool
    '''

    use_on_land: bool = None
    '''Use rule when boid is on land 

    :type: bool
    '''


class BoidRuleAverageSpeed:
    level: float = None
    '''How much velocity’s z-component is kept constant 

    :type: float
    '''

    speed: float = None
    '''Percentage of maximum speed 

    :type: float
    '''

    wander: float = None
    '''How fast velocity’s direction is randomized 

    :type: float
    '''


class BoidRuleAvoid:
    fear_factor: float = None
    '''Avoid object if danger from it is above this threshold 

    :type: float
    '''

    object: 'Object' = None
    '''Object to avoid 

    :type: 'Object'
    '''

    use_predict: bool = None
    '''Predict target movement 

    :type: bool
    '''


class BoidRuleAvoidCollision:
    look_ahead: float = None
    '''Time to look ahead in seconds 

    :type: float
    '''

    use_avoid: bool = None
    '''Avoid collision with other boids 

    :type: bool
    '''

    use_avoid_collision: bool = None
    '''Avoid collision with deflector objects 

    :type: bool
    '''


class BoidRuleFight:
    distance: float = None
    '''Attack boids at max this distance 

    :type: float
    '''

    flee_distance: float = None
    '''Flee to this distance 

    :type: float
    '''


class BoidRuleFollowLeader:
    distance: float = None
    '''Distance behind leader to follow 

    :type: float
    '''

    object: 'Object' = None
    '''Follow this object instead of a boid 

    :type: 'Object'
    '''

    queue_count: int = None
    '''How many boids in a line 

    :type: int
    '''

    use_line: bool = None
    '''Follow leader in a line 

    :type: bool
    '''


class BoidRuleGoal:
    object: 'Object' = None
    '''Goal object 

    :type: 'Object'
    '''

    use_predict: bool = None
    '''Predict target movement 

    :type: bool
    '''


class BoidSettings:
    '''Settings for boid physics '''

    accuracy: float = None
    '''Accuracy of attack 

    :type: float
    '''

    active_boid_state: 'BoidRule' = None
    '''

    :type: 'BoidRule'
    '''

    active_boid_state_index: int = None
    '''

    :type: int
    '''

    aggression: float = None
    '''Boid will fight this times stronger enemy 

    :type: float
    '''

    air_acc_max: float = None
    '''Maximum acceleration in air (relative to maximum speed) 

    :type: float
    '''

    air_ave_max: float = None
    '''Maximum angular velocity in air (relative to 180 degrees) 

    :type: float
    '''

    air_personal_space: float = None
    '''Radius of boids personal space in air (% of particle size) 

    :type: float
    '''

    air_speed_max: float = None
    '''Maximum speed in air 

    :type: float
    '''

    air_speed_min: float = None
    '''Minimum speed in air (relative to maximum speed) 

    :type: float
    '''

    bank: float = None
    '''Amount of rotation around velocity vector on turns 

    :type: float
    '''

    health: float = None
    '''Initial boid health when born 

    :type: float
    '''

    height: float = None
    '''Boid height relative to particle size 

    :type: float
    '''

    land_acc_max: float = None
    '''Maximum acceleration on land (relative to maximum speed) 

    :type: float
    '''

    land_ave_max: float = None
    '''Maximum angular velocity on land (relative to 180 degrees) 

    :type: float
    '''

    land_jump_speed: float = None
    '''Maximum speed for jumping 

    :type: float
    '''

    land_personal_space: float = None
    '''Radius of boids personal space on land (% of particle size) 

    :type: float
    '''

    land_smooth: float = None
    '''How smoothly the boids land 

    :type: float
    '''

    land_speed_max: float = None
    '''Maximum speed on land 

    :type: float
    '''

    land_stick_force: float = None
    '''How strong a force must be to start effecting a boid on land 

    :type: float
    '''

    pitch: float = None
    '''Amount of rotation around side vector 

    :type: float
    '''

    range: float = None
    '''Maximum distance from which a boid can attack 

    :type: float
    '''

    states: typing.List['BoidState'] = None
    '''

    :type: typing.List['BoidState']
    '''

    strength: float = None
    '''Maximum caused damage on attack per second 

    :type: float
    '''

    use_climb: bool = None
    '''Allow boids to climb goal objects 

    :type: bool
    '''

    use_flight: bool = None
    '''Allow boids to move in air 

    :type: bool
    '''

    use_land: bool = None
    '''Allow boids to move on land 

    :type: bool
    '''


class BoidState:
    '''Boid state for boid physics '''

    active_boid_rule: 'BoidRule' = None
    '''

    :type: 'BoidRule'
    '''

    active_boid_rule_index: int = None
    '''

    :type: int
    '''

    falloff: float = None
    '''

    :type: float
    '''

    name: str = None
    '''Boid state name 

    :type: str
    '''

    rule_fuzzy: float = None
    '''

    :type: float
    '''

    rules: typing.List['BoidRule'] = None
    '''

    :type: typing.List['BoidRule']
    '''

    ruleset_type: typing.Union[int, str] = None
    '''How the rules in the list are evaluated 

    :type: typing.Union[int, str]
    '''

    volume: float = None
    '''

    :type: float
    '''


class Bone:
    '''Bone in an Armature data-block '''

    bbone_curveinx: float = None
    '''X-axis handle offset for start of the B-Bone’s curve, adjusts curvature 

    :type: float
    '''

    bbone_curveiny: float = None
    '''Y-axis handle offset for start of the B-Bone’s curve, adjusts curvature 

    :type: float
    '''

    bbone_curveoutx: float = None
    '''X-axis handle offset for end of the B-Bone’s curve, adjusts curvature 

    :type: float
    '''

    bbone_curveouty: float = None
    '''Y-axis handle offset for end of the B-Bone’s curve, adjusts curvature 

    :type: float
    '''

    bbone_in: float = None
    '''Length of first Bezier Handle (for B-Bones only) 

    :type: float
    '''

    bbone_out: float = None
    '''Length of second Bezier Handle (for B-Bones only) 

    :type: float
    '''

    bbone_rollin: float = None
    '''Roll offset for the start of the B-Bone, adjusts twist 

    :type: float
    '''

    bbone_rollout: float = None
    '''Roll offset for the end of the B-Bone, adjusts twist 

    :type: float
    '''

    bbone_scalein: float = None
    '''Scale factor for start of the B-Bone, adjusts thickness (for tapering effects) 

    :type: float
    '''

    bbone_scaleout: float = None
    '''Scale factor for end of the B-Bone, adjusts thickness (for tapering effects) 

    :type: float
    '''

    bbone_segments: int = None
    '''Number of subdivisions of bone (for B-Bones only) 

    :type: int
    '''

    bbone_x: float = None
    '''B-Bone X size 

    :type: float
    '''

    bbone_z: float = None
    '''B-Bone Z size 

    :type: float
    '''

    children: typing.List['Bone'] = None
    '''Bones which are children of this bone 

    :type: typing.List['Bone']
    '''

    envelope_distance: float = None
    '''Bone deformation distance (for Envelope deform only) 

    :type: float
    '''

    envelope_weight: float = None
    '''Bone deformation weight (for Envelope deform only) 

    :type: float
    '''

    head: float = None
    '''Location of head end of the bone relative to its parent 

    :type: float
    '''

    head_local: float = None
    '''Location of head end of the bone relative to armature 

    :type: float
    '''

    head_radius: float = None
    '''Radius of head of bone (for Envelope deform only) 

    :type: float
    '''

    hide: bool = None
    '''Bone is not visible when it is not in Edit Mode (i.e. in Object or Pose Modes) 

    :type: bool
    '''

    hide_select: bool = None
    '''Bone is able to be selected 

    :type: bool
    '''

    layers: bool = None
    '''Layers bone exists in 

    :type: bool
    '''

    matrix: float = None
    '''3x3 bone matrix 

    :type: float
    '''

    matrix_local: float = None
    '''4x4 bone matrix relative to armature 

    :type: float
    '''

    name: str = None
    '''

    :type: str
    '''

    parent: 'Bone' = None
    '''Parent bone (in same Armature) 

    :type: 'Bone'
    '''

    select: bool = None
    '''

    :type: bool
    '''

    select_head: bool = None
    '''

    :type: bool
    '''

    select_tail: bool = None
    '''

    :type: bool
    '''

    show_wire: bool = None
    '''Bone is always drawn as Wireframe regardless of viewport draw mode (useful for non-obstructive custom bone shapes) 

    :type: bool
    '''

    tail: float = None
    '''Location of tail end of the bone 

    :type: float
    '''

    tail_local: float = None
    '''Location of tail end of the bone relative to armature 

    :type: float
    '''

    tail_radius: float = None
    '''Radius of tail of bone (for Envelope deform only) 

    :type: float
    '''

    use_connect: bool = None
    '''When bone has a parent, bone’s head is stuck to the parent’s tail 

    :type: bool
    '''

    use_cyclic_offset: bool = None
    '''When bone doesn’t have a parent, it receives cyclic offset effects (Deprecated) 

    :type: bool
    '''

    use_deform: bool = None
    '''Enable Bone to deform geometry 

    :type: bool
    '''

    use_endroll_as_inroll: bool = None
    '''Use Roll Out of parent bone as Roll In of its children 

    :type: bool
    '''

    use_envelope_multiply: bool = None
    '''When deforming bone, multiply effects of Vertex Group weights with Envelope influence 

    :type: bool
    '''

    use_inherit_rotation: bool = None
    '''Bone inherits rotation or scale from parent bone 

    :type: bool
    '''

    use_inherit_scale: bool = None
    '''Bone inherits scaling from parent bone 

    :type: bool
    '''

    use_local_location: bool = None
    '''Bone location is set in local space 

    :type: bool
    '''

    use_relative_parent: bool = None
    '''Object children will use relative transform, like deform 

    :type: bool
    '''

    basename = None
    '''The name of this bone before any ‘.’ character (readonly) '''

    center = None
    '''The midpoint between the head and the tail. (readonly) '''

    children_recursive = None
    '''A list of all children from this bone. (readonly) '''

    children_recursive_basename = None
    '''Returns a chain of children with the same base name as this bone. Only direct chains are supported, forks caused by multiple children with matching base names will terminate the function and not be returned. (readonly) '''

    length = None
    '''The distance from head to tail, when set the head is moved to fit the length. '''

    parent_recursive = None
    '''A list of parents, starting with the immediate parent (readonly) '''

    vector = None
    '''The direction this bone is pointing. Utility function for (tail - head) (readonly) '''

    x_axis = None
    '''Vector pointing down the x-axis of the bone. (readonly) '''

    y_axis = None
    '''Vector pointing down the y-axis of the bone. (readonly) '''

    z_axis = None
    '''Vector pointing down the z-axis of the bone. (readonly) '''

    def evaluate_envelope(self, point: float) -> float:
        '''Calculate bone envelope at given point 

        :param point: Point, Position in 3d space to evaluate 
        :type point: float
        :rtype: float
        :return:  Factor, Envelope factor 
        '''
        pass

    def parent_index(self, parent_test):
        '''The same as ‘bone in other_bone.parent_recursive’ but saved generating a list. 

        '''
        pass

    def translate(self, vec):
        '''Utility function to add vec to the head and tail of this bone 

        '''
        pass


class BoneGroup:
    '''Groups of Pose Channels (Bones) '''

    color_set: typing.Union[int, str] = None
    '''Custom color set to use 

    :type: typing.Union[int, str]
    '''

    colors: 'ThemeBoneColorSet' = None
    '''Copy of the colors associated with the group’s color set 

    :type: 'ThemeBoneColorSet'
    '''

    is_custom_color_set: bool = None
    '''Color set is user-defined instead of a fixed theme color set 

    :type: bool
    '''

    name: str = None
    '''

    :type: str
    '''


class BoneGroups:
    '''Collection of bone groups '''

    active: 'BoneGroup' = None
    '''Active bone group for this pose 

    :type: 'BoneGroup'
    '''

    active_index: int = None
    '''Active index in bone groups array 

    :type: int
    '''

    def new(self, name: str = "Group") -> 'BoneGroup':
        '''Add a new bone group to the object 

        :param name: Name of the new group 
        :type name: str
        :rtype: 'BoneGroup'
        :return:  New bone group 
        '''
        pass

    def remove(self, group: 'BoneGroup'):
        '''Remove a bone group from this object 

        :param group: Removed bone group 
        :type group: 'BoneGroup'
        '''
        pass


class BoolProperty:
    '''RNA boolean property definition '''

    array_length: int = None
    '''Maximum length of the array, 0 means unlimited 

    :type: int
    '''

    default: bool = None
    '''Default value for this number 

    :type: bool
    '''

    default_array: bool = None
    '''Default value for this array 

    :type: bool
    '''

    is_array: bool = None
    '''

    :type: bool
    '''


class BooleanModifier:
    '''Boolean operations modifier '''

    debug_options: typing.Set[typing.Union[int, str]] = None
    '''Debugging options, only when started with ‘-d’ 

    :type: typing.Set[typing.Union[int, str]]
    '''

    double_threshold: float = None
    '''Threshold for checking overlapping geometry 

    :type: float
    '''

    object: 'Object' = None
    '''Mesh object to use for Boolean operation 

    :type: 'Object'
    '''

    operation: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    solver: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''


class BrightContrastModifier:
    '''Bright/contrast modifier data for sequence strip '''

    bright: float = None
    '''Adjust the luminosity of the colors 

    :type: float
    '''

    contrast: float = None
    '''Adjust the difference in luminosity between pixels 

    :type: float
    '''


class Brush:
    '''Brush data-block for storing brush settings for painting and sculpting '''

    auto_smooth_factor: float = None
    '''Amount of smoothing to automatically apply to each stroke 

    :type: float
    '''

    blend: typing.Union[int, str] = None
    '''Brush blending mode 

    :type: typing.Union[int, str]
    '''

    blur_kernel_radius: int = None
    '''Radius of kernel used for soften and sharpen in pixels 

    :type: int
    '''

    blur_mode: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    brush_capabilities: 'BrushCapabilities' = None
    '''Brush’s capabilities 

    :type: 'BrushCapabilities'
    '''

    clone_alpha: float = None
    '''Opacity of clone image display 

    :type: float
    '''

    clone_image: 'Image' = None
    '''Image for clone tool 

    :type: 'Image'
    '''

    clone_offset: float = None
    '''

    :type: float
    '''

    color: float = None
    '''

    :type: float
    '''

    crease_pinch_factor: float = None
    '''How much the crease brush pinches 

    :type: float
    '''

    cursor_color_add: float = None
    '''Color of cursor when adding 

    :type: float
    '''

    cursor_color_subtract: float = None
    '''Color of cursor when subtracting 

    :type: float
    '''

    cursor_overlay_alpha: int = None
    '''

    :type: int
    '''

    curve: 'CurveMapping' = None
    '''Editable falloff curve 

    :type: 'CurveMapping'
    '''

    direction: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    fill_threshold: float = None
    '''Threshold above which filling is not propagated 

    :type: float
    '''

    grad_spacing: int = None
    '''Spacing before brush gradient goes full circle 

    :type: int
    '''

    gradient: 'ColorRamp' = None
    '''

    :type: 'ColorRamp'
    '''

    gradient_fill_mode: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    gradient_stroke_mode: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    height: float = None
    '''Affectable height of brush (layer height for layer tool, i.e.) 

    :type: float
    '''

    icon_filepath: str = None
    '''File path to brush icon 

    :type: str
    '''

    image_paint_capabilities: 'ImapaintToolCapabilities' = None
    '''Brush’s capabilities in image paint mode 

    :type: 'ImapaintToolCapabilities'
    '''

    image_tool: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    jitter: float = None
    '''Jitter the position of the brush while painting 

    :type: float
    '''

    jitter_absolute: int = None
    '''Jitter the position of the brush in pixels while painting 

    :type: int
    '''

    mask_overlay_alpha: int = None
    '''

    :type: int
    '''

    mask_stencil_dimension: float = None
    '''Dimensions of mask stencil in viewport 

    :type: float
    '''

    mask_stencil_pos: float = None
    '''Position of mask stencil in viewport 

    :type: float
    '''

    mask_texture: 'Texture' = None
    '''

    :type: 'Texture'
    '''

    mask_texture_slot: 'BrushTextureSlot' = None
    '''

    :type: 'BrushTextureSlot'
    '''

    mask_tool: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    normal_weight: float = None
    '''How much grab will pull vertexes out of surface during a grab 

    :type: float
    '''

    paint_curve: 'PaintCurve' = None
    '''Active Paint Curve 

    :type: 'PaintCurve'
    '''

    plane_offset: float = None
    '''Adjust plane on which the brush acts towards or away from the object surface 

    :type: float
    '''

    plane_trim: float = None
    '''If a vertex is further away from offset plane than this, then it is not affected 

    :type: float
    '''

    rake_factor: float = None
    '''How much grab will follow cursor rotation 

    :type: float
    '''

    rate: float = None
    '''Interval between paints for Airbrush 

    :type: float
    '''

    sculpt_capabilities: 'SculptToolCapabilities' = None
    '''Brush’s capabilities in sculpt mode 

    :type: 'SculptToolCapabilities'
    '''

    sculpt_plane: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    sculpt_tool: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    secondary_color: float = None
    '''

    :type: float
    '''

    sharp_threshold: float = None
    '''Threshold below which, no sharpening is done 

    :type: float
    '''

    size: int = None
    '''Radius of the brush in pixels 

    :type: int
    '''

    smooth_stroke_factor: float = None
    '''Higher values give a smoother stroke 

    :type: float
    '''

    smooth_stroke_radius: int = None
    '''Minimum distance from last point before stroke continues 

    :type: int
    '''

    spacing: int = None
    '''Spacing between brush daubs as a percentage of brush diameter 

    :type: int
    '''

    stencil_dimension: float = None
    '''Dimensions of stencil in viewport 

    :type: float
    '''

    stencil_pos: float = None
    '''Position of stencil in viewport 

    :type: float
    '''

    strength: float = None
    '''How powerful the effect of the brush is when applied 

    :type: float
    '''

    stroke_method: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    texture: 'Texture' = None
    '''

    :type: 'Texture'
    '''

    texture_overlay_alpha: int = None
    '''

    :type: int
    '''

    texture_sample_bias: float = None
    '''Value added to texture samples 

    :type: float
    '''

    texture_slot: 'BrushTextureSlot' = None
    '''

    :type: 'BrushTextureSlot'
    '''

    unprojected_radius: float = None
    '''Radius of brush in Blender units 

    :type: float
    '''

    use_accumulate: bool = None
    '''Accumulate stroke daubs on top of each other 

    :type: bool
    '''

    use_adaptive_space: bool = None
    '''Space daubs according to surface orientation instead of screen space 

    :type: bool
    '''

    use_airbrush: bool = None
    '''Keep applying paint effect while holding mouse (spray) 

    :type: bool
    '''

    use_alpha: bool = None
    '''When this is disabled, lock alpha while painting 

    :type: bool
    '''

    use_anchor: bool = None
    '''Keep the brush anchored to the initial location 

    :type: bool
    '''

    use_cursor_overlay: bool = None
    '''Show cursor in viewport 

    :type: bool
    '''

    use_cursor_overlay_override: bool = None
    '''Don’t show overlay during a stroke 

    :type: bool
    '''

    use_curve: bool = None
    '''Define the stroke curve with a bezier curve. Dabs are separated according to spacing 

    :type: bool
    '''

    use_custom_icon: bool = None
    '''Set the brush icon from an image file 

    :type: bool
    '''

    use_edge_to_edge: bool = None
    '''Drag anchor brush from edge-to-edge 

    :type: bool
    '''

    use_frontface: bool = None
    '''Brush only affects vertexes that face the viewer 

    :type: bool
    '''

    use_gradient: bool = None
    '''Use Gradient by utilizing a sampling method 

    :type: bool
    '''

    use_inverse_smooth_pressure: bool = None
    '''Lighter pressure causes more smoothing to be applied 

    :type: bool
    '''

    use_line: bool = None
    '''Draw a line with dabs separated according to spacing 

    :type: bool
    '''

    use_locked_size: bool = None
    '''When locked brush stays same size relative to object; when unlocked brush size is given in pixels 

    :type: bool
    '''

    use_offset_pressure: bool = None
    '''Enable tablet pressure sensitivity for offset 

    :type: bool
    '''

    use_original_normal: bool = None
    '''When locked keep using normal of surface where stroke was initiated 

    :type: bool
    '''

    use_paint_image: bool = None
    '''Use this brush in texture paint mode 

    :type: bool
    '''

    use_paint_sculpt: bool = None
    '''Use this brush in sculpt mode 

    :type: bool
    '''

    use_paint_vertex: bool = None
    '''Use this brush in vertex paint mode 

    :type: bool
    '''

    use_paint_weight: bool = None
    '''Use this brush in weight paint mode 

    :type: bool
    '''

    use_persistent: bool = None
    '''Sculpt on a persistent layer of the mesh 

    :type: bool
    '''

    use_plane_trim: bool = None
    '''Enable Plane Trim 

    :type: bool
    '''

    use_pressure_jitter: bool = None
    '''Enable tablet pressure sensitivity for jitter 

    :type: bool
    '''

    use_pressure_masking: typing.Union[int, str] = None
    '''Pen pressure makes texture influence smaller 

    :type: typing.Union[int, str]
    '''

    use_pressure_size: bool = None
    '''Enable tablet pressure sensitivity for size 

    :type: bool
    '''

    use_pressure_spacing: bool = None
    '''Enable tablet pressure sensitivity for spacing 

    :type: bool
    '''

    use_pressure_strength: bool = None
    '''Enable tablet pressure sensitivity for strength 

    :type: bool
    '''

    use_primary_overlay: bool = None
    '''Show texture in viewport 

    :type: bool
    '''

    use_primary_overlay_override: bool = None
    '''Don’t show overlay during a stroke 

    :type: bool
    '''

    use_relative_jitter: bool = None
    '''Jittering happens in screen space, not relative to brush size 

    :type: bool
    '''

    use_restore_mesh: bool = None
    '''Allow a single dot to be carefully positioned 

    :type: bool
    '''

    use_secondary_overlay: bool = None
    '''Show texture in viewport 

    :type: bool
    '''

    use_secondary_overlay_override: bool = None
    '''Don’t show overlay during a stroke 

    :type: bool
    '''

    use_smooth_stroke: bool = None
    '''Brush lags behind mouse and follows a smoother path 

    :type: bool
    '''

    use_space: bool = None
    '''Limit brush application to the distance specified by spacing 

    :type: bool
    '''

    use_space_attenuation: bool = None
    '''Automatically adjust strength to give consistent results for different spacings 

    :type: bool
    '''

    vertex_tool: typing.Union[int, str] = None
    '''Brush blending mode 

    :type: typing.Union[int, str]
    '''

    weight: float = None
    '''Vertex weight when brush is applied 

    :type: float
    '''


class BrushCapabilities:
    '''Read-only indications of which brush operations are supported by the current brush '''

    has_overlay: bool = None
    '''

    :type: bool
    '''

    has_random_texture_angle: bool = None
    '''

    :type: bool
    '''

    has_smooth_stroke: bool = None
    '''

    :type: bool
    '''

    has_spacing: bool = None
    '''

    :type: bool
    '''


class BrushTextureSlot:
    '''Texture slot for textures in a Brush data-block '''

    angle: float = None
    '''Brush texture rotation 

    :type: float
    '''

    has_random_texture_angle: bool = None
    '''

    :type: bool
    '''

    has_texture_angle: bool = None
    '''

    :type: bool
    '''

    has_texture_angle_source: bool = None
    '''

    :type: bool
    '''

    map_mode: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    mask_map_mode: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    random_angle: float = None
    '''Brush texture random angle 

    :type: float
    '''

    tex_paint_map_mode: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    use_rake: bool = None
    '''

    :type: bool
    '''

    use_random: bool = None
    '''

    :type: bool
    '''


class BuildModifier:
    '''Build effect modifier '''

    frame_duration: float = None
    '''Total time the build effect requires 

    :type: float
    '''

    frame_start: float = None
    '''Start frame of the effect 

    :type: float
    '''

    seed: int = None
    '''Seed for random if used 

    :type: int
    '''

    use_random_order: bool = None
    '''Randomize the faces or edges during build 

    :type: bool
    '''

    use_reverse: bool = None
    '''Deconstruct the mesh instead of building it 

    :type: bool
    '''


class CLIP_UL_tracking_objects:
    def draw_item(self, context, layout, data, item, icon, active_data,
                  active_propname, index):
        '''

        '''
        pass


class CYCLES:
    def bake(self, scene, obj, pass_type, pass_filter, object_id, pixel_array,
             num_pixels, depth, result):
        '''

        '''
        pass

    def render(self, scene):
        '''

        '''
        pass

    def update(self, data, scene):
        '''

        '''
        pass

    def update_render_passes(self, scene, srl):
        '''

        '''
        pass

    def update_script_node(self, node):
        '''

        '''
        pass

    def view_draw(self, context):
        '''

        '''
        pass

    def view_update(self, context):
        '''

        '''
        pass


class CacheFile:
    animation_data: 'AnimData' = None
    '''Animation data for this data-block 

    :type: 'AnimData'
    '''

    filepath: str = None
    '''Path to external displacements file 

    :type: str
    '''

    forward_axis: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    frame: float = None
    '''The time to use for looking up the data in the cache file, or to determine which file to use in a file sequence 

    :type: float
    '''

    is_sequence: bool = None
    '''Whether the cache is separated in a series of files 

    :type: bool
    '''

    object_paths: typing.List['AlembicObjectPath'] = None
    '''Paths of the objects inside the Alembic archive 

    :type: typing.List['AlembicObjectPath']
    '''

    override_frame: bool = None
    '''Whether to use a custom frame for looking up data in the cache file, instead of using the current scene frame 

    :type: bool
    '''

    scale: float = None
    '''Value by which to enlarge or shrink the object with respect to the world’s origin (only applicable through a Transform Cache constraint) 

    :type: float
    '''

    up_axis: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''


class Camera:
    '''Camera data-block for storing camera settings '''

    angle: float = None
    '''Camera lens field of view 

    :type: float
    '''

    angle_x: float = None
    '''Camera lens horizontal field of view 

    :type: float
    '''

    angle_y: float = None
    '''Camera lens vertical field of view 

    :type: float
    '''

    animation_data: 'AnimData' = None
    '''Animation data for this data-block 

    :type: 'AnimData'
    '''

    clip_end: float = None
    '''Camera far clipping distance 

    :type: float
    '''

    clip_start: float = None
    '''Camera near clipping distance 

    :type: float
    '''

    cycles: 'CyclesCameraSettings' = None
    '''Cycles camera settings 

    :type: 'CyclesCameraSettings'
    '''

    dof_distance: float = None
    '''Distance to the focus point for depth of field 

    :type: float
    '''

    dof_object: 'Object' = None
    '''Use this object to define the depth of field focal point 

    :type: 'Object'
    '''

    draw_size: float = None
    '''Apparent size of the Camera object in the 3D View 

    :type: float
    '''

    gpu_dof: 'GPUDOFSettings' = None
    '''

    :type: 'GPUDOFSettings'
    '''

    lens: float = None
    '''Perspective Camera lens value in millimeters 

    :type: float
    '''

    lens_unit: typing.Union[int, str] = None
    '''Unit to edit lens in for the user interface 

    :type: typing.Union[int, str]
    '''

    ortho_scale: float = None
    '''Orthographic Camera scale (similar to zoom) 

    :type: float
    '''

    passepartout_alpha: float = None
    '''Opacity (alpha) of the darkened overlay in Camera view 

    :type: float
    '''

    sensor_fit: typing.Union[int, str] = None
    '''Method to fit image and field of view angle inside the sensor 

    :type: typing.Union[int, str]
    '''

    sensor_height: float = None
    '''Vertical size of the image sensor area in millimeters 

    :type: float
    '''

    sensor_width: float = None
    '''Horizontal size of the image sensor area in millimeters 

    :type: float
    '''

    shift_x: float = None
    '''Camera horizontal shift 

    :type: float
    '''

    shift_y: float = None
    '''Camera vertical shift 

    :type: float
    '''

    show_guide: typing.Set[typing.Union[int, str]] = None
    '''Draw overlay 

    :type: typing.Set[typing.Union[int, str]]
    '''

    show_limits: bool = None
    '''Draw the clipping range and focus point on the camera 

    :type: bool
    '''

    show_mist: bool = None
    '''Draw a line from the Camera to indicate the mist area 

    :type: bool
    '''

    show_name: bool = None
    '''Show the active Camera’s name in Camera view 

    :type: bool
    '''

    show_passepartout: bool = None
    '''Show a darkened overlay outside the image area in Camera view 

    :type: bool
    '''

    show_safe_areas: bool = None
    '''Show TV title safe and action safe areas in Camera view 

    :type: bool
    '''

    show_safe_center: bool = None
    '''Show safe areas to fit content in a different aspect ratio 

    :type: bool
    '''

    show_sensor: bool = None
    '''Show sensor size (film gate) in Camera view 

    :type: bool
    '''

    stereo: 'CameraStereoData' = None
    '''

    :type: 'CameraStereoData'
    '''

    type: typing.Union[int, str] = None
    '''Camera types 

    :type: typing.Union[int, str]
    '''

    def view_frame(self, scene: 'Scene' = None):
        '''Return 4 points for the cameras frame (before object transformation) 

        :param scene: Scene to use for aspect calculation, when omitted 1:1 aspect is used 
        :type scene: 'Scene'
        '''
        pass


class CameraActuator:
    axis: typing.Union[int, str] = None
    '''Axis the Camera will try to get behind 

    :type: typing.Union[int, str]
    '''

    damping: float = None
    '''Strength of the constraint that drives the camera behind the target 

    :type: float
    '''

    height: float = None
    '''

    :type: float
    '''

    max: float = None
    '''

    :type: float
    '''

    min: float = None
    '''

    :type: float
    '''

    object: 'Object' = None
    '''Look at this Object 

    :type: 'Object'
    '''


class CameraSolverConstraint:
    '''Lock motion to the reconstructed camera movement '''

    clip: 'MovieClip' = None
    '''Movie Clip to get tracking data from 

    :type: 'MovieClip'
    '''

    use_active_clip: bool = None
    '''Use active clip defined in scene 

    :type: bool
    '''


class CameraStereoData:
    '''Stereoscopy settings for a Camera data-block '''

    convergence_distance: float = None
    '''The converge point for the stereo cameras (often the distance between a projector and the projection screen) 

    :type: float
    '''

    convergence_mode: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    interocular_distance: float = None
    '''Set the distance between the eyes - the stereo plane distance / 30 should be fine 

    :type: float
    '''

    pivot: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    pole_merge_angle_from: float = None
    '''Angle at which interocular distance starts to fade to 0 

    :type: float
    '''

    pole_merge_angle_to: float = None
    '''Angle at which interocular distance is 0 

    :type: float
    '''

    use_pole_merge: bool = None
    '''Fade interocular distance to 0 after the given cutoff angle 

    :type: bool
    '''

    use_spherical_stereo: bool = None
    '''Render every pixel rotating the camera around the middle of the interocular distance 

    :type: bool
    '''


class CastModifier:
    '''Modifier to cast to other shapes '''

    cast_type: typing.Union[int, str] = None
    '''Target object shape 

    :type: typing.Union[int, str]
    '''

    factor: float = None
    '''

    :type: float
    '''

    object: 'Object' = None
    '''Control object: if available, its location determines the center of the effect 

    :type: 'Object'
    '''

    radius: float = None
    '''Only deform vertices within this distance from the center of the effect (leave as 0 for infinite.) 

    :type: float
    '''

    size: float = None
    '''Size of projection shape (leave as 0 for auto) 

    :type: float
    '''

    use_radius_as_size: bool = None
    '''Use radius as size of projection shape (0 = auto) 

    :type: bool
    '''

    use_transform: bool = None
    '''Use object transform to control projection shape 

    :type: bool
    '''

    use_x: bool = None
    '''

    :type: bool
    '''

    use_y: bool = None
    '''

    :type: bool
    '''

    use_z: bool = None
    '''

    :type: bool
    '''

    vertex_group: str = None
    '''Vertex group name 

    :type: str
    '''


class ChannelDriverVariables:
    '''Collection of channel driver Variables '''

    def new(self, ) -> 'DriverVariable':
        '''Add a new variable for the driver 

        :rtype: 'DriverVariable'
        :return:  Newly created Driver Variable 
        '''
        pass

    def remove(self, variable: 'DriverVariable'):
        '''Remove an existing variable from the driver 

        :param variable: Variable to remove from the driver 
        :type variable: 'DriverVariable'
        '''
        pass


class ChildOfConstraint:
    '''Create constraint-based parent-child relationship '''

    inverse_matrix: float = None
    '''Transformation matrix to apply before 

    :type: float
    '''

    subtarget: str = None
    '''

    :type: str
    '''

    target: 'Object' = None
    '''Target Object 

    :type: 'Object'
    '''

    use_location_x: bool = None
    '''Use X Location of Parent 

    :type: bool
    '''

    use_location_y: bool = None
    '''Use Y Location of Parent 

    :type: bool
    '''

    use_location_z: bool = None
    '''Use Z Location of Parent 

    :type: bool
    '''

    use_rotation_x: bool = None
    '''Use X Rotation of Parent 

    :type: bool
    '''

    use_rotation_y: bool = None
    '''Use Y Rotation of Parent 

    :type: bool
    '''

    use_rotation_z: bool = None
    '''Use Z Rotation of Parent 

    :type: bool
    '''

    use_scale_x: bool = None
    '''Use X Scale of Parent 

    :type: bool
    '''

    use_scale_y: bool = None
    '''Use Y Scale of Parent 

    :type: bool
    '''

    use_scale_z: bool = None
    '''Use Z Scale of Parent 

    :type: bool
    '''


class ChildParticle:
    '''Child particle interpolated from simulated or edited particles '''

    pass


class ClampToConstraint:
    '''Constrain an object’s location to the nearest point along the target path '''

    main_axis: typing.Union[int, str] = None
    '''Main axis of movement 

    :type: typing.Union[int, str]
    '''

    target: 'Object' = None
    '''Target Object (Curves only) 

    :type: 'Object'
    '''

    use_cyclic: bool = None
    '''Treat curve as cyclic curve (no clamping to curve bounding box) 

    :type: bool
    '''


class ClothCollisionSettings:
    '''Cloth simulation settings for self collision and collision with other objects '''

    collision_quality: int = None
    '''How many collision iterations should be done. (higher is better quality but slower) 

    :type: int
    '''

    damping: float = None
    '''Amount of velocity lost on collision 

    :type: float
    '''

    distance_min: float = None
    '''Minimum distance between collision objects before collision response takes in 

    :type: float
    '''

    distance_repel: float = None
    '''Maximum distance to apply repulsion force, must be greater than minimum distance 

    :type: float
    '''

    friction: float = None
    '''Friction force if a collision happened (higher = less movement) 

    :type: float
    '''

    group: 'Group' = None
    '''Limit colliders to this Group 

    :type: 'Group'
    '''

    repel_force: float = None
    '''Repulsion force to apply on cloth when close to colliding 

    :type: float
    '''

    self_collision_quality: int = None
    '''How many self collision iterations should be done (higher is better quality but slower) 

    :type: int
    '''

    self_distance_min: float = None
    '''0.5 means no distance at all, 1.0 is maximum distance 

    :type: float
    '''

    self_friction: float = None
    '''Friction/damping with self contact 

    :type: float
    '''

    use_collision: bool = None
    '''Enable collisions with other objects 

    :type: bool
    '''

    use_self_collision: bool = None
    '''Enable self collisions 

    :type: bool
    '''

    vertex_group_self_collisions: str = None
    '''Vertex group to define vertices which are not used during self collisions 

    :type: str
    '''


class ClothModifier:
    '''Cloth simulation modifier '''

    collision_settings: 'ClothCollisionSettings' = None
    '''

    :type: 'ClothCollisionSettings'
    '''

    hair_grid_max: float = None
    '''

    :type: float
    '''

    hair_grid_min: float = None
    '''

    :type: float
    '''

    hair_grid_resolution: int = None
    '''

    :type: int
    '''

    point_cache: 'PointCache' = None
    '''

    :type: 'PointCache'
    '''

    settings: 'ClothSettings' = None
    '''

    :type: 'ClothSettings'
    '''

    solver_result: 'ClothSolverResult' = None
    '''

    :type: 'ClothSolverResult'
    '''


class ClothSettings:
    '''Cloth simulation settings for an object '''

    air_damping: float = None
    '''Air has normally some thickness which slows falling things down 

    :type: float
    '''

    bending_damping: float = None
    '''Damping of bending motion 

    :type: float
    '''

    bending_stiffness: float = None
    '''Wrinkle coefficient (higher = less smaller but more big wrinkles) 

    :type: float
    '''

    bending_stiffness_max: float = None
    '''Maximum bending stiffness value 

    :type: float
    '''

    collider_friction: float = None
    '''

    :type: float
    '''

    density_strength: float = None
    '''Influence of target density on the simulation 

    :type: float
    '''

    density_target: float = None
    '''Maximum density of hair 

    :type: float
    '''

    effector_weights: 'EffectorWeights' = None
    '''

    :type: 'EffectorWeights'
    '''

    goal_default: float = None
    '''Default Goal (vertex target position) value, when no Vertex Group used 

    :type: float
    '''

    goal_friction: float = None
    '''Goal (vertex target position) friction 

    :type: float
    '''

    goal_max: float = None
    '''Goal maximum, vertex group weights are scaled to match this range 

    :type: float
    '''

    goal_min: float = None
    '''Goal minimum, vertex group weights are scaled to match this range 

    :type: float
    '''

    goal_spring: float = None
    '''Goal (vertex target position) spring stiffness 

    :type: float
    '''

    gravity: float = None
    '''Gravity or external force vector 

    :type: float
    '''

    internal_friction: float = None
    '''

    :type: float
    '''

    mass: float = None
    '''Mass of cloth material 

    :type: float
    '''

    pin_stiffness: float = None
    '''Pin (vertex target position) spring stiffness 

    :type: float
    '''

    quality: int = None
    '''Quality of the simulation in steps per frame (higher is better quality but slower) 

    :type: int
    '''

    rest_shape_key: 'ShapeKey' = None
    '''Shape key to use the rest spring lengths from 

    :type: 'ShapeKey'
    '''

    sewing_force_max: float = None
    '''Maximum sewing force 

    :type: float
    '''

    shrink_max: float = None
    '''Max amount to shrink cloth by 

    :type: float
    '''

    shrink_min: float = None
    '''Min amount to shrink cloth by 

    :type: float
    '''

    spring_damping: float = None
    '''Damping of cloth velocity (higher = more smooth, less jiggling) 

    :type: float
    '''

    structural_stiffness: float = None
    '''Overall stiffness of structure 

    :type: float
    '''

    structural_stiffness_max: float = None
    '''Maximum structural stiffness value 

    :type: float
    '''

    time_scale: float = None
    '''Cloth speed is multiplied by this value 

    :type: float
    '''

    use_dynamic_mesh: bool = None
    '''Make simulation respect deformations in the base mesh 

    :type: bool
    '''

    use_pin_cloth: bool = None
    '''Enable pinning of cloth vertices to other objects/positions 

    :type: bool
    '''

    use_sewing_springs: bool = None
    '''Pulls loose edges together 

    :type: bool
    '''

    use_stiffness_scale: bool = None
    '''If enabled, stiffness can be scaled along a weight painted vertex group 

    :type: bool
    '''

    vel_damping: float = None
    '''Damp velocity to help cloth reach the resting position faster (1.0 = no damping, 0.0 = fully dampened) 

    :type: float
    '''

    vertex_group_bending: str = None
    '''Vertex group for fine control over bending stiffness 

    :type: str
    '''

    vertex_group_mass: str = None
    '''Vertex Group for pinning of vertices 

    :type: str
    '''

    vertex_group_shrink: str = None
    '''Vertex Group for shrinking cloth 

    :type: str
    '''

    vertex_group_structural_stiffness: str = None
    '''Vertex group for fine control over structural stiffness 

    :type: str
    '''

    voxel_cell_size: float = None
    '''Size of the voxel grid cells for interaction effects 

    :type: float
    '''


class ClothSolverResult:
    '''Result of cloth solver iteration '''

    avg_error: float = None
    '''Average error during substeps 

    :type: float
    '''

    avg_iterations: float = None
    '''Average iterations during substeps 

    :type: float
    '''

    max_error: float = None
    '''Maximum error during substeps 

    :type: float
    '''

    max_iterations: int = None
    '''Maximum iterations during substeps 

    :type: int
    '''

    min_error: float = None
    '''Minimum error during substeps 

    :type: float
    '''

    min_iterations: int = None
    '''Minimum iterations during substeps 

    :type: int
    '''

    status: typing.Set[typing.Union[int, str]] = None
    '''Status of the solver iteration 

    :type: typing.Set[typing.Union[int, str]]
    '''


class CloudsTexture:
    '''Procedural noise texture '''

    cloud_type: typing.Union[int, str] = None
    '''Determine whether Noise returns grayscale or RGB values 

    :type: typing.Union[int, str]
    '''

    nabla: float = None
    '''Size of derivative offset used for calculating normal 

    :type: float
    '''

    noise_basis: typing.Union[int, str] = None
    '''Noise basis used for turbulence 

    :type: typing.Union[int, str]
    '''

    noise_depth: int = None
    '''Depth of the cloud calculation 

    :type: int
    '''

    noise_scale: float = None
    '''Scaling for noise input 

    :type: float
    '''

    noise_type: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    users_material = None
    '''Materials that use this texture (readonly) '''

    users_object_modifier = None
    '''Object modifiers that use this texture (readonly) '''


class CollectionProperty:
    '''RNA collection property to define lists, arrays and mappings '''

    fixed_type: 'Struct' = None
    '''Fixed pointer type, empty if variable type 

    :type: 'Struct'
    '''


class CollisionModifier:
    '''Collision modifier defining modifier stack position used for collision '''

    settings: 'CollisionSettings' = None
    '''

    :type: 'CollisionSettings'
    '''


class CollisionSensor:
    '''Sensor to detect objects colliding with the current object, with more settings than the Touch sensor '''

    material: str = None
    '''Only look for objects with this material (blank = all objects) 

    :type: str
    '''

    property: str = None
    '''Only look for objects with this property (blank = all objects) 

    :type: str
    '''

    use_material: bool = None
    '''Toggle collision on material or property 

    :type: bool
    '''

    use_pulse: bool = None
    '''Change to the set of colliding objects generates pulse 

    :type: bool
    '''


class CollisionSettings:
    '''Collision settings for object in physics simulation '''

    absorption: float = None
    '''How much of effector force gets lost during collision with this object (in percent) 

    :type: float
    '''

    damping: float = None
    '''Amount of damping during collision 

    :type: float
    '''

    damping_factor: float = None
    '''Amount of damping during particle collision 

    :type: float
    '''

    damping_random: float = None
    '''Random variation of damping 

    :type: float
    '''

    friction_factor: float = None
    '''Amount of friction during particle collision 

    :type: float
    '''

    friction_random: float = None
    '''Random variation of friction 

    :type: float
    '''

    permeability: float = None
    '''Chance that the particle will pass through the mesh 

    :type: float
    '''

    stickiness: float = None
    '''Amount of stickiness to surface collision 

    :type: float
    '''

    thickness_inner: float = None
    '''Inner face thickness (only used by softbodies) 

    :type: float
    '''

    thickness_outer: float = None
    '''Outer face thickness 

    :type: float
    '''

    use: bool = None
    '''Enable this objects as a collider for physics systems 

    :type: bool
    '''

    use_particle_kill: bool = None
    '''Kill collided particles 

    :type: bool
    '''


class ColorBalanceModifier:
    '''Color balance modifier for sequence strip '''

    color_balance: 'SequenceColorBalanceData' = None
    '''

    :type: 'SequenceColorBalanceData'
    '''

    color_multiply: float = None
    '''Multiply the intensity of each pixel 

    :type: float
    '''


class ColorManagedDisplaySettings:
    '''Color management specific to display device '''

    display_device: typing.Union[int, str] = None
    '''Display device name 

    :type: typing.Union[int, str]
    '''


class ColorManagedInputColorspaceSettings:
    '''Input color space settings '''

    name: typing.Union[int, str] = None
    '''Color space of the image or movie on disk 

    :type: typing.Union[int, str]
    '''


class ColorManagedSequencerColorspaceSettings:
    '''Input color space settings '''

    name: typing.Union[int, str] = None
    '''Color space that the sequencer operates in 

    :type: typing.Union[int, str]
    '''


class ColorManagedViewSettings:
    '''Color management settings used for displaying images on the display '''

    curve_mapping: 'CurveMapping' = None
    '''Color curve mapping applied before display transform 

    :type: 'CurveMapping'
    '''

    exposure: float = None
    '''Exposure (stops) applied before display transform 

    :type: float
    '''

    gamma: float = None
    '''Amount of gamma modification applied after display transform 

    :type: float
    '''

    look: typing.Union[int, str] = None
    '''Additional transform applied before view transform for an artistic needs 

    :type: typing.Union[int, str]
    '''

    use_curve_mapping: bool = None
    '''Use RGB curved for pre-display transformation 

    :type: bool
    '''

    view_transform: typing.Union[int, str] = None
    '''View used when converting image to a display space 

    :type: typing.Union[int, str]
    '''


class ColorMapping:
    '''Color mapping settings '''

    blend_color: float = None
    '''Blend color to mix with texture output color 

    :type: float
    '''

    blend_factor: float = None
    '''

    :type: float
    '''

    blend_type: typing.Union[int, str] = None
    '''Mode used to mix with texture output color 

    :type: typing.Union[int, str]
    '''

    brightness: float = None
    '''Adjust the brightness of the texture 

    :type: float
    '''

    color_ramp: 'ColorRamp' = None
    '''

    :type: 'ColorRamp'
    '''

    contrast: float = None
    '''Adjust the contrast of the texture 

    :type: float
    '''

    saturation: float = None
    '''Adjust the saturation of colors in the texture 

    :type: float
    '''

    use_color_ramp: bool = None
    '''Toggle color ramp operations 

    :type: bool
    '''


class ColorRamp:
    '''Color ramp mapping a scalar value to a color '''

    color_mode: typing.Union[int, str] = None
    '''Set color mode to use for interpolation 

    :type: typing.Union[int, str]
    '''

    elements: typing.List['ColorRampElements'] = None
    '''

    :type: typing.List['ColorRampElements']
    '''

    hue_interpolation: typing.Union[int, str] = None
    '''Set color interpolation 

    :type: typing.Union[int, str]
    '''

    interpolation: typing.Union[int, str] = None
    '''Set interpolation between color stops 

    :type: typing.Union[int, str]
    '''

    def evaluate(self, position: float) -> float:
        '''Evaluate ColorRamp 

        :param position: Position, Evaluate ColorRamp at position 
        :type position: float
        :rtype: float
        :return:  Color, Color at given position 
        '''
        pass


class ColorRampElement:
    '''Element defining a color at a position in the color ramp '''

    alpha: float = None
    '''Set alpha of selected color stop 

    :type: float
    '''

    color: float = None
    '''Set color of selected color stop 

    :type: float
    '''

    position: float = None
    '''Set position of selected color stop 

    :type: float
    '''


class ColorRampElements:
    '''Collection of Color Ramp Elements '''

    def new(self, position: float) -> 'ColorRampElement':
        '''Add element to ColorRamp 

        :param position: Position, Position to add element 
        :type position: float
        :rtype: 'ColorRampElement'
        :return:  New element 
        '''
        pass

    def remove(self, element: 'ColorRampElement'):
        '''Delete element from ColorRamp 

        :param element: Element to remove 
        :type element: 'ColorRampElement'
        '''
        pass


class ColorSequence:
    '''Sequence strip creating an image filled with a single color '''

    color: float = None
    '''Effect Strip color 

    :type: float
    '''

    input_count: int = None
    '''

    :type: int
    '''


class CompositorNode:
    def tag_need_exec(self, ):
        '''Tag the node for compositor update 

        '''
        pass

    def update(self, ):
        '''

        '''
        pass


class CompositorNodeAlphaOver:
    premul: float = None
    '''Mix Factor 

    :type: float
    '''

    use_premultiply: bool = None
    '''

    :type: bool
    '''

    def update(self, ):
        '''

        '''
        pass


class CompositorNodeBilateralblur:
    iterations: int = None
    '''

    :type: int
    '''

    sigma_color: float = None
    '''

    :type: float
    '''

    sigma_space: float = None
    '''

    :type: float
    '''

    def update(self, ):
        '''

        '''
        pass


class CompositorNodeBlur:
    aspect_correction: typing.Union[int, str] = None
    '''Type of aspect correction to use 

    :type: typing.Union[int, str]
    '''

    factor: float = None
    '''

    :type: float
    '''

    factor_x: float = None
    '''

    :type: float
    '''

    factor_y: float = None
    '''

    :type: float
    '''

    filter_type: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    size_x: int = None
    '''

    :type: int
    '''

    size_y: int = None
    '''

    :type: int
    '''

    use_bokeh: bool = None
    '''Use circular filter (slower) 

    :type: bool
    '''

    use_extended_bounds: bool = None
    '''Extend bounds of the input image to fully fit blurred image 

    :type: bool
    '''

    use_gamma_correction: bool = None
    '''Apply filter on gamma corrected values 

    :type: bool
    '''

    use_relative: bool = None
    '''Use relative (percent) values to define blur radius 

    :type: bool
    '''

    use_variable_size: bool = None
    '''Support variable blur per-pixel when using an image for size input 

    :type: bool
    '''

    def update(self, ):
        '''

        '''
        pass


class CompositorNodeBokehBlur:
    blur_max: float = None
    '''Blur limit, maximum CoC radius 

    :type: float
    '''

    use_extended_bounds: bool = None
    '''Extend bounds of the input image to fully fit blurred image 

    :type: bool
    '''

    use_variable_size: bool = None
    '''Support variable blur per-pixel when using an image for size input 

    :type: bool
    '''

    def update(self, ):
        '''

        '''
        pass


class CompositorNodeBokehImage:
    angle: float = None
    '''Angle of the bokeh 

    :type: float
    '''

    catadioptric: float = None
    '''Level of catadioptric of the bokeh 

    :type: float
    '''

    flaps: int = None
    '''Number of flaps 

    :type: int
    '''

    rounding: float = None
    '''Level of rounding of the bokeh 

    :type: float
    '''

    shift: float = None
    '''Shift of the lens components 

    :type: float
    '''

    def update(self, ):
        '''

        '''
        pass


class CompositorNodeBoxMask:
    height: float = None
    '''Height of the box 

    :type: float
    '''

    mask_type: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    rotation: float = None
    '''Rotation angle of the box 

    :type: float
    '''

    width: float = None
    '''Width of the box 

    :type: float
    '''

    x: float = None
    '''X position of the middle of the box 

    :type: float
    '''

    y: float = None
    '''Y position of the middle of the box 

    :type: float
    '''

    def update(self, ):
        '''

        '''
        pass


class CompositorNodeBrightContrast:
    use_premultiply: bool = None
    '''Keep output image premultiplied alpha 

    :type: bool
    '''

    def update(self, ):
        '''

        '''
        pass


class CompositorNodeChannelMatte:
    color_space: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    limit_channel: typing.Union[int, str] = None
    '''Limit by this channel’s value 

    :type: typing.Union[int, str]
    '''

    limit_max: float = None
    '''Values higher than this setting are 100% opaque 

    :type: float
    '''

    limit_method: typing.Union[int, str] = None
    '''Algorithm to use to limit channel 

    :type: typing.Union[int, str]
    '''

    limit_min: float = None
    '''Values lower than this setting are 100% keyed 

    :type: float
    '''

    matte_channel: typing.Union[int, str] = None
    '''Channel used to determine matte 

    :type: typing.Union[int, str]
    '''

    def update(self, ):
        '''

        '''
        pass


class CompositorNodeChromaMatte:
    gain: float = None
    '''Alpha falloff 

    :type: float
    '''

    lift: float = None
    '''Alpha lift 

    :type: float
    '''

    shadow_adjust: float = None
    '''Adjusts the brightness of any shadows captured 

    :type: float
    '''

    threshold: float = None
    '''Tolerance below which colors will be considered as exact matches 

    :type: float
    '''

    tolerance: float = None
    '''Tolerance for a color to be considered a keying color 

    :type: float
    '''

    def update(self, ):
        '''

        '''
        pass


class CompositorNodeColorBalance:
    correction_method: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    gain: float = None
    '''Correction for Highlights 

    :type: float
    '''

    gamma: float = None
    '''Correction for Midtones 

    :type: float
    '''

    lift: float = None
    '''Correction for Shadows 

    :type: float
    '''

    offset: float = None
    '''Correction for Shadows 

    :type: float
    '''

    offset_basis: float = None
    '''Support negative color by using this as the RGB basis 

    :type: float
    '''

    power: float = None
    '''Correction for Midtones 

    :type: float
    '''

    slope: float = None
    '''Correction for Highlights 

    :type: float
    '''

    def update(self, ):
        '''

        '''
        pass


class CompositorNodeColorCorrection:
    blue: bool = None
    '''Blue channel active 

    :type: bool
    '''

    green: bool = None
    '''Green channel active 

    :type: bool
    '''

    highlights_contrast: float = None
    '''Highlights contrast 

    :type: float
    '''

    highlights_gain: float = None
    '''Highlights gain 

    :type: float
    '''

    highlights_gamma: float = None
    '''Highlights gamma 

    :type: float
    '''

    highlights_lift: float = None
    '''Highlights lift 

    :type: float
    '''

    highlights_saturation: float = None
    '''Highlights saturation 

    :type: float
    '''

    master_contrast: float = None
    '''Master contrast 

    :type: float
    '''

    master_gain: float = None
    '''Master gain 

    :type: float
    '''

    master_gamma: float = None
    '''Master gamma 

    :type: float
    '''

    master_lift: float = None
    '''Master lift 

    :type: float
    '''

    master_saturation: float = None
    '''Master saturation 

    :type: float
    '''

    midtones_contrast: float = None
    '''Midtones contrast 

    :type: float
    '''

    midtones_end: float = None
    '''End of midtones 

    :type: float
    '''

    midtones_gain: float = None
    '''Midtones gain 

    :type: float
    '''

    midtones_gamma: float = None
    '''Midtones gamma 

    :type: float
    '''

    midtones_lift: float = None
    '''Midtones lift 

    :type: float
    '''

    midtones_saturation: float = None
    '''Midtones saturation 

    :type: float
    '''

    midtones_start: float = None
    '''Start of midtones 

    :type: float
    '''

    red: bool = None
    '''Red channel active 

    :type: bool
    '''

    shadows_contrast: float = None
    '''Shadows contrast 

    :type: float
    '''

    shadows_gain: float = None
    '''Shadows gain 

    :type: float
    '''

    shadows_gamma: float = None
    '''Shadows gamma 

    :type: float
    '''

    shadows_lift: float = None
    '''Shadows lift 

    :type: float
    '''

    shadows_saturation: float = None
    '''Shadows saturation 

    :type: float
    '''

    def update(self, ):
        '''

        '''
        pass


class CompositorNodeColorMatte:
    color_hue: float = None
    '''Hue tolerance for colors to be considered a keying color 

    :type: float
    '''

    color_saturation: float = None
    '''Saturation Tolerance for the color 

    :type: float
    '''

    color_value: float = None
    '''Value Tolerance for the color 

    :type: float
    '''

    def update(self, ):
        '''

        '''
        pass


class CompositorNodeColorSpill:
    channel: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    limit_channel: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    limit_method: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    ratio: float = None
    '''Scale limit by value 

    :type: float
    '''

    unspill_blue: float = None
    '''Blue spillmap scale 

    :type: float
    '''

    unspill_green: float = None
    '''Green spillmap scale 

    :type: float
    '''

    unspill_red: float = None
    '''Red spillmap scale 

    :type: float
    '''

    use_unspill: bool = None
    '''Compensate all channels (differently) by hand 

    :type: bool
    '''

    def update(self, ):
        '''

        '''
        pass


class CompositorNodeCombHSVA:
    def update(self, ):
        '''

        '''
        pass


class CompositorNodeCombRGBA:
    def update(self, ):
        '''

        '''
        pass


class CompositorNodeCombYCCA:
    mode: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    def update(self, ):
        '''

        '''
        pass


class CompositorNodeCombYUVA:
    def update(self, ):
        '''

        '''
        pass


class CompositorNodeComposite:
    use_alpha: bool = None
    '''Colors are treated alpha premultiplied, or colors output straight (alpha gets set to 1) 

    :type: bool
    '''

    def update(self, ):
        '''

        '''
        pass


class CompositorNodeCornerPin:
    def update(self, ):
        '''

        '''
        pass


class CompositorNodeCrop:
    max_x: int = None
    '''

    :type: int
    '''

    max_y: int = None
    '''

    :type: int
    '''

    min_x: int = None
    '''

    :type: int
    '''

    min_y: int = None
    '''

    :type: int
    '''

    rel_max_x: float = None
    '''

    :type: float
    '''

    rel_max_y: float = None
    '''

    :type: float
    '''

    rel_min_x: float = None
    '''

    :type: float
    '''

    rel_min_y: float = None
    '''

    :type: float
    '''

    relative: bool = None
    '''Use relative values to crop image 

    :type: bool
    '''

    use_crop_size: bool = None
    '''Whether to crop the size of the input image 

    :type: bool
    '''

    def update(self, ):
        '''

        '''
        pass


class CompositorNodeCurveRGB:
    mapping: 'CurveMapping' = None
    '''

    :type: 'CurveMapping'
    '''

    def update(self, ):
        '''

        '''
        pass


class CompositorNodeCurveVec:
    mapping: 'CurveMapping' = None
    '''

    :type: 'CurveMapping'
    '''

    def update(self, ):
        '''

        '''
        pass


class CompositorNodeDBlur:
    angle: float = None
    '''

    :type: float
    '''

    center_x: float = None
    '''

    :type: float
    '''

    center_y: float = None
    '''

    :type: float
    '''

    distance: float = None
    '''

    :type: float
    '''

    iterations: int = None
    '''

    :type: int
    '''

    spin: float = None
    '''

    :type: float
    '''

    use_wrap: bool = None
    '''

    :type: bool
    '''

    zoom: float = None
    '''

    :type: float
    '''

    def update(self, ):
        '''

        '''
        pass


class CompositorNodeDefocus:
    angle: float = None
    '''Bokeh shape rotation offset 

    :type: float
    '''

    blur_max: float = None
    '''Blur limit, maximum CoC radius 

    :type: float
    '''

    bokeh: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    f_stop: float = None
    '''Amount of focal blur, 128=infinity=perfect focus, half the value doubles the blur radius 

    :type: float
    '''

    scene: 'Scene' = None
    '''Scene from which to select the active camera (render scene if undefined) 

    :type: 'Scene'
    '''

    threshold: float = None
    '''CoC radius threshold, prevents background bleed on in-focus midground, 0=off 

    :type: float
    '''

    use_gamma_correction: bool = None
    '''Enable gamma correction before and after main process 

    :type: bool
    '''

    use_preview: bool = None
    '''Enable low quality mode, useful for preview 

    :type: bool
    '''

    use_zbuffer: bool = None
    '''Disable when using an image as input instead of actual z-buffer (auto enabled if node not image based, eg. time node) 

    :type: bool
    '''

    z_scale: float = None
    '''Scale the Z input when not using a z-buffer, controls maximum blur designated by the color white or input value 1 

    :type: float
    '''

    def update(self, ):
        '''

        '''
        pass


class CompositorNodeDespeckle:
    threshold: float = None
    '''Threshold for detecting pixels to despeckle 

    :type: float
    '''

    threshold_neighbor: float = None
    '''Threshold for the number of neighbor pixels that must match 

    :type: float
    '''

    def update(self, ):
        '''

        '''
        pass


class CompositorNodeDiffMatte:
    falloff: float = None
    '''Color distances below this additional threshold are partially keyed 

    :type: float
    '''

    tolerance: float = None
    '''Color distances below this threshold are keyed 

    :type: float
    '''

    def update(self, ):
        '''

        '''
        pass


class CompositorNodeDilateErode:
    distance: int = None
    '''Distance to grow/shrink (number of iterations) 

    :type: int
    '''

    edge: float = None
    '''Edge to inset 

    :type: float
    '''

    falloff: typing.Union[int, str] = None
    '''Falloff type the feather 

    :type: typing.Union[int, str]
    '''

    mode: typing.Union[int, str] = None
    '''Growing/shrinking mode 

    :type: typing.Union[int, str]
    '''

    def update(self, ):
        '''

        '''
        pass


class CompositorNodeDisplace:
    def update(self, ):
        '''

        '''
        pass


class CompositorNodeDistanceMatte:
    channel: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    falloff: float = None
    '''Color distances below this additional threshold are partially keyed 

    :type: float
    '''

    tolerance: float = None
    '''Color distances below this threshold are keyed 

    :type: float
    '''

    def update(self, ):
        '''

        '''
        pass


class CompositorNodeDoubleEdgeMask:
    edge_mode: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    inner_mode: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    def update(self, ):
        '''

        '''
        pass


class CompositorNodeEllipseMask:
    height: float = None
    '''Height of the ellipse 

    :type: float
    '''

    mask_type: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    rotation: float = None
    '''Rotation angle of the ellipse 

    :type: float
    '''

    width: float = None
    '''Width of the ellipse 

    :type: float
    '''

    x: float = None
    '''X position of the middle of the ellipse 

    :type: float
    '''

    y: float = None
    '''Y position of the middle of the ellipse 

    :type: float
    '''

    def update(self, ):
        '''

        '''
        pass


class CompositorNodeFilter:
    filter_type: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    def update(self, ):
        '''

        '''
        pass


class CompositorNodeFlip:
    axis: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    def update(self, ):
        '''

        '''
        pass


class CompositorNodeGamma:
    def update(self, ):
        '''

        '''
        pass


class CompositorNodeGlare:
    angle_offset: float = None
    '''Streak angle offset 

    :type: float
    '''

    color_modulation: float = None
    '''Amount of Color Modulation, modulates colors of streaks and ghosts for a spectral dispersion effect 

    :type: float
    '''

    fade: float = None
    '''Streak fade-out factor 

    :type: float
    '''

    glare_type: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    iterations: int = None
    '''

    :type: int
    '''

    mix: float = None
    '''-1 is original image only, 0 is exact 50/50 mix, 1 is processed image only 

    :type: float
    '''

    quality: typing.Union[int, str] = None
    '''If not set to high quality, the effect will be applied to a low-res copy of the source image 

    :type: typing.Union[int, str]
    '''

    size: int = None
    '''Glow/glare size (not actual size; relative to initial size of bright area of pixels) 

    :type: int
    '''

    streaks: int = None
    '''Total number of streaks 

    :type: int
    '''

    threshold: float = None
    '''The glare filter will only be applied to pixels brighter than this value 

    :type: float
    '''

    use_rotate_45: bool = None
    '''Simple star filter: add 45 degree rotation offset 

    :type: bool
    '''

    def update(self, ):
        '''

        '''
        pass


class CompositorNodeGroup:
    interface: 'PropertyGroup' = None
    '''Interface socket data 

    :type: 'PropertyGroup'
    '''

    node_tree: 'NodeTree' = None
    '''

    :type: 'NodeTree'
    '''

    def update(self, ):
        '''

        '''
        pass


class CompositorNodeHueCorrect:
    mapping: 'CurveMapping' = None
    '''

    :type: 'CurveMapping'
    '''

    def update(self, ):
        '''

        '''
        pass


class CompositorNodeHueSat:
    def update(self, ):
        '''

        '''
        pass


class CompositorNodeIDMask:
    index: int = None
    '''Pass index number to convert to alpha 

    :type: int
    '''

    use_antialiasing: bool = None
    '''Apply an anti-aliasing filter to the mask 

    :type: bool
    '''

    def update(self, ):
        '''

        '''
        pass


class CompositorNodeImage:
    frame_duration: int = None
    '''Number of images of a movie to use 

    :type: int
    '''

    frame_offset: int = None
    '''Offset the number of the frame to use in the animation 

    :type: int
    '''

    frame_start: int = None
    '''Global starting frame of the movie/sequence, assuming first picture has a #1 

    :type: int
    '''

    has_layers: bool = None
    '''True if this image has any named layer 

    :type: bool
    '''

    has_views: bool = None
    '''True if this image has multiple views 

    :type: bool
    '''

    image: 'Image' = None
    '''

    :type: 'Image'
    '''

    layer: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    use_auto_refresh: bool = None
    '''Always refresh image on frame changes 

    :type: bool
    '''

    use_cyclic: bool = None
    '''Cycle the images in the movie 

    :type: bool
    '''

    use_straight_alpha_output: bool = None
    '''Put Node output buffer to straight alpha instead of premultiplied 

    :type: bool
    '''

    view: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    def update(self, ):
        '''

        '''
        pass


class CompositorNodeInpaint:
    distance: int = None
    '''Distance to inpaint (number of iterations) 

    :type: int
    '''

    def update(self, ):
        '''

        '''
        pass


class CompositorNodeInvert:
    invert_alpha: bool = None
    '''

    :type: bool
    '''

    invert_rgb: bool = None
    '''

    :type: bool
    '''

    def update(self, ):
        '''

        '''
        pass


class CompositorNodeKeying:
    blur_post: int = None
    '''Matte blur size which applies after clipping and dilate/eroding 

    :type: int
    '''

    blur_pre: int = None
    '''Chroma pre-blur size which applies before running keyer 

    :type: int
    '''

    clip_black: float = None
    '''Value of non-scaled matte pixel which considers as fully background pixel 

    :type: float
    '''

    clip_white: float = None
    '''Value of non-scaled matte pixel which considers as fully foreground pixel 

    :type: float
    '''

    despill_balance: float = None
    '''Balance between non-key colors used to detect amount of key color to be removed 

    :type: float
    '''

    despill_factor: float = None
    '''Factor of despilling screen color from image 

    :type: float
    '''

    dilate_distance: int = None
    '''Matte dilate/erode side 

    :type: int
    '''

    edge_kernel_radius: int = None
    '''Radius of kernel used to detect whether pixel belongs to edge 

    :type: int
    '''

    edge_kernel_tolerance: float = None
    '''Tolerance to pixels inside kernel which are treating as belonging to the same plane 

    :type: float
    '''

    feather_distance: int = None
    '''Distance to grow/shrink the feather 

    :type: int
    '''

    feather_falloff: typing.Union[int, str] = None
    '''Falloff type the feather 

    :type: typing.Union[int, str]
    '''

    screen_balance: float = None
    '''Balance between two non-primary channels primary channel is comparing against 

    :type: float
    '''

    def update(self, ):
        '''

        '''
        pass


class CompositorNodeKeyingScreen:
    clip: 'MovieClip' = None
    '''

    :type: 'MovieClip'
    '''

    tracking_object: str = None
    '''

    :type: str
    '''

    def update(self, ):
        '''

        '''
        pass


class CompositorNodeLensdist:
    use_fit: bool = None
    '''For positive distortion factor only: scale image such that black areas are not visible 

    :type: bool
    '''

    use_jitter: bool = None
    '''Enable/disable jittering (faster, but also noisier) 

    :type: bool
    '''

    use_projector: bool = None
    '''Enable/disable projector mode (the effect is applied in horizontal direction only) 

    :type: bool
    '''

    def update(self, ):
        '''

        '''
        pass


class CompositorNodeLevels:
    channel: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    def update(self, ):
        '''

        '''
        pass


class CompositorNodeLumaMatte:
    limit_max: float = None
    '''Values higher than this setting are 100% opaque 

    :type: float
    '''

    limit_min: float = None
    '''Values lower than this setting are 100% keyed 

    :type: float
    '''

    def update(self, ):
        '''

        '''
        pass


class CompositorNodeMapRange:
    use_clamp: bool = None
    '''Clamp result of the node to 0..1 range 

    :type: bool
    '''

    def update(self, ):
        '''

        '''
        pass


class CompositorNodeMapUV:
    alpha: int = None
    '''

    :type: int
    '''

    def update(self, ):
        '''

        '''
        pass


class CompositorNodeMapValue:
    max: float = None
    '''

    :type: float
    '''

    min: float = None
    '''

    :type: float
    '''

    offset: float = None
    '''

    :type: float
    '''

    size: float = None
    '''

    :type: float
    '''

    use_max: bool = None
    '''

    :type: bool
    '''

    use_min: bool = None
    '''

    :type: bool
    '''

    def update(self, ):
        '''

        '''
        pass


class CompositorNodeMask:
    mask: 'Mask' = None
    '''

    :type: 'Mask'
    '''

    motion_blur_samples: int = None
    '''Number of motion blur samples 

    :type: int
    '''

    motion_blur_shutter: float = None
    '''Exposure for motion blur as a factor of FPS 

    :type: float
    '''

    size_source: typing.Union[int, str] = None
    '''Where to get the mask size from for aspect/size information 

    :type: typing.Union[int, str]
    '''

    size_x: int = None
    '''

    :type: int
    '''

    size_y: int = None
    '''

    :type: int
    '''

    use_antialiasing: bool = None
    '''Apply an anti-aliasing filter to the mask 

    :type: bool
    '''

    use_feather: bool = None
    '''Use feather information from the mask 

    :type: bool
    '''

    use_motion_blur: bool = None
    '''Use multi-sampled motion blur of the mask 

    :type: bool
    '''

    def update(self, ):
        '''

        '''
        pass


class CompositorNodeMath:
    operation: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    use_clamp: bool = None
    '''Clamp result of the node to 0..1 range 

    :type: bool
    '''

    def update(self, ):
        '''

        '''
        pass


class CompositorNodeMixRGB:
    blend_type: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    use_alpha: bool = None
    '''Include alpha of second input in this operation 

    :type: bool
    '''

    use_clamp: bool = None
    '''Clamp result of the node to 0..1 range 

    :type: bool
    '''

    def update(self, ):
        '''

        '''
        pass


class CompositorNodeMovieClip:
    clip: 'MovieClip' = None
    '''

    :type: 'MovieClip'
    '''

    def update(self, ):
        '''

        '''
        pass


class CompositorNodeMovieDistortion:
    clip: 'MovieClip' = None
    '''

    :type: 'MovieClip'
    '''

    distortion_type: typing.Union[int, str] = None
    '''Distortion to use to filter image 

    :type: typing.Union[int, str]
    '''

    def update(self, ):
        '''

        '''
        pass


class CompositorNodeNormal:
    def update(self, ):
        '''

        '''
        pass


class CompositorNodeNormalize:
    def update(self, ):
        '''

        '''
        pass


class CompositorNodeOutputFile:
    active_input_index: int = None
    '''Active input index in details view list 

    :type: int
    '''

    base_path: str = None
    '''Base output path for the image 

    :type: str
    '''

    file_slots: typing.List['CompositorNodeOutputFileFileSlots'] = None
    '''

    :type: typing.List['CompositorNodeOutputFileFileSlots']
    '''

    format: 'ImageFormatSettings' = None
    '''

    :type: 'ImageFormatSettings'
    '''

    layer_slots: typing.List['CompositorNodeOutputFileLayerSlots'] = None
    '''

    :type: typing.List['CompositorNodeOutputFileLayerSlots']
    '''

    def update(self, ):
        '''

        '''
        pass


class CompositorNodeOutputFileFileSlots:
    '''Collection of File Output node slots '''

    def new(self, name: str) -> 'NodeSocket':
        '''Add a file slot to this node 

        :param name: Name 
        :type name: str
        :rtype: 'NodeSocket'
        :return:  New socket 
        '''
        pass

    def remove(self, socket: 'NodeSocket'):
        '''Remove a file slot from this node 

        :param socket: The socket to remove 
        :type socket: 'NodeSocket'
        '''
        pass

    def clear(self, ):
        '''Remove all file slots from this node 

        '''
        pass

    def move(self, from_index: int, to_index: int):
        '''Move a file slot to another position 

        :param from_index: From Index, Index of the socket to move 
        :type from_index: int
        :param to_index: To Index, Target index for the socket 
        :type to_index: int
        '''
        pass


class CompositorNodeOutputFileLayerSlots:
    '''Collection of File Output node slots '''

    def new(self, name: str) -> 'NodeSocket':
        '''Add a file slot to this node 

        :param name: Name 
        :type name: str
        :rtype: 'NodeSocket'
        :return:  New socket 
        '''
        pass

    def remove(self, socket: 'NodeSocket'):
        '''Remove a file slot from this node 

        :param socket: The socket to remove 
        :type socket: 'NodeSocket'
        '''
        pass

    def clear(self, ):
        '''Remove all file slots from this node 

        '''
        pass

    def move(self, from_index: int, to_index: int):
        '''Move a file slot to another position 

        :param from_index: From Index, Index of the socket to move 
        :type from_index: int
        :param to_index: To Index, Target index for the socket 
        :type to_index: int
        '''
        pass


class CompositorNodePixelate:
    def update(self, ):
        '''

        '''
        pass


class CompositorNodePlaneTrackDeform:
    clip: 'MovieClip' = None
    '''

    :type: 'MovieClip'
    '''

    motion_blur_samples: int = None
    '''Number of motion blur samples 

    :type: int
    '''

    motion_blur_shutter: float = None
    '''Exposure for motion blur as a factor of FPS 

    :type: float
    '''

    plane_track_name: str = None
    '''

    :type: str
    '''

    tracking_object: str = None
    '''

    :type: str
    '''

    use_motion_blur: bool = None
    '''Use multi-sampled motion blur of the mask 

    :type: bool
    '''

    def update(self, ):
        '''

        '''
        pass


class CompositorNodePremulKey:
    mapping: typing.Union[int, str] = None
    '''Conversion between premultiplied alpha and key alpha 

    :type: typing.Union[int, str]
    '''

    def update(self, ):
        '''

        '''
        pass


class CompositorNodeRGB:
    def update(self, ):
        '''

        '''
        pass


class CompositorNodeRGBToBW:
    def update(self, ):
        '''

        '''
        pass


class CompositorNodeRLayers:
    layer: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    scene: 'Scene' = None
    '''

    :type: 'Scene'
    '''

    def update(self, ):
        '''

        '''
        pass


class CompositorNodeRotate:
    filter_type: typing.Union[int, str] = None
    '''Method to use to filter rotation 

    :type: typing.Union[int, str]
    '''

    def update(self, ):
        '''

        '''
        pass


class CompositorNodeScale:
    frame_method: typing.Union[int, str] = None
    '''How the image fits in the camera frame 

    :type: typing.Union[int, str]
    '''

    offset_x: float = None
    '''Offset image horizontally (factor of image size) 

    :type: float
    '''

    offset_y: float = None
    '''Offset image vertically (factor of image size) 

    :type: float
    '''

    space: typing.Union[int, str] = None
    '''Coordinate space to scale relative to 

    :type: typing.Union[int, str]
    '''

    def update(self, ):
        '''

        '''
        pass


class CompositorNodeSepHSVA:
    def update(self, ):
        '''

        '''
        pass


class CompositorNodeSepRGBA:
    def update(self, ):
        '''

        '''
        pass


class CompositorNodeSepYCCA:
    mode: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    def update(self, ):
        '''

        '''
        pass


class CompositorNodeSepYUVA:
    def update(self, ):
        '''

        '''
        pass


class CompositorNodeSetAlpha:
    def update(self, ):
        '''

        '''
        pass


class CompositorNodeSplitViewer:
    axis: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    factor: int = None
    '''

    :type: int
    '''

    def update(self, ):
        '''

        '''
        pass


class CompositorNodeStabilize:
    clip: 'MovieClip' = None
    '''

    :type: 'MovieClip'
    '''

    filter_type: typing.Union[int, str] = None
    '''Method to use to filter stabilization 

    :type: typing.Union[int, str]
    '''

    invert: bool = None
    '''Invert stabilization to re-introduce motion to the frame 

    :type: bool
    '''

    def update(self, ):
        '''

        '''
        pass


class CompositorNodeSunBeams:
    ray_length: float = None
    '''Length of rays as a factor of the image size 

    :type: float
    '''

    source: float = None
    '''Source point of rays as a factor of the image width & height 

    :type: float
    '''

    def update(self, ):
        '''

        '''
        pass


class CompositorNodeSwitch:
    check: bool = None
    '''Off: first socket, On: second socket 

    :type: bool
    '''

    def update(self, ):
        '''

        '''
        pass


class CompositorNodeSwitchView:
    def update(self, ):
        '''

        '''
        pass


class CompositorNodeTexture:
    node_output: int = None
    '''For node-based textures, which output node to use 

    :type: int
    '''

    texture: 'Texture' = None
    '''

    :type: 'Texture'
    '''

    def update(self, ):
        '''

        '''
        pass


class CompositorNodeTime:
    curve: 'CurveMapping' = None
    '''

    :type: 'CurveMapping'
    '''

    frame_end: int = None
    '''

    :type: int
    '''

    frame_start: int = None
    '''

    :type: int
    '''

    def update(self, ):
        '''

        '''
        pass


class CompositorNodeTonemap:
    adaptation: float = None
    '''If 0, global; if 1, based on pixel intensity 

    :type: float
    '''

    contrast: float = None
    '''Set to 0 to use estimate from input image 

    :type: float
    '''

    correction: float = None
    '''If 0, same for all channels; if 1, each independent 

    :type: float
    '''

    gamma: float = None
    '''If not used, set to 1 

    :type: float
    '''

    intensity: float = None
    '''If less than zero, darkens image; otherwise, makes it brighter 

    :type: float
    '''

    key: float = None
    '''The value the average luminance is mapped to 

    :type: float
    '''

    offset: float = None
    '''Normally always 1, but can be used as an extra control to alter the brightness curve 

    :type: float
    '''

    tonemap_type: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    def update(self, ):
        '''

        '''
        pass


class CompositorNodeTrackPos:
    clip: 'MovieClip' = None
    '''

    :type: 'MovieClip'
    '''

    frame_relative: int = None
    '''Frame to be used for relative position 

    :type: int
    '''

    position: typing.Union[int, str] = None
    '''Which marker position to use for output 

    :type: typing.Union[int, str]
    '''

    track_name: str = None
    '''

    :type: str
    '''

    tracking_object: str = None
    '''

    :type: str
    '''

    def update(self, ):
        '''

        '''
        pass


class CompositorNodeTransform:
    filter_type: typing.Union[int, str] = None
    '''Method to use to filter transform 

    :type: typing.Union[int, str]
    '''

    def update(self, ):
        '''

        '''
        pass


class CompositorNodeTranslate:
    use_relative: bool = None
    '''Use relative (fraction of input image size) values to define translation 

    :type: bool
    '''

    wrap_axis: typing.Union[int, str] = None
    '''Wrap image on a specific axis 

    :type: typing.Union[int, str]
    '''

    def update(self, ):
        '''

        '''
        pass


class CompositorNodeTree:
    '''Node tree consisting of linked nodes used for compositing '''

    chunk_size: typing.Union[int, str] = None
    '''Max size of a tile (smaller values gives better distribution of multiple threads, but more overhead) 

    :type: typing.Union[int, str]
    '''

    edit_quality: typing.Union[int, str] = None
    '''Quality when editing 

    :type: typing.Union[int, str]
    '''

    render_quality: typing.Union[int, str] = None
    '''Quality when rendering 

    :type: typing.Union[int, str]
    '''

    use_groupnode_buffer: bool = None
    '''Enable buffering of group nodes 

    :type: bool
    '''

    use_opencl: bool = None
    '''Enable GPU calculations 

    :type: bool
    '''

    use_two_pass: bool = None
    '''Use two pass execution during editing: first calculate fast nodes, second pass calculate all nodes 

    :type: bool
    '''

    use_viewer_border: bool = None
    '''Use boundaries for viewer nodes and composite backdrop 

    :type: bool
    '''


class CompositorNodeValToRGB:
    color_ramp: 'ColorRamp' = None
    '''

    :type: 'ColorRamp'
    '''

    def update(self, ):
        '''

        '''
        pass


class CompositorNodeValue:
    def update(self, ):
        '''

        '''
        pass


class CompositorNodeVecBlur:
    factor: float = None
    '''Scaling factor for motion vectors (actually, ‘shutter speed’, in frames) 

    :type: float
    '''

    samples: int = None
    '''

    :type: int
    '''

    speed_max: int = None
    '''Maximum speed, or zero for none 

    :type: int
    '''

    speed_min: int = None
    '''Minimum speed for a pixel to be blurred (used to separate background from foreground) 

    :type: int
    '''

    use_curved: bool = None
    '''Interpolate between frames in a Bezier curve, rather than linearly 

    :type: bool
    '''

    def update(self, ):
        '''

        '''
        pass


class CompositorNodeViewer:
    center_x: float = None
    '''

    :type: float
    '''

    center_y: float = None
    '''

    :type: float
    '''

    tile_order: typing.Union[int, str] = None
    '''Tile order 

    :type: typing.Union[int, str]
    '''

    use_alpha: bool = None
    '''Colors are treated alpha premultiplied, or colors output straight (alpha gets set to 1) 

    :type: bool
    '''

    def update(self, ):
        '''

        '''
        pass


class CompositorNodeZcombine:
    use_alpha: bool = None
    '''Take Alpha channel into account when doing the Z operation 

    :type: bool
    '''

    use_antialias_z: bool = None
    '''Anti-alias the z-buffer to try to avoid artifacts, mostly useful for Blender renders 

    :type: bool
    '''

    def update(self, ):
        '''

        '''
        pass


class ConsoleLine:
    '''Input line for the interactive console '''

    body: str = None
    '''Text in the line 

    :type: str
    '''

    current_character: int = None
    '''

    :type: int
    '''

    type: typing.Union[int, str] = None
    '''Console line type when used in scrollback 

    :type: typing.Union[int, str]
    '''


class Constraint:
    '''Constraint modifying the transformation of objects and bones '''

    active: bool = None
    '''Constraint is the one being edited 

    :type: bool
    '''

    error_location: float = None
    '''Amount of residual error in Blender space unit for constraints that work on position 

    :type: float
    '''

    error_rotation: float = None
    '''Amount of residual error in radians for constraints that work on orientation 

    :type: float
    '''

    influence: float = None
    '''Amount of influence constraint will have on the final solution 

    :type: float
    '''

    is_proxy_local: bool = None
    '''Constraint was added in this proxy instance (i.e. did not belong to source Armature) 

    :type: bool
    '''

    is_valid: bool = None
    '''Constraint has valid settings and can be evaluated 

    :type: bool
    '''

    mute: bool = None
    '''Enable/Disable Constraint 

    :type: bool
    '''

    name: str = None
    '''Constraint name 

    :type: str
    '''

    owner_space: typing.Union[int, str] = None
    '''Space that owner is evaluated in 

    :type: typing.Union[int, str]
    '''

    show_expanded: bool = None
    '''Constraint’s panel is expanded in UI 

    :type: bool
    '''

    target_space: typing.Union[int, str] = None
    '''Space that target is evaluated in 

    :type: typing.Union[int, str]
    '''

    type: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''


class ConstraintActuator:
    '''Actuator to handle Constraints '''

    angle_max: float = None
    '''Maximum angle allowed with target direction (no correction is done if angle with target direction is between min and max) 

    :type: float
    '''

    angle_min: float = None
    '''Minimum angle to maintain with target direction (no correction is done if angle with target direction is between min and max) 

    :type: float
    '''

    damping: int = None
    '''Damping factor: time constant (in frame) of low pass filter 

    :type: int
    '''

    damping_rotation: int = None
    '''Use a different damping for orientation 

    :type: int
    '''

    direction: typing.Union[int, str] = None
    '''Direction of the ray 

    :type: typing.Union[int, str]
    '''

    direction_axis: typing.Union[int, str] = None
    '''Select the axis to be aligned along the reference direction 

    :type: typing.Union[int, str]
    '''

    direction_axis_pos: typing.Union[int, str] = None
    '''Select the axis to be aligned along the reference direction 

    :type: typing.Union[int, str]
    '''

    distance: float = None
    '''Keep this distance to target 

    :type: float
    '''

    fh_damping: float = None
    '''Damping factor of the force field spring 

    :type: float
    '''

    fh_force: float = None
    '''Spring force within the force field area 

    :type: float
    '''

    fh_height: float = None
    '''Height of the force field area 

    :type: float
    '''

    limit: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    limit_max: float = None
    '''

    :type: float
    '''

    limit_min: float = None
    '''

    :type: float
    '''

    material: str = None
    '''Ray detects only Objects with this material 

    :type: str
    '''

    mode: typing.Union[int, str] = None
    '''The type of the constraint 

    :type: typing.Union[int, str]
    '''

    property: str = None
    '''Ray detects only Objects with this property 

    :type: str
    '''

    range: float = None
    '''Maximum length of ray 

    :type: float
    '''

    rotation_max: float = None
    '''Reference Direction 

    :type: float
    '''

    time: int = None
    '''Maximum activation time in frame, 0 for unlimited 

    :type: int
    '''

    use_fh_normal: bool = None
    '''Add a horizontal spring force on slopes 

    :type: bool
    '''

    use_fh_paralel_axis: bool = None
    '''Keep object axis parallel to normal 

    :type: bool
    '''

    use_force_distance: bool = None
    '''Force distance of object to point of impact of ray 

    :type: bool
    '''

    use_local: bool = None
    '''Set ray along object’s axis or global axis 

    :type: bool
    '''

    use_material_detect: bool = None
    '''Detect material instead of property 

    :type: bool
    '''

    use_normal: bool = None
    '''Set object axis along (local axis) or parallel (global axis) to the normal at hit position 

    :type: bool
    '''

    use_persistent: bool = None
    '''Persistent actuator: stays active even if ray does not reach target 

    :type: bool
    '''


class ConstraintTarget:
    '''Target object for multi-target constraints '''

    subtarget: str = None
    '''

    :type: str
    '''

    target: 'Object' = None
    '''Target Object 

    :type: 'Object'
    '''


class Context:
    '''Current windowmanager and data context '''

    area: 'Area' = None
    '''

    :type: 'Area'
    '''

    blend_data: 'BlendData' = None
    '''

    :type: 'BlendData'
    '''

    mode: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    region: 'Region' = None
    '''

    :type: 'Region'
    '''

    region_data: 'RegionView3D' = None
    '''

    :type: 'RegionView3D'
    '''

    scene: 'Scene' = None
    '''

    :type: 'Scene'
    '''

    screen: 'Screen' = None
    '''

    :type: 'Screen'
    '''

    space_data: 'Space' = None
    '''

    :type: 'Space'
    '''

    tool_settings: 'ToolSettings' = None
    '''

    :type: 'ToolSettings'
    '''

    user_preferences: 'UserPreferences' = None
    '''

    :type: 'UserPreferences'
    '''

    window: 'Window' = None
    '''

    :type: 'Window'
    '''

    window_manager: 'WindowManager' = None
    '''

    :type: 'WindowManager'
    '''

    active_object: 'Object' = None
    '''

    :type: 'Object'
    '''

    preferences = None
    ''''''

    visible_objects: typing.List['Object'] = None
    '''

    :type: typing.List['Object']
    '''

    selectable_objects: typing.List['Object'] = None
    '''

    :type: typing.List['Object']
    '''

    selected_objects: typing.List['Object'] = None
    '''

    :type: typing.List['Object']
    '''

    editable_objects: typing.List['Object'] = None
    '''

    :type: typing.List['Object']
    '''

    selected_editable_objects: typing.List['Object'] = None
    '''

    :type: typing.List['Object']
    '''

    objects_in_mode: typing.List['Object'] = None
    '''

    :type: typing.List['Object']
    '''

    objects_in_mode_unique_data: typing.List['Object'] = None
    '''

    :type: typing.List['Object']
    '''

    visible_bones: typing.List['EditBone'] = None
    '''

    :type: typing.List['EditBone']
    '''

    editable_bones: typing.List['EditBone'] = None
    '''

    :type: typing.List['EditBone']
    '''

    selected_bones: typing.List['EditBone'] = None
    '''

    :type: typing.List['EditBone']
    '''

    selected_editable_bones: typing.List['EditBone'] = None
    '''

    :type: typing.List['EditBone']
    '''

    visible_pose_bones: typing.List['EditBone'] = None
    '''

    :type: typing.List['EditBone']
    '''

    selected_pose_bones: typing.List['EditBone'] = None
    '''

    :type: typing.List['EditBone']
    '''

    selected_pose_bones_from_active_object: typing.List['EditBone'] = None
    '''

    :type: typing.List['EditBone']
    '''

    active_bone: 'EditBone' = None
    '''

    :type: 'EditBone'
    '''

    active_pose_bone: 'PoseBone' = None
    '''

    :type: 'PoseBone'
    '''

    object: 'Object' = None
    '''

    :type: 'Object'
    '''

    edit_object: 'Object' = None
    '''

    :type: 'Object'
    '''

    sculpt_object: 'Object' = None
    '''

    :type: 'Object'
    '''

    vertex_paint_object: 'Object' = None
    '''

    :type: 'Object'
    '''

    weight_paint_object: 'Object' = None
    '''

    :type: 'Object'
    '''

    image_paint_object: 'Object' = None
    '''

    :type: 'Object'
    '''

    particle_edit_object: 'Object' = None
    '''

    :type: 'Object'
    '''

    pose_object: 'Object' = None
    '''

    :type: 'Object'
    '''

    sequences: typing.List['Sequence'] = None
    '''

    :type: typing.List['Sequence']
    '''

    selected_sequences: typing.List['Sequence'] = None
    '''

    :type: typing.List['Sequence']
    '''

    selected_editable_sequences: typing.List['Sequence'] = None
    '''

    :type: typing.List['Sequence']
    '''

    gpencil_data: 'GreasePencil' = None
    '''

    :type: 'GreasePencil'
    '''

    gpencil_data_owner: 'ID' = None
    '''

    :type: 'ID'
    '''

    visible_gpencil_layers: typing.List['GPencilLayer'] = None
    '''

    :type: typing.List['GPencilLayer']
    '''

    editable_gpencil_layers: typing.List['GPencilLayer'] = None
    '''

    :type: typing.List['GPencilLayer']
    '''

    editable_gpencil_strokes: typing.List['GPencilStroke'] = None
    '''

    :type: typing.List['GPencilStroke']
    '''

    active_gpencil_layer: typing.List['GPencilLayer'] = None
    '''

    :type: typing.List['GPencilLayer']
    '''

    active_gpencil_frame: list = None
    '''

    :type: list
    '''

    active_operator: 'Operator' = None
    '''

    :type: 'Operator'
    '''

    selected_editable_fcurves: typing.List['FCurve'] = None
    '''

    :type: typing.List['FCurve']
    '''

    active_base: 'ObjectBase' = None
    '''

    :type: 'ObjectBase'
    '''

    texture_slot: 'MaterialTextureSlot' = None
    '''

    :type: 'MaterialTextureSlot'
    '''

    world: 'World' = None
    '''

    :type: 'World'
    '''

    mesh: 'Mesh' = None
    '''

    :type: 'Mesh'
    '''

    armature: 'Armature' = None
    '''

    :type: 'Armature'
    '''

    lattice: 'Lattice' = None
    '''

    :type: 'Lattice'
    '''

    curve: 'Curve' = None
    '''

    :type: 'Curve'
    '''

    meta_ball: 'MetaBall' = None
    '''

    :type: 'MetaBall'
    '''

    light = None
    ''''''

    speaker: 'Speaker' = None
    '''

    :type: 'Speaker'
    '''

    lightprobe = None
    ''''''

    camera: 'Camera' = None
    '''

    :type: 'Camera'
    '''

    material: 'Material' = None
    '''

    :type: 'Material'
    '''

    material_slot: 'MaterialSlot' = None
    '''

    :type: 'MaterialSlot'
    '''

    texture: 'Texture' = None
    '''

    :type: 'Texture'
    '''

    texture_user: 'ID' = None
    '''

    :type: 'ID'
    '''

    texture_user_property: 'Property' = None
    '''

    :type: 'Property'
    '''

    bone: 'Bone' = None
    '''

    :type: 'Bone'
    '''

    edit_bone: 'EditBone' = None
    '''

    :type: 'EditBone'
    '''

    pose_bone: 'PoseBone' = None
    '''

    :type: 'PoseBone'
    '''

    particle_system: 'ParticleSystem' = None
    '''

    :type: 'ParticleSystem'
    '''

    particle_system_editable: 'ParticleSystem' = None
    '''

    :type: 'ParticleSystem'
    '''

    particle_settings: 'ParticleSettings' = None
    '''

    :type: 'ParticleSettings'
    '''

    cloth: 'ClothModifier' = None
    '''

    :type: 'ClothModifier'
    '''

    soft_body: 'SoftBodyModifier' = None
    '''

    :type: 'SoftBodyModifier'
    '''

    fluid: 'FluidSimulationModifier' = None
    '''

    :type: 'FluidSimulationModifier'
    '''

    smoke: 'SmokeModifier' = None
    '''

    :type: 'SmokeModifier'
    '''

    collision: 'CollisionModifier' = None
    '''

    :type: 'CollisionModifier'
    '''

    brush: 'Brush' = None
    '''

    :type: 'Brush'
    '''

    dynamic_paint: 'DynamicPaintModifier' = None
    '''

    :type: 'DynamicPaintModifier'
    '''

    line_style: 'FreestyleLineStyle' = None
    '''

    :type: 'FreestyleLineStyle'
    '''

    collection = None
    ''''''

    gpencil: 'GreasePencil' = None
    '''

    :type: 'GreasePencil'
    '''

    edit_image: 'Image' = None
    '''

    :type: 'Image'
    '''

    edit_mask: 'Mask' = None
    '''

    :type: 'Mask'
    '''

    selected_nodes: typing.List['Node'] = None
    '''

    :type: typing.List['Node']
    '''

    active_node: 'Node' = None
    '''

    :type: 'Node'
    '''

    edit_text: 'Text' = None
    '''

    :type: 'Text'
    '''

    edit_movieclip: 'MovieClip' = None
    '''

    :type: 'MovieClip'
    '''

    def copy(self, ):
        '''

        '''
        pass


class ControlFluidSettings:
    '''Fluid simulation settings for objects controlling the motion of fluid in the simulation '''

    attraction_radius: float = None
    '''Force field radius around the control object 

    :type: float
    '''

    attraction_strength: float = None
    '''Force strength for directional attraction towards the control object 

    :type: float
    '''

    end_time: float = None
    '''Time when the control particles are deactivated 

    :type: float
    '''

    quality: float = None
    '''Quality which is used for object sampling (higher = better but slower) 

    :type: float
    '''

    start_time: float = None
    '''Time when the control particles are activated 

    :type: float
    '''

    use: bool = None
    '''Object contributes to the fluid simulation 

    :type: bool
    '''

    use_reverse_frames: bool = None
    '''Reverse control object movement 

    :type: bool
    '''

    velocity_radius: float = None
    '''Force field radius around the control object 

    :type: float
    '''

    velocity_strength: float = None
    '''Force strength of how much of the control object’s velocity is influencing the fluid velocity 

    :type: float
    '''


class Controller:
    '''Game engine logic brick to process events, connecting sensors to actuators '''

    active: bool = None
    '''Set the active state of the controller 

    :type: bool
    '''

    actuators: typing.List['Actuator'] = None
    '''The list containing the actuators connected to the controller 

    :type: typing.List['Actuator']
    '''

    name: str = None
    '''

    :type: str
    '''

    show_expanded: bool = None
    '''Set controller expanded in the user interface 

    :type: bool
    '''

    states: int = None
    '''Set Controller state index (1 to 30) 

    :type: int
    '''

    type: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    use_priority: bool = None
    '''Mark controller for execution before all non-marked controllers (good for startup scripts) 

    :type: bool
    '''

    def link(self, sensor: 'Sensor' = None, actuator: 'Actuator' = None):
        '''Link the controller with a sensor/actuator 

        :param sensor: Sensor to link the controller to 
        :type sensor: 'Sensor'
        :param actuator: Actuator to link the controller to 
        :type actuator: 'Actuator'
        '''
        pass

    def unlink(self, sensor: 'Sensor' = None, actuator: 'Actuator' = None):
        '''Unlink the controller from a sensor/actuator 

        :param sensor: Sensor to unlink the controller from 
        :type sensor: 'Sensor'
        :param actuator: Actuator to unlink the controller from 
        :type actuator: 'Actuator'
        '''
        pass


class CopyLocationConstraint:
    '''Copy the location of the target '''

    head_tail: float = None
    '''Target along length of bone: Head=0, Tail=1 

    :type: float
    '''

    invert_x: bool = None
    '''Invert the X location 

    :type: bool
    '''

    invert_y: bool = None
    '''Invert the Y location 

    :type: bool
    '''

    invert_z: bool = None
    '''Invert the Z location 

    :type: bool
    '''

    subtarget: str = None
    '''

    :type: str
    '''

    target: 'Object' = None
    '''Target Object 

    :type: 'Object'
    '''

    use_bbone_shape: bool = None
    '''Follow shape of B-Bone segments when calculating Head/Tail position 

    :type: bool
    '''

    use_offset: bool = None
    '''Add original location into copied location 

    :type: bool
    '''

    use_x: bool = None
    '''Copy the target’s X location 

    :type: bool
    '''

    use_y: bool = None
    '''Copy the target’s Y location 

    :type: bool
    '''

    use_z: bool = None
    '''Copy the target’s Z location 

    :type: bool
    '''


class CopyRotationConstraint:
    '''Copy the rotation of the target '''

    invert_x: bool = None
    '''Invert the X rotation 

    :type: bool
    '''

    invert_y: bool = None
    '''Invert the Y rotation 

    :type: bool
    '''

    invert_z: bool = None
    '''Invert the Z rotation 

    :type: bool
    '''

    subtarget: str = None
    '''

    :type: str
    '''

    target: 'Object' = None
    '''Target Object 

    :type: 'Object'
    '''

    use_offset: bool = None
    '''Add original rotation into copied rotation 

    :type: bool
    '''

    use_x: bool = None
    '''Copy the target’s X rotation 

    :type: bool
    '''

    use_y: bool = None
    '''Copy the target’s Y rotation 

    :type: bool
    '''

    use_z: bool = None
    '''Copy the target’s Z rotation 

    :type: bool
    '''


class CopyScaleConstraint:
    '''Copy the scale of the target '''

    subtarget: str = None
    '''

    :type: str
    '''

    target: 'Object' = None
    '''Target Object 

    :type: 'Object'
    '''

    use_offset: bool = None
    '''Add original scale into copied scale 

    :type: bool
    '''

    use_x: bool = None
    '''Copy the target’s X scale 

    :type: bool
    '''

    use_y: bool = None
    '''Copy the target’s Y scale 

    :type: bool
    '''

    use_z: bool = None
    '''Copy the target’s Z scale 

    :type: bool
    '''


class CopyTransformsConstraint:
    '''Copy all the transforms of the target '''

    head_tail: float = None
    '''Target along length of bone: Head=0, Tail=1 

    :type: float
    '''

    subtarget: str = None
    '''

    :type: str
    '''

    target: 'Object' = None
    '''Target Object 

    :type: 'Object'
    '''

    use_bbone_shape: bool = None
    '''Follow shape of B-Bone segments when calculating Head/Tail position 

    :type: bool
    '''


class CorrectiveSmoothModifier:
    '''Correct distortion caused by deformation '''

    factor: float = None
    '''Smooth factor effect 

    :type: float
    '''

    invert_vertex_group: bool = None
    '''Invert vertex group influence 

    :type: bool
    '''

    is_bind: bool = None
    '''

    :type: bool
    '''

    iterations: int = None
    '''

    :type: int
    '''

    rest_source: typing.Union[int, str] = None
    '''Select the source of rest positions 

    :type: typing.Union[int, str]
    '''

    smooth_type: typing.Union[int, str] = None
    '''Method used for smoothing 

    :type: typing.Union[int, str]
    '''

    use_only_smooth: bool = None
    '''Apply smoothing without reconstructing the surface 

    :type: bool
    '''

    use_pin_boundary: bool = None
    '''Excludes boundary vertices from being smoothed 

    :type: bool
    '''

    vertex_group: str = None
    '''Name of Vertex Group which determines influence of modifier per point 

    :type: str
    '''


class CrossSequence:
    '''Cross Sequence '''

    input_1: 'Sequence' = None
    '''First input for the effect strip 

    :type: 'Sequence'
    '''

    input_2: 'Sequence' = None
    '''Second input for the effect strip 

    :type: 'Sequence'
    '''

    input_count: int = None
    '''

    :type: int
    '''


class Curve:
    '''Curve data-block storing curves, splines and NURBS '''

    animation_data: 'AnimData' = None
    '''Animation data for this data-block 

    :type: 'AnimData'
    '''

    bevel_depth: float = None
    '''Bevel depth when not using a bevel object 

    :type: float
    '''

    bevel_factor_end: float = None
    '''Factor that defines to where beveling of spline happens (0=to the very beginning, 1=to the very end) 

    :type: float
    '''

    bevel_factor_mapping_end: typing.Union[int, str] = None
    '''Determines how the end bevel factor is mapped to a spline 

    :type: typing.Union[int, str]
    '''

    bevel_factor_mapping_start: typing.Union[int, str] = None
    '''Determines how the start bevel factor is mapped to a spline 

    :type: typing.Union[int, str]
    '''

    bevel_factor_start: float = None
    '''Factor that defines from where beveling of spline happens (0=from the very beginning, 1=from the very end) 

    :type: float
    '''

    bevel_object: 'Object' = None
    '''Curve object name that defines the bevel shape 

    :type: 'Object'
    '''

    bevel_resolution: int = None
    '''Bevel resolution when depth is non-zero and no specific bevel object has been defined 

    :type: int
    '''

    cycles: 'CyclesMeshSettings' = None
    '''Cycles mesh settings 

    :type: 'CyclesMeshSettings'
    '''

    dimensions: typing.Union[int, str] = None
    '''Select 2D or 3D curve type 

    :type: typing.Union[int, str]
    '''

    eval_time: float = None
    '''Parametric position along the length of the curve that Objects ‘following’ it should be at (position is evaluated by dividing by the ‘Path Length’ value) 

    :type: float
    '''

    extrude: float = None
    '''Amount of curve extrusion when not using a bevel object 

    :type: float
    '''

    fill_mode: typing.Union[int, str] = None
    '''Mode of filling curve 

    :type: typing.Union[int, str]
    '''

    is_editmode: bool = None
    '''True when used in editmode 

    :type: bool
    '''

    materials: typing.List['Material'] = None
    '''

    :type: typing.List['Material']
    '''

    offset: float = None
    '''Offset the curve to adjust the width of a text 

    :type: float
    '''

    path_duration: int = None
    '''The number of frames that are needed to traverse the path, defining the maximum value for the ‘Evaluation Time’ setting 

    :type: int
    '''

    render_resolution_u: int = None
    '''Surface resolution in U direction used while rendering (zero uses preview resolution) 

    :type: int
    '''

    render_resolution_v: int = None
    '''Surface resolution in V direction used while rendering (zero uses preview resolution) 

    :type: int
    '''

    resolution_u: int = None
    '''Surface resolution in U direction 

    :type: int
    '''

    resolution_v: int = None
    '''Surface resolution in V direction 

    :type: int
    '''

    shape_keys: 'Key' = None
    '''

    :type: 'Key'
    '''

    show_handles: bool = None
    '''Display Bezier handles in editmode 

    :type: bool
    '''

    show_normal_face: bool = None
    '''Display 3D curve normals in editmode 

    :type: bool
    '''

    splines: typing.List['Spline'] = None
    '''Collection of splines in this curve data object 

    :type: typing.List['Spline']
    '''

    taper_object: 'Object' = None
    '''Curve object name that defines the taper (width) 

    :type: 'Object'
    '''

    texspace_location: float = None
    '''Texture space location 

    :type: float
    '''

    texspace_size: float = None
    '''Texture space size 

    :type: float
    '''

    twist_mode: typing.Union[int, str] = None
    '''The type of tilt calculation for 3D Curves 

    :type: typing.Union[int, str]
    '''

    twist_smooth: float = None
    '''Smoothing iteration for tangents 

    :type: float
    '''

    use_auto_texspace: bool = None
    '''Adjust active object’s texture space automatically when transforming object 

    :type: bool
    '''

    use_deform_bounds: bool = None
    '''Option for curve-deform: Use the mesh bounds to clamp the deformation 

    :type: bool
    '''

    use_fill_caps: bool = None
    '''Fill caps for beveled curves 

    :type: bool
    '''

    use_fill_deform: bool = None
    '''Fill curve after applying shape keys and all modifiers 

    :type: bool
    '''

    use_map_taper: bool = None
    '''Map effect of taper object on actually beveled curve 

    :type: bool
    '''

    use_path: bool = None
    '''Enable the curve to become a translation path 

    :type: bool
    '''

    use_path_follow: bool = None
    '''Make curve path children to rotate along the path 

    :type: bool
    '''

    use_radius: bool = None
    '''Option for paths and curve-deform: apply the curve radius with path following it and deforming 

    :type: bool
    '''

    use_stretch: bool = None
    '''Option for curve-deform: make deformed child to stretch along entire path 

    :type: bool
    '''

    use_uv_as_generated: bool = None
    '''Uses the UV values as Generated textured coordinates 

    :type: bool
    '''

    def transform(self, matrix: float, shape_keys: bool = False):
        '''Transform curve by a matrix 

        :param matrix: Matrix 
        :type matrix: float
        :param shape_keys: Transform Shape Keys 
        :type shape_keys: bool
        '''
        pass

    def validate_material_indices(self, ) -> bool:
        '''Validate material indices of splines or letters, return True when the curve has had invalid indices corrected (to default 0) 

        :rtype: bool
        :return:  Result 
        '''
        pass


class CurveMap:
    '''Curve in a curve mapping '''

    extend: typing.Union[int, str] = None
    '''Extrapolate the curve or extend it horizontally 

    :type: typing.Union[int, str]
    '''

    points: typing.List['CurveMapPoints'] = None
    '''

    :type: typing.List['CurveMapPoints']
    '''

    def evaluate(self, position: float) -> float:
        '''Evaluate curve at given location 

        :param position: Position, Position to evaluate curve at 
        :type position: float
        :rtype: float
        :return:  Value, Value of curve at given location 
        '''
        pass


class CurveMapPoint:
    '''Point of a curve used for a curve mapping '''

    handle_type: typing.Union[int, str] = None
    '''Curve interpolation at this point: Bezier or vector 

    :type: typing.Union[int, str]
    '''

    location: float = None
    '''X/Y coordinates of the curve point 

    :type: float
    '''

    select: bool = None
    '''Selection state of the curve point 

    :type: bool
    '''


class CurveMapPoints:
    '''Collection of Curve Map Points '''

    def new(self, position: float, value: float) -> 'CurveMapPoint':
        '''Add point to CurveMap 

        :param position: Position, Position to add point 
        :type position: float
        :param value: Value, Value of point 
        :type value: float
        :rtype: 'CurveMapPoint'
        :return:  New point 
        '''
        pass

    def remove(self, point: 'CurveMapPoint'):
        '''Delete point from CurveMap 

        :param point: PointElement to remove 
        :type point: 'CurveMapPoint'
        '''
        pass


class CurveMapping:
    '''Curve mapping to map color, vector and scalar values to other values using a user defined curve '''

    black_level: float = None
    '''For RGB curves, the color that black is mapped to 

    :type: float
    '''

    clip_max_x: float = None
    '''

    :type: float
    '''

    clip_max_y: float = None
    '''

    :type: float
    '''

    clip_min_x: float = None
    '''

    :type: float
    '''

    clip_min_y: float = None
    '''

    :type: float
    '''

    curves: typing.List['CurveMap'] = None
    '''

    :type: typing.List['CurveMap']
    '''

    use_clip: bool = None
    '''Force the curve view to fit a defined boundary 

    :type: bool
    '''

    white_level: float = None
    '''For RGB curves, the color that white is mapped to 

    :type: float
    '''

    def update(self, ):
        '''Update curve mapping after making changes 

        '''
        pass

    def initialize(self, ):
        '''Initialize curve 

        '''
        pass


class CurveModifier:
    '''Curve deformation modifier '''

    deform_axis: typing.Union[int, str] = None
    '''The axis that the curve deforms along 

    :type: typing.Union[int, str]
    '''

    object: 'Object' = None
    '''Curve object to deform with 

    :type: 'Object'
    '''

    vertex_group: str = None
    '''Name of Vertex Group which determines influence of modifier per point 

    :type: str
    '''


class CurvePaintSettings:
    corner_angle: float = None
    '''Angles above this are considered corners 

    :type: float
    '''

    curve_type: typing.Union[int, str] = None
    '''Type of curve to use for new strokes 

    :type: typing.Union[int, str]
    '''

    depth_mode: typing.Union[int, str] = None
    '''Method of projecting depth 

    :type: typing.Union[int, str]
    '''

    error_threshold: int = None
    '''Allow deviation for a smoother, less precise line 

    :type: int
    '''

    fit_method: typing.Union[int, str] = None
    '''Curve fitting method 

    :type: typing.Union[int, str]
    '''

    radius_max: float = None
    '''Radius to use when the maximum pressure is applied (or when a tablet isn’t used) 

    :type: float
    '''

    radius_min: float = None
    '''Minimum radius when the minimum pressure is applied (also the minimum when tapering) 

    :type: float
    '''

    radius_taper_end: float = None
    '''Taper factor for the radius of each point along the curve 

    :type: float
    '''

    radius_taper_start: float = None
    '''Taper factor for the radius of each point along the curve 

    :type: float
    '''

    surface_offset: float = None
    '''Offset the stroke from the surface 

    :type: float
    '''

    surface_plane: typing.Union[int, str] = None
    '''Plane for projected stroke 

    :type: typing.Union[int, str]
    '''

    use_corners_detect: bool = None
    '''Detect corners and use non-aligned handles 

    :type: bool
    '''

    use_offset_absolute: bool = None
    '''Apply a fixed offset (don’t scale by the radius) 

    :type: bool
    '''

    use_pressure_radius: bool = None
    '''Map tablet pressure to curve radius 

    :type: bool
    '''

    use_stroke_endpoints: bool = None
    '''Use the start of the stroke for the depth 

    :type: bool
    '''


class CurveSplines:
    '''Collection of curve splines '''

    active: 'Spline' = None
    '''Active curve spline 

    :type: 'Spline'
    '''

    def new(self, type: typing.Union[int, str]) -> 'Spline':
        '''Add a new spline to the curve 

        :param type: type for the new spline 
        :type type: typing.Union[int, str]
        :rtype: 'Spline'
        :return:  The newly created spline 
        '''
        pass

    def remove(self, spline: 'Spline'):
        '''Remove a spline from a curve 

        :param spline: The spline to remove 
        :type spline: 'Spline'
        '''
        pass

    def clear(self, ):
        '''Remove all splines from a curve 

        '''
        pass


class CurvesModifier:
    '''RGB curves modifier for sequence strip '''

    curve_mapping: 'CurveMapping' = None
    '''

    :type: 'CurveMapping'
    '''


class CyclesCameraSettings:
    aperture_blades: int = None
    '''Number of blades in aperture for polygonal bokeh (at least 3) 

    :type: int
    '''

    aperture_fstop: float = None
    '''F-stop ratio (lower numbers give more defocus, higher numbers give a sharper image) 

    :type: float
    '''

    aperture_ratio: float = None
    '''Distortion to simulate anamorphic lens bokeh 

    :type: float
    '''

    aperture_rotation: float = None
    '''Rotation of blades in aperture 

    :type: float
    '''

    aperture_size: float = None
    '''Radius of the aperture for depth of field (higher values give more defocus) 

    :type: float
    '''

    aperture_type: typing.Union[int, str] = None
    '''Use f-stop number or aperture radius 

    :type: typing.Union[int, str]
    '''

    fisheye_fov: float = None
    '''Field of view for the fisheye lens 

    :type: float
    '''

    fisheye_lens: float = None
    '''Lens focal length (mm) 

    :type: float
    '''

    latitude_max: float = None
    '''Maximum latitude (vertical angle) for the equirectangular lens 

    :type: float
    '''

    latitude_min: float = None
    '''Minimum latitude (vertical angle) for the equirectangular lens 

    :type: float
    '''

    longitude_max: float = None
    '''Maximum longitude (horizontal angle) for the equirectangular lens 

    :type: float
    '''

    longitude_min: float = None
    '''Minimum longitude (horizontal angle) for the equirectangular lens 

    :type: float
    '''

    panorama_type: typing.Union[int, str] = None
    '''Distortion to use for the calculation 

    :type: typing.Union[int, str]
    '''


class CyclesCurveRenderSettings:
    cull_backfacing: bool = None
    '''Do not test the back-face of each strand 

    :type: bool
    '''

    maximum_width: float = None
    '''Maximum extension that strand radius can be increased by 

    :type: float
    '''

    minimum_width: float = None
    '''Minimal pixel width for strands (0 - deactivated) 

    :type: float
    '''

    primitive: typing.Union[int, str] = None
    '''Type of primitive used for hair rendering 

    :type: typing.Union[int, str]
    '''

    resolution: int = None
    '''Resolution of generated mesh 

    :type: int
    '''

    shape: typing.Union[int, str] = None
    '''Form of hair 

    :type: typing.Union[int, str]
    '''

    subdivisions: int = None
    '''Number of subdivisions used in Cardinal curve intersection (power of 2) 

    :type: int
    '''

    use_curves: bool = None
    '''Activate Cycles hair rendering for particle system 

    :type: bool
    '''


class CyclesCurveSettings:
    radius_scale: float = None
    '''Multiplier of width properties 

    :type: float
    '''

    root_width: float = None
    '''Strand’s width at root 

    :type: float
    '''

    shape: float = None
    '''Strand shape parameter 

    :type: float
    '''

    tip_width: float = None
    '''Strand’s width at tip 

    :type: float
    '''

    use_closetip: bool = None
    '''Set tip radius to zero 

    :type: bool
    '''


class CyclesDeviceSettings:
    id: str = None
    '''

    :type: str
    '''

    name: str = None
    '''

    :type: str
    '''

    type: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    use: bool = None
    '''

    :type: bool
    '''


class CyclesLampSettings:
    cast_shadow: bool = None
    '''Lamp casts shadows 

    :type: bool
    '''

    is_portal: bool = None
    '''Use this area lamp to guide sampling of the background, note that this will make the lamp invisible 

    :type: bool
    '''

    max_bounces: int = None
    '''Maximum number of bounces the light will contribute to the render 

    :type: int
    '''

    samples: int = None
    '''Number of light samples to render for each AA sample 

    :type: int
    '''

    use_multiple_importance_sampling: bool = None
    '''Use multiple importance sampling for the lamp, reduces noise for area lamps and sharp glossy materials 

    :type: bool
    '''


class CyclesMaterialSettings:
    displacement_method: typing.Union[int, str] = None
    '''Method to use for the displacement 

    :type: typing.Union[int, str]
    '''

    homogeneous_volume: bool = None
    '''When using volume rendering, assume volume has the same density everywhere (not using any textures), for faster rendering 

    :type: bool
    '''

    sample_as_light: bool = None
    '''Use multiple importance sampling for this material, disabling may reduce overall noise for large objects that emit little light compared to other light sources 

    :type: bool
    '''

    use_transparent_shadow: bool = None
    '''Use transparent shadows for this material if it contains a Transparent BSDF, disabling will render faster but not give accurate shadows 

    :type: bool
    '''

    volume_interpolation: typing.Union[int, str] = None
    '''Interpolation method to use for smoke/fire volumes 

    :type: typing.Union[int, str]
    '''

    volume_sampling: typing.Union[int, str] = None
    '''Sampling method to use for volumes 

    :type: typing.Union[int, str]
    '''


class CyclesMeshSettings:
    pass


class CyclesObjectSettings:
    dicing_rate: float = None
    '''Multiplier for scene dicing rate (located in the Geometry Panel) 

    :type: float
    '''

    is_shadow_catcher: bool = None
    '''Only render shadows on this object, for compositing renders into real footage 

    :type: bool
    '''

    motion_steps: int = None
    '''Control accuracy of deformation motion blur, more steps gives more memory usage (actual number of steps is 2^(steps - 1)) 

    :type: int
    '''

    use_adaptive_subdivision: bool = None
    '''Use adaptive render time subdivision 

    :type: bool
    '''

    use_camera_cull: bool = None
    '''Allow this object and its duplicators to be culled by camera space culling 

    :type: bool
    '''

    use_deform_motion: bool = None
    '''Use deformation motion blur for this object 

    :type: bool
    '''

    use_distance_cull: bool = None
    '''Allow this object and its duplicators to be culled by distance from camera 

    :type: bool
    '''

    use_motion_blur: bool = None
    '''Use motion blur for this object 

    :type: bool
    '''


class CyclesPreferences:
    compute_device_type: typing.Union[int, str] = None
    '''Device to use for computation (rendering with Cycles) 

    :type: typing.Union[int, str]
    '''

    devices: typing.List['CyclesDeviceSettings'] = None
    '''

    :type: typing.List['CyclesDeviceSettings']
    '''

    def draw(self, context):
        '''

        '''
        pass

    def draw_impl(self, layout, context):
        '''

        '''
        pass

    def find_existing_device_entry(self, device):
        '''

        '''
        pass

    def get_device_types(self, context):
        '''

        '''
        pass

    def get_devices(self, ):
        '''

        '''
        pass

    def get_num_gpu_devices(self, ):
        '''

        '''
        pass

    def has_active_device(self, ):
        '''

        '''
        pass

    def update_device_entries(self, device_list):
        '''

        '''
        pass


class CyclesRenderLayerSettings:
    denoising_diffuse_direct: bool = None
    '''Denoise the direct diffuse lighting 

    :type: bool
    '''

    denoising_diffuse_indirect: bool = None
    '''Denoise the indirect diffuse lighting 

    :type: bool
    '''

    denoising_feature_strength: float = None
    '''Controls removal of noisy image feature passes (lower values preserve more detail, but aren’t as smooth) 

    :type: float
    '''

    denoising_glossy_direct: bool = None
    '''Denoise the direct glossy lighting 

    :type: bool
    '''

    denoising_glossy_indirect: bool = None
    '''Denoise the indirect glossy lighting 

    :type: bool
    '''

    denoising_radius: int = None
    '''Size of the image area that’s used to denoise a pixel (higher values are smoother, but might lose detail and are slower) 

    :type: int
    '''

    denoising_relative_pca: bool = None
    '''When removing pixels that don’t carry information, use a relative threshold instead of an absolute one (can help to reduce artifacts, but might cause detail loss around edges) 

    :type: bool
    '''

    denoising_store_passes: bool = None
    '''Store the denoising feature passes and the noisy image 

    :type: bool
    '''

    denoising_strength: float = None
    '''Controls neighbor pixel weighting for the denoising filter (lower values preserve more detail, but aren’t as smooth) 

    :type: float
    '''

    denoising_subsurface_direct: bool = None
    '''Denoise the direct subsurface lighting 

    :type: bool
    '''

    denoising_subsurface_indirect: bool = None
    '''Denoise the indirect subsurface lighting 

    :type: bool
    '''

    denoising_transmission_direct: bool = None
    '''Denoise the direct transmission lighting 

    :type: bool
    '''

    denoising_transmission_indirect: bool = None
    '''Denoise the indirect transmission lighting 

    :type: bool
    '''

    pass_debug_bvh_intersections: bool = None
    '''Store Debug BVH Intersections 

    :type: bool
    '''

    pass_debug_bvh_traversed_instances: bool = None
    '''Store Debug BVH Traversed Instances pass 

    :type: bool
    '''

    pass_debug_bvh_traversed_nodes: bool = None
    '''Store Debug BVH Traversed Nodes pass 

    :type: bool
    '''

    pass_debug_ray_bounces: bool = None
    '''Store Debug Ray Bounces pass 

    :type: bool
    '''

    use_denoising: bool = None
    '''Denoise the rendered image 

    :type: bool
    '''


class CyclesRenderSettings:
    aa_samples: int = None
    '''Number of antialiasing samples to render for each pixel 

    :type: int
    '''

    ao_bounces: int = None
    '''Approximate indirect light with background tinted ambient occlusion at the specified bounce, 0 disables this feature 

    :type: int
    '''

    ao_bounces_render: int = None
    '''Approximate indirect light with background tinted ambient occlusion at the specified bounce, 0 disables this feature 

    :type: int
    '''

    ao_samples: int = None
    '''Number of ambient occlusion samples to render for each AA sample 

    :type: int
    '''

    bake_type: typing.Union[int, str] = None
    '''Type of pass to bake 

    :type: typing.Union[int, str]
    '''

    blur_glossy: float = None
    '''Adaptively blur glossy shaders after blurry bounces, to reduce noise at the cost of accuracy 

    :type: float
    '''

    camera_cull_margin: float = None
    '''Margin for the camera space culling 

    :type: float
    '''

    caustics_reflective: bool = None
    '''Use reflective caustics, resulting in a brighter image (more noise but added realism) 

    :type: bool
    '''

    caustics_refractive: bool = None
    '''Use refractive caustics, resulting in a brighter image (more noise but added realism) 

    :type: bool
    '''

    debug_bvh_time_steps: int = None
    '''Split BVH primitives by this number of time steps to speed up render time in cost of memory 

    :type: int
    '''

    debug_bvh_type: typing.Union[int, str] = None
    '''Choose between faster updates, or faster render 

    :type: typing.Union[int, str]
    '''

    debug_cancel_timeout: float = None
    '''

    :type: float
    '''

    debug_opencl_device_type: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    debug_opencl_kernel_single_program: bool = None
    '''

    :type: bool
    '''

    debug_opencl_kernel_type: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    debug_opencl_mem_limit: int = None
    '''Artificial limit on OpenCL memory usage in MB (0 to disable limit) 

    :type: int
    '''

    debug_reset_timeout: float = None
    '''

    :type: float
    '''

    debug_text_timeout: float = None
    '''

    :type: float
    '''

    debug_tile_size: int = None
    '''

    :type: int
    '''

    debug_use_cpu_avx: bool = None
    '''

    :type: bool
    '''

    debug_use_cpu_avx2: bool = None
    '''

    :type: bool
    '''

    debug_use_cpu_split_kernel: bool = None
    '''

    :type: bool
    '''

    debug_use_cpu_sse2: bool = None
    '''

    :type: bool
    '''

    debug_use_cpu_sse3: bool = None
    '''

    :type: bool
    '''

    debug_use_cpu_sse41: bool = None
    '''

    :type: bool
    '''

    debug_use_cuda_adaptive_compile: bool = None
    '''

    :type: bool
    '''

    debug_use_cuda_split_kernel: bool = None
    '''

    :type: bool
    '''

    debug_use_hair_bvh: bool = None
    '''Use special type BVH optimized for hair (uses more ram but renders faster) 

    :type: bool
    '''

    debug_use_opencl_debug: bool = None
    '''

    :type: bool
    '''

    debug_use_qbvh: bool = None
    '''

    :type: bool
    '''

    debug_use_spatial_splits: bool = None
    '''Use BVH spatial splits: longer builder time, faster render 

    :type: bool
    '''

    device: typing.Union[int, str] = None
    '''Device to use for rendering 

    :type: typing.Union[int, str]
    '''

    dicing_rate: float = None
    '''Size of a micropolygon in pixels 

    :type: float
    '''

    diffuse_bounces: int = None
    '''Maximum number of diffuse reflection bounces, bounded by total maximum 

    :type: int
    '''

    diffuse_samples: int = None
    '''Number of diffuse bounce samples to render for each AA sample 

    :type: int
    '''

    distance_cull_margin: float = None
    '''Cull objects which are further away from camera than this distance 

    :type: float
    '''

    feature_set: typing.Union[int, str] = None
    '''Feature set to use for rendering 

    :type: typing.Union[int, str]
    '''

    film_exposure: float = None
    '''Image brightness scale 

    :type: float
    '''

    film_transparent: bool = None
    '''World background is transparent with premultiplied alpha 

    :type: bool
    '''

    filter_type: typing.Union[int, str] = None
    '''Pixel filter type 

    :type: typing.Union[int, str]
    '''

    filter_width: float = None
    '''Pixel filter width 

    :type: float
    '''

    glossy_bounces: int = None
    '''Maximum number of glossy reflection bounces, bounded by total maximum 

    :type: int
    '''

    glossy_samples: int = None
    '''Number of glossy bounce samples to render for each AA sample 

    :type: int
    '''

    light_sampling_threshold: float = None
    '''Probabilistically terminate light samples when the light contribution is below this threshold (more noise but faster rendering). Zero disables the test and never ignores lights 

    :type: float
    '''

    max_bounces: int = None
    '''Total maximum number of bounces 

    :type: int
    '''

    max_subdivisions: int = None
    '''Stop subdividing when this level is reached even if the dice rate would produce finer tessellation 

    :type: int
    '''

    mesh_light_samples: int = None
    '''Number of mesh emission light samples to render for each AA sample 

    :type: int
    '''

    min_bounces: int = None
    '''Minimum number of bounces, setting this lower than the maximum enables probabilistic path termination (faster but noisier) 

    :type: int
    '''

    motion_blur_position: typing.Union[int, str] = None
    '''Offset for the shutter’s time interval, allows to change the motion blur trails 

    :type: typing.Union[int, str]
    '''

    pixel_filter_type: typing.Union[int, str] = None
    '''Pixel filter type 

    :type: typing.Union[int, str]
    '''

    preview_aa_samples: int = None
    '''Number of antialiasing samples to render in the viewport, unlimited if 0 

    :type: int
    '''

    preview_active_layer: bool = None
    '''Preview active render layer in viewport 

    :type: bool
    '''

    preview_dicing_rate: float = None
    '''Size of a micropolygon in pixels during preview render 

    :type: float
    '''

    preview_pause: bool = None
    '''Pause all viewport preview renders 

    :type: bool
    '''

    preview_samples: int = None
    '''Number of samples to render in the viewport, unlimited if 0 

    :type: int
    '''

    preview_start_resolution: int = None
    '''Resolution to start rendering preview at, progressively increasing it to the full viewport size 

    :type: int
    '''

    progressive: typing.Union[int, str] = None
    '''Method to sample lights and materials 

    :type: typing.Union[int, str]
    '''

    rolling_shutter_duration: float = None
    '''Scanline “exposure” time for the rolling shutter effect 

    :type: float
    '''

    rolling_shutter_type: typing.Union[int, str] = None
    '''Type of rolling shutter effect matching CMOS-based cameras 

    :type: typing.Union[int, str]
    '''

    sample_all_lights_direct: bool = None
    '''Sample all lights (for direct samples), rather than randomly picking one 

    :type: bool
    '''

    sample_all_lights_indirect: bool = None
    '''Sample all lights (for indirect samples), rather than randomly picking one 

    :type: bool
    '''

    sample_clamp_direct: float = None
    '''If non-zero, the maximum value for a direct sample, higher values will be scaled down to avoid too much noise and slow convergence at the cost of accuracy 

    :type: float
    '''

    sample_clamp_indirect: float = None
    '''If non-zero, the maximum value for an indirect sample, higher values will be scaled down to avoid too much noise and slow convergence at the cost of accuracy 

    :type: float
    '''

    samples: int = None
    '''Number of samples to render for each pixel 

    :type: int
    '''

    sampling_pattern: typing.Union[int, str] = None
    '''Random sampling pattern used by the integrator 

    :type: typing.Union[int, str]
    '''

    seed: int = None
    '''Seed value for integrator to get different noise patterns 

    :type: int
    '''

    shading_system: bool = None
    '''Use Open Shading Language (CPU rendering only) 

    :type: bool
    '''

    subsurface_samples: int = None
    '''Number of subsurface scattering samples to render for each AA sample 

    :type: int
    '''

    texture_limit: typing.Union[int, str] = None
    '''Limit texture size used by viewport rendering 

    :type: typing.Union[int, str]
    '''

    texture_limit_render: typing.Union[int, str] = None
    '''Limit texture size used by final rendering 

    :type: typing.Union[int, str]
    '''

    tile_order: typing.Union[int, str] = None
    '''Tile order for rendering 

    :type: typing.Union[int, str]
    '''

    transmission_bounces: int = None
    '''Maximum number of transmission bounces, bounded by total maximum 

    :type: int
    '''

    transmission_samples: int = None
    '''Number of transmission bounce samples to render for each AA sample 

    :type: int
    '''

    transparent_max_bounces: int = None
    '''Maximum number of transparent bounces 

    :type: int
    '''

    transparent_min_bounces: int = None
    '''Minimum number of transparent bounces, setting this lower than the maximum enables probabilistic path termination (faster but noisier) 

    :type: int
    '''

    use_animated_seed: bool = None
    '''Use different seed values (and hence noise patterns) at different frames 

    :type: bool
    '''

    use_camera_cull: bool = None
    '''Allow objects to be culled based on the camera frustum 

    :type: bool
    '''

    use_distance_cull: bool = None
    '''Allow objects to be culled based on the distance from camera 

    :type: bool
    '''

    use_layer_samples: typing.Union[int, str] = None
    '''How to use per render layer sample settings 

    :type: typing.Union[int, str]
    '''

    use_progressive_refine: bool = None
    '''Instead of rendering each tile until it is finished, refine the whole image progressively (this renders somewhat slower, but time can be saved by manually stopping the render when the noise is low enough) 

    :type: bool
    '''

    use_square_samples: bool = None
    '''Square sampling values for easier artist control 

    :type: bool
    '''

    use_transparent_shadows: bool = None
    '''Use transparency of surfaces for rendering shadows 

    :type: bool
    '''

    volume_bounces: int = None
    '''Maximum number of volumetric scattering events 

    :type: int
    '''

    volume_max_steps: int = None
    '''Maximum number of steps through the volume before giving up, to avoid extremely long render times with big objects or small step sizes 

    :type: int
    '''

    volume_samples: int = None
    '''Number of volume scattering samples to render for each AA sample 

    :type: int
    '''

    volume_step_size: float = None
    '''Distance between volume shader samples when rendering the volume (lower values give more accurate and detailed results, but also increased render time) 

    :type: float
    '''


class CyclesVisibilitySettings:
    camera: bool = None
    '''Object visibility for camera rays 

    :type: bool
    '''

    diffuse: bool = None
    '''Object visibility for diffuse reflection rays 

    :type: bool
    '''

    glossy: bool = None
    '''Object visibility for glossy reflection rays 

    :type: bool
    '''

    scatter: bool = None
    '''Object visibility for volume scatter rays 

    :type: bool
    '''

    shadow: bool = None
    '''Object visibility for shadow rays 

    :type: bool
    '''

    transmission: bool = None
    '''Object visibility for transmission rays 

    :type: bool
    '''


class CyclesWorldSettings:
    homogeneous_volume: bool = None
    '''When using volume rendering, assume volume has the same density everywhere(not using any textures), for faster rendering 

    :type: bool
    '''

    max_bounces: int = None
    '''Maximum number of bounces the background light will contribute to the render 

    :type: int
    '''

    sample_as_light: bool = None
    '''Use multiple importance sampling for the environment, enabling for non-solid colors is recommended 

    :type: bool
    '''

    sample_map_resolution: int = None
    '''Importance map size is resolution x resolution; higher values potentially produce less noise, at the cost of memory and speed 

    :type: int
    '''

    samples: int = None
    '''Number of light samples to render for each AA sample 

    :type: int
    '''

    volume_interpolation: typing.Union[int, str] = None
    '''Interpolation method to use for volumes 

    :type: typing.Union[int, str]
    '''

    volume_sampling: typing.Union[int, str] = None
    '''Sampling method to use for volumes 

    :type: typing.Union[int, str]
    '''


class DampedTrackConstraint:
    '''Point toward target by taking the shortest rotation path '''

    head_tail: float = None
    '''Target along length of bone: Head=0, Tail=1 

    :type: float
    '''

    subtarget: str = None
    '''

    :type: str
    '''

    target: 'Object' = None
    '''Target Object 

    :type: 'Object'
    '''

    track_axis: typing.Union[int, str] = None
    '''Axis that points to the target object 

    :type: typing.Union[int, str]
    '''

    use_bbone_shape: bool = None
    '''Follow shape of B-Bone segments when calculating Head/Tail position 

    :type: bool
    '''


class DataTransferModifier:
    '''Modifier transferring some data from a source mesh '''

    data_types_edges: typing.Set[typing.Union[int, str]] = None
    '''Which edge data layers to transfer 

    :type: typing.Set[typing.Union[int, str]]
    '''

    data_types_loops: typing.Set[typing.Union[int, str]] = None
    '''Which face corner data layers to transfer 

    :type: typing.Set[typing.Union[int, str]]
    '''

    data_types_polys: typing.Set[typing.Union[int, str]] = None
    '''Which poly data layers to transfer 

    :type: typing.Set[typing.Union[int, str]]
    '''

    data_types_verts: typing.Set[typing.Union[int, str]] = None
    '''Which vertex data layers to transfer 

    :type: typing.Set[typing.Union[int, str]]
    '''

    edge_mapping: typing.Union[int, str] = None
    '''Method used to map source edges to destination ones 

    :type: typing.Union[int, str]
    '''

    invert_vertex_group: bool = None
    '''Invert vertex group influence 

    :type: bool
    '''

    islands_precision: float = None
    '''Factor controlling precision of islands handling (typically, 0.1 should be enough, higher values can make things really slow) 

    :type: float
    '''

    layers_uv_select_dst: typing.Union[int, str] = None
    '''How to match source and destination layers 

    :type: typing.Union[int, str]
    '''

    layers_uv_select_src: typing.Union[int, str] = None
    '''Which layers to transfer, in case of multi-layers types 

    :type: typing.Union[int, str]
    '''

    layers_vcol_select_dst: typing.Union[int, str] = None
    '''How to match source and destination layers 

    :type: typing.Union[int, str]
    '''

    layers_vcol_select_src: typing.Union[int, str] = None
    '''Which layers to transfer, in case of multi-layers types 

    :type: typing.Union[int, str]
    '''

    layers_vgroup_select_dst: typing.Union[int, str] = None
    '''How to match source and destination layers 

    :type: typing.Union[int, str]
    '''

    layers_vgroup_select_src: typing.Union[int, str] = None
    '''Which layers to transfer, in case of multi-layers types 

    :type: typing.Union[int, str]
    '''

    loop_mapping: typing.Union[int, str] = None
    '''Method used to map source faces’ corners to destination ones 

    :type: typing.Union[int, str]
    '''

    max_distance: float = None
    '''Maximum allowed distance between source and destination element, for non-topology mappings 

    :type: float
    '''

    mix_factor: float = None
    '''Factor to use when applying data to destination (exact behavior depends on mix mode) 

    :type: float
    '''

    mix_mode: typing.Union[int, str] = None
    '''How to affect destination elements with source values 

    :type: typing.Union[int, str]
    '''

    object: 'Object' = None
    '''Object to transfer data from 

    :type: 'Object'
    '''

    poly_mapping: typing.Union[int, str] = None
    '''Method used to map source faces to destination ones 

    :type: typing.Union[int, str]
    '''

    ray_radius: float = None
    '''‘Width’ of rays (especially useful when raycasting against vertices or edges) 

    :type: float
    '''

    use_edge_data: bool = None
    '''Enable edge data transfer 

    :type: bool
    '''

    use_loop_data: bool = None
    '''Enable face corner data transfer 

    :type: bool
    '''

    use_max_distance: bool = None
    '''Source elements must be closer than given distance from destination one 

    :type: bool
    '''

    use_object_transform: bool = None
    '''Evaluate source and destination meshes in global space 

    :type: bool
    '''

    use_poly_data: bool = None
    '''Enable face data transfer 

    :type: bool
    '''

    use_vert_data: bool = None
    '''Enable vertex data transfer 

    :type: bool
    '''

    vert_mapping: typing.Union[int, str] = None
    '''Method used to map source vertices to destination ones 

    :type: typing.Union[int, str]
    '''

    vertex_group: str = None
    '''Vertex group name for selecting the affected areas 

    :type: str
    '''


class DecimateModifier:
    '''Decimation modifier '''

    angle_limit: float = None
    '''Only dissolve angles below this (planar only) 

    :type: float
    '''

    decimate_type: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    delimit: typing.Set[typing.Union[int, str]] = None
    '''Limit merging geometry 

    :type: typing.Set[typing.Union[int, str]]
    '''

    face_count: int = None
    '''The current number of faces in the decimated mesh 

    :type: int
    '''

    invert_vertex_group: bool = None
    '''Invert vertex group influence (collapse only) 

    :type: bool
    '''

    iterations: int = None
    '''Number of times reduce the geometry (unsubdivide only) 

    :type: int
    '''

    ratio: float = None
    '''Ratio of triangles to reduce to (collapse only) 

    :type: float
    '''

    symmetry_axis: typing.Union[int, str] = None
    '''Axis of symmetry 

    :type: typing.Union[int, str]
    '''

    use_collapse_triangulate: bool = None
    '''Keep triangulated faces resulting from decimation (collapse only) 

    :type: bool
    '''

    use_dissolve_boundaries: bool = None
    '''Dissolve all vertices inbetween face boundaries (planar only) 

    :type: bool
    '''

    use_symmetry: bool = None
    '''Maintain symmetry on an axis 

    :type: bool
    '''

    vertex_group: str = None
    '''Vertex group name (collapse only) 

    :type: str
    '''

    vertex_group_factor: float = None
    '''Vertex group strength 

    :type: float
    '''


class DelaySensor:
    '''Sensor to send delayed events '''

    delay: int = None
    '''Delay in number of logic tics before the positive trigger (default 60 per second) 

    :type: int
    '''

    duration: int = None
    '''If >0, delay in number of logic tics before the negative trigger following the positive trigger 

    :type: int
    '''

    use_repeat: bool = None
    '''Toggle repeat option (if selected, the sensor restarts after Delay+Duration logic tics) 

    :type: bool
    '''


class Depsgraph:
    def debug_graphviz(self, filename: str):
        '''debug_graphviz 

        :param filename: File Name, File in which to store graphviz debug output 
        :type filename: str
        '''
        pass

    def debug_rebuild(self, ):
        '''debug_rebuild 

        '''
        pass

    def debug_stats(self, ):
        '''Report the number of elements in the Dependency Graph 

        '''
        pass


class DisplaceModifier:
    '''Displacement modifier '''

    direction: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    mid_level: float = None
    '''Material value that gives no displacement 

    :type: float
    '''

    space: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    strength: float = None
    '''Amount to displace geometry 

    :type: float
    '''

    texture: 'Texture' = None
    '''

    :type: 'Texture'
    '''

    texture_coords: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    texture_coords_object: 'Object' = None
    '''Object to set the texture coordinates 

    :type: 'Object'
    '''

    uv_layer: str = None
    '''UV map name 

    :type: str
    '''

    vertex_group: str = None
    '''Name of Vertex Group which determines influence of modifier per point 

    :type: str
    '''


class DisplaySafeAreas:
    '''Safe Areas used in 3D view and the VSE '''

    action: float = None
    '''Safe area for general elements 

    :type: float
    '''

    action_center: float = None
    '''Safe area for general elements in a different aspect ratio 

    :type: float
    '''

    title: float = None
    '''Safe area for text and graphics 

    :type: float
    '''

    title_center: float = None
    '''Safe area for text and graphics in a different aspect ratio 

    :type: float
    '''


class DistortedNoiseTexture:
    '''Procedural distorted noise texture '''

    distortion: float = None
    '''Amount of distortion 

    :type: float
    '''

    nabla: float = None
    '''Size of derivative offset used for calculating normal 

    :type: float
    '''

    noise_basis: typing.Union[int, str] = None
    '''Noise basis used for turbulence 

    :type: typing.Union[int, str]
    '''

    noise_distortion: typing.Union[int, str] = None
    '''Noise basis for the distortion 

    :type: typing.Union[int, str]
    '''

    noise_scale: float = None
    '''Scaling for noise input 

    :type: float
    '''

    users_material = None
    '''Materials that use this texture (readonly) '''

    users_object_modifier = None
    '''Object modifiers that use this texture (readonly) '''


class DomainFluidSettings:
    '''Fluid simulation settings for the domain of a fluid simulation '''

    compressibility: float = None
    '''Allowed compressibility due to gravitational force for standing fluid (directly affects simulation step size) 

    :type: float
    '''

    end_time: float = None
    '''Simulation time of the last blender frame (in seconds) 

    :type: float
    '''

    filepath: str = None
    '''Directory (and/or filename prefix) to store baked fluid simulation files in 

    :type: str
    '''

    fluid_mesh_vertices: typing.List['FluidVertexVelocity'] = None
    '''Vertices of the fluid mesh generated by simulation 

    :type: typing.List['FluidVertexVelocity']
    '''

    frame_offset: int = None
    '''Offset when reading baked cache 

    :type: int
    '''

    generate_particles: float = None
    '''Amount of particles to generate (0=off, 1=normal, >1=more) 

    :type: float
    '''

    gravity: float = None
    '''Gravity in X, Y and Z direction 

    :type: float
    '''

    grid_levels: int = None
    '''Number of coarsened grids to use (-1 for automatic) 

    :type: int
    '''

    memory_estimate: str = None
    '''Estimated amount of memory needed for baking the domain 

    :type: str
    '''

    partial_slip_factor: float = None
    '''Amount of mixing between no- and free-slip, 0 is no slip and 1 is free slip 

    :type: float
    '''

    preview_resolution: int = None
    '''Preview resolution in X,Y and Z direction 

    :type: int
    '''

    render_display_mode: typing.Union[int, str] = None
    '''How to display the mesh for rendering 

    :type: typing.Union[int, str]
    '''

    resolution: int = None
    '''Domain resolution in X,Y and Z direction 

    :type: int
    '''

    simulation_rate: float = None
    '''Fluid motion rate (0 = stationary, 1 = normal speed) 

    :type: float
    '''

    simulation_scale: float = None
    '''Size of the simulation domain in meters 

    :type: float
    '''

    slip_type: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    start_time: float = None
    '''Simulation time of the first blender frame (in seconds) 

    :type: float
    '''

    surface_smooth: float = None
    '''Amount of surface smoothing (a value of 0 is off, 1 is normal smoothing and more than 1 is extra smoothing) 

    :type: float
    '''

    surface_subdivisions: int = None
    '''Number of isosurface subdivisions (this is necessary for the inclusion of particles into the surface generation - WARNING: can lead to longer computation times !) 

    :type: int
    '''

    threads: int = None
    '''Override number of threads for the simulation, 0 is automatic 

    :type: int
    '''

    tracer_particles: int = None
    '''Number of tracer particles to generate 

    :type: int
    '''

    use_reverse_frames: bool = None
    '''Reverse fluid frames 

    :type: bool
    '''

    use_speed_vectors: bool = None
    '''Generate speed vectors for vector blur 

    :type: bool
    '''

    use_surface_noobs: bool = None
    '''Removes the air gap between fluid surface and obstacles - WARNING: Can result in a dissolving surface in other areas 

    :type: bool
    '''

    use_time_override: bool = None
    '''Use a custom start and end time (in seconds) instead of the scene’s timeline 

    :type: bool
    '''

    viewport_display_mode: typing.Union[int, str] = None
    '''How to display the mesh in the viewport 

    :type: typing.Union[int, str]
    '''

    viscosity_base: float = None
    '''Viscosity setting: value that is multiplied by 10 to the power of (exponent*-1) 

    :type: float
    '''

    viscosity_exponent: int = None
    '''Negative exponent for the viscosity value (to simplify entering small values e.g. 5*10^-6) 

    :type: int
    '''


class DopeSheet:
    '''Settings for filtering the channels shown in animation editors '''

    filter_fcurve_name: str = None
    '''F-Curve live filtering string 

    :type: str
    '''

    filter_group: 'Group' = None
    '''Group that included object should be a member of 

    :type: 'Group'
    '''

    filter_text: str = None
    '''Live filtering string 

    :type: str
    '''

    show_armatures: bool = None
    '''Include visualization of armature related animation data 

    :type: bool
    '''

    show_cameras: bool = None
    '''Include visualization of camera related animation data 

    :type: bool
    '''

    show_curves: bool = None
    '''Include visualization of curve related animation data 

    :type: bool
    '''

    show_datablock_filters: bool = None
    '''Show options for whether channels related to certain types of data are included 

    :type: bool
    '''

    show_expanded_summary: bool = None
    '''Collapse summary when shown, so all other channels get hidden (Dope Sheet editors only) 

    :type: bool
    '''

    show_gpencil: bool = None
    '''Include visualization of Grease Pencil related animation data and frames 

    :type: bool
    '''

    show_gpencil_3d_only: bool = None
    '''Only show Grease Pencil data-blocks used as part of the active scene 

    :type: bool
    '''

    show_hidden: bool = None
    '''Include channels from objects/bone that are not visible 

    :type: bool
    '''

    show_lamps: bool = None
    '''Include visualization of lamp related animation data 

    :type: bool
    '''

    show_lattices: bool = None
    '''Include visualization of lattice related animation data 

    :type: bool
    '''

    show_linestyles: bool = None
    '''Include visualization of Line Style related Animation data 

    :type: bool
    '''

    show_materials: bool = None
    '''Include visualization of material related animation data 

    :type: bool
    '''

    show_meshes: bool = None
    '''Include visualization of mesh related animation data 

    :type: bool
    '''

    show_metaballs: bool = None
    '''Include visualization of metaball related animation data 

    :type: bool
    '''

    show_missing_nla: bool = None
    '''Include animation data-blocks with no NLA data (NLA editor only) 

    :type: bool
    '''

    show_modifiers: bool = None
    '''Include visualization of animation data related to data-blocks linked to modifiers 

    :type: bool
    '''

    show_nodes: bool = None
    '''Include visualization of node related animation data 

    :type: bool
    '''

    show_only_errors: bool = None
    '''Only include F-Curves and drivers that are disabled or have errors 

    :type: bool
    '''

    show_only_group_objects: bool = None
    '''Only include channels from objects in the specified group 

    :type: bool
    '''

    show_only_matching_fcurves: bool = None
    '''Only include F-Curves with names containing search text 

    :type: bool
    '''

    show_only_selected: bool = None
    '''Only include channels relating to selected objects and data 

    :type: bool
    '''

    show_particles: bool = None
    '''Include visualization of particle related animation data 

    :type: bool
    '''

    show_scenes: bool = None
    '''Include visualization of scene related animation data 

    :type: bool
    '''

    show_shapekeys: bool = None
    '''Include visualization of shape key related animation data 

    :type: bool
    '''

    show_speakers: bool = None
    '''Include visualization of speaker related animation data 

    :type: bool
    '''

    show_summary: bool = None
    '''Display an additional ‘summary’ line (Dope Sheet editors only) 

    :type: bool
    '''

    show_textures: bool = None
    '''Include visualization of texture related animation data 

    :type: bool
    '''

    show_transforms: bool = None
    '''Include visualization of object-level animation data (mostly transforms) 

    :type: bool
    '''

    show_worlds: bool = None
    '''Include visualization of world related animation data 

    :type: bool
    '''

    source: 'ID' = None
    '''ID-Block representing source data, usually ID_SCE (i.e. Scene) 

    :type: 'ID'
    '''

    use_datablock_sort: bool = None
    '''Alphabetically sorts data-blocks - mainly objects in the scene (disable to increase viewport speed) 

    :type: bool
    '''

    use_filter_text: bool = None
    '''Only include channels with names containing search text 

    :type: bool
    '''

    use_multi_word_filter: bool = None
    '''Perform fuzzy/multi-word matching (WARNING: May be slow) 

    :type: bool
    '''


class Driver:
    '''Driver for the value of a setting based on an external value '''

    expression: str = None
    '''Expression to use for Scripted Expression 

    :type: str
    '''

    is_valid: bool = None
    '''Driver could not be evaluated in past, so should be skipped 

    :type: bool
    '''

    show_debug_info: bool = None
    '''Show intermediate values for the driver calculations to allow debugging of drivers 

    :type: bool
    '''

    type: typing.Union[int, str] = None
    '''Driver type 

    :type: typing.Union[int, str]
    '''

    use_self: bool = None
    '''Include a ‘self’ variable in the name-space, so drivers can easily reference the data being modified (object, bone, etc…) 

    :type: bool
    '''

    variables: typing.List['ChannelDriverVariables'] = None
    '''Properties acting as inputs for this driver 

    :type: typing.List['ChannelDriverVariables']
    '''


class DriverTarget:
    '''Source of input values for driver variables '''

    bone_target: str = None
    '''Name of PoseBone to use as target 

    :type: str
    '''

    data_path: str = None
    '''RNA Path (from ID-block) to property used 

    :type: str
    '''

    id: 'ID' = None
    '''ID-block that the specific property used can be found from (id_type property must be set first) 

    :type: 'ID'
    '''

    id_type: typing.Union[int, str] = None
    '''Type of ID-block that can be used 

    :type: typing.Union[int, str]
    '''

    transform_space: typing.Union[int, str] = None
    '''Space in which transforms are used 

    :type: typing.Union[int, str]
    '''

    transform_type: typing.Union[int, str] = None
    '''Driver variable type 

    :type: typing.Union[int, str]
    '''


class DriverVariable:
    '''Variable from some source/target for driver relationship '''

    is_name_valid: bool = None
    '''Is this a valid name for a driver variable 

    :type: bool
    '''

    name: str = None
    '''Name to use in scripted expressions/functions (no spaces or dots are allowed, and must start with a letter) 

    :type: str
    '''

    targets: typing.List['DriverTarget'] = None
    '''Sources of input data for evaluating this variable 

    :type: typing.List['DriverTarget']
    '''

    type: typing.Union[int, str] = None
    '''Driver variable type 

    :type: typing.Union[int, str]
    '''


class DupliObject:
    '''An object duplicate '''

    hide: bool = None
    '''Don’t show dupli object in viewport or render 

    :type: bool
    '''

    index: int = None
    '''Index in the lowest-level dupli list 

    :type: int
    '''

    matrix: float = None
    '''Object duplicate transformation matrix 

    :type: float
    '''

    object: 'Object' = None
    '''Object being duplicated 

    :type: 'Object'
    '''

    orco: float = None
    '''Generated coordinates in parent object space 

    :type: float
    '''

    particle_system: 'ParticleSystem' = None
    '''Particle system that this dupli object was instanced from 

    :type: 'ParticleSystem'
    '''

    persistent_id: int = None
    '''Persistent identifier for inter-frame matching of objects with motion blur 

    :type: int
    '''

    random_id: int = None
    '''Random id for this dupli object 

    :type: int
    '''

    type: typing.Union[int, str] = None
    '''Duplicator type that generated this dupli object 

    :type: typing.Union[int, str]
    '''

    uv: float = None
    '''UV coordinates in parent object space 

    :type: float
    '''


class DynamicPaintBrushSettings:
    '''Brush settings '''

    invert_proximity: bool = None
    '''Proximity falloff is applied inside the volume 

    :type: bool
    '''

    material: 'Material' = None
    '''Material to use (if not defined, material linked to the mesh is used) 

    :type: 'Material'
    '''

    paint_alpha: float = None
    '''Paint alpha 

    :type: float
    '''

    paint_color: float = None
    '''Color of the paint 

    :type: float
    '''

    paint_distance: float = None
    '''Maximum distance from brush to mesh surface to affect paint 

    :type: float
    '''

    paint_ramp: 'ColorRamp' = None
    '''Color ramp used to define proximity falloff 

    :type: 'ColorRamp'
    '''

    paint_source: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    paint_wetness: float = None
    '''Paint wetness, visible in wetmap (some effects only affect wet paint) 

    :type: float
    '''

    particle_system: 'ParticleSystem' = None
    '''The particle system to paint with 

    :type: 'ParticleSystem'
    '''

    proximity_falloff: typing.Union[int, str] = None
    '''Proximity falloff type 

    :type: typing.Union[int, str]
    '''

    ray_direction: typing.Union[int, str] = None
    '''Ray direction to use for projection (if brush object is located in that direction it’s painted) 

    :type: typing.Union[int, str]
    '''

    smooth_radius: float = None
    '''Smooth falloff added after solid radius 

    :type: float
    '''

    smudge_strength: float = None
    '''Smudge effect strength 

    :type: float
    '''

    solid_radius: float = None
    '''Radius that will be painted solid 

    :type: float
    '''

    use_absolute_alpha: bool = None
    '''Only increase alpha value if paint alpha is higher than existing 

    :type: bool
    '''

    use_material: bool = None
    '''Use object material to define color and influence 

    :type: bool
    '''

    use_negative_volume: bool = None
    '''Negate influence inside the volume 

    :type: bool
    '''

    use_paint_erase: bool = None
    '''Erase / remove paint instead of adding it 

    :type: bool
    '''

    use_particle_radius: bool = None
    '''Use radius from particle settings 

    :type: bool
    '''

    use_proximity_project: bool = None
    '''Brush is projected to canvas from defined direction within brush proximity 

    :type: bool
    '''

    use_proximity_ramp_alpha: bool = None
    '''Only read color ramp alpha 

    :type: bool
    '''

    use_smudge: bool = None
    '''Make this brush to smudge existing paint as it moves 

    :type: bool
    '''

    use_velocity_alpha: bool = None
    '''Multiply brush influence by velocity color ramp alpha 

    :type: bool
    '''

    use_velocity_color: bool = None
    '''Replace brush color by velocity color ramp 

    :type: bool
    '''

    use_velocity_depth: bool = None
    '''Multiply brush intersection depth (displace, waves) by velocity ramp alpha 

    :type: bool
    '''

    velocity_max: float = None
    '''Velocity considered as maximum influence (Blender units per frame) 

    :type: float
    '''

    velocity_ramp: 'ColorRamp' = None
    '''Color ramp used to define brush velocity effect 

    :type: 'ColorRamp'
    '''

    wave_clamp: float = None
    '''Maximum level of surface intersection used to influence waves (use 0.0 to disable) 

    :type: float
    '''

    wave_factor: float = None
    '''Multiplier for wave influence of this brush 

    :type: float
    '''

    wave_type: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''


class DynamicPaintCanvasSettings:
    '''Dynamic Paint canvas settings '''

    canvas_surfaces: typing.List['DynamicPaintSurfaces'] = None
    '''Paint surface list 

    :type: typing.List['DynamicPaintSurfaces']
    '''


class DynamicPaintModifier:
    '''Dynamic Paint modifier '''

    brush_settings: 'DynamicPaintBrushSettings' = None
    '''

    :type: 'DynamicPaintBrushSettings'
    '''

    canvas_settings: 'DynamicPaintCanvasSettings' = None
    '''

    :type: 'DynamicPaintCanvasSettings'
    '''

    ui_type: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''


class DynamicPaintSurface:
    '''A canvas surface layer '''

    brush_group: 'Group' = None
    '''Only use brush objects from this group 

    :type: 'Group'
    '''

    brush_influence_scale: float = None
    '''Adjust influence brush objects have on this surface 

    :type: float
    '''

    brush_radius_scale: float = None
    '''Adjust radius of proximity brushes or particles for this surface 

    :type: float
    '''

    color_dry_threshold: float = None
    '''The wetness level when colors start to shift to the background 

    :type: float
    '''

    color_spread_speed: float = None
    '''How fast colors get mixed within wet paint 

    :type: float
    '''

    depth_clamp: float = None
    '''Maximum level of depth intersection in object space (use 0.0 to disable) 

    :type: float
    '''

    displace_factor: float = None
    '''Strength of displace when applied to the mesh 

    :type: float
    '''

    displace_type: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    dissolve_speed: int = None
    '''Approximately in how many frames should dissolve happen 

    :type: int
    '''

    drip_acceleration: float = None
    '''How much surface acceleration affects dripping 

    :type: float
    '''

    drip_velocity: float = None
    '''How much surface velocity affects dripping 

    :type: float
    '''

    dry_speed: int = None
    '''Approximately in how many frames should drying happen 

    :type: int
    '''

    effect_ui: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    effector_weights: 'EffectorWeights' = None
    '''

    :type: 'EffectorWeights'
    '''

    frame_end: int = None
    '''Simulation end frame 

    :type: int
    '''

    frame_start: int = None
    '''Simulation start frame 

    :type: int
    '''

    frame_substeps: int = None
    '''Do extra frames between scene frames to ensure smooth motion 

    :type: int
    '''

    image_fileformat: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    image_output_path: str = None
    '''Directory to save the textures 

    :type: str
    '''

    image_resolution: int = None
    '''Output image resolution 

    :type: int
    '''

    init_color: float = None
    '''Initial color of the surface 

    :type: float
    '''

    init_color_type: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    init_layername: str = None
    '''

    :type: str
    '''

    init_texture: 'Texture' = None
    '''

    :type: 'Texture'
    '''

    is_active: bool = None
    '''Toggle whether surface is processed or ignored 

    :type: bool
    '''

    is_cache_user: bool = None
    '''

    :type: bool
    '''

    name: str = None
    '''Surface name 

    :type: str
    '''

    output_name_a: str = None
    '''Name used to save output from this surface 

    :type: str
    '''

    output_name_b: str = None
    '''Name used to save output from this surface 

    :type: str
    '''

    point_cache: 'PointCache' = None
    '''

    :type: 'PointCache'
    '''

    preview_id: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    show_preview: bool = None
    '''Display surface preview in 3D-views 

    :type: bool
    '''

    shrink_speed: float = None
    '''How fast shrink effect moves on the canvas surface 

    :type: float
    '''

    spread_speed: float = None
    '''How fast spread effect moves on the canvas surface 

    :type: float
    '''

    surface_format: typing.Union[int, str] = None
    '''Surface Format 

    :type: typing.Union[int, str]
    '''

    surface_type: typing.Union[int, str] = None
    '''Surface Type 

    :type: typing.Union[int, str]
    '''

    use_antialiasing: bool = None
    '''Use 5x multisampling to smooth paint edges 

    :type: bool
    '''

    use_color_preview: bool = None
    '''Whether this surface has some color preview for 3D view 

    :type: bool
    '''

    use_dissolve: bool = None
    '''Enable to make surface changes disappear over time 

    :type: bool
    '''

    use_dissolve_log: bool = None
    '''Use logarithmic dissolve (makes high values to fade faster than low values) 

    :type: bool
    '''

    use_drip: bool = None
    '''Process drip effect (drip wet paint to gravity direction) 

    :type: bool
    '''

    use_dry_log: bool = None
    '''Use logarithmic drying (makes high values to dry faster than low values) 

    :type: bool
    '''

    use_drying: bool = None
    '''Enable to make surface wetness dry over time 

    :type: bool
    '''

    use_incremental_displace: bool = None
    '''New displace is added cumulatively on top of existing 

    :type: bool
    '''

    use_output_a: bool = None
    '''Save this output layer 

    :type: bool
    '''

    use_output_b: bool = None
    '''Save this output layer 

    :type: bool
    '''

    use_premultiply: bool = None
    '''Multiply color by alpha (recommended for Blender input) 

    :type: bool
    '''

    use_shrink: bool = None
    '''Process shrink effect (shrink paint areas) 

    :type: bool
    '''

    use_spread: bool = None
    '''Process spread effect (spread wet paint around surface) 

    :type: bool
    '''

    use_wave_open_border: bool = None
    '''Pass waves through mesh edges 

    :type: bool
    '''

    uv_layer: str = None
    '''UV map name 

    :type: str
    '''

    wave_damping: float = None
    '''Wave damping factor 

    :type: float
    '''

    wave_smoothness: float = None
    '''Limit maximum steepness of wave slope between simulation points (use higher values for smoother waves at expense of reduced detail) 

    :type: float
    '''

    wave_speed: float = None
    '''Wave propagation speed 

    :type: float
    '''

    wave_spring: float = None
    '''Spring force that pulls water level back to zero 

    :type: float
    '''

    wave_timescale: float = None
    '''Wave time scaling factor 

    :type: float
    '''

    def output_exists(self, object, index: int) -> bool:
        '''Checks if surface output layer of given name exists 

        :param index: Index 
        :type index: int
        :rtype: bool
        '''
        pass


class DynamicPaintSurfaces:
    '''Collection of Dynamic Paint Canvas surfaces '''

    active: 'DynamicPaintSurface' = None
    '''Active Dynamic Paint surface being displayed 

    :type: 'DynamicPaintSurface'
    '''

    active_index: int = None
    '''

    :type: int
    '''


class EdgeSplitModifier:
    '''Edge splitting modifier to create sharp edges '''

    split_angle: float = None
    '''Angle above which to split edges 

    :type: float
    '''

    use_edge_angle: bool = None
    '''Split edges with high angle between faces 

    :type: bool
    '''

    use_edge_sharp: bool = None
    '''Split edges that are marked as sharp 

    :type: bool
    '''


class EditBone:
    '''Editmode bone in an Armature data-block '''

    bbone_curveinx: float = None
    '''X-axis handle offset for start of the B-Bone’s curve, adjusts curvature 

    :type: float
    '''

    bbone_curveiny: float = None
    '''Y-axis handle offset for start of the B-Bone’s curve, adjusts curvature 

    :type: float
    '''

    bbone_curveoutx: float = None
    '''X-axis handle offset for end of the B-Bone’s curve, adjusts curvature 

    :type: float
    '''

    bbone_curveouty: float = None
    '''Y-axis handle offset for end of the B-Bone’s curve, adjusts curvature 

    :type: float
    '''

    bbone_in: float = None
    '''Length of first Bezier Handle (for B-Bones only) 

    :type: float
    '''

    bbone_out: float = None
    '''Length of second Bezier Handle (for B-Bones only) 

    :type: float
    '''

    bbone_rollin: float = None
    '''Roll offset for the start of the B-Bone, adjusts twist 

    :type: float
    '''

    bbone_rollout: float = None
    '''Roll offset for the end of the B-Bone, adjusts twist 

    :type: float
    '''

    bbone_scalein: float = None
    '''Scale factor for start of the B-Bone, adjusts thickness (for tapering effects) 

    :type: float
    '''

    bbone_scaleout: float = None
    '''Scale factor for end of the B-Bone, adjusts thickness (for tapering effects) 

    :type: float
    '''

    bbone_segments: int = None
    '''Number of subdivisions of bone (for B-Bones only) 

    :type: int
    '''

    bbone_x: float = None
    '''B-Bone X size 

    :type: float
    '''

    bbone_z: float = None
    '''B-Bone Z size 

    :type: float
    '''

    envelope_distance: float = None
    '''Bone deformation distance (for Envelope deform only) 

    :type: float
    '''

    envelope_weight: float = None
    '''Bone deformation weight (for Envelope deform only) 

    :type: float
    '''

    head: float = None
    '''Location of head end of the bone 

    :type: float
    '''

    head_radius: float = None
    '''Radius of head of bone (for Envelope deform only) 

    :type: float
    '''

    hide: bool = None
    '''Bone is not visible when in Edit Mode 

    :type: bool
    '''

    hide_select: bool = None
    '''Bone is able to be selected 

    :type: bool
    '''

    layers: bool = None
    '''Layers bone exists in 

    :type: bool
    '''

    lock: bool = None
    '''Bone is not able to be transformed when in Edit Mode 

    :type: bool
    '''

    matrix: float = None
    '''Matrix combining loc/rot of the bone (head position, direction and roll), in armature space (WARNING: does not include/support bone’s length/size) 

    :type: float
    '''

    name: str = None
    '''

    :type: str
    '''

    parent: 'EditBone' = None
    '''Parent edit bone (in same Armature) 

    :type: 'EditBone'
    '''

    roll: float = None
    '''Bone rotation around head-tail axis 

    :type: float
    '''

    select: bool = None
    '''

    :type: bool
    '''

    select_head: bool = None
    '''

    :type: bool
    '''

    select_tail: bool = None
    '''

    :type: bool
    '''

    show_wire: bool = None
    '''Bone is always drawn as Wireframe regardless of viewport draw mode (useful for non-obstructive custom bone shapes) 

    :type: bool
    '''

    tail: float = None
    '''Location of tail end of the bone 

    :type: float
    '''

    tail_radius: float = None
    '''Radius of tail of bone (for Envelope deform only) 

    :type: float
    '''

    use_connect: bool = None
    '''When bone has a parent, bone’s head is stuck to the parent’s tail 

    :type: bool
    '''

    use_cyclic_offset: bool = None
    '''When bone doesn’t have a parent, it receives cyclic offset effects (Deprecated) 

    :type: bool
    '''

    use_deform: bool = None
    '''Enable Bone to deform geometry 

    :type: bool
    '''

    use_endroll_as_inroll: bool = None
    '''Use Roll Out of parent bone as Roll In of its children 

    :type: bool
    '''

    use_envelope_multiply: bool = None
    '''When deforming bone, multiply effects of Vertex Group weights with Envelope influence 

    :type: bool
    '''

    use_inherit_rotation: bool = None
    '''Bone inherits rotation or scale from parent bone 

    :type: bool
    '''

    use_inherit_scale: bool = None
    '''Bone inherits scaling from parent bone 

    :type: bool
    '''

    use_local_location: bool = None
    '''Bone location is set in local space 

    :type: bool
    '''

    use_relative_parent: bool = None
    '''Object children will use relative transform, like deform 

    :type: bool
    '''

    basename = None
    '''The name of this bone before any ‘.’ character (readonly) '''

    center = None
    '''The midpoint between the head and the tail. (readonly) '''

    children = None
    '''A list of all the bones children. (readonly) '''

    children_recursive = None
    '''A list of all children from this bone. (readonly) '''

    children_recursive_basename = None
    '''Returns a chain of children with the same base name as this bone. Only direct chains are supported, forks caused by multiple children with matching base names will terminate the function and not be returned. (readonly) '''

    length = None
    '''The distance from head to tail, when set the head is moved to fit the length. '''

    parent_recursive = None
    '''A list of parents, starting with the immediate parent (readonly) '''

    vector = None
    '''The direction this bone is pointing. Utility function for (tail - head) (readonly) '''

    x_axis = None
    '''Vector pointing down the x-axis of the bone. (readonly) '''

    y_axis = None
    '''Vector pointing down the y-axis of the bone. (readonly) '''

    z_axis = None
    '''Vector pointing down the z-axis of the bone. (readonly) '''

    def align_roll(self, vector: float):
        '''Align the bone to a localspace roll so the Z axis points in the direction of the vector given 

        :param vector: Vector 
        :type vector: float
        '''
        pass

    def align_orientation(self, other):
        '''Align this bone to another by moving its tail and settings its roll the length of the other bone is not used. 

        '''
        pass

    def parent_index(self, parent_test):
        '''The same as ‘bone in other_bone.parent_recursive’ but saved generating a list. 

        '''
        pass

    def transform(self,
                  matrix: 'mathutils.Matrix',
                  scale: bool = True,
                  roll: bool = True):
        '''Transform the the bones head, tail, roll and envelope (when the matrix has a scale component). 

        :param matrix: 3x3 or 4x4 transformation matrix. 
        :type matrix: 'mathutils.Matrix'
        :param scale: Scale the bone envelope by the matrix. 
        :type scale: bool
        :param roll: Correct the roll to point in the same relative direction to the head and tail. 
        :type roll: bool
        '''
        pass

    def translate(self, vec):
        '''Utility function to add vec to the head and tail of this bone 

        '''
        pass


class EditObjectActuator:
    '''Actuator used to edit objects '''

    angular_velocity: float = None
    '''Angular velocity upon creation 

    :type: float
    '''

    dynamic_operation: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    linear_velocity: float = None
    '''Velocity upon creation 

    :type: float
    '''

    mass: float = None
    '''The mass of the object 

    :type: float
    '''

    mesh: 'Mesh' = None
    '''Replace the existing, when left blank ‘Phys’ will remake the existing physics mesh 

    :type: 'Mesh'
    '''

    mode: typing.Union[int, str] = None
    '''The mode of the actuator 

    :type: typing.Union[int, str]
    '''

    object: 'Object' = None
    '''Add this Object and all its children (can’t be on a visible layer) 

    :type: 'Object'
    '''

    time: int = None
    '''Duration the new Object lives or the track takes 

    :type: int
    '''

    track_axis: typing.Union[int, str] = None
    '''The axis that points to the target object 

    :type: typing.Union[int, str]
    '''

    track_object: 'Object' = None
    '''Track to this Object 

    :type: 'Object'
    '''

    up_axis: typing.Union[int, str] = None
    '''The axis that points upward 

    :type: typing.Union[int, str]
    '''

    use_3d_tracking: bool = None
    '''Enable 3D tracking 

    :type: bool
    '''

    use_local_angular_velocity: bool = None
    '''Apply the rotation locally 

    :type: bool
    '''

    use_local_linear_velocity: bool = None
    '''Apply the transformation locally 

    :type: bool
    '''

    use_replace_display_mesh: bool = None
    '''Replace the display mesh 

    :type: bool
    '''

    use_replace_physics_mesh: bool = None
    '''Replace the physics mesh (triangle bounds only - compound shapes not supported) 

    :type: bool
    '''


class EffectSequence:
    '''Sequence strip applying an effect on the images created by other strips '''

    alpha_mode: typing.Union[int, str] = None
    '''Representation of alpha information in the RGBA pixels 

    :type: typing.Union[int, str]
    '''

    color_multiply: float = None
    '''

    :type: float
    '''

    color_saturation: float = None
    '''Adjust the intensity of the input’s color 

    :type: float
    '''

    crop: 'SequenceCrop' = None
    '''

    :type: 'SequenceCrop'
    '''

    proxy: 'SequenceProxy' = None
    '''

    :type: 'SequenceProxy'
    '''

    strobe: float = None
    '''Only display every nth frame 

    :type: float
    '''

    transform: 'SequenceTransform' = None
    '''

    :type: 'SequenceTransform'
    '''

    use_crop: bool = None
    '''Crop image before processing 

    :type: bool
    '''

    use_deinterlace: bool = None
    '''Remove fields from video movies 

    :type: bool
    '''

    use_flip_x: bool = None
    '''Flip on the X axis 

    :type: bool
    '''

    use_flip_y: bool = None
    '''Flip on the Y axis 

    :type: bool
    '''

    use_float: bool = None
    '''Convert input to float data 

    :type: bool
    '''

    use_proxy: bool = None
    '''Use a preview proxy and/or timecode index for this strip 

    :type: bool
    '''

    use_reverse_frames: bool = None
    '''Reverse frame order 

    :type: bool
    '''

    use_translation: bool = None
    '''Translate image before processing 

    :type: bool
    '''


class EffectorWeights:
    '''Effector weights for physics simulation '''

    all: float = None
    '''All effector’s weight 

    :type: float
    '''

    apply_to_hair_growing: bool = None
    '''Use force fields when growing hair 

    :type: bool
    '''

    boid: float = None
    '''Boid effector weight 

    :type: float
    '''

    charge: float = None
    '''Charge effector weight 

    :type: float
    '''

    curve_guide: float = None
    '''Curve guide effector weight 

    :type: float
    '''

    drag: float = None
    '''Drag effector weight 

    :type: float
    '''

    force: float = None
    '''Force effector weight 

    :type: float
    '''

    gravity: float = None
    '''Global gravity weight 

    :type: float
    '''

    group: 'Group' = None
    '''Limit effectors to this Group 

    :type: 'Group'
    '''

    harmonic: float = None
    '''Harmonic effector weight 

    :type: float
    '''

    lennardjones: float = None
    '''Lennard-Jones effector weight 

    :type: float
    '''

    magnetic: float = None
    '''Magnetic effector weight 

    :type: float
    '''

    smokeflow: float = None
    '''Smoke Flow effector weight 

    :type: float
    '''

    texture: float = None
    '''Texture effector weight 

    :type: float
    '''

    turbulence: float = None
    '''Turbulence effector weight 

    :type: float
    '''

    vortex: float = None
    '''Vortex effector weight 

    :type: float
    '''

    wind: float = None
    '''Wind effector weight 

    :type: float
    '''


class EnumProperty:
    '''RNA enumeration property definition, to choose from a number of predefined options '''

    default: typing.Union[int, str] = None
    '''Default value for this enum 

    :type: typing.Union[int, str]
    '''

    default_flag: typing.Set[typing.Union[int, str]] = None
    '''Default value for this enum 

    :type: typing.Set[typing.Union[int, str]]
    '''

    enum_items: typing.List['EnumPropertyItem'] = None
    '''Possible values for the property 

    :type: typing.List['EnumPropertyItem']
    '''

    enum_items_static: typing.List['EnumPropertyItem'] = None
    '''Possible values for the property (never calls optional dynamic generation of those) 

    :type: typing.List['EnumPropertyItem']
    '''


class EnumPropertyItem:
    '''Definition of a choice in an RNA enum property '''

    description: str = None
    '''Description of the item’s purpose 

    :type: str
    '''

    icon: typing.Union[int, str] = None
    '''Icon of the item 

    :type: typing.Union[int, str]
    '''

    identifier: str = None
    '''Unique name used in the code and scripting 

    :type: str
    '''

    name: str = None
    '''Human readable name 

    :type: str
    '''

    value: int = None
    '''Value of the item 

    :type: int
    '''


class EnvironmentMap:
    '''Environment map created by the renderer and cached for subsequent renders '''

    clip_end: float = None
    '''Objects further than this are not visible to map 

    :type: float
    '''

    clip_start: float = None
    '''Objects nearer than this are not visible to map 

    :type: float
    '''

    depth: int = None
    '''Number of times a map will be rendered recursively (mirror effects) 

    :type: int
    '''

    is_valid: bool = None
    '''True if this map is ready for use, False if it needs rendering 

    :type: bool
    '''

    layers_ignore: bool = None
    '''Hide objects on these layers when generating the Environment Map 

    :type: bool
    '''

    mapping: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    resolution: int = None
    '''Pixel resolution of the rendered environment map 

    :type: int
    '''

    source: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    viewpoint_object: 'Object' = None
    '''Object to use as the environment map’s viewpoint location 

    :type: 'Object'
    '''

    zoom: float = None
    '''

    :type: float
    '''

    def clear(self, ):
        '''Discard the environment map and free it from memory 

        '''
        pass

    def save(self,
             filepath: str,
             scene: 'Scene' = None,
             layout: float = (0.0, 0.0, 1.0, 0.0, 2.0, 0.0, 0.0, 1.0, 1.0, 1.0,
                              2.0, 1.0)):
        '''Save the environment map to disc using the scene render settings 

        :param filepath: File path, Location of the output file 
        :type filepath: str
        :param scene: Overrides the scene from which image parameters are taken 
        :type scene: 'Scene'
        :param layout: File layout, Flat array describing the X,Y position of each cube face in the output image, where 1 is the size of a face - order is [+Z -Z +Y -X -Y +X] (use -1 to skip a face) 
        :type layout: float
        '''
        pass


class EnvironmentMapTexture:
    '''Environment map texture '''

    environment_map: 'EnvironmentMap' = None
    '''Get the environment map associated with this texture 

    :type: 'EnvironmentMap'
    '''

    filter_eccentricity: int = None
    '''Maximum eccentricity (higher gives less blur at distant/oblique angles, but is also slower) 

    :type: int
    '''

    filter_probes: int = None
    '''Maximum number of samples (higher gives less blur at distant/oblique angles, but is also slower) 

    :type: int
    '''

    filter_size: float = None
    '''Multiply the filter size used by MIP Map and Interpolation 

    :type: float
    '''

    filter_type: typing.Union[int, str] = None
    '''Texture filter to use for sampling image 

    :type: typing.Union[int, str]
    '''

    image: 'Image' = None
    '''Source image file to read the environment map from 

    :type: 'Image'
    '''

    image_user: 'ImageUser' = None
    '''Parameters defining which layer, pass and frame of the image is displayed 

    :type: 'ImageUser'
    '''

    use_filter_size_min: bool = None
    '''Use Filter Size as a minimal filter value in pixels 

    :type: bool
    '''

    use_mipmap: bool = None
    '''Use auto-generated MIP maps for the image 

    :type: bool
    '''

    use_mipmap_gauss: bool = None
    '''Use Gauss filter to sample down MIP maps 

    :type: bool
    '''

    users_material = None
    '''Materials that use this texture (readonly) '''

    users_object_modifier = None
    '''Object modifiers that use this texture (readonly) '''


class Event:
    '''Window Manager Event '''

    alt: bool = None
    '''True when the Alt/Option key is held 

    :type: bool
    '''

    ascii: str = None
    '''Single ASCII character for this event 

    :type: str
    '''

    ctrl: bool = None
    '''True when the Ctrl key is held 

    :type: bool
    '''

    is_tablet: bool = None
    '''The pressure of the tablet or 1.0 if no tablet present 

    :type: bool
    '''

    mouse_prev_x: int = None
    '''The window relative horizontal location of the mouse 

    :type: int
    '''

    mouse_prev_y: int = None
    '''The window relative vertical location of the mouse 

    :type: int
    '''

    mouse_region_x: int = None
    '''The region relative horizontal location of the mouse 

    :type: int
    '''

    mouse_region_y: int = None
    '''The region relative vertical location of the mouse 

    :type: int
    '''

    mouse_x: int = None
    '''The window relative horizontal location of the mouse 

    :type: int
    '''

    mouse_y: int = None
    '''The window relative vertical location of the mouse 

    :type: int
    '''

    oskey: bool = None
    '''True when the Cmd key is held 

    :type: bool
    '''

    pressure: float = None
    '''The pressure of the tablet or 1.0 if no tablet present 

    :type: float
    '''

    shift: bool = None
    '''True when the Shift key is held 

    :type: bool
    '''

    tilt: float = None
    '''The pressure of the tablet or zeroes if no tablet present 

    :type: float
    '''

    type: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    unicode: str = None
    '''Single unicode character for this event 

    :type: str
    '''

    value: typing.Union[int, str] = None
    '''The type of event, only applies to some 

    :type: typing.Union[int, str]
    '''


class ExplodeModifier:
    '''Explosion effect modifier based on a particle system '''

    particle_uv: str = None
    '''UV map to change with particle age 

    :type: str
    '''

    protect: float = None
    '''Clean vertex group edges 

    :type: float
    '''

    show_alive: bool = None
    '''Show mesh when particles are alive 

    :type: bool
    '''

    show_dead: bool = None
    '''Show mesh when particles are dead 

    :type: bool
    '''

    show_unborn: bool = None
    '''Show mesh when particles are unborn 

    :type: bool
    '''

    use_edge_cut: bool = None
    '''Cut face edges for nicer shrapnel 

    :type: bool
    '''

    use_size: bool = None
    '''Use particle size for the shrapnel 

    :type: bool
    '''

    vertex_group: str = None
    '''

    :type: str
    '''


class ExpressionController:
    '''Controller passing on events based on the evaluation of an expression '''

    expression: str = None
    '''

    :type: str
    '''


class FCurve:
    '''F-Curve defining values of a period of time '''

    array_index: int = None
    '''Index to the specific property affected by F-Curve if applicable 

    :type: int
    '''

    color: float = None
    '''Color of the F-Curve in the Graph Editor 

    :type: float
    '''

    color_mode: typing.Union[int, str] = None
    '''Method used to determine color of F-Curve in Graph Editor 

    :type: typing.Union[int, str]
    '''

    data_path: str = None
    '''RNA Path to property affected by F-Curve 

    :type: str
    '''

    driver: 'Driver' = None
    '''Channel Driver (only set for Driver F-Curves) 

    :type: 'Driver'
    '''

    extrapolation: typing.Union[int, str] = None
    '''Method used for evaluating value of F-Curve outside first and last keyframes 

    :type: typing.Union[int, str]
    '''

    group: 'ActionGroup' = None
    '''Action Group that this F-Curve belongs to 

    :type: 'ActionGroup'
    '''

    hide: bool = None
    '''F-Curve and its keyframes are hidden in the Graph Editor graphs 

    :type: bool
    '''

    is_valid: bool = None
    '''False when F-Curve could not be evaluated in past, so should be skipped when evaluating 

    :type: bool
    '''

    keyframe_points: typing.List['Keyframe'] = None
    '''User-editable keyframes 

    :type: typing.List['Keyframe']
    '''

    lock: bool = None
    '''F-Curve’s settings cannot be edited 

    :type: bool
    '''

    modifiers: typing.List['FModifier'] = None
    '''Modifiers affecting the shape of the F-Curve 

    :type: typing.List['FModifier']
    '''

    mute: bool = None
    '''F-Curve is not evaluated 

    :type: bool
    '''

    sampled_points: typing.List['FCurveSample'] = None
    '''Sampled animation data 

    :type: typing.List['FCurveSample']
    '''

    select: bool = None
    '''F-Curve is selected for editing 

    :type: bool
    '''

    def evaluate(self, frame: float) -> float:
        '''Evaluate F-Curve 

        :param frame: Frame, Evaluate F-Curve at given frame 
        :type frame: float
        :rtype: float
        :return:  Value, Value of F-Curve specific frame 
        '''
        pass

    def update(self, ):
        '''Ensure keyframes are sorted in chronological order and handles are set correctly 

        '''
        pass

    def range(self, ) -> float:
        '''Get the time extents for F-Curve 

        :rtype: float
        :return:  Range, Min/Max values 
        '''
        pass

    def update_autoflags(self, data: 'AnyType'):
        '''Update FCurve flags set automatically from affected property (currently, integer/discrete flags set when the property is not a float) 

        :param data: Data, Data containing the property controlled by given FCurve 
        :type data: 'AnyType'
        '''
        pass

    def convert_to_samples(self, start: int, end: int):
        '''Convert current FCurve from keyframes to sample points, if necessary 

        :param start: Start Frame 
        :type start: int
        :param end: End Frame 
        :type end: int
        '''
        pass

    def convert_to_keyframes(self, start: int, end: int):
        '''Convert current FCurve from sample points to keyframes (linear interpolation), if necessary 

        :param start: Start Frame 
        :type start: int
        :param end: End Frame 
        :type end: int
        '''
        pass


class FCurveKeyframePoints:
    '''Collection of keyframe points '''

    def insert(
            self,
            frame: float,
            value: float,
            options: typing.Set[typing.Union[int, str]] = {},
            keyframe_type: typing.Union[int, str] = 'KEYFRAME') -> 'Keyframe':
        '''Add a keyframe point to a F-Curve 

        :param frame: X Value of this keyframe point 
        :type frame: float
        :param value: Y Value of this keyframe point 
        :type value: float
        :param options: Keyframe optionsREPLACE Replace, Don’t add any new keyframes, but just replace existing ones.NEEDED Needed, Only adds keyframes that are needed.FAST Fast, Fast keyframe insertion to avoid recalculating the curve each time. 
        :type options: typing.Set[typing.Union[int, str]]
        :param keyframe_type: Type of keyframe to insertKEYFRAME Keyframe, Normal keyframe - e.g. for key poses.BREAKDOWN Breakdown, A breakdown pose - e.g. for transitions between key poses.MOVING_HOLD Moving Hold, A keyframe that is part of a moving hold.EXTREME Extreme, An ‘extreme’ pose, or some other purpose as needed.JITTER Jitter, A filler or baked keyframe for keying on ones, or some other purpose as needed. 
        :type keyframe_type: typing.Union[int, str]
        :rtype: 'Keyframe'
        :return:  Newly created keyframe 
        '''
        pass

    def add(self, count: int = 1):
        '''Add a keyframe point to a F-Curve 

        :param count: Number, Number of points to add to the spline 
        :type count: int
        '''
        pass

    def remove(self, keyframe: 'Keyframe', fast: bool = False):
        '''Remove keyframe from an F-Curve 

        :param keyframe: Keyframe to remove 
        :type keyframe: 'Keyframe'
        :param fast: Fast, Fast keyframe removal to avoid recalculating the curve each time 
        :type fast: bool
        '''
        pass


class FCurveModifiers:
    '''Collection of F-Curve Modifiers '''

    active: 'FModifier' = None
    '''Active F-Curve Modifier 

    :type: 'FModifier'
    '''

    def new(self, type: typing.Union[int, str]) -> 'FModifier':
        '''Add a constraint to this object 

        :param type: Constraint type to addNULL Invalid.GENERATOR Generator, Generate a curve using a factorized or expanded polynomial.FNGENERATOR Built-In Function, Generate a curve using standard math functions such as sin and cos.ENVELOPE Envelope, Reshape F-Curve values - e.g. change amplitude of movements.CYCLES Cycles, Cyclic extend/repeat keyframe sequence.NOISE Noise, Add pseudo-random noise on top of F-Curves.LIMITS Limits, Restrict maximum and minimum values of F-Curve.STEPPED Stepped Interpolation, Snap values to nearest grid-step - e.g. for a stop-motion look. 
        :type type: typing.Union[int, str]
        :rtype: 'FModifier'
        :return:  New fmodifier 
        '''
        pass

    def remove(self, modifier: 'FModifier'):
        '''Remove a modifier from this F-Curve 

        :param modifier: Removed modifier 
        :type modifier: 'FModifier'
        '''
        pass


class FCurveSample:
    '''Sample point for F-Curve '''

    co: float = None
    '''Point coordinates 

    :type: float
    '''

    select: bool = None
    '''Selection status 

    :type: bool
    '''


class FFmpegSettings:
    '''FFmpeg related settings for the scene '''

    audio_bitrate: int = None
    '''Audio bitrate (kb/s) 

    :type: int
    '''

    audio_channels: typing.Union[int, str] = None
    '''Audio channel count 

    :type: typing.Union[int, str]
    '''

    audio_codec: typing.Union[int, str] = None
    '''FFmpeg audio codec to use 

    :type: typing.Union[int, str]
    '''

    audio_mixrate: int = None
    '''Audio samplerate(samples/s) 

    :type: int
    '''

    audio_volume: float = None
    '''Audio volume 

    :type: float
    '''

    buffersize: int = None
    '''Rate control: buffer size (kb) 

    :type: int
    '''

    codec: typing.Union[int, str] = None
    '''FFmpeg codec to use 

    :type: typing.Union[int, str]
    '''

    constant_rate_factor: typing.Union[int, str] = None
    '''Constant Rate Factor (CRF); tradeoff between video quality and file size 

    :type: typing.Union[int, str]
    '''

    ffmpeg_preset: typing.Union[int, str] = None
    '''Tradeoff between encoding speed and compression ratio 

    :type: typing.Union[int, str]
    '''

    format: typing.Union[int, str] = None
    '''Output file container 

    :type: typing.Union[int, str]
    '''

    gopsize: int = None
    '''Distance between key frames, also known as GOP size; influences file size and seekability 

    :type: int
    '''

    max_b_frames: int = None
    '''Maximum number of B-frames between non-B-frames; influences file size and seekability 

    :type: int
    '''

    maxrate: int = None
    '''Rate control: max rate (kb/s) 

    :type: int
    '''

    minrate: int = None
    '''Rate control: min rate (kb/s) 

    :type: int
    '''

    muxrate: int = None
    '''Mux rate (bits/s(!)) 

    :type: int
    '''

    packetsize: int = None
    '''Mux packet size (byte) 

    :type: int
    '''

    use_autosplit: bool = None
    '''Autosplit output at 2GB boundary 

    :type: bool
    '''

    use_lossless_output: bool = None
    '''Use lossless output for video streams 

    :type: bool
    '''

    use_max_b_frames: bool = None
    '''Set a maximum number of B-frames 

    :type: bool
    '''

    video_bitrate: int = None
    '''Video bitrate (kb/s) 

    :type: int
    '''


class FILEBROWSER_UL_dir:
    def draw_item(self, context, layout, data, item, icon, active_data,
                  active_propname, index):
        '''

        '''
        pass


class FModifier:
    '''Modifier for values of F-Curve '''

    active: bool = None
    '''F-Curve Modifier is the one being edited 

    :type: bool
    '''

    blend_in: float = None
    '''Number of frames from start frame for influence to take effect 

    :type: float
    '''

    blend_out: float = None
    '''Number of frames from end frame for influence to fade out 

    :type: float
    '''

    frame_end: float = None
    '''Frame that modifier’s influence ends (if Restrict Frame Range is in use) 

    :type: float
    '''

    frame_start: float = None
    '''Frame that modifier’s influence starts (if Restrict Frame Range is in use) 

    :type: float
    '''

    influence: float = None
    '''Amount of influence F-Curve Modifier will have when not fading in/out 

    :type: float
    '''

    is_valid: bool = None
    '''F-Curve Modifier has invalid settings and will not be evaluated 

    :type: bool
    '''

    mute: bool = None
    '''F-Curve Modifier will not be evaluated 

    :type: bool
    '''

    show_expanded: bool = None
    '''F-Curve Modifier’s panel is expanded in UI 

    :type: bool
    '''

    type: typing.Union[int, str] = None
    '''F-Curve Modifier Type 

    :type: typing.Union[int, str]
    '''

    use_influence: bool = None
    '''F-Curve Modifier’s effects will be tempered by a default factor 

    :type: bool
    '''

    use_restricted_range: bool = None
    '''F-Curve Modifier is only applied for the specified frame range to help mask off effects in order to chain them 

    :type: bool
    '''


class FModifierCycles:
    '''Repeat the values of the modified F-Curve '''

    cycles_after: int = None
    '''Maximum number of cycles to allow after last keyframe (0 = infinite) 

    :type: int
    '''

    cycles_before: int = None
    '''Maximum number of cycles to allow before first keyframe (0 = infinite) 

    :type: int
    '''

    mode_after: typing.Union[int, str] = None
    '''Cycling mode to use after last keyframe 

    :type: typing.Union[int, str]
    '''

    mode_before: typing.Union[int, str] = None
    '''Cycling mode to use before first keyframe 

    :type: typing.Union[int, str]
    '''


class FModifierEnvelope:
    '''Scale the values of the modified F-Curve '''

    control_points: typing.List['FModifierEnvelopeControlPoint'] = None
    '''Control points defining the shape of the envelope 

    :type: typing.List['FModifierEnvelopeControlPoint']
    '''

    default_max: float = None
    '''Upper distance from Reference Value for 1:1 default influence 

    :type: float
    '''

    default_min: float = None
    '''Lower distance from Reference Value for 1:1 default influence 

    :type: float
    '''

    reference_value: float = None
    '''Value that envelope’s influence is centered around / based on 

    :type: float
    '''


class FModifierEnvelopeControlPoint:
    '''Control point for envelope F-Modifier '''

    frame: float = None
    '''Frame this control-point occurs on 

    :type: float
    '''

    max: float = None
    '''Upper bound of envelope at this control-point 

    :type: float
    '''

    min: float = None
    '''Lower bound of envelope at this control-point 

    :type: float
    '''


class FModifierEnvelopeControlPoints:
    '''Control points defining the shape of the envelope '''

    def add(self, frame: float) -> 'FModifierEnvelopeControlPoint':
        '''Add a control point to a FModifierEnvelope 

        :param frame: Frame to add this control-point 
        :type frame: float
        :rtype: 'FModifierEnvelopeControlPoint'
        :return:  Newly created control-point 
        '''
        pass

    def remove(self, point: 'FModifierEnvelopeControlPoint'):
        '''Remove a control-point from an FModifierEnvelope 

        :param point: Control-point to remove 
        :type point: 'FModifierEnvelopeControlPoint'
        '''
        pass


class FModifierFunctionGenerator:
    '''Generate values using a Built-In Function '''

    amplitude: float = None
    '''Scale factor determining the maximum/minimum values 

    :type: float
    '''

    function_type: typing.Union[int, str] = None
    '''Type of built-in function to use 

    :type: typing.Union[int, str]
    '''

    phase_multiplier: float = None
    '''Scale factor determining the ‘speed’ of the function 

    :type: float
    '''

    phase_offset: float = None
    '''Constant factor to offset time by for function 

    :type: float
    '''

    use_additive: bool = None
    '''Values generated by this modifier are applied on top of the existing values instead of overwriting them 

    :type: bool
    '''

    value_offset: float = None
    '''Constant factor to offset values by 

    :type: float
    '''


class FModifierGenerator:
    '''Deterministically generate values for the modified F-Curve '''

    coefficients: float = None
    '''Coefficients for ‘x’ (starting from lowest power of x^0) 

    :type: float
    '''

    mode: typing.Union[int, str] = None
    '''Type of generator to use 

    :type: typing.Union[int, str]
    '''

    poly_order: int = None
    '''The highest power of ‘x’ for this polynomial (number of coefficients - 1) 

    :type: int
    '''

    use_additive: bool = None
    '''Values generated by this modifier are applied on top of the existing values instead of overwriting them 

    :type: bool
    '''


class FModifierLimits:
    '''Limit the time/value ranges of the modified F-Curve '''

    max_x: float = None
    '''Highest X value to allow 

    :type: float
    '''

    max_y: float = None
    '''Highest Y value to allow 

    :type: float
    '''

    min_x: float = None
    '''Lowest X value to allow 

    :type: float
    '''

    min_y: float = None
    '''Lowest Y value to allow 

    :type: float
    '''

    use_max_x: bool = None
    '''Use the maximum X value 

    :type: bool
    '''

    use_max_y: bool = None
    '''Use the maximum Y value 

    :type: bool
    '''

    use_min_x: bool = None
    '''Use the minimum X value 

    :type: bool
    '''

    use_min_y: bool = None
    '''Use the minimum Y value 

    :type: bool
    '''


class FModifierNoise:
    '''Give randomness to the modified F-Curve '''

    blend_type: typing.Union[int, str] = None
    '''Method of modifying the existing F-Curve 

    :type: typing.Union[int, str]
    '''

    depth: int = None
    '''Amount of fine level detail present in the noise 

    :type: int
    '''

    offset: float = None
    '''Time offset for the noise effect 

    :type: float
    '''

    phase: float = None
    '''A random seed for the noise effect 

    :type: float
    '''

    scale: float = None
    '''Scaling (in time) of the noise 

    :type: float
    '''

    strength: float = None
    '''Amplitude of the noise - the amount that it modifies the underlying curve 

    :type: float
    '''


class FModifierPython:
    '''Perform user-defined operation on the modified F-Curve '''

    pass


class FModifierStepped:
    '''Hold each interpolated value from the F-Curve for several frames without changing the timing '''

    frame_end: float = None
    '''Frame that modifier’s influence ends (if applicable) 

    :type: float
    '''

    frame_offset: float = None
    '''Reference number of frames before frames get held (use to get hold for ‘1-3’ vs ‘5-7’ holding patterns) 

    :type: float
    '''

    frame_start: float = None
    '''Frame that modifier’s influence starts (if applicable) 

    :type: float
    '''

    frame_step: float = None
    '''Number of frames to hold each value 

    :type: float
    '''

    use_frame_end: bool = None
    '''Restrict modifier to only act before its ‘end’ frame 

    :type: bool
    '''

    use_frame_start: bool = None
    '''Restrict modifier to only act after its ‘start’ frame 

    :type: bool
    '''


class FieldSettings:
    '''Field settings for an object in physics simulation '''

    apply_to_location: bool = None
    '''Effect particles’ location 

    :type: bool
    '''

    apply_to_rotation: bool = None
    '''Effect particles’ dynamic rotation 

    :type: bool
    '''

    distance_max: float = None
    '''Maximum distance for the field to work 

    :type: float
    '''

    distance_min: float = None
    '''Minimum distance for the field’s fall-off 

    :type: float
    '''

    falloff_power: float = None
    '''

    :type: float
    '''

    falloff_type: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    flow: float = None
    '''Convert effector force into air flow velocity 

    :type: float
    '''

    guide_clump_amount: float = None
    '''Amount of clumping 

    :type: float
    '''

    guide_clump_shape: float = None
    '''Shape of clumping 

    :type: float
    '''

    guide_free: float = None
    '''Guide-free time from particle life’s end 

    :type: float
    '''

    guide_kink_amplitude: float = None
    '''The amplitude of the offset 

    :type: float
    '''

    guide_kink_axis: typing.Union[int, str] = None
    '''Which axis to use for offset 

    :type: typing.Union[int, str]
    '''

    guide_kink_frequency: float = None
    '''The frequency of the offset (1/total length) 

    :type: float
    '''

    guide_kink_shape: float = None
    '''Adjust the offset to the beginning/end 

    :type: float
    '''

    guide_kink_type: typing.Union[int, str] = None
    '''Type of periodic offset on the curve 

    :type: typing.Union[int, str]
    '''

    guide_minimum: float = None
    '''The distance from which particles are affected fully 

    :type: float
    '''

    harmonic_damping: float = None
    '''Damping of the harmonic force 

    :type: float
    '''

    inflow: float = None
    '''Inwards component of the vortex force 

    :type: float
    '''

    linear_drag: float = None
    '''Drag component proportional to velocity 

    :type: float
    '''

    noise: float = None
    '''Amount of noise for the force strength 

    :type: float
    '''

    quadratic_drag: float = None
    '''Drag component proportional to the square of velocity 

    :type: float
    '''

    radial_falloff: float = None
    '''Radial falloff power (real gravitational falloff = 2) 

    :type: float
    '''

    radial_max: float = None
    '''Maximum radial distance for the field to work 

    :type: float
    '''

    radial_min: float = None
    '''Minimum radial distance for the field’s fall-off 

    :type: float
    '''

    rest_length: float = None
    '''Rest length of the harmonic force 

    :type: float
    '''

    seed: int = None
    '''Seed of the noise 

    :type: int
    '''

    shape: typing.Union[int, str] = None
    '''Which direction is used to calculate the effector force 

    :type: typing.Union[int, str]
    '''

    size: float = None
    '''Size of the turbulence 

    :type: float
    '''

    source_object: 'Object' = None
    '''Select domain object of the smoke simulation 

    :type: 'Object'
    '''

    strength: float = None
    '''Strength of force field 

    :type: float
    '''

    texture: 'Texture' = None
    '''Texture to use as force 

    :type: 'Texture'
    '''

    texture_mode: typing.Union[int, str] = None
    '''How the texture effect is calculated (RGB & Curl need a RGB texture, else Gradient will be used instead) 

    :type: typing.Union[int, str]
    '''

    texture_nabla: float = None
    '''Defines size of derivative offset used for calculating gradient and curl 

    :type: float
    '''

    type: typing.Union[int, str] = None
    '''Type of field 

    :type: typing.Union[int, str]
    '''

    use_2d_force: bool = None
    '''Apply force only in 2D 

    :type: bool
    '''

    use_absorption: bool = None
    '''Force gets absorbed by collision objects 

    :type: bool
    '''

    use_global_coords: bool = None
    '''Use effector/global coordinates for turbulence 

    :type: bool
    '''

    use_gravity_falloff: bool = None
    '''Multiply force by 1/distance² 

    :type: bool
    '''

    use_guide_path_add: bool = None
    '''Based on distance/falloff it adds a portion of the entire path 

    :type: bool
    '''

    use_guide_path_weight: bool = None
    '''Use curve weights to influence the particle influence along the curve 

    :type: bool
    '''

    use_max_distance: bool = None
    '''Use a maximum distance for the field to work 

    :type: bool
    '''

    use_min_distance: bool = None
    '''Use a minimum distance for the field’s fall-off 

    :type: bool
    '''

    use_multiple_springs: bool = None
    '''Every point is effected by multiple springs 

    :type: bool
    '''

    use_object_coords: bool = None
    '''Use object/global coordinates for texture 

    :type: bool
    '''

    use_radial_max: bool = None
    '''Use a maximum radial distance for the field to work 

    :type: bool
    '''

    use_radial_min: bool = None
    '''Use a minimum radial distance for the field’s fall-off 

    :type: bool
    '''

    use_root_coords: bool = None
    '''Texture coordinates from root particle locations 

    :type: bool
    '''

    use_smoke_density: bool = None
    '''Adjust force strength based on smoke density 

    :type: bool
    '''

    z_direction: typing.Union[int, str] = None
    '''Effect in full or only positive/negative Z direction 

    :type: typing.Union[int, str]
    '''


class FileBrowserFSMenuEntry:
    '''File Select Parameters '''

    is_valid: bool = None
    '''Whether this path is currently reachable 

    :type: bool
    '''

    name: str = None
    '''

    :type: str
    '''

    path: str = None
    '''

    :type: str
    '''

    use_save: bool = None
    '''Whether this path is saved in bookmarks, or generated from OS 

    :type: bool
    '''


class FileSelectParams:
    '''File Select Parameters '''

    directory: str = None
    '''Directory displayed in the file browser 

    :type: str
    '''

    display_size: typing.Union[int, str] = None
    '''Change the size of the display (width of columns or thumbnails size) 

    :type: typing.Union[int, str]
    '''

    display_type: typing.Union[int, str] = None
    '''Display mode for the file list 

    :type: typing.Union[int, str]
    '''

    filename: str = None
    '''Active file in the file browser 

    :type: str
    '''

    filter_glob: str = None
    '''

    :type: str
    '''

    filter_id: typing.Set[typing.Union[int, str]] = None
    '''Which ID types to show/hide, when browsing a library 

    :type: typing.Set[typing.Union[int, str]]
    '''

    filter_id_category: typing.Set[typing.Union[int, str]] = None
    '''Which ID categories to show/hide, when browsing a library 

    :type: typing.Set[typing.Union[int, str]]
    '''

    filter_search: str = None
    '''Filter by name, supports ‘*’ wildcard 

    :type: str
    '''

    recursion_level: typing.Union[int, str] = None
    '''Numbers of dirtree levels to show simultaneously 

    :type: typing.Union[int, str]
    '''

    show_hidden: bool = None
    '''Show hidden dot files 

    :type: bool
    '''

    sort_method: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    title: str = None
    '''Title for the file browser 

    :type: str
    '''

    use_filter: bool = None
    '''Enable filtering of files 

    :type: bool
    '''

    use_filter_backup: bool = None
    '''Show .blend1, .blend2, etc. files 

    :type: bool
    '''

    use_filter_blender: bool = None
    '''Show .blend files 

    :type: bool
    '''

    use_filter_blendid: bool = None
    '''Show .blend files items (objects, materials, etc.) 

    :type: bool
    '''

    use_filter_folder: bool = None
    '''Show folders 

    :type: bool
    '''

    use_filter_font: bool = None
    '''Show font files 

    :type: bool
    '''

    use_filter_image: bool = None
    '''Show image files 

    :type: bool
    '''

    use_filter_movie: bool = None
    '''Show movie files 

    :type: bool
    '''

    use_filter_script: bool = None
    '''Show script files 

    :type: bool
    '''

    use_filter_sound: bool = None
    '''Show sound files 

    :type: bool
    '''

    use_filter_text: bool = None
    '''Show text files 

    :type: bool
    '''

    use_library_browsing: bool = None
    '''Whether we may browse blender files’ content or not 

    :type: bool
    '''


class Filter2DActuator:
    '''Actuator to apply screen graphic effects '''

    filter_pass: int = None
    '''Set filter order 

    :type: int
    '''

    glsl_shader: 'Text' = None
    '''

    :type: 'Text'
    '''

    mode: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    motion_blur_factor: float = None
    '''Motion blur factor 

    :type: float
    '''

    use_motion_blur: bool = None
    '''Enable/Disable Motion Blur 

    :type: bool
    '''


class FloatProperty:
    '''RNA floating pointer number property definition '''

    array_length: int = None
    '''Maximum length of the array, 0 means unlimited 

    :type: int
    '''

    default: float = None
    '''Default value for this number 

    :type: float
    '''

    default_array: float = None
    '''Default value for this array 

    :type: float
    '''

    hard_max: float = None
    '''Maximum value used by buttons 

    :type: float
    '''

    hard_min: float = None
    '''Minimum value used by buttons 

    :type: float
    '''

    is_array: bool = None
    '''

    :type: bool
    '''

    precision: int = None
    '''Number of digits after the dot used by buttons 

    :type: int
    '''

    soft_max: float = None
    '''Maximum value used by buttons 

    :type: float
    '''

    soft_min: float = None
    '''Minimum value used by buttons 

    :type: float
    '''

    step: float = None
    '''Step size used by number buttons, for floats 1/100th of the step size 

    :type: float
    '''


class FloorConstraint:
    '''Use the target object for location limitation '''

    floor_location: typing.Union[int, str] = None
    '''Location of target that object will not pass through 

    :type: typing.Union[int, str]
    '''

    offset: float = None
    '''Offset of floor from object origin 

    :type: float
    '''

    subtarget: str = None
    '''

    :type: str
    '''

    target: 'Object' = None
    '''Target Object 

    :type: 'Object'
    '''

    use_rotation: bool = None
    '''Use the target’s rotation to determine floor 

    :type: bool
    '''

    use_sticky: bool = None
    '''Immobilize object while constrained 

    :type: bool
    '''


class FluidFluidSettings:
    '''Fluid simulation settings for the fluid in the simulation '''

    initial_velocity: float = None
    '''Initial velocity of fluid 

    :type: float
    '''

    use: bool = None
    '''Object contributes to the fluid simulation 

    :type: bool
    '''

    use_animated_mesh: bool = None
    '''Export this mesh as an animated one (slower and enforces No Slip, only use if really necessary [e.g. armatures or parented objects], animated pos/rot/scale F-Curves do not require it) 

    :type: bool
    '''

    volume_initialization: typing.Union[int, str] = None
    '''Volume initialization type (WARNING: complex volumes might require too much memory and break simulation) 

    :type: typing.Union[int, str]
    '''


class FluidSettings:
    '''Fluid simulation settings for an object taking part in the simulation '''

    type: typing.Union[int, str] = None
    '''Type of participation in the fluid simulation 

    :type: typing.Union[int, str]
    '''


class FluidSimulationModifier:
    '''Fluid simulation modifier '''

    settings: 'FluidSettings' = None
    '''Settings for how this object is used in the fluid simulation 

    :type: 'FluidSettings'
    '''


class FluidVertexVelocity:
    '''Velocity of a simulated fluid mesh '''

    velocity: float = None
    '''

    :type: float
    '''


class FollowPathConstraint:
    '''Lock motion to the target path '''

    forward_axis: typing.Union[int, str] = None
    '''Axis that points forward along the path 

    :type: typing.Union[int, str]
    '''

    offset: float = None
    '''Offset from the position corresponding to the time frame 

    :type: float
    '''

    offset_factor: float = None
    '''Percentage value defining target position along length of curve 

    :type: float
    '''

    target: 'Object' = None
    '''Target Object 

    :type: 'Object'
    '''

    up_axis: typing.Union[int, str] = None
    '''Axis that points upward 

    :type: typing.Union[int, str]
    '''

    use_curve_follow: bool = None
    '''Object will follow the heading and banking of the curve 

    :type: bool
    '''

    use_curve_radius: bool = None
    '''Object is scaled by the curve radius 

    :type: bool
    '''

    use_fixed_location: bool = None
    '''Object will stay locked to a single point somewhere along the length of the curve regardless of time 

    :type: bool
    '''


class FollowTrackConstraint:
    '''Lock motion to the target motion track '''

    camera: 'Object' = None
    '''Camera to which motion is parented (if empty active scene camera is used) 

    :type: 'Object'
    '''

    clip: 'MovieClip' = None
    '''Movie Clip to get tracking data from 

    :type: 'MovieClip'
    '''

    depth_object: 'Object' = None
    '''Object used to define depth in camera space by projecting onto surface of this object 

    :type: 'Object'
    '''

    frame_method: typing.Union[int, str] = None
    '''How the footage fits in the camera frame 

    :type: typing.Union[int, str]
    '''

    object: str = None
    '''Movie tracking object to follow (if empty, camera object is used) 

    :type: str
    '''

    track: str = None
    '''Movie tracking track to follow 

    :type: str
    '''

    use_3d_position: bool = None
    '''Use 3D position of track to parent to 

    :type: bool
    '''

    use_active_clip: bool = None
    '''Use active clip defined in scene 

    :type: bool
    '''

    use_undistorted_position: bool = None
    '''Parent to undistorted position of 2D track 

    :type: bool
    '''


class FreestyleLineSet:
    '''Line set for associating lines and style parameters '''

    edge_type_combination: typing.Union[int, str] = None
    '''Specify a logical combination of selection conditions on feature edge types 

    :type: typing.Union[int, str]
    '''

    edge_type_negation: typing.Union[int, str] = None
    '''Specify either inclusion or exclusion of feature edges selected by edge types 

    :type: typing.Union[int, str]
    '''

    exclude_border: bool = None
    '''Exclude border edges 

    :type: bool
    '''

    exclude_contour: bool = None
    '''Exclude contours 

    :type: bool
    '''

    exclude_crease: bool = None
    '''Exclude crease edges 

    :type: bool
    '''

    exclude_edge_mark: bool = None
    '''Exclude edge marks 

    :type: bool
    '''

    exclude_external_contour: bool = None
    '''Exclude external contours 

    :type: bool
    '''

    exclude_material_boundary: bool = None
    '''Exclude edges at material boundaries 

    :type: bool
    '''

    exclude_ridge_valley: bool = None
    '''Exclude ridges and valleys 

    :type: bool
    '''

    exclude_silhouette: bool = None
    '''Exclude silhouette edges 

    :type: bool
    '''

    exclude_suggestive_contour: bool = None
    '''Exclude suggestive contours 

    :type: bool
    '''

    face_mark_condition: typing.Union[int, str] = None
    '''Specify a feature edge selection condition based on face marks 

    :type: typing.Union[int, str]
    '''

    face_mark_negation: typing.Union[int, str] = None
    '''Specify either inclusion or exclusion of feature edges selected by face marks 

    :type: typing.Union[int, str]
    '''

    group: 'Group' = None
    '''A group of objects based on which feature edges are selected 

    :type: 'Group'
    '''

    group_negation: typing.Union[int, str] = None
    '''Specify either inclusion or exclusion of feature edges belonging to a group of objects 

    :type: typing.Union[int, str]
    '''

    linestyle: 'FreestyleLineStyle' = None
    '''Line style settings 

    :type: 'FreestyleLineStyle'
    '''

    name: str = None
    '''Line set name 

    :type: str
    '''

    qi_end: int = None
    '''Last QI value of the QI range 

    :type: int
    '''

    qi_start: int = None
    '''First QI value of the QI range 

    :type: int
    '''

    select_border: bool = None
    '''Select border edges (open mesh edges) 

    :type: bool
    '''

    select_by_edge_types: bool = None
    '''Select feature edges based on edge types 

    :type: bool
    '''

    select_by_face_marks: bool = None
    '''Select feature edges by face marks 

    :type: bool
    '''

    select_by_group: bool = None
    '''Select feature edges based on a group of objects 

    :type: bool
    '''

    select_by_image_border: bool = None
    '''Select feature edges by image border (less memory consumption) 

    :type: bool
    '''

    select_by_visibility: bool = None
    '''Select feature edges based on visibility 

    :type: bool
    '''

    select_contour: bool = None
    '''Select contours (outer silhouettes of each object) 

    :type: bool
    '''

    select_crease: bool = None
    '''Select crease edges (those between two faces making an angle smaller than the Crease Angle) 

    :type: bool
    '''

    select_edge_mark: bool = None
    '''Select edge marks (edges annotated by Freestyle edge marks) 

    :type: bool
    '''

    select_external_contour: bool = None
    '''Select external contours (outer silhouettes of occluding and occluded objects) 

    :type: bool
    '''

    select_material_boundary: bool = None
    '''Select edges at material boundaries 

    :type: bool
    '''

    select_ridge_valley: bool = None
    '''Select ridges and valleys (boundary lines between convex and concave areas of surface) 

    :type: bool
    '''

    select_silhouette: bool = None
    '''Select silhouettes (edges at the boundary of visible and hidden faces) 

    :type: bool
    '''

    select_suggestive_contour: bool = None
    '''Select suggestive contours (almost silhouette/contour edges) 

    :type: bool
    '''

    show_render: bool = None
    '''Enable or disable this line set during stroke rendering 

    :type: bool
    '''

    visibility: typing.Union[int, str] = None
    '''Determine how to use visibility for feature edge selection 

    :type: typing.Union[int, str]
    '''


class FreestyleLineStyle:
    '''Freestyle line style, reusable by multiple line sets '''

    active_texture: 'Texture' = None
    '''Active texture slot being displayed 

    :type: 'Texture'
    '''

    active_texture_index: int = None
    '''Index of active texture slot 

    :type: int
    '''

    alpha: float = None
    '''Base alpha transparency, possibly modified by alpha transparency modifiers 

    :type: float
    '''

    alpha_modifiers: typing.List['LineStyleAlphaModifier'] = None
    '''List of alpha transparency modifiers 

    :type: typing.List['LineStyleAlphaModifier']
    '''

    angle_max: float = None
    '''Maximum 2D angle for splitting chains 

    :type: float
    '''

    angle_min: float = None
    '''Minimum 2D angle for splitting chains 

    :type: float
    '''

    animation_data: 'AnimData' = None
    '''Animation data for this data-block 

    :type: 'AnimData'
    '''

    caps: typing.Union[int, str] = None
    '''Select the shape of both ends of strokes 

    :type: typing.Union[int, str]
    '''

    chain_count: int = None
    '''Chain count for the selection of first N chains 

    :type: int
    '''

    chaining: typing.Union[int, str] = None
    '''Select the way how feature edges are jointed to form chains 

    :type: typing.Union[int, str]
    '''

    color: float = None
    '''Base line color, possibly modified by line color modifiers 

    :type: float
    '''

    color_modifiers: typing.List['LineStyleColorModifier'] = None
    '''List of line color modifiers 

    :type: typing.List['LineStyleColorModifier']
    '''

    dash1: int = None
    '''Length of the 1st dash for dashed lines 

    :type: int
    '''

    dash2: int = None
    '''Length of the 2nd dash for dashed lines 

    :type: int
    '''

    dash3: int = None
    '''Length of the 3rd dash for dashed lines 

    :type: int
    '''

    gap1: int = None
    '''Length of the 1st gap for dashed lines 

    :type: int
    '''

    gap2: int = None
    '''Length of the 2nd gap for dashed lines 

    :type: int
    '''

    gap3: int = None
    '''Length of the 3rd gap for dashed lines 

    :type: int
    '''

    geometry_modifiers: typing.List['LineStyleGeometryModifier'] = None
    '''List of stroke geometry modifiers 

    :type: typing.List['LineStyleGeometryModifier']
    '''

    integration_type: typing.Union[int, str] = None
    '''Select the way how the sort key is computed for each chain 

    :type: typing.Union[int, str]
    '''

    length_max: float = None
    '''Maximum curvilinear 2D length for the selection of chains 

    :type: float
    '''

    length_min: float = None
    '''Minimum curvilinear 2D length for the selection of chains 

    :type: float
    '''

    material_boundary: bool = None
    '''If true, chains of feature edges are split at material boundaries 

    :type: bool
    '''

    node_tree: 'NodeTree' = None
    '''Node tree for node-based shaders 

    :type: 'NodeTree'
    '''

    panel: typing.Union[int, str] = None
    '''Select the property panel to be shown 

    :type: typing.Union[int, str]
    '''

    rounds: int = None
    '''Number of rounds in a sketchy multiple touch 

    :type: int
    '''

    sort_key: typing.Union[int, str] = None
    '''Select the sort key to determine the stacking order of chains 

    :type: typing.Union[int, str]
    '''

    sort_order: typing.Union[int, str] = None
    '''Select the sort order 

    :type: typing.Union[int, str]
    '''

    split_dash1: int = None
    '''Length of the 1st dash for splitting 

    :type: int
    '''

    split_dash2: int = None
    '''Length of the 2nd dash for splitting 

    :type: int
    '''

    split_dash3: int = None
    '''Length of the 3rd dash for splitting 

    :type: int
    '''

    split_gap1: int = None
    '''Length of the 1st gap for splitting 

    :type: int
    '''

    split_gap2: int = None
    '''Length of the 2nd gap for splitting 

    :type: int
    '''

    split_gap3: int = None
    '''Length of the 3rd gap for splitting 

    :type: int
    '''

    split_length: float = None
    '''Curvilinear 2D length for chain splitting 

    :type: float
    '''

    texture_slots: typing.List['LineStyleTextureSlot'] = None
    '''Texture slots defining the mapping and influence of textures 

    :type: typing.List['LineStyleTextureSlot']
    '''

    texture_spacing: float = None
    '''Spacing for textures along stroke length 

    :type: float
    '''

    thickness: float = None
    '''Base line thickness, possibly modified by line thickness modifiers 

    :type: float
    '''

    thickness_modifiers: typing.List['LineStyleThicknessModifier'] = None
    '''List of line thickness modifiers 

    :type: typing.List['LineStyleThicknessModifier']
    '''

    thickness_position: typing.Union[int, str] = None
    '''Thickness position of silhouettes and border edges (applicable when plain chaining is used with the Same Object option) 

    :type: typing.Union[int, str]
    '''

    thickness_ratio: float = None
    '''A number between 0 (inside) and 1 (outside) specifying the relative position of stroke thickness 

    :type: float
    '''

    use_angle_max: bool = None
    '''Split chains at points with angles larger than the maximum 2D angle 

    :type: bool
    '''

    use_angle_min: bool = None
    '''Split chains at points with angles smaller than the minimum 2D angle 

    :type: bool
    '''

    use_chain_count: bool = None
    '''Enable the selection of first N chains 

    :type: bool
    '''

    use_chaining: bool = None
    '''Enable chaining of feature edges 

    :type: bool
    '''

    use_dashed_line: bool = None
    '''Enable or disable dashed line 

    :type: bool
    '''

    use_length_max: bool = None
    '''Enable the selection of chains by a maximum 2D length 

    :type: bool
    '''

    use_length_min: bool = None
    '''Enable the selection of chains by a minimum 2D length 

    :type: bool
    '''

    use_nodes: bool = None
    '''Use shader nodes for the line style 

    :type: bool
    '''

    use_same_object: bool = None
    '''If true, only feature edges of the same object are joined 

    :type: bool
    '''

    use_sorting: bool = None
    '''Arrange the stacking order of strokes 

    :type: bool
    '''

    use_split_length: bool = None
    '''Enable chain splitting by curvilinear 2D length 

    :type: bool
    '''

    use_split_pattern: bool = None
    '''Enable chain splitting by dashed line patterns 

    :type: bool
    '''

    use_texture: bool = None
    '''Enable or disable textured strokes 

    :type: bool
    '''


class FreestyleModuleSettings:
    '''Style module configuration for specifying a style module '''

    script: 'Text' = None
    '''Python script to define a style module 

    :type: 'Text'
    '''

    use: bool = None
    '''Enable or disable this style module during stroke rendering 

    :type: bool
    '''


class FreestyleModules:
    '''A list of style modules (to be applied from top to bottom) '''

    def new(self, ) -> 'FreestyleModuleSettings':
        '''Add a style module to scene render layer Freestyle settings 

        :rtype: 'FreestyleModuleSettings'
        :return:  Newly created style module 
        '''
        pass

    def remove(self, module: 'FreestyleModuleSettings'):
        '''Remove a style module from scene render layer Freestyle settings 

        :param module: Style module to remove 
        :type module: 'FreestyleModuleSettings'
        '''
        pass


class FreestyleSettings:
    '''Freestyle settings for a SceneRenderLayer data-block '''

    crease_angle: float = None
    '''Angular threshold for detecting crease edges 

    :type: float
    '''

    kr_derivative_epsilon: float = None
    '''Kr derivative epsilon for computing suggestive contours 

    :type: float
    '''

    linesets: typing.List['Linesets'] = None
    '''

    :type: typing.List['Linesets']
    '''

    mode: typing.Union[int, str] = None
    '''Select the Freestyle control mode 

    :type: typing.Union[int, str]
    '''

    modules: typing.List['FreestyleModules'] = None
    '''A list of style modules (to be applied from top to bottom) 

    :type: typing.List['FreestyleModules']
    '''

    sphere_radius: float = None
    '''Sphere radius for computing curvatures 

    :type: float
    '''

    use_advanced_options: bool = None
    '''Enable advanced edge detection options (sphere radius and Kr derivative epsilon) 

    :type: bool
    '''

    use_culling: bool = None
    '''If enabled, out-of-view edges are ignored 

    :type: bool
    '''

    use_material_boundaries: bool = None
    '''Enable material boundaries 

    :type: bool
    '''

    use_ridges_and_valleys: bool = None
    '''Enable ridges and valleys 

    :type: bool
    '''

    use_smoothness: bool = None
    '''Take face smoothness into account in view map calculation 

    :type: bool
    '''

    use_suggestive_contours: bool = None
    '''Enable suggestive contours 

    :type: bool
    '''

    use_view_map_cache: bool = None
    '''Keep the computed view map and avoid re-calculating it if mesh geometry is unchanged 

    :type: bool
    '''


class Function:
    '''RNA function definition '''

    description: str = None
    '''Description of the Function’s purpose 

    :type: str
    '''

    identifier: str = None
    '''Unique name used in the code and scripting 

    :type: str
    '''

    is_registered: bool = None
    '''Function is registered as callback as part of type registration 

    :type: bool
    '''

    is_registered_optional: bool = None
    '''Function is optionally registered as callback part of type registration 

    :type: bool
    '''

    parameters: typing.List['Property'] = None
    '''Parameters for the function 

    :type: typing.List['Property']
    '''

    use_self: bool = None
    '''Function does not pass its self as an argument (becomes a static method in python) 

    :type: bool
    '''

    use_self_type: bool = None
    '''Function passes its self type as an argument (becomes a class method in python if use_self is false) 

    :type: bool
    '''


class GPENCIL_PIE_sculpt:
    def draw(self, context):
        '''

        '''
        pass

    def draw_preset(self, context):
        '''Optionally: - preset_extensions (set of strings) - preset_operator_defaults (dict of keyword args) 

        '''
        pass

    def path_menu(self,
                  searchpaths: list,
                  operator: str,
                  *,
                  props_default: dict = None,
                  prop_filepath: str = 'filepath',
                  filter_ext: str = None,
                  filter_path=None,
                  display_name: str = None):
        '''Populate a menu from a list of paths. 

        :param searchpaths: Paths to scan. 
        :type searchpaths: list
        :param operator: The operator id to use with each file. 
        :type operator: str
        :param prop_filepath: Optional operator filepath property (defaults to “filepath”). 
        :type prop_filepath: str
        :param props_default: Properties to assign to each operator. 
        :type props_default: dict
        :param filter_ext: Optional callback that takes the file extensions.Returning false excludes the file from the list. 
        :type filter_ext: str
        :param display_name: Optional callback that takes the full path, returns the name to display. 
        :type display_name: str
        '''
        pass


class GPENCIL_PIE_settings_palette:
    def draw(self, context):
        '''

        '''
        pass

    def draw_preset(self, context):
        '''Optionally: - preset_extensions (set of strings) - preset_operator_defaults (dict of keyword args) 

        '''
        pass

    def path_menu(self,
                  searchpaths: list,
                  operator: str,
                  *,
                  props_default: dict = None,
                  prop_filepath: str = 'filepath',
                  filter_ext: str = None,
                  filter_path=None,
                  display_name: str = None):
        '''Populate a menu from a list of paths. 

        :param searchpaths: Paths to scan. 
        :type searchpaths: list
        :param operator: The operator id to use with each file. 
        :type operator: str
        :param prop_filepath: Optional operator filepath property (defaults to “filepath”). 
        :type prop_filepath: str
        :param props_default: Properties to assign to each operator. 
        :type props_default: dict
        :param filter_ext: Optional callback that takes the file extensions.Returning false excludes the file from the list. 
        :type filter_ext: str
        :param display_name: Optional callback that takes the full path, returns the name to display. 
        :type display_name: str
        '''
        pass


class GPENCIL_PIE_tool_palette:
    def draw(self, context):
        '''

        '''
        pass

    def draw_preset(self, context):
        '''Optionally: - preset_extensions (set of strings) - preset_operator_defaults (dict of keyword args) 

        '''
        pass

    def path_menu(self,
                  searchpaths: list,
                  operator: str,
                  *,
                  props_default: dict = None,
                  prop_filepath: str = 'filepath',
                  filter_ext: str = None,
                  filter_path=None,
                  display_name: str = None):
        '''Populate a menu from a list of paths. 

        :param searchpaths: Paths to scan. 
        :type searchpaths: list
        :param operator: The operator id to use with each file. 
        :type operator: str
        :param prop_filepath: Optional operator filepath property (defaults to “filepath”). 
        :type prop_filepath: str
        :param props_default: Properties to assign to each operator. 
        :type props_default: dict
        :param filter_ext: Optional callback that takes the file extensions.Returning false excludes the file from the list. 
        :type filter_ext: str
        :param display_name: Optional callback that takes the full path, returns the name to display. 
        :type display_name: str
        '''
        pass


class GPENCIL_PIE_tools_more:
    def draw(self, context):
        '''

        '''
        pass

    def draw_preset(self, context):
        '''Optionally: - preset_extensions (set of strings) - preset_operator_defaults (dict of keyword args) 

        '''
        pass

    def path_menu(self,
                  searchpaths: list,
                  operator: str,
                  *,
                  props_default: dict = None,
                  prop_filepath: str = 'filepath',
                  filter_ext: str = None,
                  filter_path=None,
                  display_name: str = None):
        '''Populate a menu from a list of paths. 

        :param searchpaths: Paths to scan. 
        :type searchpaths: list
        :param operator: The operator id to use with each file. 
        :type operator: str
        :param prop_filepath: Optional operator filepath property (defaults to “filepath”). 
        :type prop_filepath: str
        :param props_default: Properties to assign to each operator. 
        :type props_default: dict
        :param filter_ext: Optional callback that takes the file extensions.Returning false excludes the file from the list. 
        :type filter_ext: str
        :param display_name: Optional callback that takes the full path, returns the name to display. 
        :type display_name: str
        '''
        pass


class GPENCIL_UL_brush:
    def draw_item(self, context, layout, data, item, icon, active_data,
                  active_propname, index):
        '''

        '''
        pass


class GPENCIL_UL_layer:
    def draw_item(self, context, layout, data, item, icon, active_data,
                  active_propname, index):
        '''

        '''
        pass


class GPENCIL_UL_palettecolor:
    def draw_item(self, context, layout, data, item, icon, active_data,
                  active_propname, index):
        '''

        '''
        pass


class GPUDOFSettings:
    '''Settings for GPU based depth of field '''

    blades: int = None
    '''Blades for dof effect 

    :type: int
    '''

    focal_length: float = None
    '''Focal length for dof effect 

    :type: float
    '''

    focus_distance: float = None
    '''Viewport depth of field focus distance 

    :type: float
    '''

    fstop: float = None
    '''F-stop for dof effect 

    :type: float
    '''

    is_hq_supported: bool = None
    '''Use high quality depth of field 

    :type: bool
    '''

    sensor: float = None
    '''Size of sensor 

    :type: float
    '''

    use_high_quality: bool = None
    '''Use high quality depth of field 

    :type: bool
    '''


class GPUFXSettings:
    '''Settings for GPU based compositing '''

    dof: 'GPUDOFSettings' = None
    '''

    :type: 'GPUDOFSettings'
    '''

    ssao: 'GPUSSAOSettings' = None
    '''

    :type: 'GPUSSAOSettings'
    '''

    use_dof: bool = None
    '''Use depth of field on viewport using the values from active camera 

    :type: bool
    '''

    use_ssao: bool = None
    '''Use screen space ambient occlusion of field on viewport 

    :type: bool
    '''


class GPUSSAOSettings:
    '''Settings for GPU based screen space ambient occlusion '''

    attenuation: float = None
    '''Attenuation constant 

    :type: float
    '''

    color: float = None
    '''Color for screen space ambient occlusion effect 

    :type: float
    '''

    distance_max: float = None
    '''Distance of object that contribute to the SSAO effect 

    :type: float
    '''

    factor: float = None
    '''Strength of the SSAO effect 

    :type: float
    '''

    samples: int = None
    '''Number of samples 

    :type: int
    '''


class GPencilBrush:
    '''Collection of brushes being used to control the line style of new strokes '''

    angle: float = None
    '''Direction of the stroke at which brush gives maximal thickness (0° for horizontal) 

    :type: float
    '''

    angle_factor: float = None
    '''Reduce brush thickness by this factor when stroke is perpendicular to ‘Angle’ direction 

    :type: float
    '''

    curve_jitter: 'CurveMapping' = None
    '''Curve used for the jitter effect 

    :type: 'CurveMapping'
    '''

    curve_sensitivity: 'CurveMapping' = None
    '''Curve used for the sensitivity 

    :type: 'CurveMapping'
    '''

    curve_strength: 'CurveMapping' = None
    '''Curve used for the strength 

    :type: 'CurveMapping'
    '''

    jitter: float = None
    '''Jitter factor for new strokes 

    :type: float
    '''

    line_width: int = None
    '''Thickness of strokes (in pixels) 

    :type: int
    '''

    name: str = None
    '''Brush name 

    :type: str
    '''

    pen_sensitivity_factor: float = None
    '''Pressure sensitivity factor for new strokes 

    :type: float
    '''

    pen_smooth_factor: float = None
    '''Amount of smoothing to apply to newly created strokes, to reduce jitter/noise 

    :type: float
    '''

    pen_smooth_steps: int = None
    '''Number of times to smooth newly created strokes 

    :type: int
    '''

    pen_subdivision_steps: int = None
    '''Number of times to subdivide newly created strokes, for less jagged strokes 

    :type: int
    '''

    random_press: float = None
    '''Randomness factor for pressure and strength in new strokes 

    :type: float
    '''

    random_subdiv: float = None
    '''Randomness factor for new strokes after subdivision 

    :type: float
    '''

    strength: float = None
    '''Color strength for new strokes (affect alpha factor of color) 

    :type: float
    '''

    use_jitter_pressure: bool = None
    '''Use tablet pressure for jitter 

    :type: bool
    '''

    use_pressure: bool = None
    '''Use tablet pressure 

    :type: bool
    '''

    use_random_pressure: bool = None
    '''Use random value for pressure 

    :type: bool
    '''

    use_random_strength: bool = None
    '''Use random value for strength 

    :type: bool
    '''

    use_strength_pressure: bool = None
    '''Use tablet pressure for color strength 

    :type: bool
    '''


class GPencilFrame:
    '''Collection of related sketches on a particular frame '''

    frame_number: int = None
    '''The frame on which this sketch appears 

    :type: int
    '''

    is_edited: bool = None
    '''Frame is being edited (painted on) 

    :type: bool
    '''

    select: bool = None
    '''Frame is selected for editing in the Dope Sheet 

    :type: bool
    '''

    strokes: typing.List['GPencilStrokes'] = None
    '''Freehand curves defining the sketch on this frame 

    :type: typing.List['GPencilStrokes']
    '''

    def clear(self, ):
        '''Remove all the grease pencil frame data 

        '''
        pass


class GPencilFrames:
    '''Collection of grease pencil frames '''

    def new(self, frame_number: int) -> 'GPencilFrame':
        '''Add a new grease pencil frame 

        :param frame_number: Frame Number, The frame on which this sketch appears 
        :type frame_number: int
        :rtype: 'GPencilFrame'
        :return:  The newly created frame 
        '''
        pass

    def remove(self, frame: 'GPencilFrame'):
        '''Remove a grease pencil frame 

        :param frame: Frame, The frame to remove 
        :type frame: 'GPencilFrame'
        '''
        pass

    def copy(self, source: 'GPencilFrame') -> 'GPencilFrame':
        '''Copy a grease pencil frame 

        :param source: Source, The source frame 
        :type source: 'GPencilFrame'
        :rtype: 'GPencilFrame'
        :return:  The newly copied frame 
        '''
        pass


class GPencilInterpolateSettings:
    '''Settings for Grease Pencil interpolation tools '''

    amplitude: float = None
    '''Amount to boost elastic bounces for ‘elastic’ easing 

    :type: float
    '''

    back: float = None
    '''Amount of overshoot for ‘back’ easing 

    :type: float
    '''

    easing: typing.Union[int, str] = None
    '''Which ends of the segment between the preceding and following grease pencil frames easing interpolation is applied to 

    :type: typing.Union[int, str]
    '''

    interpolate_all_layers: bool = None
    '''Interpolate all layers, not only active 

    :type: bool
    '''

    interpolate_selected_only: bool = None
    '''Interpolate only selected strokes in the original frame 

    :type: bool
    '''

    interpolation_curve: 'CurveMapping' = None
    '''Custom curve to control ‘sequence’ interpolation between Grease Pencil frames 

    :type: 'CurveMapping'
    '''

    period: float = None
    '''Time between bounces for elastic easing 

    :type: float
    '''

    type: typing.Union[int, str] = None
    '''Interpolation method to use the next time ‘Interpolate Sequence’ is run 

    :type: typing.Union[int, str]
    '''


class GPencilLayer:
    '''Collection of related sketches '''

    active_frame: 'GPencilFrame' = None
    '''Frame currently being displayed for this layer 

    :type: 'GPencilFrame'
    '''

    after_color: float = None
    '''Base color for ghosts after the active frame 

    :type: float
    '''

    before_color: float = None
    '''Base color for ghosts before the active frame 

    :type: float
    '''

    frames: typing.List['GPencilFrames'] = None
    '''Sketches for this layer on different frames 

    :type: typing.List['GPencilFrames']
    '''

    ghost_after_range: int = None
    '''Maximum number of frames to show after current frame (0 = show only the next sketch, -1 = don’t show any frames after current) 

    :type: int
    '''

    ghost_before_range: int = None
    '''Maximum number of frames to show before current frame (0 = show only the previous sketch, -1 = don’t show any frames before current) 

    :type: int
    '''

    hide: bool = None
    '''Set layer Visibility 

    :type: bool
    '''

    info: str = None
    '''Layer name 

    :type: str
    '''

    is_parented: bool = None
    '''True when the layer parent object is set 

    :type: bool
    '''

    line_change: int = None
    '''Thickness change to apply to current strokes (in pixels) 

    :type: int
    '''

    lock: bool = None
    '''Protect layer from further editing and/or frame changes 

    :type: bool
    '''

    lock_frame: bool = None
    '''Lock current frame displayed by layer 

    :type: bool
    '''

    matrix_inverse: float = None
    '''Parent inverse transformation matrix 

    :type: float
    '''

    opacity: float = None
    '''Layer Opacity 

    :type: float
    '''

    parent: 'Object' = None
    '''Parent Object 

    :type: 'Object'
    '''

    parent_bone: str = None
    '''Name of parent bone in case of a bone parenting relation 

    :type: str
    '''

    parent_type: typing.Union[int, str] = None
    '''Type of parent relation 

    :type: typing.Union[int, str]
    '''

    select: bool = None
    '''Layer is selected for editing in the Dope Sheet 

    :type: bool
    '''

    show_points: bool = None
    '''Draw the points which make up the strokes (for debugging purposes) 

    :type: bool
    '''

    show_x_ray: bool = None
    '''Make the layer draw in front of objects 

    :type: bool
    '''

    tint_color: float = None
    '''Color for tinting stroke colors 

    :type: float
    '''

    tint_factor: float = None
    '''Factor of tinting color 

    :type: float
    '''

    unlock_color: bool = None
    '''Unprotect selected colors from further editing and/or frame changes 

    :type: bool
    '''

    use_ghost_custom_colors: bool = None
    '''Use custom colors for ghost frames 

    :type: bool
    '''

    use_ghosts_always: bool = None
    '''Ghosts are shown in renders and animation playback. Useful for special effects (e.g. motion blur) 

    :type: bool
    '''

    use_onion_skinning: bool = None
    '''Ghost frames on either side of frame 

    :type: bool
    '''

    use_volumetric_strokes: bool = None
    '''Draw strokes as a series of circular blobs, resulting in a volumetric effect 

    :type: bool
    '''

    def clear(self, ):
        '''Remove all the grease pencil layer data 

        '''
        pass


class GPencilPalette:
    '''Collection of related palettes '''

    colors: typing.List['GPencilPaletteColors'] = None
    '''Colors of the palette 

    :type: typing.List['GPencilPaletteColors']
    '''

    name: str = None
    '''Palette name 

    :type: str
    '''


class GPencilPaletteColor:
    '''Collection of related colors '''

    alpha: float = None
    '''Color Opacity 

    :type: float
    '''

    color: float = None
    '''Color for strokes 

    :type: float
    '''

    fill_alpha: float = None
    '''Opacity for filling region bounded by each stroke 

    :type: float
    '''

    fill_color: float = None
    '''Color for filling region bounded by each stroke 

    :type: float
    '''

    ghost: bool = None
    '''Display strokes using this color when showing onion skins 

    :type: bool
    '''

    hide: bool = None
    '''Set color Visibility 

    :type: bool
    '''

    is_fill_visible: bool = None
    '''True when opacity of fill is set high enough to be visible 

    :type: bool
    '''

    is_stroke_visible: bool = None
    '''True when opacity of stroke is set high enough to be visible 

    :type: bool
    '''

    lock: bool = None
    '''Protect color from further editing and/or frame changes 

    :type: bool
    '''

    name: str = None
    '''Color name 

    :type: str
    '''

    use_hq_fill: bool = None
    '''Fill strokes using high quality to avoid glitches (slower fps during animation play) 

    :type: bool
    '''

    use_volumetric_strokes: bool = None
    '''Draw strokes as a series of circular blobs, resulting in a volumetric effect 

    :type: bool
    '''


class GPencilPaletteColors:
    '''Collection of palette colors '''

    active: 'GPencilPaletteColor' = None
    '''Current active color 

    :type: 'GPencilPaletteColor'
    '''

    active_index: int = None
    '''Index of active palette color 

    :type: int
    '''

    def new(self, ) -> 'GPencilPaletteColor':
        '''Add a new color to the palette 

        :rtype: 'GPencilPaletteColor'
        :return:  The newly created color 
        '''
        pass

    def remove(self, color: 'GPencilPaletteColor'):
        '''Remove a color from the palette 

        :param color: The color to remove 
        :type color: 'GPencilPaletteColor'
        '''
        pass


class GPencilSculptBrush:
    '''Stroke editing brush '''

    affect_pressure: bool = None
    '''Affect pressure values as well when smoothing strokes 

    :type: bool
    '''

    direction: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    size: int = None
    '''Radius of the brush in pixels 

    :type: int
    '''

    strength: float = None
    '''Brush strength 

    :type: float
    '''

    use_falloff: bool = None
    '''Strength of brush decays with distance from cursor 

    :type: bool
    '''

    use_pressure_strength: bool = None
    '''Enable tablet pressure sensitivity for strength 

    :type: bool
    '''


class GPencilSculptSettings:
    '''Properties for Grease Pencil stroke sculpting tool '''

    affect_position: bool = None
    '''The brush affects the position of the point 

    :type: bool
    '''

    affect_strength: bool = None
    '''The brush affects the color strength of the point 

    :type: bool
    '''

    affect_thickness: bool = None
    '''The brush affects the thickness of the point 

    :type: bool
    '''

    brush: 'GPencilSculptBrush' = None
    '''

    :type: 'GPencilSculptBrush'
    '''

    lockaxis: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    selection_alpha: float = None
    '''Alpha value for selected vertices 

    :type: float
    '''

    tool: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    use_select_mask: bool = None
    '''Only sculpt selected stroke points 

    :type: bool
    '''


class GPencilStroke:
    '''Freehand curve defining part of a sketch '''

    color: 'GPencilPaletteColor' = None
    '''Color from palette used in Stroke 

    :type: 'GPencilPaletteColor'
    '''

    colorname: str = None
    '''Palette color name 

    :type: str
    '''

    draw_cyclic: bool = None
    '''Enable cyclic drawing, closing the stroke 

    :type: bool
    '''

    draw_mode: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    line_width: int = None
    '''Thickness of stroke (in pixels) 

    :type: int
    '''

    points: typing.List['GPencilStrokePoint'] = None
    '''Stroke data points 

    :type: typing.List['GPencilStrokePoint']
    '''

    select: bool = None
    '''Stroke is selected for viewport editing 

    :type: bool
    '''

    triangles: typing.List['GPencilTriangle'] = None
    '''Triangulation data for HQ fill 

    :type: typing.List['GPencilTriangle']
    '''


class GPencilStrokePoint:
    '''Data point for freehand stroke curve '''

    co: float = None
    '''

    :type: float
    '''

    pressure: float = None
    '''Pressure of tablet at point when drawing it 

    :type: float
    '''

    select: bool = None
    '''Point is selected for viewport editing 

    :type: bool
    '''

    strength: float = None
    '''Color intensity (alpha factor) 

    :type: float
    '''


class GPencilStrokePoints:
    '''Collection of grease pencil stroke points '''

    def add(self, count: int = 1, pressure: float = 1.0,
            strength: float = 1.0):
        '''Add a new grease pencil stroke point 

        :param count: Number, Number of points to add to the stroke 
        :type count: int
        :param pressure: Pressure, Pressure for newly created points 
        :type pressure: float
        :param strength: Strength, Color intensity (alpha factor) for newly created points 
        :type strength: float
        '''
        pass

    def pop(self, index: int = -1):
        '''Remove a grease pencil stroke point 

        :param index: Index, point index 
        :type index: int
        '''
        pass


class GPencilStrokes:
    '''Collection of grease pencil stroke '''

    def new(self, colorname: str = "") -> 'GPencilStroke':
        '''Add a new grease pencil stroke 

        :param colorname: Color, Name of the color 
        :type colorname: str
        :rtype: 'GPencilStroke'
        :return:  The newly created stroke 
        '''
        pass

    def remove(self, stroke: 'GPencilStroke'):
        '''Remove a grease pencil stroke 

        :param stroke: Stroke, The stroke to remove 
        :type stroke: 'GPencilStroke'
        '''
        pass


class GPencilTriangle:
    '''Triangulation data for HQ fill '''

    v1: int = None
    '''First triangle vertex index 

    :type: int
    '''

    v2: int = None
    '''Second triangle vertex index 

    :type: int
    '''

    v3: int = None
    '''Third triangle vertex index 

    :type: int
    '''


class GameActuator:
    filename: str = None
    '''The file to use, depending on the mode (e.g. the blend file to load or a destination for saving a screenshot) - use the “//” prefix for a relative path 

    :type: str
    '''

    mode: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''


class GameBooleanProperty:
    '''Game engine user defined Boolean property '''

    value: bool = None
    '''Property value 

    :type: bool
    '''


class GameFloatProperty:
    '''Game engine user defined floating point number property '''

    value: float = None
    '''Property value 

    :type: float
    '''


class GameIntProperty:
    '''Game engine user defined integer number property '''

    value: int = None
    '''Property value 

    :type: int
    '''


class GameObjectSettings:
    '''Game engine related settings for the object '''

    actuators: typing.List['Actuator'] = None
    '''Game engine actuators to act on events 

    :type: typing.List['Actuator']
    '''

    angular_velocity_max: float = None
    '''Clamp angular velocity to this maximum speed, in angle per second 

    :type: float
    '''

    angular_velocity_min: float = None
    '''Clamp angular velocity to this minimum speed (except when totally still), in angle per second 

    :type: float
    '''

    collision_bounds_type: typing.Union[int, str] = None
    '''Select the collision shape that better fits the object 

    :type: typing.Union[int, str]
    '''

    collision_group: bool = None
    '''The collision group of the object 

    :type: bool
    '''

    collision_margin: float = None
    '''Extra margin around object for collision detection, small amount required for stability 

    :type: float
    '''

    collision_mask: bool = None
    '''The groups this object can collide with 

    :type: bool
    '''

    controllers: typing.List['Controller'] = None
    '''Game engine controllers to process events, connecting sensors to actuators 

    :type: typing.List['Controller']
    '''

    damping: float = None
    '''General movement damping 

    :type: float
    '''

    fall_speed: float = None
    '''Maximum speed at which the character will fall 

    :type: float
    '''

    form_factor: float = None
    '''Form factor scales the inertia tensor 

    :type: float
    '''

    friction_coefficients: float = None
    '''Relative friction coefficients in the in the X, Y and Z directions, when anisotropic friction is enabled 

    :type: float
    '''

    jump_max: int = None
    '''The maximum number of jumps the character can make before it hits the ground 

    :type: int
    '''

    jump_speed: float = None
    '''Upward velocity applied to the character when jumping 

    :type: float
    '''

    lock_location_x: bool = None
    '''Disable simulation of linear motion along the X axis 

    :type: bool
    '''

    lock_location_y: bool = None
    '''Disable simulation of linear motion along the Y axis 

    :type: bool
    '''

    lock_location_z: bool = None
    '''Disable simulation of linear motion along the Z axis 

    :type: bool
    '''

    lock_rotation_x: bool = None
    '''Disable simulation of angular motion along the X axis 

    :type: bool
    '''

    lock_rotation_y: bool = None
    '''Disable simulation of angular motion along the Y axis 

    :type: bool
    '''

    lock_rotation_z: bool = None
    '''Disable simulation of angular motion along the Z axis 

    :type: bool
    '''

    mass: float = None
    '''Mass of the object 

    :type: float
    '''

    obstacle_radius: float = None
    '''Radius of object representation in obstacle simulation 

    :type: float
    '''

    physics_type: typing.Union[int, str] = None
    '''Select the type of physical representation 

    :type: typing.Union[int, str]
    '''

    properties: typing.List['GameProperty'] = None
    '''Game engine properties 

    :type: typing.List['GameProperty']
    '''

    radius: float = None
    '''Radius of bounding sphere and material physics 

    :type: float
    '''

    rotation_damping: float = None
    '''General rotation damping 

    :type: float
    '''

    sensors: typing.List['Sensor'] = None
    '''Game engine sensor to detect events 

    :type: typing.List['Sensor']
    '''

    show_actuators: bool = None
    '''Shows actuators for this object in the user interface 

    :type: bool
    '''

    show_controllers: bool = None
    '''Shows controllers for this object in the user interface 

    :type: bool
    '''

    show_debug_state: bool = None
    '''Print state debug info in the game engine 

    :type: bool
    '''

    show_sensors: bool = None
    '''Shows sensors for this object in the user interface 

    :type: bool
    '''

    show_state_panel: bool = None
    '''Show state panel 

    :type: bool
    '''

    soft_body: 'GameSoftBodySettings' = None
    '''Settings for Bullet soft body simulation 

    :type: 'GameSoftBodySettings'
    '''

    states_initial: bool = None
    '''Initial state when the game starts 

    :type: bool
    '''

    states_visible: bool = None
    '''State determining which controllers are displayed 

    :type: bool
    '''

    step_height: float = None
    '''Maximum height of steps the character can run over 

    :type: float
    '''

    use_activity_culling: bool = None
    '''Disable simulation of angular motion along the Z axis 

    :type: bool
    '''

    use_actor: bool = None
    '''Object is detected by the Near and Radar sensor 

    :type: bool
    '''

    use_all_states: bool = None
    '''Set all state bits 

    :type: bool
    '''

    use_anisotropic_friction: bool = None
    '''Enable anisotropic friction 

    :type: bool
    '''

    use_collision_bounds: bool = None
    '''Specify a collision bounds type other than the default 

    :type: bool
    '''

    use_collision_compound: bool = None
    '''Add children to form a compound collision object 

    :type: bool
    '''

    use_ghost: bool = None
    '''Object does not react to collisions, like a ghost 

    :type: bool
    '''

    use_material_physics_fh: bool = None
    '''React to force field physics settings in materials 

    :type: bool
    '''

    use_obstacle_create: bool = None
    '''Create representation for obstacle simulation 

    :type: bool
    '''

    use_record_animation: bool = None
    '''Record animation objects without physics 

    :type: bool
    '''

    use_rotate_from_normal: bool = None
    '''Use face normal to rotate object, so that it points away from the surface 

    :type: bool
    '''

    use_sleep: bool = None
    '''Disable auto (de)activation in physics simulation 

    :type: bool
    '''

    used_states: bool = None
    '''States which are being used by controllers 

    :type: bool
    '''

    velocity_max: float = None
    '''Clamp velocity to this maximum speed, in distance per second 

    :type: float
    '''

    velocity_min: float = None
    '''Clamp velocity to this minimum speed (except when totally still), in distance per second 

    :type: float
    '''


class GameProperty:
    '''Game engine user defined object property '''

    name: str = None
    '''Available as GameObject attributes in the game engine’s python API 

    :type: str
    '''

    show_debug: bool = None
    '''Print debug information for this property 

    :type: bool
    '''

    type: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''


class GameSoftBodySettings:
    '''Soft body simulation settings for an object in the game engine '''

    cluster_iterations: int = None
    '''Number of cluster iterations 

    :type: int
    '''

    collision_margin: float = None
    '''Collision margin for soft body. Small value makes the algorithm unstable 

    :type: float
    '''

    dynamic_friction: float = None
    '''Dynamic Friction 

    :type: float
    '''

    linear_stiffness: float = None
    '''Linear stiffness of the soft body links 

    :type: float
    '''

    location_iterations: int = None
    '''Position solver iterations 

    :type: int
    '''

    shape_threshold: float = None
    '''Shape matching threshold 

    :type: float
    '''

    use_bending_constraints: bool = None
    '''Enable bending constraints 

    :type: bool
    '''

    use_cluster_rigid_to_softbody: bool = None
    '''Enable cluster collision between soft and rigid body 

    :type: bool
    '''

    use_cluster_soft_to_softbody: bool = None
    '''Enable cluster collision between soft and soft body 

    :type: bool
    '''

    use_shape_match: bool = None
    '''Enable soft body shape matching goal 

    :type: bool
    '''

    weld_threshold: float = None
    '''Welding threshold: distance between nearby vertices to be considered equal => set to 0.0 to disable welding test and speed up scene loading (ok if the mesh has no duplicates) 

    :type: float
    '''


class GameStringProperty:
    '''Game engine user defined text string property '''

    value: str = None
    '''Property value 

    :type: str
    '''


class GameTimerProperty:
    '''Game engine user defined timer property '''

    value: float = None
    '''Property value 

    :type: float
    '''


class GammaCrossSequence:
    '''Gamma Cross Sequence '''

    input_1: 'Sequence' = None
    '''First input for the effect strip 

    :type: 'Sequence'
    '''

    input_2: 'Sequence' = None
    '''Second input for the effect strip 

    :type: 'Sequence'
    '''

    input_count: int = None
    '''

    :type: int
    '''


class GaussianBlurSequence:
    '''Sequence strip creating a gaussian blur '''

    input_1: 'Sequence' = None
    '''First input for the effect strip 

    :type: 'Sequence'
    '''

    input_count: int = None
    '''

    :type: int
    '''

    size_x: float = None
    '''Size of the blur along X axis 

    :type: float
    '''

    size_y: float = None
    '''Size of the blur along Y axis 

    :type: float
    '''


class GlowSequence:
    '''Sequence strip creating a glow effect '''

    blur_radius: float = None
    '''Radius of glow effect 

    :type: float
    '''

    boost_factor: float = None
    '''Brightness multiplier 

    :type: float
    '''

    clamp: float = None
    '''Brightness limit of intensity 

    :type: float
    '''

    input_1: 'Sequence' = None
    '''First input for the effect strip 

    :type: 'Sequence'
    '''

    input_count: int = None
    '''

    :type: int
    '''

    quality: int = None
    '''Accuracy of the blur effect 

    :type: int
    '''

    threshold: float = None
    '''Minimum intensity to trigger a glow 

    :type: float
    '''

    use_only_boost: bool = None
    '''Show the glow buffer only 

    :type: bool
    '''


class GreasePencil:
    '''Freehand annotation sketchbook '''

    animation_data: 'AnimData' = None
    '''Animation data for this data-block 

    :type: 'AnimData'
    '''

    layers: typing.List['GreasePencilLayers'] = None
    '''

    :type: typing.List['GreasePencilLayers']
    '''

    palettes: typing.List['GPencilPalette'] = None
    '''

    :type: typing.List['GPencilPalette']
    '''

    show_stroke_direction: bool = None
    '''Show stroke drawing direction with a bigger green dot (start) and smaller red dot (end) points 

    :type: bool
    '''

    use_onion_skinning: bool = None
    '''Show ghosts of the frames before and after the current frame, toggle to enable on active layer or disable all 

    :type: bool
    '''

    use_stroke_edit_mode: bool = None
    '''Edit Grease Pencil strokes instead of viewport data 

    :type: bool
    '''

    def clear(self, ):
        '''Remove all the grease pencil data 

        '''
        pass


class GreasePencilBrushes:
    '''Collection of grease pencil brushes '''

    active: 'GPencilBrush' = None
    '''Current active brush 

    :type: 'GPencilBrush'
    '''

    active_index: int = None
    '''Index of active brush 

    :type: int
    '''

    def new(self, name: str, set_active: bool = False) -> 'GPencilBrush':
        '''Add a new grease pencil brush 

        :param name: Name, Name of the brush 
        :type name: str
        :param set_active: Set Active, Set the newly created brush to the active brush 
        :type set_active: bool
        :rtype: 'GPencilBrush'
        :return:  The newly created brush 
        '''
        pass

    def remove(self, brush: 'GPencilBrush'):
        '''Remove a grease pencil brush 

        :param brush: The brush to remove 
        :type brush: 'GPencilBrush'
        '''
        pass


class GreasePencilLayers:
    '''Collection of grease pencil layers '''

    active: 'GPencilLayer' = None
    '''Active grease pencil layer 

    :type: 'GPencilLayer'
    '''

    active_index: int = None
    '''Index of active grease pencil layer 

    :type: int
    '''

    def new(self, name: str, set_active: bool = True) -> 'GPencilLayer':
        '''Add a new grease pencil layer 

        :param name: Name, Name of the layer 
        :type name: str
        :param set_active: Set Active, Set the newly created layer to the active layer 
        :type set_active: bool
        :rtype: 'GPencilLayer'
        :return:  The newly created layer 
        '''
        pass

    def remove(self, layer: 'GPencilLayer'):
        '''Remove a grease pencil layer 

        :param layer: The layer to remove 
        :type layer: 'GPencilLayer'
        '''
        pass


class GreasePencilPalettes:
    '''Collection of grease pencil palettes '''

    active: 'GPencilPalette' = None
    '''Current active palette 

    :type: 'GPencilPalette'
    '''

    active_index: int = None
    '''Index of active palette 

    :type: int
    '''

    def new(self, name: str, set_active: bool = True) -> 'GPencilPalette':
        '''Add a new grease pencil palette 

        :param name: Name, Name of the palette 
        :type name: str
        :param set_active: Set Active, Activate the newly created palette 
        :type set_active: bool
        :rtype: 'GPencilPalette'
        :return:  The newly created palette 
        '''
        pass

    def remove(self, palette: 'GPencilPalette'):
        '''Remove a grease pencil palette 

        :param palette: The palette to remove 
        :type palette: 'GPencilPalette'
        '''
        pass


class Group:
    '''Group of Object data-blocks '''

    dupli_offset: float = None
    '''Offset from the origin to use when instancing as DupliGroup 

    :type: float
    '''

    layers: bool = None
    '''Layers visible when this group is instanced as a dupli 

    :type: bool
    '''

    objects: typing.List['GroupObjects'] = None
    '''A collection of this groups objects 

    :type: typing.List['GroupObjects']
    '''

    users_dupli_group = None
    '''The dupli group this group is used in (readonly) '''


class GroupObjects:
    '''Collection of group objects '''

    def link(self, object: 'Object'):
        '''Add this object to a group 

        :param object: Object to add 
        :type object: 'Object'
        '''
        pass

    def unlink(self, object: 'Object'):
        '''Remove this object to a group 

        :param object: Object to remove 
        :type object: 'Object'
        '''
        pass


class Header:
    '''Editor header containing UI elements '''

    bl_idname: str = None
    '''If this is set, the header gets a custom ID, otherwise it takes the name of the class used to define the panel; for example, if the class name is “OBJECT_HT_hello”, and bl_idname is not set by the script, then bl_idname = “OBJECT_HT_hello” 

    :type: str
    '''

    bl_space_type: typing.Union[int, str] = None
    '''The space where the header is going to be used in 

    :type: typing.Union[int, str]
    '''

    layout: 'UILayout' = None
    '''Structure of the header in the UI 

    :type: 'UILayout'
    '''

    def draw(self, context):
        '''Draw UI elements into the header UI layout 

        '''
        pass


class HemiLamp:
    '''180 degree constant lamp '''

    pass


class Histogram:
    '''Statistical view of the levels of color in an image '''

    mode: typing.Union[int, str] = None
    '''Channels to display when drawing the histogram 

    :type: typing.Union[int, str]
    '''

    show_line: bool = None
    '''Display lines rather than filled shapes 

    :type: bool
    '''


class HookModifier:
    '''Hook modifier to modify the location of vertices '''

    center: float = None
    '''

    :type: float
    '''

    falloff_curve: 'CurveMapping' = None
    '''Custom Lamp Falloff Curve 

    :type: 'CurveMapping'
    '''

    falloff_radius: float = None
    '''If not zero, the distance from the hook where influence ends 

    :type: float
    '''

    falloff_type: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    matrix_inverse: float = None
    '''Reverse the transformation between this object and its target 

    :type: float
    '''

    object: 'Object' = None
    '''Parent Object for hook, also recalculates and clears offset 

    :type: 'Object'
    '''

    strength: float = None
    '''Relative force of the hook 

    :type: float
    '''

    subtarget: str = None
    '''Name of Parent Bone for hook (if applicable), also recalculates and clears offset 

    :type: str
    '''

    use_falloff_uniform: bool = None
    '''Compensate for non-uniform object scale 

    :type: bool
    '''

    vertex_group: str = None
    '''Name of Vertex Group which determines influence of modifier per point 

    :type: str
    '''


class HueCorrectModifier:
    '''Hue correction modifier for sequence strip '''

    curve_mapping: 'CurveMapping' = None
    '''

    :type: 'CurveMapping'
    '''


class ID:
    '''Base type for data-blocks, defining a unique name, linking from other libraries and garbage collection '''

    is_library_indirect: bool = None
    '''Is this ID block linked indirectly 

    :type: bool
    '''

    is_updated: bool = None
    '''Data-block is tagged for recalculation 

    :type: bool
    '''

    is_updated_data: bool = None
    '''Data-block data is tagged for recalculation 

    :type: bool
    '''

    library: 'Library' = None
    '''Library file the data-block is linked from 

    :type: 'Library'
    '''

    name: str = None
    '''Unique data-block ID name 

    :type: str
    '''

    preview: 'ImagePreview' = None
    '''Preview image and icon of this data-block (None if not supported for this type of data) 

    :type: 'ImagePreview'
    '''

    tag: bool = None
    '''Tools can use this to tag data for their own purposes (initial state is undefined) 

    :type: bool
    '''

    use_fake_user: bool = None
    '''Save this data-block even if it has no users 

    :type: bool
    '''

    users: int = None
    '''Number of times this data-block is referenced 

    :type: int
    '''

    def copy(self, ) -> 'ID':
        '''Create a copy of this data-block (not supported for all data-blocks) 

        :rtype: 'ID'
        :return:  New copy of the ID 
        '''
        pass

    def user_clear(self, ):
        '''This function is for advanced use only, misuse can crash blender since the user count is used to prevent data being removed when it is used. 

        '''
        pass

    def user_remap(self, new_id: 'ID'):
        '''Replace all usage in the .blend file of this ID by new given one 

        :param new_id: New ID to use 
        :type new_id: 'ID'
        '''
        pass

    def make_local(self, clear_proxy: bool = True) -> 'ID':
        '''Make this datablock local, return local one (may be a copy of the original, in case it is also indirectly used) 

        :param clear_proxy: Whether to clear proxies (the default behavior, note that if object has to be duplicated to be made local, proxies are always cleared) 
        :type clear_proxy: bool
        :rtype: 'ID'
        :return:  This ID, or the new ID if it was copied 
        '''
        pass

    def user_of_id(self, id: 'ID') -> int:
        '''Count the number of times that ID uses/references given one 

        :param id: ID to count usages 
        :type id: 'ID'
        :rtype: int
        :return:  Number of usages/references of given id by current data-block 
        '''
        pass

    def animation_data_create(self, ) -> 'AnimData':
        '''Create animation data to this ID, note that not all ID types support this 

        :rtype: 'AnimData'
        :return:  New animation data or NULL 
        '''
        pass

    def animation_data_clear(self, ):
        '''Clear animation on this this ID 

        '''
        pass

    def update_tag(self, refresh: typing.Set[typing.Union[int, str]] = {}):
        '''Tag the ID to update its display data, e.g. when calling bpy.types.Scene.update 

        :param refresh: Type of updates to perform 
        :type refresh: typing.Set[typing.Union[int, str]]
        '''
        pass


class IDMaterials:
    '''Collection of materials '''

    def append(self, material: 'Material'):
        '''Add a new material to the data-block 

        :param material: Material to add 
        :type material: 'Material'
        '''
        pass

    def pop(self, index: int = -1, update_data: bool = False) -> 'Material':
        '''Remove a material from the data-block 

        :param index: Index of material to remove 
        :type index: int
        :param update_data: Update data by re-adjusting the material slots assigned 
        :type update_data: bool
        :rtype: 'Material'
        :return:  Material to remove 
        '''
        pass

    def clear(self, update_data: bool = False):
        '''Remove all materials from the data-block 

        :param update_data: Update data by re-adjusting the material slots assigned 
        :type update_data: bool
        '''
        pass


class IKParam:
    '''Base type for IK solver parameters '''

    ik_solver: typing.Union[int, str] = None
    '''IK solver for which these parameters are defined 

    :type: typing.Union[int, str]
    '''


class IMAGE_UV_sculpt:
    def draw(self, context):
        '''

        '''
        pass


class IMAGE_UV_sculpt_curve:
    def draw(self, context):
        '''

        '''
        pass


class Image:
    '''Image data-block referencing an external or packed image '''

    alpha_mode: typing.Union[int, str] = None
    '''Representation of alpha information in the RGBA pixels 

    :type: typing.Union[int, str]
    '''

    bindcode: int = None
    '''OpenGL bindcode 

    :type: int
    '''

    channels: int = None
    '''Number of channels in pixels buffer 

    :type: int
    '''

    colorspace_settings: 'ColorManagedInputColorspaceSettings' = None
    '''Input color space settings 

    :type: 'ColorManagedInputColorspaceSettings'
    '''

    depth: int = None
    '''Image bit depth 

    :type: int
    '''

    display_aspect: float = None
    '''Display Aspect for this image, does not affect rendering 

    :type: float
    '''

    field_order: typing.Union[int, str] = None
    '''Order of video fields (select which lines are displayed first) 

    :type: typing.Union[int, str]
    '''

    file_format: typing.Union[int, str] = None
    '''Format used for re-saving this file 

    :type: typing.Union[int, str]
    '''

    filepath: str = None
    '''Image/Movie file name 

    :type: str
    '''

    filepath_raw: str = None
    '''Image/Movie file name (without data refreshing) 

    :type: str
    '''

    fps: int = None
    '''Speed of the animation in frames per second 

    :type: int
    '''

    frame_duration: int = None
    '''Duration (in frames) of the image (1 when not a video/sequence) 

    :type: int
    '''

    frame_end: int = None
    '''End frame of an animated texture 

    :type: int
    '''

    frame_start: int = None
    '''Start frame of an animated texture 

    :type: int
    '''

    generated_color: float = None
    '''Fill color for the generated image 

    :type: float
    '''

    generated_height: int = None
    '''Generated image height 

    :type: int
    '''

    generated_type: typing.Union[int, str] = None
    '''Generated image type 

    :type: typing.Union[int, str]
    '''

    generated_width: int = None
    '''Generated image width 

    :type: int
    '''

    has_data: bool = None
    '''True if the image data is loaded into memory 

    :type: bool
    '''

    is_dirty: bool = None
    '''Image has changed and is not saved 

    :type: bool
    '''

    is_float: bool = None
    '''True if this image is stored in float buffer 

    :type: bool
    '''

    is_multiview: bool = None
    '''Image has more than one view 

    :type: bool
    '''

    is_stereo_3d: bool = None
    '''Image has left and right views 

    :type: bool
    '''

    mapping: typing.Union[int, str] = None
    '''Mapping type to use for this image in the game engine 

    :type: typing.Union[int, str]
    '''

    packed_file: 'PackedFile' = None
    '''First packed file of the image 

    :type: 'PackedFile'
    '''

    packed_files: typing.List['ImagePackedFile'] = None
    '''Collection of packed images 

    :type: typing.List['ImagePackedFile']
    '''

    pixels: float = None
    '''Image pixels in floating point values 

    :type: float
    '''

    render_slots: typing.List['RenderSlots'] = None
    '''Render slots of the image 

    :type: typing.List['RenderSlots']
    '''

    resolution: float = None
    '''X/Y pixels per meter 

    :type: float
    '''

    size: int = None
    '''Width and height in pixels, zero when image data cant be loaded 

    :type: int
    '''

    source: typing.Union[int, str] = None
    '''Where the image comes from 

    :type: typing.Union[int, str]
    '''

    stereo_3d_format: 'Stereo3dFormat' = None
    '''Settings for stereo 3d 

    :type: 'Stereo3dFormat'
    '''

    tiles_x: int = None
    '''Degree of repetition in the X direction 

    :type: int
    '''

    tiles_y: int = None
    '''Degree of repetition in the Y direction 

    :type: int
    '''

    type: typing.Union[int, str] = None
    '''How to generate the image 

    :type: typing.Union[int, str]
    '''

    use_alpha: bool = None
    '''Use the alpha channel information from the image or make image fully opaque 

    :type: bool
    '''

    use_animation: bool = None
    '''Use as animated texture in the game engine 

    :type: bool
    '''

    use_clamp_x: bool = None
    '''Disable texture repeating horizontally 

    :type: bool
    '''

    use_clamp_y: bool = None
    '''Disable texture repeating vertically 

    :type: bool
    '''

    use_deinterlace: bool = None
    '''Deinterlace movie file on load 

    :type: bool
    '''

    use_fields: bool = None
    '''Use fields of the image 

    :type: bool
    '''

    use_generated_float: bool = None
    '''Generate floating point buffer 

    :type: bool
    '''

    use_multiview: bool = None
    '''Use Multiple Views (when available) 

    :type: bool
    '''

    use_tiles: bool = None
    '''Use of tilemode for faces (default shift-LMB to pick the tile for selected faces) 

    :type: bool
    '''

    use_view_as_render: bool = None
    '''Apply render part of display transformation when displaying this image on the screen 

    :type: bool
    '''

    views_format: typing.Union[int, str] = None
    '''Mode to load image views 

    :type: typing.Union[int, str]
    '''

    def save_render(self, filepath: str, scene: 'Scene' = None):
        '''Save image to a specific path using a scenes render settings 

        :param filepath: Save path 
        :type filepath: str
        :param scene: Scene to take image parameters from 
        :type scene: 'Scene'
        '''
        pass

    def save(self, ):
        '''Save image to its source path 

        '''
        pass

    def pack(self, as_png: bool = False, data: str = "", data_len: int = 0):
        '''Pack an image as embedded data into the .blend file 

        :param as_png: as_png, Pack the image as PNG (needed for generated/dirty images) 
        :type as_png: bool
        :param data: data, Raw data (bytes, exact content of the embedded file) 
        :type data: str
        :param data_len: data_len, length of given data (mandatory if data is provided) 
        :type data_len: int
        '''
        pass

    def unpack(self, method: typing.Union[int, str] = 'USE_LOCAL'):
        '''Save an image packed in the .blend file to disk 

        :param method: method, How to unpack 
        :type method: typing.Union[int, str]
        '''
        pass

    def reload(self, ):
        '''Reload the image from its source path 

        '''
        pass

    def update(self, ):
        '''Update the display image from the floating point buffer 

        '''
        pass

    def scale(self, width: int, height: int):
        '''Scale the image in pixels 

        :param width: Width 
        :type width: int
        :param height: Height 
        :type height: int
        '''
        pass

    def gl_touch(self, frame: int = 0, filter: int = 9985,
                 mag: int = 9729) -> int:
        '''Delay the image from being cleaned from the cache due inactivity 

        :param frame: Frame, Frame of image sequence or movie 
        :type frame: int
        :param filter: Filter, The texture minifying function to use if the image wasn’t loaded 
        :type filter: int
        :param mag: Magnification, The texture magnification function to use if the image wasn’t loaded 
        :type mag: int
        :rtype: int
        :return:  Error, OpenGL error value 
        '''
        pass

    def gl_load(self, frame: int = 0, filter: int = 9985,
                mag: int = 9729) -> int:
        '''Load the image into OpenGL graphics memory 

        :param frame: Frame, Frame of image sequence or movie 
        :type frame: int
        :param filter: Filter, The texture minifying function 
        :type filter: int
        :param mag: Magnification, The texture magnification function 
        :type mag: int
        :rtype: int
        :return:  Error, OpenGL error value 
        '''
        pass

    def gl_free(self, ):
        '''Free the image from OpenGL graphics memory 

        '''
        pass

    def filepath_from_user(self, image_user: 'ImageUser' = None) -> str:
        '''Return the absolute path to the filepath of an image frame specified by the image user 

        :param image_user: Image user of the image to get filepath for 
        :type image_user: 'ImageUser'
        :rtype: str
        :return:  File Path, The resulting filepath from the image and it’s user 
        '''
        pass

    def buffers_free(self, ):
        '''Free the image buffers from memory 

        '''
        pass


class ImageFormatSettings:
    '''Settings for image formats '''

    cineon_black: int = None
    '''Log conversion reference blackpoint 

    :type: int
    '''

    cineon_gamma: float = None
    '''Log conversion gamma 

    :type: float
    '''

    cineon_white: int = None
    '''Log conversion reference whitepoint 

    :type: int
    '''

    color_depth: typing.Union[int, str] = None
    '''Bit depth per channel 

    :type: typing.Union[int, str]
    '''

    color_mode: typing.Union[int, str] = None
    '''Choose BW for saving grayscale images, RGB for saving red, green and blue channels, and RGBA for saving red, green, blue and alpha channels 

    :type: typing.Union[int, str]
    '''

    compression: int = None
    '''Amount of time to determine best compression: 0 = no compression with fast file output, 100 = maximum lossless compression with slow file output 

    :type: int
    '''

    display_settings: 'ColorManagedDisplaySettings' = None
    '''Settings of device saved image would be displayed on 

    :type: 'ColorManagedDisplaySettings'
    '''

    exr_codec: typing.Union[int, str] = None
    '''Codec settings for OpenEXR 

    :type: typing.Union[int, str]
    '''

    file_format: typing.Union[int, str] = None
    '''File format to save the rendered images as 

    :type: typing.Union[int, str]
    '''

    jpeg2k_codec: typing.Union[int, str] = None
    '''Codec settings for Jpeg2000 

    :type: typing.Union[int, str]
    '''

    quality: int = None
    '''Quality for image formats that support lossy compression 

    :type: int
    '''

    stereo_3d_format: 'Stereo3dFormat' = None
    '''Settings for stereo 3d 

    :type: 'Stereo3dFormat'
    '''

    tiff_codec: typing.Union[int, str] = None
    '''Compression mode for TIFF 

    :type: typing.Union[int, str]
    '''

    use_cineon_log: bool = None
    '''Convert to logarithmic color space 

    :type: bool
    '''

    use_jpeg2k_cinema_48: bool = None
    '''Use Openjpeg Cinema Preset (48fps) 

    :type: bool
    '''

    use_jpeg2k_cinema_preset: bool = None
    '''Use Openjpeg Cinema Preset 

    :type: bool
    '''

    use_jpeg2k_ycc: bool = None
    '''Save luminance-chrominance-chrominance channels instead of RGB colors 

    :type: bool
    '''

    use_preview: bool = None
    '''When rendering animations, save JPG preview images in same directory 

    :type: bool
    '''

    use_zbuffer: bool = None
    '''Save the z-depth per pixel (32 bit unsigned int z-buffer) 

    :type: bool
    '''

    view_settings: 'ColorManagedViewSettings' = None
    '''Color management settings applied on image before saving 

    :type: 'ColorManagedViewSettings'
    '''

    views_format: typing.Union[int, str] = None
    '''Format of multiview media 

    :type: typing.Union[int, str]
    '''


class ImagePackedFile:
    filepath: str = None
    '''

    :type: str
    '''

    packed_file: 'PackedFile' = None
    '''

    :type: 'PackedFile'
    '''

    def save(self, ):
        '''Save the packed file to its filepath 

        '''
        pass


class ImagePaint:
    '''Properties of image and texture painting mode '''

    canvas: 'Image' = None
    '''Image used as canvas 

    :type: 'Image'
    '''

    clone_image: 'Image' = None
    '''Image used as clone source 

    :type: 'Image'
    '''

    dither: float = None
    '''Amount of dithering when painting on byte images 

    :type: float
    '''

    invert_stencil: bool = None
    '''Invert the stencil layer 

    :type: bool
    '''

    missing_materials: bool = None
    '''The mesh is missing materials 

    :type: bool
    '''

    missing_stencil: bool = None
    '''Image Painting does not have a stencil 

    :type: bool
    '''

    missing_texture: bool = None
    '''Image Painting does not have a texture to paint on 

    :type: bool
    '''

    missing_uvs: bool = None
    '''A UV layer is missing on the mesh 

    :type: bool
    '''

    mode: typing.Union[int, str] = None
    '''Mode of operation for projection painting 

    :type: typing.Union[int, str]
    '''

    normal_angle: int = None
    '''Paint most on faces pointing towards the view according to this angle 

    :type: int
    '''

    screen_grab_size: int = None
    '''Size to capture the image for re-projecting 

    :type: int
    '''

    seam_bleed: int = None
    '''Extend paint beyond the faces UVs to reduce seams (in pixels, slower) 

    :type: int
    '''

    stencil_color: float = None
    '''Stencil color in the viewport 

    :type: float
    '''

    stencil_image: 'Image' = None
    '''Image used as stencil 

    :type: 'Image'
    '''

    use_backface_culling: bool = None
    '''Ignore faces pointing away from the view (faster) 

    :type: bool
    '''

    use_clone_layer: bool = None
    '''Use another UV map as clone source, otherwise use the 3D cursor as the source 

    :type: bool
    '''

    use_normal_falloff: bool = None
    '''Paint most on faces pointing towards the view 

    :type: bool
    '''

    use_occlude: bool = None
    '''Only paint onto the faces directly under the brush (slower) 

    :type: bool
    '''

    use_stencil_layer: bool = None
    '''Set the mask layer from the UV map buttons 

    :type: bool
    '''

    def detect_data(self, ) -> bool:
        '''Check if required texpaint data exist 

        :rtype: bool
        '''
        pass


class ImagePreview:
    '''Preview image and icon '''

    icon_id: int = None
    '''Unique integer identifying this preview as an icon (zero means invalid) 

    :type: int
    '''

    icon_pixels: int = None
    '''Icon pixels, as bytes (always RGBA 32bits) 

    :type: int
    '''

    icon_pixels_float: float = None
    '''Icon pixels components, as floats (RGBA concatenated values) 

    :type: float
    '''

    icon_size: int = None
    '''Width and height in pixels 

    :type: int
    '''

    image_pixels: int = None
    '''Image pixels, as bytes (always RGBA 32bits) 

    :type: int
    '''

    image_pixels_float: float = None
    '''Image pixels components, as floats (RGBA concatenated values) 

    :type: float
    '''

    image_size: int = None
    '''Width and height in pixels 

    :type: int
    '''

    is_icon_custom: bool = None
    '''True if this preview icon has been modified by py script,and is no more auto-generated by Blender 

    :type: bool
    '''

    is_image_custom: bool = None
    '''True if this preview image has been modified by py script,and is no more auto-generated by Blender 

    :type: bool
    '''

    def reload(self, ):
        '''Reload the preview from its source path 

        '''
        pass


class ImageSequence:
    '''Sequence strip to load one or more images '''

    alpha_mode: typing.Union[int, str] = None
    '''Representation of alpha information in the RGBA pixels 

    :type: typing.Union[int, str]
    '''

    animation_offset_end: int = None
    '''Animation end offset (trim end) 

    :type: int
    '''

    animation_offset_start: int = None
    '''Animation start offset (trim start) 

    :type: int
    '''

    color_multiply: float = None
    '''

    :type: float
    '''

    color_saturation: float = None
    '''Adjust the intensity of the input’s color 

    :type: float
    '''

    colorspace_settings: 'ColorManagedInputColorspaceSettings' = None
    '''Input color space settings 

    :type: 'ColorManagedInputColorspaceSettings'
    '''

    crop: 'SequenceCrop' = None
    '''

    :type: 'SequenceCrop'
    '''

    directory: str = None
    '''

    :type: str
    '''

    elements: typing.List['SequenceElement'] = None
    '''

    :type: typing.List['SequenceElement']
    '''

    proxy: 'SequenceProxy' = None
    '''

    :type: 'SequenceProxy'
    '''

    stereo_3d_format: 'Stereo3dFormat' = None
    '''Settings for stereo 3d 

    :type: 'Stereo3dFormat'
    '''

    strobe: float = None
    '''Only display every nth frame 

    :type: float
    '''

    transform: 'SequenceTransform' = None
    '''

    :type: 'SequenceTransform'
    '''

    use_crop: bool = None
    '''Crop image before processing 

    :type: bool
    '''

    use_deinterlace: bool = None
    '''Remove fields from video movies 

    :type: bool
    '''

    use_flip_x: bool = None
    '''Flip on the X axis 

    :type: bool
    '''

    use_flip_y: bool = None
    '''Flip on the Y axis 

    :type: bool
    '''

    use_float: bool = None
    '''Convert input to float data 

    :type: bool
    '''

    use_multiview: bool = None
    '''Use Multiple Views (when available) 

    :type: bool
    '''

    use_proxy: bool = None
    '''Use a preview proxy and/or timecode index for this strip 

    :type: bool
    '''

    use_reverse_frames: bool = None
    '''Reverse frame order 

    :type: bool
    '''

    use_translation: bool = None
    '''Translate image before processing 

    :type: bool
    '''

    views_format: typing.Union[int, str] = None
    '''Mode to load image views 

    :type: typing.Union[int, str]
    '''


class ImageTexture:
    checker_distance: float = None
    '''Distance between checker tiles 

    :type: float
    '''

    crop_max_x: float = None
    '''Maximum X value to crop the image 

    :type: float
    '''

    crop_max_y: float = None
    '''Maximum Y value to crop the image 

    :type: float
    '''

    crop_min_x: float = None
    '''Minimum X value to crop the image 

    :type: float
    '''

    crop_min_y: float = None
    '''Minimum Y value to crop the image 

    :type: float
    '''

    extension: typing.Union[int, str] = None
    '''How the image is extrapolated past its original bounds 

    :type: typing.Union[int, str]
    '''

    filter_eccentricity: int = None
    '''Maximum eccentricity (higher gives less blur at distant/oblique angles, but is also slower) 

    :type: int
    '''

    filter_probes: int = None
    '''Maximum number of samples (higher gives less blur at distant/oblique angles, but is also slower) 

    :type: int
    '''

    filter_size: float = None
    '''Multiply the filter size used by MIP Map and Interpolation 

    :type: float
    '''

    filter_type: typing.Union[int, str] = None
    '''Texture filter to use for sampling image 

    :type: typing.Union[int, str]
    '''

    image: 'Image' = None
    '''

    :type: 'Image'
    '''

    image_user: 'ImageUser' = None
    '''Parameters defining which layer, pass and frame of the image is displayed 

    :type: 'ImageUser'
    '''

    invert_alpha: bool = None
    '''Invert all the alpha values in the image 

    :type: bool
    '''

    repeat_x: int = None
    '''Repetition multiplier in the X direction 

    :type: int
    '''

    repeat_y: int = None
    '''Repetition multiplier in the Y direction 

    :type: int
    '''

    use_alpha: bool = None
    '''Use the alpha channel information in the image 

    :type: bool
    '''

    use_calculate_alpha: bool = None
    '''Calculate an alpha channel based on RGB values in the image 

    :type: bool
    '''

    use_checker_even: bool = None
    '''Even checker tiles 

    :type: bool
    '''

    use_checker_odd: bool = None
    '''Odd checker tiles 

    :type: bool
    '''

    use_derivative_map: bool = None
    '''Use red and green as derivative values 

    :type: bool
    '''

    use_filter_size_min: bool = None
    '''Use Filter Size as a minimal filter value in pixels 

    :type: bool
    '''

    use_flip_axis: bool = None
    '''Flip the texture’s X and Y axis 

    :type: bool
    '''

    use_interpolation: bool = None
    '''Interpolate pixels using selected filter 

    :type: bool
    '''

    use_mipmap: bool = None
    '''Use auto-generated MIP maps for the image 

    :type: bool
    '''

    use_mipmap_gauss: bool = None
    '''Use Gauss filter to sample down MIP maps 

    :type: bool
    '''

    use_mirror_x: bool = None
    '''Mirror the image repetition on the X direction 

    :type: bool
    '''

    use_mirror_y: bool = None
    '''Mirror the image repetition on the Y direction 

    :type: bool
    '''

    use_normal_map: bool = None
    '''Use image RGB values for normal mapping 

    :type: bool
    '''

    users_material = None
    '''Materials that use this texture (readonly) '''

    users_object_modifier = None
    '''Object modifiers that use this texture (readonly) '''


class ImageUser:
    '''Parameters defining how an Image data-block is used by another data-block '''

    fields_per_frame: int = None
    '''Number of fields per rendered frame (2 fields is 1 image) 

    :type: int
    '''

    frame_current: int = None
    '''Current frame number in image sequence or movie 

    :type: int
    '''

    frame_duration: int = None
    '''Number of images of a movie to use 

    :type: int
    '''

    frame_offset: int = None
    '''Offset the number of the frame to use in the animation 

    :type: int
    '''

    frame_start: int = None
    '''Global starting frame of the movie/sequence, assuming first picture has a #1 

    :type: int
    '''

    multilayer_layer: int = None
    '''Layer in multilayer image 

    :type: int
    '''

    multilayer_pass: int = None
    '''Pass in multilayer image 

    :type: int
    '''

    multilayer_view: int = None
    '''View in multilayer image 

    :type: int
    '''

    use_auto_refresh: bool = None
    '''Always refresh image on frame changes 

    :type: bool
    '''

    use_cyclic: bool = None
    '''Cycle the images in the movie 

    :type: bool
    '''


class ImapaintToolCapabilities:
    '''Read-only indications of which brush operations are supported by the current image paint brush '''

    has_accumulate: bool = None
    '''

    :type: bool
    '''

    has_radius: bool = None
    '''

    :type: bool
    '''

    has_space_attenuation: bool = None
    '''

    :type: bool
    '''


class InflowFluidSettings:
    '''Fluid simulation settings for objects adding fluids in the simulation '''

    inflow_velocity: float = None
    '''Initial velocity of fluid 

    :type: float
    '''

    use: bool = None
    '''Object contributes to the fluid simulation 

    :type: bool
    '''

    use_animated_mesh: bool = None
    '''Export this mesh as an animated one (slower and enforces No Slip, only use if really necessary [e.g. armatures or parented objects], animated pos/rot/scale F-Curves do not require it) 

    :type: bool
    '''

    use_local_coords: bool = None
    '''Use local coordinates for inflow (e.g. for rotating objects) 

    :type: bool
    '''

    volume_initialization: typing.Union[int, str] = None
    '''Volume initialization type (WARNING: complex volumes might require too much memory and break simulation) 

    :type: typing.Union[int, str]
    '''


class IntProperty:
    '''RNA integer number property definition '''

    array_length: int = None
    '''Maximum length of the array, 0 means unlimited 

    :type: int
    '''

    default: int = None
    '''Default value for this number 

    :type: int
    '''

    default_array: int = None
    '''Default value for this array 

    :type: int
    '''

    hard_max: int = None
    '''Maximum value used by buttons 

    :type: int
    '''

    hard_min: int = None
    '''Minimum value used by buttons 

    :type: int
    '''

    is_array: bool = None
    '''

    :type: bool
    '''

    soft_max: int = None
    '''Maximum value used by buttons 

    :type: int
    '''

    soft_min: int = None
    '''Minimum value used by buttons 

    :type: int
    '''

    step: int = None
    '''Step size used by number buttons, for floats 1/100th of the step size 

    :type: int
    '''


class Itasc:
    '''Parameters for the iTaSC IK solver '''

    damping_epsilon: float = None
    '''Singular value under which damping is progressively applied (higher values=more stability, less reactivity - default=0.1) 

    :type: float
    '''

    damping_max: float = None
    '''Maximum damping coefficient when singular value is nearly 0 (higher values=more stability, less reactivity - default=0.5) 

    :type: float
    '''

    feedback: float = None
    '''Feedback coefficient for error correction, average response time is 1/feedback (default=20) 

    :type: float
    '''

    iterations: int = None
    '''Maximum number of iterations for convergence in case of reiteration 

    :type: int
    '''

    mode: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    precision: float = None
    '''Precision of convergence in case of reiteration 

    :type: float
    '''

    reiteration_method: typing.Union[int, str] = None
    '''Defines if the solver is allowed to reiterate (converge until precision is met) on none, first or all frames 

    :type: typing.Union[int, str]
    '''

    solver: typing.Union[int, str] = None
    '''Solving method selection: automatic damping or manual damping 

    :type: typing.Union[int, str]
    '''

    step_count: int = None
    '''Divide the frame interval into this many steps 

    :type: int
    '''

    step_max: float = None
    '''Higher bound for timestep in second in case of automatic substeps 

    :type: float
    '''

    step_min: float = None
    '''Lower bound for timestep in second in case of automatic substeps 

    :type: float
    '''

    use_auto_step: bool = None
    '''Automatically determine the optimal number of steps for best performance/accuracy trade off 

    :type: bool
    '''

    velocity_max: float = None
    '''Maximum joint velocity in rad/s (default=50) 

    :type: float
    '''


class JoystickSensor:
    '''Sensor to detect joystick events '''

    axis_direction: typing.Union[int, str] = None
    '''The direction of the axis 

    :type: typing.Union[int, str]
    '''

    axis_number: int = None
    '''Which axis pair to use, 1 is usually the main direction input 

    :type: int
    '''

    axis_threshold: int = None
    '''Precision of the axis 

    :type: int
    '''

    button_number: int = None
    '''Which button to use 

    :type: int
    '''

    event_type: typing.Union[int, str] = None
    '''The type of event this joystick sensor is triggered on 

    :type: typing.Union[int, str]
    '''

    hat_direction: typing.Union[int, str] = None
    '''Hat direction 

    :type: typing.Union[int, str]
    '''

    hat_number: int = None
    '''Which hat to use 

    :type: int
    '''

    joystick_index: int = None
    '''Which joystick to use 

    :type: int
    '''

    single_axis_number: int = None
    '''Single axis (vertical/horizontal/other) to detect 

    :type: int
    '''

    use_all_events: bool = None
    '''Triggered by all events on this joystick’s current type (axis/button/hat) 

    :type: bool
    '''


class Key:
    '''Shape keys data-block containing different shapes of geometric data-blocks '''

    animation_data: 'AnimData' = None
    '''Animation data for this data-block 

    :type: 'AnimData'
    '''

    eval_time: float = None
    '''Evaluation time for absolute shape keys 

    :type: float
    '''

    key_blocks: typing.List['ShapeKey'] = None
    '''Shape keys 

    :type: typing.List['ShapeKey']
    '''

    reference_key: 'ShapeKey' = None
    '''

    :type: 'ShapeKey'
    '''

    use_relative: bool = None
    '''Make shape keys relative, otherwise play through shapes as a sequence using the evaluation time 

    :type: bool
    '''

    user: 'ID' = None
    '''Data-block using these shape keys 

    :type: 'ID'
    '''


class KeyConfig:
    '''Input configuration, including keymaps '''

    is_user_defined: bool = None
    '''Indicates that a keyconfig was defined by the user 

    :type: bool
    '''

    keymaps: typing.List['KeyMaps'] = None
    '''Key maps configured as part of this configuration 

    :type: typing.List['KeyMaps']
    '''

    name: str = None
    '''Name of the key configuration 

    :type: str
    '''


class KeyConfigurations:
    '''Collection of KeyConfigs '''

    active: 'KeyConfig' = None
    '''Active key configuration (preset) 

    :type: 'KeyConfig'
    '''

    addon: 'KeyConfig' = None
    '''Key configuration that can be extended by add-ons, and is added to the active configuration when handling events 

    :type: 'KeyConfig'
    '''

    default: 'KeyConfig' = None
    '''Default builtin key configuration 

    :type: 'KeyConfig'
    '''

    user: 'KeyConfig' = None
    '''Final key configuration that combines keymaps from the active and add-on configurations, and can be edited by the user 

    :type: 'KeyConfig'
    '''

    def new(self, name: str) -> 'KeyConfig':
        '''new 

        :param name: Name 
        :type name: str
        :rtype: 'KeyConfig'
        :return:  Key Configuration, Added key configuration 
        '''
        pass

    def remove(self, keyconfig: 'KeyConfig'):
        '''remove 

        :param keyconfig: Key Configuration, Removed key configuration 
        :type keyconfig: 'KeyConfig'
        '''
        pass


class KeyMap:
    '''Input configuration, including keymaps '''

    is_modal: bool = None
    '''Indicates that a keymap is used for translate modal events for an operator 

    :type: bool
    '''

    is_user_modified: bool = None
    '''Keymap is defined by the user 

    :type: bool
    '''

    keymap_items: typing.List['KeyMapItems'] = None
    '''Items in the keymap, linking an operator to an input event 

    :type: typing.List['KeyMapItems']
    '''

    name: str = None
    '''Name of the key map 

    :type: str
    '''

    region_type: typing.Union[int, str] = None
    '''Optional region type keymap is associated with 

    :type: typing.Union[int, str]
    '''

    show_expanded_children: bool = None
    '''Children expanded in the user interface 

    :type: bool
    '''

    show_expanded_items: bool = None
    '''Expanded in the user interface 

    :type: bool
    '''

    space_type: typing.Union[int, str] = None
    '''Optional space type keymap is associated with 

    :type: typing.Union[int, str]
    '''

    def active(self, ) -> 'KeyMap':
        '''active 

        :rtype: 'KeyMap'
        :return:  Key Map, Active key map 
        '''
        pass

    def restore_to_default(self, ):
        '''restore_to_default 

        '''
        pass

    def restore_item_to_default(self, item: 'KeyMapItem'):
        '''restore_item_to_default 

        :param item: Item 
        :type item: 'KeyMapItem'
        '''
        pass


class KeyMapItem:
    '''Item in a Key Map '''

    active: bool = None
    '''Activate or deactivate item 

    :type: bool
    '''

    alt: bool = None
    '''Alt key pressed 

    :type: bool
    '''

    any: bool = None
    '''Any modifier keys pressed 

    :type: bool
    '''

    ctrl: bool = None
    '''Control key pressed 

    :type: bool
    '''

    id: int = None
    '''ID of the item 

    :type: int
    '''

    idname: str = None
    '''Identifier of operator to call on input event 

    :type: str
    '''

    is_user_defined: bool = None
    '''Is this keymap item user defined (doesn’t just replace a builtin item) 

    :type: bool
    '''

    is_user_modified: bool = None
    '''Is this keymap item modified by the user 

    :type: bool
    '''

    key_modifier: typing.Union[int, str] = None
    '''Regular key pressed as a modifier 

    :type: typing.Union[int, str]
    '''

    map_type: typing.Union[int, str] = None
    '''Type of event mapping 

    :type: typing.Union[int, str]
    '''

    name: str = None
    '''Name of operator (translated) to call on input event 

    :type: str
    '''

    oskey: bool = None
    '''Operating system key pressed 

    :type: bool
    '''

    properties: 'OperatorProperties' = None
    '''Properties to set when the operator is called 

    :type: 'OperatorProperties'
    '''

    propvalue: typing.Union[int, str] = None
    '''The value this event translates to in a modal keymap 

    :type: typing.Union[int, str]
    '''

    shift: bool = None
    '''Shift key pressed 

    :type: bool
    '''

    show_expanded: bool = None
    '''Show key map event and property details in the user interface 

    :type: bool
    '''

    type: typing.Union[int, str] = None
    '''Type of event 

    :type: typing.Union[int, str]
    '''

    value: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    def compare(self, item: 'KeyMapItem') -> bool:
        '''compare 

        :param item: Item 
        :type item: 'KeyMapItem'
        :rtype: bool
        :return:  Comparison result 
        '''
        pass


class KeyMapItems:
    '''Collection of keymap items '''

    def new(self,
            idname: str,
            type: typing.Union[int, str],
            value: typing.Union[int, str],
            any: bool = False,
            shift: bool = False,
            ctrl: bool = False,
            alt: bool = False,
            oskey: bool = False,
            key_modifier: typing.Union[int, str] = 'NONE',
            head: bool = False) -> 'KeyMapItem':
        '''new 

        :param idname: Operator Identifier 
        :type idname: str
        :param type: TypeNONE .LEFTMOUSE Left Mouse, LMB.MIDDLEMOUSE Middle Mouse, MMB.RIGHTMOUSE Right Mouse, RMB.BUTTON4MOUSE Button4 Mouse, MB4.BUTTON5MOUSE Button5 Mouse, MB5.BUTTON6MOUSE Button6 Mouse, MB6.BUTTON7MOUSE Button7 Mouse, MB7.ACTIONMOUSE Action Mouse, MBA.SELECTMOUSE Select Mouse, MBS.PEN Pen.ERASER Eraser.MOUSEMOVE Mouse Move, MsMov.INBETWEEN_MOUSEMOVE In-between Move, MsSubMov.TRACKPADPAN Mouse/Trackpad Pan, MsPan.TRACKPADZOOM Mouse/Trackpad Zoom, MsZoom.MOUSEROTATE Mouse/Trackpad Rotate, MsRot.WHEELUPMOUSE Wheel Up, WhUp.WHEELDOWNMOUSE Wheel Down, WhDown.WHEELINMOUSE Wheel In, WhIn.WHEELOUTMOUSE Wheel Out, WhOut.EVT_TWEAK_L Tweak Left, TwkL.EVT_TWEAK_M Tweak Middle, TwkM.EVT_TWEAK_R Tweak Right, TwkR.EVT_TWEAK_A Tweak Action, TwkA.EVT_TWEAK_S Tweak Select, TwkS.A A.B B.C C.D D.E E.F F.G G.H H.I I.J J.K K.L L.M M.N N.O O.P P.Q Q.R R.S S.T T.U U.V V.W W.X X.Y Y.Z Z.ZERO 0.ONE 1.TWO 2.THREE 3.FOUR 4.FIVE 5.SIX 6.SEVEN 7.EIGHT 8.NINE 9.LEFT_CTRL Left Ctrl, CtrlL.LEFT_ALT Left Alt, AltL.LEFT_SHIFT Left Shift, ShiftL.RIGHT_ALT Right Alt, AltR.RIGHT_CTRL Right Ctrl, CtrlR.RIGHT_SHIFT Right Shift, ShiftR.OSKEY OS Key, Cmd.GRLESS Grless.ESC Esc.TAB Tab.RET Return, Enter.SPACE Spacebar, Space.LINE_FEED Line Feed.BACK_SPACE Back Space, BkSpace.DEL Delete, Del.SEMI_COLON ;.PERIOD ..COMMA ,.QUOTE “.ACCENT_GRAVE `.MINUS -.PLUS +.SLASH /.BACK_SLASH .EQUAL =.LEFT_BRACKET [.RIGHT_BRACKET ].LEFT_ARROW Left Arrow, ←.DOWN_ARROW Down Arrow, ↓.RIGHT_ARROW Right Arrow, →.UP_ARROW Up Arrow, ↑.NUMPAD_2 Numpad 2, Pad2.NUMPAD_4 Numpad 4, Pad4.NUMPAD_6 Numpad 6, Pad6.NUMPAD_8 Numpad 8, Pad8.NUMPAD_1 Numpad 1, Pad1.NUMPAD_3 Numpad 3, Pad3.NUMPAD_5 Numpad 5, Pad5.NUMPAD_7 Numpad 7, Pad7.NUMPAD_9 Numpad 9, Pad9.NUMPAD_PERIOD Numpad ., Pad..NUMPAD_SLASH Numpad /, Pad/.NUMPAD_ASTERIX Numpad *, Pad*.NUMPAD_0 Numpad 0, Pad0.NUMPAD_MINUS Numpad -, Pad-.NUMPAD_ENTER Numpad Enter, PadEnter.NUMPAD_PLUS Numpad +, Pad+.F1 F1.F2 F2.F3 F3.F4 F4.F5 F5.F6 F6.F7 F7.F8 F8.F9 F9.F10 F10.F11 F11.F12 F12.F13 F13.F14 F14.F15 F15.F16 F16.F17 F17.F18 F18.F19 F19.PAUSE Pause.INSERT Insert, Ins.HOME Home.PAGE_UP Page Up, PgUp.PAGE_DOWN Page Down, PgDown.END End.MEDIA_PLAY Media Play/Pause, >/||.MEDIA_STOP Media Stop, Stop.MEDIA_FIRST Media First, |<<.MEDIA_LAST Media Last, >>|.TEXTINPUT Text Input, TxtIn.WINDOW_DEACTIVATE Window Deactivate.TIMER Timer, Tmr.TIMER0 Timer 0, Tmr0.TIMER1 Timer 1, Tmr1.TIMER2 Timer 2, Tmr2.TIMER_JOBS Timer Jobs, TmrJob.TIMER_AUTOSAVE Timer Autosave, TmrSave.TIMER_REPORT Timer Report, TmrReport.TIMERREGION Timer Region, TmrReg.NDOF_MOTION NDOF Motion, NdofMov.NDOF_BUTTON_MENU NDOF Menu, NdofMenu.NDOF_BUTTON_FIT NDOF Fit, NdofFit.NDOF_BUTTON_TOP NDOF Top, Ndof↑.NDOF_BUTTON_BOTTOM NDOF Bottom, Ndof↓.NDOF_BUTTON_LEFT NDOF Left, Ndof←.NDOF_BUTTON_RIGHT NDOF Right, Ndof→.NDOF_BUTTON_FRONT NDOF Front, NdofFront.NDOF_BUTTON_BACK NDOF Back, NdofBack.NDOF_BUTTON_ISO1 NDOF Isometric 1, NdofIso1.NDOF_BUTTON_ISO2 NDOF Isometric 2, NdofIso2.NDOF_BUTTON_ROLL_CW NDOF Roll CW, NdofRCW.NDOF_BUTTON_ROLL_CCW NDOF Roll CCW, NdofRCCW.NDOF_BUTTON_SPIN_CW NDOF Spin CW, NdofSCW.NDOF_BUTTON_SPIN_CCW NDOF Spin CCW, NdofSCCW.NDOF_BUTTON_TILT_CW NDOF Tilt CW, NdofTCW.NDOF_BUTTON_TILT_CCW NDOF Tilt CCW, NdofTCCW.NDOF_BUTTON_ROTATE NDOF Rotate, NdofRot.NDOF_BUTTON_PANZOOM NDOF Pan/Zoom, NdofPanZoom.NDOF_BUTTON_DOMINANT NDOF Dominant, NdofDom.NDOF_BUTTON_PLUS NDOF Plus, Ndof+.NDOF_BUTTON_MINUS NDOF Minus, Ndof-.NDOF_BUTTON_ESC NDOF Esc, NdofEsc.NDOF_BUTTON_ALT NDOF Alt, NdofAlt.NDOF_BUTTON_SHIFT NDOF Shift, NdofShift.NDOF_BUTTON_CTRL NDOF Ctrl, NdofCtrl.NDOF_BUTTON_1 NDOF Button 1, NdofB1.NDOF_BUTTON_2 NDOF Button 2, NdofB2.NDOF_BUTTON_3 NDOF Button 3, NdofB3.NDOF_BUTTON_4 NDOF Button 4, NdofB4.NDOF_BUTTON_5 NDOF Button 5, NdofB5.NDOF_BUTTON_6 NDOF Button 6, NdofB6.NDOF_BUTTON_7 NDOF Button 7, NdofB7.NDOF_BUTTON_8 NDOF Button 8, NdofB8.NDOF_BUTTON_9 NDOF Button 9, NdofB9.NDOF_BUTTON_10 NDOF Button 10, NdofB10.NDOF_BUTTON_A NDOF Button A, NdofBA.NDOF_BUTTON_B NDOF Button B, NdofBB.NDOF_BUTTON_C NDOF Button C, NdofBC. 
        :type type: typing.Union[int, str]
        :param value: Value 
        :type value: typing.Union[int, str]
        :param any: Any 
        :type any: bool
        :param shift: Shift 
        :type shift: bool
        :param ctrl: Ctrl 
        :type ctrl: bool
        :param alt: Alt 
        :type alt: bool
        :param oskey: OS Key 
        :type oskey: bool
        :param key_modifier: Key ModifierNONE .LEFTMOUSE Left Mouse, LMB.MIDDLEMOUSE Middle Mouse, MMB.RIGHTMOUSE Right Mouse, RMB.BUTTON4MOUSE Button4 Mouse, MB4.BUTTON5MOUSE Button5 Mouse, MB5.BUTTON6MOUSE Button6 Mouse, MB6.BUTTON7MOUSE Button7 Mouse, MB7.ACTIONMOUSE Action Mouse, MBA.SELECTMOUSE Select Mouse, MBS.PEN Pen.ERASER Eraser.MOUSEMOVE Mouse Move, MsMov.INBETWEEN_MOUSEMOVE In-between Move, MsSubMov.TRACKPADPAN Mouse/Trackpad Pan, MsPan.TRACKPADZOOM Mouse/Trackpad Zoom, MsZoom.MOUSEROTATE Mouse/Trackpad Rotate, MsRot.WHEELUPMOUSE Wheel Up, WhUp.WHEELDOWNMOUSE Wheel Down, WhDown.WHEELINMOUSE Wheel In, WhIn.WHEELOUTMOUSE Wheel Out, WhOut.EVT_TWEAK_L Tweak Left, TwkL.EVT_TWEAK_M Tweak Middle, TwkM.EVT_TWEAK_R Tweak Right, TwkR.EVT_TWEAK_A Tweak Action, TwkA.EVT_TWEAK_S Tweak Select, TwkS.A A.B B.C C.D D.E E.F F.G G.H H.I I.J J.K K.L L.M M.N N.O O.P P.Q Q.R R.S S.T T.U U.V V.W W.X X.Y Y.Z Z.ZERO 0.ONE 1.TWO 2.THREE 3.FOUR 4.FIVE 5.SIX 6.SEVEN 7.EIGHT 8.NINE 9.LEFT_CTRL Left Ctrl, CtrlL.LEFT_ALT Left Alt, AltL.LEFT_SHIFT Left Shift, ShiftL.RIGHT_ALT Right Alt, AltR.RIGHT_CTRL Right Ctrl, CtrlR.RIGHT_SHIFT Right Shift, ShiftR.OSKEY OS Key, Cmd.GRLESS Grless.ESC Esc.TAB Tab.RET Return, Enter.SPACE Spacebar, Space.LINE_FEED Line Feed.BACK_SPACE Back Space, BkSpace.DEL Delete, Del.SEMI_COLON ;.PERIOD ..COMMA ,.QUOTE “.ACCENT_GRAVE `.MINUS -.PLUS +.SLASH /.BACK_SLASH .EQUAL =.LEFT_BRACKET [.RIGHT_BRACKET ].LEFT_ARROW Left Arrow, ←.DOWN_ARROW Down Arrow, ↓.RIGHT_ARROW Right Arrow, →.UP_ARROW Up Arrow, ↑.NUMPAD_2 Numpad 2, Pad2.NUMPAD_4 Numpad 4, Pad4.NUMPAD_6 Numpad 6, Pad6.NUMPAD_8 Numpad 8, Pad8.NUMPAD_1 Numpad 1, Pad1.NUMPAD_3 Numpad 3, Pad3.NUMPAD_5 Numpad 5, Pad5.NUMPAD_7 Numpad 7, Pad7.NUMPAD_9 Numpad 9, Pad9.NUMPAD_PERIOD Numpad ., Pad..NUMPAD_SLASH Numpad /, Pad/.NUMPAD_ASTERIX Numpad *, Pad*.NUMPAD_0 Numpad 0, Pad0.NUMPAD_MINUS Numpad -, Pad-.NUMPAD_ENTER Numpad Enter, PadEnter.NUMPAD_PLUS Numpad +, Pad+.F1 F1.F2 F2.F3 F3.F4 F4.F5 F5.F6 F6.F7 F7.F8 F8.F9 F9.F10 F10.F11 F11.F12 F12.F13 F13.F14 F14.F15 F15.F16 F16.F17 F17.F18 F18.F19 F19.PAUSE Pause.INSERT Insert, Ins.HOME Home.PAGE_UP Page Up, PgUp.PAGE_DOWN Page Down, PgDown.END End.MEDIA_PLAY Media Play/Pause, >/||.MEDIA_STOP Media Stop, Stop.MEDIA_FIRST Media First, |<<.MEDIA_LAST Media Last, >>|.TEXTINPUT Text Input, TxtIn.WINDOW_DEACTIVATE Window Deactivate.TIMER Timer, Tmr.TIMER0 Timer 0, Tmr0.TIMER1 Timer 1, Tmr1.TIMER2 Timer 2, Tmr2.TIMER_JOBS Timer Jobs, TmrJob.TIMER_AUTOSAVE Timer Autosave, TmrSave.TIMER_REPORT Timer Report, TmrReport.TIMERREGION Timer Region, TmrReg.NDOF_MOTION NDOF Motion, NdofMov.NDOF_BUTTON_MENU NDOF Menu, NdofMenu.NDOF_BUTTON_FIT NDOF Fit, NdofFit.NDOF_BUTTON_TOP NDOF Top, Ndof↑.NDOF_BUTTON_BOTTOM NDOF Bottom, Ndof↓.NDOF_BUTTON_LEFT NDOF Left, Ndof←.NDOF_BUTTON_RIGHT NDOF Right, Ndof→.NDOF_BUTTON_FRONT NDOF Front, NdofFront.NDOF_BUTTON_BACK NDOF Back, NdofBack.NDOF_BUTTON_ISO1 NDOF Isometric 1, NdofIso1.NDOF_BUTTON_ISO2 NDOF Isometric 2, NdofIso2.NDOF_BUTTON_ROLL_CW NDOF Roll CW, NdofRCW.NDOF_BUTTON_ROLL_CCW NDOF Roll CCW, NdofRCCW.NDOF_BUTTON_SPIN_CW NDOF Spin CW, NdofSCW.NDOF_BUTTON_SPIN_CCW NDOF Spin CCW, NdofSCCW.NDOF_BUTTON_TILT_CW NDOF Tilt CW, NdofTCW.NDOF_BUTTON_TILT_CCW NDOF Tilt CCW, NdofTCCW.NDOF_BUTTON_ROTATE NDOF Rotate, NdofRot.NDOF_BUTTON_PANZOOM NDOF Pan/Zoom, NdofPanZoom.NDOF_BUTTON_DOMINANT NDOF Dominant, NdofDom.NDOF_BUTTON_PLUS NDOF Plus, Ndof+.NDOF_BUTTON_MINUS NDOF Minus, Ndof-.NDOF_BUTTON_ESC NDOF Esc, NdofEsc.NDOF_BUTTON_ALT NDOF Alt, NdofAlt.NDOF_BUTTON_SHIFT NDOF Shift, NdofShift.NDOF_BUTTON_CTRL NDOF Ctrl, NdofCtrl.NDOF_BUTTON_1 NDOF Button 1, NdofB1.NDOF_BUTTON_2 NDOF Button 2, NdofB2.NDOF_BUTTON_3 NDOF Button 3, NdofB3.NDOF_BUTTON_4 NDOF Button 4, NdofB4.NDOF_BUTTON_5 NDOF Button 5, NdofB5.NDOF_BUTTON_6 NDOF Button 6, NdofB6.NDOF_BUTTON_7 NDOF Button 7, NdofB7.NDOF_BUTTON_8 NDOF Button 8, NdofB8.NDOF_BUTTON_9 NDOF Button 9, NdofB9.NDOF_BUTTON_10 NDOF Button 10, NdofB10.NDOF_BUTTON_A NDOF Button A, NdofBA.NDOF_BUTTON_B NDOF Button B, NdofBB.NDOF_BUTTON_C NDOF Button C, NdofBC. 
        :type key_modifier: typing.Union[int, str]
        :param head: At Head, Force item to be added at start (not end) of key map so that it doesn’t get blocked by an existing key map item 
        :type head: bool
        :rtype: 'KeyMapItem'
        :return:  Item, Added key map item 
        '''
        pass

    def new_modal(
            self,
            propvalue: str,
            type: typing.Union[int, str],
            value: typing.Union[int, str],
            any: bool = False,
            shift: bool = False,
            ctrl: bool = False,
            alt: bool = False,
            oskey: bool = False,
            key_modifier: typing.Union[int, str] = 'NONE') -> 'KeyMapItem':
        '''new_modal 

        :param propvalue: Property Value 
        :type propvalue: str
        :param type: TypeNONE .LEFTMOUSE Left Mouse, LMB.MIDDLEMOUSE Middle Mouse, MMB.RIGHTMOUSE Right Mouse, RMB.BUTTON4MOUSE Button4 Mouse, MB4.BUTTON5MOUSE Button5 Mouse, MB5.BUTTON6MOUSE Button6 Mouse, MB6.BUTTON7MOUSE Button7 Mouse, MB7.ACTIONMOUSE Action Mouse, MBA.SELECTMOUSE Select Mouse, MBS.PEN Pen.ERASER Eraser.MOUSEMOVE Mouse Move, MsMov.INBETWEEN_MOUSEMOVE In-between Move, MsSubMov.TRACKPADPAN Mouse/Trackpad Pan, MsPan.TRACKPADZOOM Mouse/Trackpad Zoom, MsZoom.MOUSEROTATE Mouse/Trackpad Rotate, MsRot.WHEELUPMOUSE Wheel Up, WhUp.WHEELDOWNMOUSE Wheel Down, WhDown.WHEELINMOUSE Wheel In, WhIn.WHEELOUTMOUSE Wheel Out, WhOut.EVT_TWEAK_L Tweak Left, TwkL.EVT_TWEAK_M Tweak Middle, TwkM.EVT_TWEAK_R Tweak Right, TwkR.EVT_TWEAK_A Tweak Action, TwkA.EVT_TWEAK_S Tweak Select, TwkS.A A.B B.C C.D D.E E.F F.G G.H H.I I.J J.K K.L L.M M.N N.O O.P P.Q Q.R R.S S.T T.U U.V V.W W.X X.Y Y.Z Z.ZERO 0.ONE 1.TWO 2.THREE 3.FOUR 4.FIVE 5.SIX 6.SEVEN 7.EIGHT 8.NINE 9.LEFT_CTRL Left Ctrl, CtrlL.LEFT_ALT Left Alt, AltL.LEFT_SHIFT Left Shift, ShiftL.RIGHT_ALT Right Alt, AltR.RIGHT_CTRL Right Ctrl, CtrlR.RIGHT_SHIFT Right Shift, ShiftR.OSKEY OS Key, Cmd.GRLESS Grless.ESC Esc.TAB Tab.RET Return, Enter.SPACE Spacebar, Space.LINE_FEED Line Feed.BACK_SPACE Back Space, BkSpace.DEL Delete, Del.SEMI_COLON ;.PERIOD ..COMMA ,.QUOTE “.ACCENT_GRAVE `.MINUS -.PLUS +.SLASH /.BACK_SLASH .EQUAL =.LEFT_BRACKET [.RIGHT_BRACKET ].LEFT_ARROW Left Arrow, ←.DOWN_ARROW Down Arrow, ↓.RIGHT_ARROW Right Arrow, →.UP_ARROW Up Arrow, ↑.NUMPAD_2 Numpad 2, Pad2.NUMPAD_4 Numpad 4, Pad4.NUMPAD_6 Numpad 6, Pad6.NUMPAD_8 Numpad 8, Pad8.NUMPAD_1 Numpad 1, Pad1.NUMPAD_3 Numpad 3, Pad3.NUMPAD_5 Numpad 5, Pad5.NUMPAD_7 Numpad 7, Pad7.NUMPAD_9 Numpad 9, Pad9.NUMPAD_PERIOD Numpad ., Pad..NUMPAD_SLASH Numpad /, Pad/.NUMPAD_ASTERIX Numpad *, Pad*.NUMPAD_0 Numpad 0, Pad0.NUMPAD_MINUS Numpad -, Pad-.NUMPAD_ENTER Numpad Enter, PadEnter.NUMPAD_PLUS Numpad +, Pad+.F1 F1.F2 F2.F3 F3.F4 F4.F5 F5.F6 F6.F7 F7.F8 F8.F9 F9.F10 F10.F11 F11.F12 F12.F13 F13.F14 F14.F15 F15.F16 F16.F17 F17.F18 F18.F19 F19.PAUSE Pause.INSERT Insert, Ins.HOME Home.PAGE_UP Page Up, PgUp.PAGE_DOWN Page Down, PgDown.END End.MEDIA_PLAY Media Play/Pause, >/||.MEDIA_STOP Media Stop, Stop.MEDIA_FIRST Media First, |<<.MEDIA_LAST Media Last, >>|.TEXTINPUT Text Input, TxtIn.WINDOW_DEACTIVATE Window Deactivate.TIMER Timer, Tmr.TIMER0 Timer 0, Tmr0.TIMER1 Timer 1, Tmr1.TIMER2 Timer 2, Tmr2.TIMER_JOBS Timer Jobs, TmrJob.TIMER_AUTOSAVE Timer Autosave, TmrSave.TIMER_REPORT Timer Report, TmrReport.TIMERREGION Timer Region, TmrReg.NDOF_MOTION NDOF Motion, NdofMov.NDOF_BUTTON_MENU NDOF Menu, NdofMenu.NDOF_BUTTON_FIT NDOF Fit, NdofFit.NDOF_BUTTON_TOP NDOF Top, Ndof↑.NDOF_BUTTON_BOTTOM NDOF Bottom, Ndof↓.NDOF_BUTTON_LEFT NDOF Left, Ndof←.NDOF_BUTTON_RIGHT NDOF Right, Ndof→.NDOF_BUTTON_FRONT NDOF Front, NdofFront.NDOF_BUTTON_BACK NDOF Back, NdofBack.NDOF_BUTTON_ISO1 NDOF Isometric 1, NdofIso1.NDOF_BUTTON_ISO2 NDOF Isometric 2, NdofIso2.NDOF_BUTTON_ROLL_CW NDOF Roll CW, NdofRCW.NDOF_BUTTON_ROLL_CCW NDOF Roll CCW, NdofRCCW.NDOF_BUTTON_SPIN_CW NDOF Spin CW, NdofSCW.NDOF_BUTTON_SPIN_CCW NDOF Spin CCW, NdofSCCW.NDOF_BUTTON_TILT_CW NDOF Tilt CW, NdofTCW.NDOF_BUTTON_TILT_CCW NDOF Tilt CCW, NdofTCCW.NDOF_BUTTON_ROTATE NDOF Rotate, NdofRot.NDOF_BUTTON_PANZOOM NDOF Pan/Zoom, NdofPanZoom.NDOF_BUTTON_DOMINANT NDOF Dominant, NdofDom.NDOF_BUTTON_PLUS NDOF Plus, Ndof+.NDOF_BUTTON_MINUS NDOF Minus, Ndof-.NDOF_BUTTON_ESC NDOF Esc, NdofEsc.NDOF_BUTTON_ALT NDOF Alt, NdofAlt.NDOF_BUTTON_SHIFT NDOF Shift, NdofShift.NDOF_BUTTON_CTRL NDOF Ctrl, NdofCtrl.NDOF_BUTTON_1 NDOF Button 1, NdofB1.NDOF_BUTTON_2 NDOF Button 2, NdofB2.NDOF_BUTTON_3 NDOF Button 3, NdofB3.NDOF_BUTTON_4 NDOF Button 4, NdofB4.NDOF_BUTTON_5 NDOF Button 5, NdofB5.NDOF_BUTTON_6 NDOF Button 6, NdofB6.NDOF_BUTTON_7 NDOF Button 7, NdofB7.NDOF_BUTTON_8 NDOF Button 8, NdofB8.NDOF_BUTTON_9 NDOF Button 9, NdofB9.NDOF_BUTTON_10 NDOF Button 10, NdofB10.NDOF_BUTTON_A NDOF Button A, NdofBA.NDOF_BUTTON_B NDOF Button B, NdofBB.NDOF_BUTTON_C NDOF Button C, NdofBC. 
        :type type: typing.Union[int, str]
        :param value: Value 
        :type value: typing.Union[int, str]
        :param any: Any 
        :type any: bool
        :param shift: Shift 
        :type shift: bool
        :param ctrl: Ctrl 
        :type ctrl: bool
        :param alt: Alt 
        :type alt: bool
        :param oskey: OS Key 
        :type oskey: bool
        :param key_modifier: Key ModifierNONE .LEFTMOUSE Left Mouse, LMB.MIDDLEMOUSE Middle Mouse, MMB.RIGHTMOUSE Right Mouse, RMB.BUTTON4MOUSE Button4 Mouse, MB4.BUTTON5MOUSE Button5 Mouse, MB5.BUTTON6MOUSE Button6 Mouse, MB6.BUTTON7MOUSE Button7 Mouse, MB7.ACTIONMOUSE Action Mouse, MBA.SELECTMOUSE Select Mouse, MBS.PEN Pen.ERASER Eraser.MOUSEMOVE Mouse Move, MsMov.INBETWEEN_MOUSEMOVE In-between Move, MsSubMov.TRACKPADPAN Mouse/Trackpad Pan, MsPan.TRACKPADZOOM Mouse/Trackpad Zoom, MsZoom.MOUSEROTATE Mouse/Trackpad Rotate, MsRot.WHEELUPMOUSE Wheel Up, WhUp.WHEELDOWNMOUSE Wheel Down, WhDown.WHEELINMOUSE Wheel In, WhIn.WHEELOUTMOUSE Wheel Out, WhOut.EVT_TWEAK_L Tweak Left, TwkL.EVT_TWEAK_M Tweak Middle, TwkM.EVT_TWEAK_R Tweak Right, TwkR.EVT_TWEAK_A Tweak Action, TwkA.EVT_TWEAK_S Tweak Select, TwkS.A A.B B.C C.D D.E E.F F.G G.H H.I I.J J.K K.L L.M M.N N.O O.P P.Q Q.R R.S S.T T.U U.V V.W W.X X.Y Y.Z Z.ZERO 0.ONE 1.TWO 2.THREE 3.FOUR 4.FIVE 5.SIX 6.SEVEN 7.EIGHT 8.NINE 9.LEFT_CTRL Left Ctrl, CtrlL.LEFT_ALT Left Alt, AltL.LEFT_SHIFT Left Shift, ShiftL.RIGHT_ALT Right Alt, AltR.RIGHT_CTRL Right Ctrl, CtrlR.RIGHT_SHIFT Right Shift, ShiftR.OSKEY OS Key, Cmd.GRLESS Grless.ESC Esc.TAB Tab.RET Return, Enter.SPACE Spacebar, Space.LINE_FEED Line Feed.BACK_SPACE Back Space, BkSpace.DEL Delete, Del.SEMI_COLON ;.PERIOD ..COMMA ,.QUOTE “.ACCENT_GRAVE `.MINUS -.PLUS +.SLASH /.BACK_SLASH .EQUAL =.LEFT_BRACKET [.RIGHT_BRACKET ].LEFT_ARROW Left Arrow, ←.DOWN_ARROW Down Arrow, ↓.RIGHT_ARROW Right Arrow, →.UP_ARROW Up Arrow, ↑.NUMPAD_2 Numpad 2, Pad2.NUMPAD_4 Numpad 4, Pad4.NUMPAD_6 Numpad 6, Pad6.NUMPAD_8 Numpad 8, Pad8.NUMPAD_1 Numpad 1, Pad1.NUMPAD_3 Numpad 3, Pad3.NUMPAD_5 Numpad 5, Pad5.NUMPAD_7 Numpad 7, Pad7.NUMPAD_9 Numpad 9, Pad9.NUMPAD_PERIOD Numpad ., Pad..NUMPAD_SLASH Numpad /, Pad/.NUMPAD_ASTERIX Numpad *, Pad*.NUMPAD_0 Numpad 0, Pad0.NUMPAD_MINUS Numpad -, Pad-.NUMPAD_ENTER Numpad Enter, PadEnter.NUMPAD_PLUS Numpad +, Pad+.F1 F1.F2 F2.F3 F3.F4 F4.F5 F5.F6 F6.F7 F7.F8 F8.F9 F9.F10 F10.F11 F11.F12 F12.F13 F13.F14 F14.F15 F15.F16 F16.F17 F17.F18 F18.F19 F19.PAUSE Pause.INSERT Insert, Ins.HOME Home.PAGE_UP Page Up, PgUp.PAGE_DOWN Page Down, PgDown.END End.MEDIA_PLAY Media Play/Pause, >/||.MEDIA_STOP Media Stop, Stop.MEDIA_FIRST Media First, |<<.MEDIA_LAST Media Last, >>|.TEXTINPUT Text Input, TxtIn.WINDOW_DEACTIVATE Window Deactivate.TIMER Timer, Tmr.TIMER0 Timer 0, Tmr0.TIMER1 Timer 1, Tmr1.TIMER2 Timer 2, Tmr2.TIMER_JOBS Timer Jobs, TmrJob.TIMER_AUTOSAVE Timer Autosave, TmrSave.TIMER_REPORT Timer Report, TmrReport.TIMERREGION Timer Region, TmrReg.NDOF_MOTION NDOF Motion, NdofMov.NDOF_BUTTON_MENU NDOF Menu, NdofMenu.NDOF_BUTTON_FIT NDOF Fit, NdofFit.NDOF_BUTTON_TOP NDOF Top, Ndof↑.NDOF_BUTTON_BOTTOM NDOF Bottom, Ndof↓.NDOF_BUTTON_LEFT NDOF Left, Ndof←.NDOF_BUTTON_RIGHT NDOF Right, Ndof→.NDOF_BUTTON_FRONT NDOF Front, NdofFront.NDOF_BUTTON_BACK NDOF Back, NdofBack.NDOF_BUTTON_ISO1 NDOF Isometric 1, NdofIso1.NDOF_BUTTON_ISO2 NDOF Isometric 2, NdofIso2.NDOF_BUTTON_ROLL_CW NDOF Roll CW, NdofRCW.NDOF_BUTTON_ROLL_CCW NDOF Roll CCW, NdofRCCW.NDOF_BUTTON_SPIN_CW NDOF Spin CW, NdofSCW.NDOF_BUTTON_SPIN_CCW NDOF Spin CCW, NdofSCCW.NDOF_BUTTON_TILT_CW NDOF Tilt CW, NdofTCW.NDOF_BUTTON_TILT_CCW NDOF Tilt CCW, NdofTCCW.NDOF_BUTTON_ROTATE NDOF Rotate, NdofRot.NDOF_BUTTON_PANZOOM NDOF Pan/Zoom, NdofPanZoom.NDOF_BUTTON_DOMINANT NDOF Dominant, NdofDom.NDOF_BUTTON_PLUS NDOF Plus, Ndof+.NDOF_BUTTON_MINUS NDOF Minus, Ndof-.NDOF_BUTTON_ESC NDOF Esc, NdofEsc.NDOF_BUTTON_ALT NDOF Alt, NdofAlt.NDOF_BUTTON_SHIFT NDOF Shift, NdofShift.NDOF_BUTTON_CTRL NDOF Ctrl, NdofCtrl.NDOF_BUTTON_1 NDOF Button 1, NdofB1.NDOF_BUTTON_2 NDOF Button 2, NdofB2.NDOF_BUTTON_3 NDOF Button 3, NdofB3.NDOF_BUTTON_4 NDOF Button 4, NdofB4.NDOF_BUTTON_5 NDOF Button 5, NdofB5.NDOF_BUTTON_6 NDOF Button 6, NdofB6.NDOF_BUTTON_7 NDOF Button 7, NdofB7.NDOF_BUTTON_8 NDOF Button 8, NdofB8.NDOF_BUTTON_9 NDOF Button 9, NdofB9.NDOF_BUTTON_10 NDOF Button 10, NdofB10.NDOF_BUTTON_A NDOF Button A, NdofBA.NDOF_BUTTON_B NDOF Button B, NdofBB.NDOF_BUTTON_C NDOF Button C, NdofBC. 
        :type key_modifier: typing.Union[int, str]
        :rtype: 'KeyMapItem'
        :return:  Item, Added key map item 
        '''
        pass

    def remove(self, item: 'KeyMapItem'):
        '''remove 

        :param item: Item 
        :type item: 'KeyMapItem'
        '''
        pass

    def from_id(self, id: int) -> 'KeyMapItem':
        '''from_id 

        :param id: id, ID of the item 
        :type id: int
        :rtype: 'KeyMapItem'
        :return:  Item 
        '''
        pass


class KeyMaps:
    '''Collection of keymaps '''

    def new(self,
            name: str,
            space_type: typing.Union[int, str] = 'EMPTY',
            region_type: typing.Union[int, str] = 'WINDOW',
            modal: bool = False) -> 'KeyMap':
        '''new 

        :param name: Name 
        :type name: str
        :param space_type: Space TypeEMPTY Empty.VIEW_3D 3D View, 3D viewport.TIMELINE Timeline, Timeline and playback controls.GRAPH_EDITOR Graph Editor, Edit drivers and keyframe interpolation.DOPESHEET_EDITOR Dope Sheet, Adjust timing of keyframes.NLA_EDITOR NLA Editor, Combine and layer Actions.IMAGE_EDITOR UV/Image Editor, View and edit images and UV Maps.CLIP_EDITOR Movie Clip Editor, Motion tracking tools.SEQUENCE_EDITOR Video Sequence Editor, Video editing tools.NODE_EDITOR Node Editor, Editor for node-based shading and compositing tools.TEXT_EDITOR Text Editor, Edit scripts and in-file documentation.LOGIC_EDITOR Logic Editor, Game logic editing.PROPERTIES Properties, Edit properties of active object and related data-blocks.OUTLINER Outliner, Overview of scene graph and all available data-blocks.USER_PREFERENCES User Preferences, Edit persistent configuration settings.INFO Info, Main menu bar and list of error messages (drag down to expand and display).FILE_BROWSER File Browser, Browse for files and assets.CONSOLE Python Console, Interactive programmatic console for advanced editing and script development. 
        :type space_type: typing.Union[int, str]
        :param region_type: Region Type 
        :type region_type: typing.Union[int, str]
        :param modal: Modal 
        :type modal: bool
        :rtype: 'KeyMap'
        :return:  Key Map, Added key map 
        '''
        pass

    def remove(self, keymap: 'KeyMap'):
        '''remove 

        :param keymap: Key Map, Removed key map 
        :type keymap: 'KeyMap'
        '''
        pass

    def find(self,
             name: str,
             space_type: typing.Union[int, str] = 'EMPTY',
             region_type: typing.Union[int, str] = 'WINDOW') -> 'KeyMap':
        '''find 

        :param name: Name 
        :type name: str
        :param space_type: Space TypeEMPTY Empty.VIEW_3D 3D View, 3D viewport.TIMELINE Timeline, Timeline and playback controls.GRAPH_EDITOR Graph Editor, Edit drivers and keyframe interpolation.DOPESHEET_EDITOR Dope Sheet, Adjust timing of keyframes.NLA_EDITOR NLA Editor, Combine and layer Actions.IMAGE_EDITOR UV/Image Editor, View and edit images and UV Maps.CLIP_EDITOR Movie Clip Editor, Motion tracking tools.SEQUENCE_EDITOR Video Sequence Editor, Video editing tools.NODE_EDITOR Node Editor, Editor for node-based shading and compositing tools.TEXT_EDITOR Text Editor, Edit scripts and in-file documentation.LOGIC_EDITOR Logic Editor, Game logic editing.PROPERTIES Properties, Edit properties of active object and related data-blocks.OUTLINER Outliner, Overview of scene graph and all available data-blocks.USER_PREFERENCES User Preferences, Edit persistent configuration settings.INFO Info, Main menu bar and list of error messages (drag down to expand and display).FILE_BROWSER File Browser, Browse for files and assets.CONSOLE Python Console, Interactive programmatic console for advanced editing and script development. 
        :type space_type: typing.Union[int, str]
        :param region_type: Region Type 
        :type region_type: typing.Union[int, str]
        :rtype: 'KeyMap'
        :return:  Key Map, Corresponding key map 
        '''
        pass

    def find_modal(self, name: str) -> 'KeyMap':
        '''find_modal 

        :param name: Operator Name 
        :type name: str
        :rtype: 'KeyMap'
        :return:  Key Map, Corresponding key map 
        '''
        pass


class KeyboardSensor:
    '''Sensor to detect keyboard events '''

    key: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    log: str = None
    '''Property that indicates whether to log keystrokes as a string 

    :type: str
    '''

    modifier_key_1: typing.Union[int, str] = None
    '''Modifier key code 

    :type: typing.Union[int, str]
    '''

    modifier_key_2: typing.Union[int, str] = None
    '''Modifier key code 

    :type: typing.Union[int, str]
    '''

    target: str = None
    '''Property that receives the keystrokes in case a string is logged 

    :type: str
    '''

    use_all_keys: bool = None
    '''Trigger this sensor on any keystroke 

    :type: bool
    '''


class Keyframe:
    '''Bezier curve point with two handles defining a Keyframe on an F-Curve '''

    amplitude: float = None
    '''Amount to boost elastic bounces for ‘elastic’ easing 

    :type: float
    '''

    back: float = None
    '''Amount of overshoot for ‘back’ easing 

    :type: float
    '''

    co: float = None
    '''Coordinates of the control point 

    :type: float
    '''

    easing: typing.Union[int, str] = None
    '''Which ends of the segment between this and the next keyframe easing interpolation is applied to 

    :type: typing.Union[int, str]
    '''

    handle_left: float = None
    '''Coordinates of the left handle (before the control point) 

    :type: float
    '''

    handle_left_type: typing.Union[int, str] = None
    '''Handle types 

    :type: typing.Union[int, str]
    '''

    handle_right: float = None
    '''Coordinates of the right handle (after the control point) 

    :type: float
    '''

    handle_right_type: typing.Union[int, str] = None
    '''Handle types 

    :type: typing.Union[int, str]
    '''

    interpolation: typing.Union[int, str] = None
    '''Interpolation method to use for segment of the F-Curve from this Keyframe until the next Keyframe 

    :type: typing.Union[int, str]
    '''

    period: float = None
    '''Time between bounces for elastic easing 

    :type: float
    '''

    select_control_point: bool = None
    '''Control point selection status 

    :type: bool
    '''

    select_left_handle: bool = None
    '''Left handle selection status 

    :type: bool
    '''

    select_right_handle: bool = None
    '''Right handle selection status 

    :type: bool
    '''

    type: typing.Union[int, str] = None
    '''Type of keyframe (for visual purposes only) 

    :type: typing.Union[int, str]
    '''


class KeyingSet:
    '''Settings that should be keyframed together '''

    bl_description: str = None
    '''A short description of the keying set 

    :type: str
    '''

    bl_idname: str = None
    '''If this is set, the Keying Set gets a custom ID, otherwise it takes the name of the class used to define the Keying Set (for example, if the class name is “BUILTIN_KSI_location”, and bl_idname is not set by the script, then bl_idname = “BUILTIN_KSI_location”) 

    :type: str
    '''

    bl_label: str = None
    '''

    :type: str
    '''

    is_path_absolute: bool = None
    '''Keying Set defines specific paths/settings to be keyframed (i.e. is not reliant on context info) 

    :type: bool
    '''

    paths: typing.List['KeyingSetPaths'] = None
    '''Keying Set Paths to define settings that get keyframed together 

    :type: typing.List['KeyingSetPaths']
    '''

    type_info: 'KeyingSetInfo' = None
    '''Callback function defines for built-in Keying Sets 

    :type: 'KeyingSetInfo'
    '''

    use_insertkey_needed: bool = None
    '''Only insert keyframes where they’re needed in the relevant F-Curves 

    :type: bool
    '''

    use_insertkey_override_needed: bool = None
    '''Override default setting to only insert keyframes where they’re needed in the relevant F-Curves 

    :type: bool
    '''

    use_insertkey_override_visual: bool = None
    '''Override default setting to insert keyframes based on ‘visual transforms’ 

    :type: bool
    '''

    use_insertkey_override_xyz_to_rgb: bool = None
    '''Override default setting to set color for newly added transformation F-Curves (Location, Rotation, Scale) to be based on the transform axis 

    :type: bool
    '''

    use_insertkey_visual: bool = None
    '''Insert keyframes based on ‘visual transforms’ 

    :type: bool
    '''

    use_insertkey_xyz_to_rgb: bool = None
    '''Color for newly added transformation F-Curves (Location, Rotation, Scale) is based on the transform axis 

    :type: bool
    '''

    def refresh(self, ):
        '''Refresh Keying Set to ensure that it is valid for the current context (call before each use of one) 

        '''
        pass


class KeyingSetInfo:
    '''Callback function defines for builtin Keying Sets '''

    bl_description: str = None
    '''A short description of the keying set 

    :type: str
    '''

    bl_idname: str = None
    '''If this is set, the Keying Set gets a custom ID, otherwise it takes the name of the class used to define the Keying Set (for example, if the class name is “BUILTIN_KSI_location”, and bl_idname is not set by the script, then bl_idname = “BUILTIN_KSI_location”) 

    :type: str
    '''

    bl_label: str = None
    '''

    :type: str
    '''

    bl_options: typing.Set[typing.Union[int, str]] = None
    '''Keying Set options to use when inserting keyframes 

    :type: typing.Set[typing.Union[int, str]]
    '''

    def poll(self, context) -> bool:
        '''Test if Keying Set can be used or not 

        :rtype: bool
        '''
        pass

    def iterator(self, context, ks):
        '''Call generate() on the structs which have properties to be keyframed 

        '''
        pass

    def generate(self, context, ks, data):
        '''Add Paths to the Keying Set to keyframe the properties of the given data 

        '''
        pass


class KeyingSetPath:
    '''Path to a setting for use in a Keying Set '''

    array_index: int = None
    '''Index to the specific setting if applicable 

    :type: int
    '''

    data_path: str = None
    '''Path to property setting 

    :type: str
    '''

    group: str = None
    '''Name of Action Group to assign setting(s) for this path to 

    :type: str
    '''

    group_method: typing.Union[int, str] = None
    '''Method used to define which Group-name to use 

    :type: typing.Union[int, str]
    '''

    id: 'ID' = None
    '''ID-Block that keyframes for Keying Set should be added to (for Absolute Keying Sets only) 

    :type: 'ID'
    '''

    id_type: typing.Union[int, str] = None
    '''Type of ID-block that can be used 

    :type: typing.Union[int, str]
    '''

    use_entire_array: bool = None
    '''When an ‘array/vector’ type is chosen (Location, Rotation, Color, etc.), entire array is to be used 

    :type: bool
    '''

    use_insertkey_needed: bool = None
    '''Only insert keyframes where they’re needed in the relevant F-Curves 

    :type: bool
    '''

    use_insertkey_override_needed: bool = None
    '''Override default setting to only insert keyframes where they’re needed in the relevant F-Curves 

    :type: bool
    '''

    use_insertkey_override_visual: bool = None
    '''Override default setting to insert keyframes based on ‘visual transforms’ 

    :type: bool
    '''

    use_insertkey_override_xyz_to_rgb: bool = None
    '''Override default setting to set color for newly added transformation F-Curves (Location, Rotation, Scale) to be based on the transform axis 

    :type: bool
    '''

    use_insertkey_visual: bool = None
    '''Insert keyframes based on ‘visual transforms’ 

    :type: bool
    '''

    use_insertkey_xyz_to_rgb: bool = None
    '''Color for newly added transformation F-Curves (Location, Rotation, Scale) is based on the transform axis 

    :type: bool
    '''


class KeyingSetPaths:
    '''Collection of keying set paths '''

    active: 'KeyingSetPath' = None
    '''Active Keying Set used to insert/delete keyframes 

    :type: 'KeyingSetPath'
    '''

    active_index: int = None
    '''Current Keying Set index 

    :type: int
    '''

    def add(self,
            target_id: 'ID',
            data_path: str,
            index: int = -1,
            group_method: typing.Union[int, str] = 'KEYINGSET',
            group_name: str = "") -> 'KeyingSetPath':
        '''Add a new path for the Keying Set 

        :param target_id: Target ID, ID data-block for the destination 
        :type target_id: 'ID'
        :param data_path: Data-Path, RNA-Path to destination property 
        :type data_path: str
        :param index: Index, The index of the destination property (i.e. axis of Location/Rotation/etc.), or -1 for the entire array 
        :type index: int
        :param group_method: Grouping Method, Method used to define which Group-name to use 
        :type group_method: typing.Union[int, str]
        :param group_name: Group Name, Name of Action Group to assign destination to (only if grouping mode is to use this name) 
        :type group_name: str
        :rtype: 'KeyingSetPath'
        :return:  New Path, Path created and added to the Keying Set 
        '''
        pass

    def remove(self, path: 'KeyingSetPath'):
        '''Remove the given path from the Keying Set 

        :param path: Path 
        :type path: 'KeyingSetPath'
        '''
        pass

    def clear(self, ):
        '''Remove all the paths from the Keying Set 

        '''
        pass


class KeyingSets:
    '''Scene keying sets '''

    active: 'KeyingSet' = None
    '''Active Keying Set used to insert/delete keyframes 

    :type: 'KeyingSet'
    '''

    active_index: int = None
    '''Current Keying Set index (negative for ‘builtin’ and positive for ‘absolute’) 

    :type: int
    '''

    def new(self, idname: str = "KeyingSet",
            name: str = "KeyingSet") -> 'KeyingSet':
        '''Add a new Keying Set to Scene 

        :param idname: IDName, Internal identifier of Keying Set 
        :type idname: str
        :param name: Name, User visible name of Keying Set 
        :type name: str
        :rtype: 'KeyingSet'
        :return:  Newly created Keying Set 
        '''
        pass


class KeyingSetsAll:
    '''All available keying sets '''

    active: 'KeyingSet' = None
    '''Active Keying Set used to insert/delete keyframes 

    :type: 'KeyingSet'
    '''

    active_index: int = None
    '''Current Keying Set index (negative for ‘builtin’ and positive for ‘absolute’) 

    :type: int
    '''


class KinematicConstraint:
    '''Inverse Kinematics '''

    chain_count: int = None
    '''How many bones are included in the IK effect - 0 uses all bones 

    :type: int
    '''

    distance: float = None
    '''Radius of limiting sphere 

    :type: float
    '''

    ik_type: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    iterations: int = None
    '''Maximum number of solving iterations 

    :type: int
    '''

    limit_mode: typing.Union[int, str] = None
    '''Distances in relation to sphere of influence to allow 

    :type: typing.Union[int, str]
    '''

    lock_location_x: bool = None
    '''Constraint position along X axis 

    :type: bool
    '''

    lock_location_y: bool = None
    '''Constraint position along Y axis 

    :type: bool
    '''

    lock_location_z: bool = None
    '''Constraint position along Z axis 

    :type: bool
    '''

    lock_rotation_x: bool = None
    '''Constraint rotation along X axis 

    :type: bool
    '''

    lock_rotation_y: bool = None
    '''Constraint rotation along Y axis 

    :type: bool
    '''

    lock_rotation_z: bool = None
    '''Constraint rotation along Z axis 

    :type: bool
    '''

    orient_weight: float = None
    '''For Tree-IK: Weight of orientation control for this target 

    :type: float
    '''

    pole_angle: float = None
    '''Pole rotation offset 

    :type: float
    '''

    pole_subtarget: str = None
    '''

    :type: str
    '''

    pole_target: 'Object' = None
    '''Object for pole rotation 

    :type: 'Object'
    '''

    reference_axis: typing.Union[int, str] = None
    '''Constraint axis Lock options relative to Bone or Target reference 

    :type: typing.Union[int, str]
    '''

    subtarget: str = None
    '''

    :type: str
    '''

    target: 'Object' = None
    '''Target Object 

    :type: 'Object'
    '''

    use_location: bool = None
    '''Chain follows position of target 

    :type: bool
    '''

    use_rotation: bool = None
    '''Chain follows rotation of target 

    :type: bool
    '''

    use_stretch: bool = None
    '''Enable IK Stretching 

    :type: bool
    '''

    use_tail: bool = None
    '''Include bone’s tail as last element in chain 

    :type: bool
    '''

    weight: float = None
    '''For Tree-IK: Weight of position control for this target 

    :type: float
    '''


class Lamp:
    '''Lamp data-block for lighting a scene '''

    active_texture: 'Texture' = None
    '''Active texture slot being displayed 

    :type: 'Texture'
    '''

    active_texture_index: int = None
    '''Index of active texture slot 

    :type: int
    '''

    animation_data: 'AnimData' = None
    '''Animation data for this data-block 

    :type: 'AnimData'
    '''

    color: float = None
    '''Light color 

    :type: float
    '''

    cycles: 'CyclesLampSettings' = None
    '''Cycles lamp settings 

    :type: 'CyclesLampSettings'
    '''

    distance: float = None
    '''Falloff distance - the light is at half the original intensity at this point 

    :type: float
    '''

    energy: float = None
    '''Amount of light that the lamp emits 

    :type: float
    '''

    node_tree: 'NodeTree' = None
    '''Node tree for node based lamps 

    :type: 'NodeTree'
    '''

    texture_slots: typing.List['LampTextureSlots'] = None
    '''Texture slots defining the mapping and influence of textures 

    :type: typing.List['LampTextureSlots']
    '''

    type: typing.Union[int, str] = None
    '''Type of Lamp 

    :type: typing.Union[int, str]
    '''

    use_diffuse: bool = None
    '''Do diffuse shading 

    :type: bool
    '''

    use_negative: bool = None
    '''Cast negative light 

    :type: bool
    '''

    use_nodes: bool = None
    '''Use shader nodes to render the lamp 

    :type: bool
    '''

    use_own_layer: bool = None
    '''Illuminate objects only on the same layers the lamp is on 

    :type: bool
    '''

    use_specular: bool = None
    '''Create specular highlights 

    :type: bool
    '''


class LampSkySettings:
    '''Sky related settings for a sun lamp '''

    atmosphere_distance_factor: float = None
    '''Multiplier to convert blender units to physical distance 

    :type: float
    '''

    atmosphere_extinction: float = None
    '''Extinction scattering contribution factor 

    :type: float
    '''

    atmosphere_inscattering: float = None
    '''Scatter contribution factor 

    :type: float
    '''

    atmosphere_turbidity: float = None
    '''Sky turbidity 

    :type: float
    '''

    backscattered_light: float = None
    '''Backscattered light 

    :type: float
    '''

    horizon_brightness: float = None
    '''Horizon brightness 

    :type: float
    '''

    sky_blend: float = None
    '''Blend factor with sky 

    :type: float
    '''

    sky_blend_type: typing.Union[int, str] = None
    '''Blend mode for combining sun sky with world sky 

    :type: typing.Union[int, str]
    '''

    sky_color_space: typing.Union[int, str] = None
    '''Color space to use for internal XYZ->RGB color conversion 

    :type: typing.Union[int, str]
    '''

    sky_exposure: float = None
    '''Strength of sky shading exponential exposure correction 

    :type: float
    '''

    spread: float = None
    '''Horizon Spread 

    :type: float
    '''

    sun_brightness: float = None
    '''Sun brightness 

    :type: float
    '''

    sun_intensity: float = None
    '''Sun intensity 

    :type: float
    '''

    sun_size: float = None
    '''Sun size 

    :type: float
    '''

    use_atmosphere: bool = None
    '''Apply sun effect on atmosphere 

    :type: bool
    '''

    use_sky: bool = None
    '''Apply sun effect on sky 

    :type: bool
    '''


class LampTextureSlot:
    '''Texture slot for textures in a Lamp data-block '''

    color_factor: float = None
    '''Amount texture affects color values 

    :type: float
    '''

    object: 'Object' = None
    '''Object to use for mapping with Object texture coordinates 

    :type: 'Object'
    '''

    shadow_factor: float = None
    '''Amount texture affects shadow 

    :type: float
    '''

    texture_coords: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    use_map_color: bool = None
    '''Let the texture affect the basic color of the lamp 

    :type: bool
    '''

    use_map_shadow: bool = None
    '''Let the texture affect the shadow color of the lamp 

    :type: bool
    '''


class LampTextureSlots:
    '''Collection of texture slots '''

    pass


class LaplacianDeformModifier:
    '''Mesh deform modifier '''

    is_bind: bool = None
    '''Whether geometry has been bound to anchors 

    :type: bool
    '''

    iterations: int = None
    '''

    :type: int
    '''

    vertex_group: str = None
    '''Name of Vertex Group which determines Anchors 

    :type: str
    '''


class LaplacianSmoothModifier:
    '''Smoothing effect modifier '''

    iterations: int = None
    '''

    :type: int
    '''

    lambda_border: float = None
    '''Lambda factor in border 

    :type: float
    '''

    lambda_factor: float = None
    '''Smooth factor effect 

    :type: float
    '''

    use_normalized: bool = None
    '''Improve and stabilize the enhanced shape 

    :type: bool
    '''

    use_volume_preserve: bool = None
    '''Apply volume preservation after smooth 

    :type: bool
    '''

    use_x: bool = None
    '''Smooth object along X axis 

    :type: bool
    '''

    use_y: bool = None
    '''Smooth object along Y axis 

    :type: bool
    '''

    use_z: bool = None
    '''Smooth object along Z axis 

    :type: bool
    '''

    vertex_group: str = None
    '''Name of Vertex Group which determines influence of modifier per point 

    :type: str
    '''


class Lattice:
    '''Lattice data-block defining a grid for deforming other objects '''

    animation_data: 'AnimData' = None
    '''Animation data for this data-block 

    :type: 'AnimData'
    '''

    interpolation_type_u: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    interpolation_type_v: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    interpolation_type_w: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    is_editmode: bool = None
    '''True when used in editmode 

    :type: bool
    '''

    points: typing.List['LatticePoint'] = None
    '''Points of the lattice 

    :type: typing.List['LatticePoint']
    '''

    points_u: int = None
    '''Point in U direction (can’t be changed when there are shape keys) 

    :type: int
    '''

    points_v: int = None
    '''Point in V direction (can’t be changed when there are shape keys) 

    :type: int
    '''

    points_w: int = None
    '''Point in W direction (can’t be changed when there are shape keys) 

    :type: int
    '''

    shape_keys: 'Key' = None
    '''

    :type: 'Key'
    '''

    use_outside: bool = None
    '''Only draw, and take into account, the outer vertices 

    :type: bool
    '''

    vertex_group: str = None
    '''Vertex group to apply the influence of the lattice 

    :type: str
    '''

    def transform(self, matrix: float, shape_keys: bool = False):
        '''Transform lattice by a matrix 

        :param matrix: Matrix 
        :type matrix: float
        :param shape_keys: Transform Shape Keys 
        :type shape_keys: bool
        '''
        pass


class LatticeModifier:
    '''Lattice deformation modifier '''

    object: 'Object' = None
    '''Lattice object to deform with 

    :type: 'Object'
    '''

    strength: float = None
    '''Strength of modifier effect 

    :type: float
    '''

    vertex_group: str = None
    '''Name of Vertex Group which determines influence of modifier per point 

    :type: str
    '''


class LatticePoint:
    '''Point in the lattice grid '''

    co: float = None
    '''Original undeformed location used to calculate the strength of the deform effect (edit/animate the Deformed Location instead) 

    :type: float
    '''

    co_deform: float = None
    '''

    :type: float
    '''

    groups: typing.List['VertexGroupElement'] = None
    '''Weights for the vertex groups this point is member of 

    :type: typing.List['VertexGroupElement']
    '''

    select: bool = None
    '''Selection status 

    :type: bool
    '''

    weight_softbody: float = None
    '''Softbody goal weight 

    :type: float
    '''


class Library:
    '''External .blend file from which data is linked '''

    filepath: str = None
    '''Path to the library .blend file 

    :type: str
    '''

    packed_file: 'PackedFile' = None
    '''

    :type: 'PackedFile'
    '''

    parent: 'Library' = None
    '''

    :type: 'Library'
    '''

    users_id = None
    '''ID data blocks which use this library (readonly) '''

    def reload(self, ):
        '''Reload this library and all its linked data-blocks 

        '''
        pass


class LimitDistanceConstraint:
    '''Limit the distance from target object '''

    distance: float = None
    '''Radius of limiting sphere 

    :type: float
    '''

    head_tail: float = None
    '''Target along length of bone: Head=0, Tail=1 

    :type: float
    '''

    limit_mode: typing.Union[int, str] = None
    '''Distances in relation to sphere of influence to allow 

    :type: typing.Union[int, str]
    '''

    subtarget: str = None
    '''

    :type: str
    '''

    target: 'Object' = None
    '''Target Object 

    :type: 'Object'
    '''

    use_bbone_shape: bool = None
    '''Follow shape of B-Bone segments when calculating Head/Tail position 

    :type: bool
    '''

    use_transform_limit: bool = None
    '''Transforms are affected by this constraint as well 

    :type: bool
    '''


class LimitLocationConstraint:
    '''Limit the location of the constrained object '''

    max_x: float = None
    '''Highest X value to allow 

    :type: float
    '''

    max_y: float = None
    '''Highest Y value to allow 

    :type: float
    '''

    max_z: float = None
    '''Highest Z value to allow 

    :type: float
    '''

    min_x: float = None
    '''Lowest X value to allow 

    :type: float
    '''

    min_y: float = None
    '''Lowest Y value to allow 

    :type: float
    '''

    min_z: float = None
    '''Lowest Z value to allow 

    :type: float
    '''

    use_max_x: bool = None
    '''Use the maximum X value 

    :type: bool
    '''

    use_max_y: bool = None
    '''Use the maximum Y value 

    :type: bool
    '''

    use_max_z: bool = None
    '''Use the maximum Z value 

    :type: bool
    '''

    use_min_x: bool = None
    '''Use the minimum X value 

    :type: bool
    '''

    use_min_y: bool = None
    '''Use the minimum Y value 

    :type: bool
    '''

    use_min_z: bool = None
    '''Use the minimum Z value 

    :type: bool
    '''

    use_transform_limit: bool = None
    '''Transforms are affected by this constraint as well 

    :type: bool
    '''


class LimitRotationConstraint:
    '''Limit the rotation of the constrained object '''

    max_x: float = None
    '''Highest X value to allow 

    :type: float
    '''

    max_y: float = None
    '''Highest Y value to allow 

    :type: float
    '''

    max_z: float = None
    '''Highest Z value to allow 

    :type: float
    '''

    min_x: float = None
    '''Lowest X value to allow 

    :type: float
    '''

    min_y: float = None
    '''Lowest Y value to allow 

    :type: float
    '''

    min_z: float = None
    '''Lowest Z value to allow 

    :type: float
    '''

    use_limit_x: bool = None
    '''Use the minimum X value 

    :type: bool
    '''

    use_limit_y: bool = None
    '''Use the minimum Y value 

    :type: bool
    '''

    use_limit_z: bool = None
    '''Use the minimum Z value 

    :type: bool
    '''

    use_transform_limit: bool = None
    '''Transforms are affected by this constraint as well 

    :type: bool
    '''


class LimitScaleConstraint:
    '''Limit the scaling of the constrained object '''

    max_x: float = None
    '''Highest X value to allow 

    :type: float
    '''

    max_y: float = None
    '''Highest Y value to allow 

    :type: float
    '''

    max_z: float = None
    '''Highest Z value to allow 

    :type: float
    '''

    min_x: float = None
    '''Lowest X value to allow 

    :type: float
    '''

    min_y: float = None
    '''Lowest Y value to allow 

    :type: float
    '''

    min_z: float = None
    '''Lowest Z value to allow 

    :type: float
    '''

    use_max_x: bool = None
    '''Use the maximum X value 

    :type: bool
    '''

    use_max_y: bool = None
    '''Use the maximum Y value 

    :type: bool
    '''

    use_max_z: bool = None
    '''Use the maximum Z value 

    :type: bool
    '''

    use_min_x: bool = None
    '''Use the minimum X value 

    :type: bool
    '''

    use_min_y: bool = None
    '''Use the minimum Y value 

    :type: bool
    '''

    use_min_z: bool = None
    '''Use the minimum Z value 

    :type: bool
    '''

    use_transform_limit: bool = None
    '''Transforms are affected by this constraint as well 

    :type: bool
    '''


class LineStyleAlphaModifier:
    '''Base type to define alpha transparency modifiers '''

    pass


class LineStyleAlphaModifier_AlongStroke:
    '''Change alpha transparency along stroke '''

    blend: typing.Union[int, str] = None
    '''Specify how the modifier value is blended into the base value 

    :type: typing.Union[int, str]
    '''

    curve: 'CurveMapping' = None
    '''Curve used for the curve mapping 

    :type: 'CurveMapping'
    '''

    expanded: bool = None
    '''True if the modifier tab is expanded 

    :type: bool
    '''

    influence: float = None
    '''Influence factor by which the modifier changes the property 

    :type: float
    '''

    invert: bool = None
    '''Invert the fade-out direction of the linear mapping 

    :type: bool
    '''

    mapping: typing.Union[int, str] = None
    '''Select the mapping type 

    :type: typing.Union[int, str]
    '''

    name: str = None
    '''Name of the modifier 

    :type: str
    '''

    type: typing.Union[int, str] = None
    '''Type of the modifier 

    :type: typing.Union[int, str]
    '''

    use: bool = None
    '''Enable or disable this modifier during stroke rendering 

    :type: bool
    '''


class LineStyleAlphaModifier_CreaseAngle:
    '''Alpha transparency based on the angle between two adjacent faces '''

    angle_max: float = None
    '''Maximum angle to modify thickness 

    :type: float
    '''

    angle_min: float = None
    '''Minimum angle to modify thickness 

    :type: float
    '''

    blend: typing.Union[int, str] = None
    '''Specify how the modifier value is blended into the base value 

    :type: typing.Union[int, str]
    '''

    curve: 'CurveMapping' = None
    '''Curve used for the curve mapping 

    :type: 'CurveMapping'
    '''

    expanded: bool = None
    '''True if the modifier tab is expanded 

    :type: bool
    '''

    influence: float = None
    '''Influence factor by which the modifier changes the property 

    :type: float
    '''

    invert: bool = None
    '''Invert the fade-out direction of the linear mapping 

    :type: bool
    '''

    mapping: typing.Union[int, str] = None
    '''Select the mapping type 

    :type: typing.Union[int, str]
    '''

    name: str = None
    '''Name of the modifier 

    :type: str
    '''

    type: typing.Union[int, str] = None
    '''Type of the modifier 

    :type: typing.Union[int, str]
    '''

    use: bool = None
    '''Enable or disable this modifier during stroke rendering 

    :type: bool
    '''


class LineStyleAlphaModifier_Curvature_3D:
    '''Alpha transparency based on the radial curvature of 3D mesh surfaces '''

    blend: typing.Union[int, str] = None
    '''Specify how the modifier value is blended into the base value 

    :type: typing.Union[int, str]
    '''

    curvature_max: float = None
    '''Maximum Curvature 

    :type: float
    '''

    curvature_min: float = None
    '''Minimum Curvature 

    :type: float
    '''

    curve: 'CurveMapping' = None
    '''Curve used for the curve mapping 

    :type: 'CurveMapping'
    '''

    expanded: bool = None
    '''True if the modifier tab is expanded 

    :type: bool
    '''

    influence: float = None
    '''Influence factor by which the modifier changes the property 

    :type: float
    '''

    invert: bool = None
    '''Invert the fade-out direction of the linear mapping 

    :type: bool
    '''

    mapping: typing.Union[int, str] = None
    '''Select the mapping type 

    :type: typing.Union[int, str]
    '''

    name: str = None
    '''Name of the modifier 

    :type: str
    '''

    type: typing.Union[int, str] = None
    '''Type of the modifier 

    :type: typing.Union[int, str]
    '''

    use: bool = None
    '''Enable or disable this modifier during stroke rendering 

    :type: bool
    '''


class LineStyleAlphaModifier_DistanceFromCamera:
    '''Change alpha transparency based on the distance from the camera '''

    blend: typing.Union[int, str] = None
    '''Specify how the modifier value is blended into the base value 

    :type: typing.Union[int, str]
    '''

    curve: 'CurveMapping' = None
    '''Curve used for the curve mapping 

    :type: 'CurveMapping'
    '''

    expanded: bool = None
    '''True if the modifier tab is expanded 

    :type: bool
    '''

    influence: float = None
    '''Influence factor by which the modifier changes the property 

    :type: float
    '''

    invert: bool = None
    '''Invert the fade-out direction of the linear mapping 

    :type: bool
    '''

    mapping: typing.Union[int, str] = None
    '''Select the mapping type 

    :type: typing.Union[int, str]
    '''

    name: str = None
    '''Name of the modifier 

    :type: str
    '''

    range_max: float = None
    '''Upper bound of the input range the mapping is applied 

    :type: float
    '''

    range_min: float = None
    '''Lower bound of the input range the mapping is applied 

    :type: float
    '''

    type: typing.Union[int, str] = None
    '''Type of the modifier 

    :type: typing.Union[int, str]
    '''

    use: bool = None
    '''Enable or disable this modifier during stroke rendering 

    :type: bool
    '''


class LineStyleAlphaModifier_DistanceFromObject:
    '''Change alpha transparency based on the distance from an object '''

    blend: typing.Union[int, str] = None
    '''Specify how the modifier value is blended into the base value 

    :type: typing.Union[int, str]
    '''

    curve: 'CurveMapping' = None
    '''Curve used for the curve mapping 

    :type: 'CurveMapping'
    '''

    expanded: bool = None
    '''True if the modifier tab is expanded 

    :type: bool
    '''

    influence: float = None
    '''Influence factor by which the modifier changes the property 

    :type: float
    '''

    invert: bool = None
    '''Invert the fade-out direction of the linear mapping 

    :type: bool
    '''

    mapping: typing.Union[int, str] = None
    '''Select the mapping type 

    :type: typing.Union[int, str]
    '''

    name: str = None
    '''Name of the modifier 

    :type: str
    '''

    range_max: float = None
    '''Upper bound of the input range the mapping is applied 

    :type: float
    '''

    range_min: float = None
    '''Lower bound of the input range the mapping is applied 

    :type: float
    '''

    target: 'Object' = None
    '''Target object from which the distance is measured 

    :type: 'Object'
    '''

    type: typing.Union[int, str] = None
    '''Type of the modifier 

    :type: typing.Union[int, str]
    '''

    use: bool = None
    '''Enable or disable this modifier during stroke rendering 

    :type: bool
    '''


class LineStyleAlphaModifier_Material:
    '''Change alpha transparency based on a material attribute '''

    blend: typing.Union[int, str] = None
    '''Specify how the modifier value is blended into the base value 

    :type: typing.Union[int, str]
    '''

    curve: 'CurveMapping' = None
    '''Curve used for the curve mapping 

    :type: 'CurveMapping'
    '''

    expanded: bool = None
    '''True if the modifier tab is expanded 

    :type: bool
    '''

    influence: float = None
    '''Influence factor by which the modifier changes the property 

    :type: float
    '''

    invert: bool = None
    '''Invert the fade-out direction of the linear mapping 

    :type: bool
    '''

    mapping: typing.Union[int, str] = None
    '''Select the mapping type 

    :type: typing.Union[int, str]
    '''

    material_attribute: typing.Union[int, str] = None
    '''Specify which material attribute is used 

    :type: typing.Union[int, str]
    '''

    name: str = None
    '''Name of the modifier 

    :type: str
    '''

    type: typing.Union[int, str] = None
    '''Type of the modifier 

    :type: typing.Union[int, str]
    '''

    use: bool = None
    '''Enable or disable this modifier during stroke rendering 

    :type: bool
    '''


class LineStyleAlphaModifier_Noise:
    '''Alpha transparency based on random noise '''

    amplitude: float = None
    '''Amplitude of the noise 

    :type: float
    '''

    blend: typing.Union[int, str] = None
    '''Specify how the modifier value is blended into the base value 

    :type: typing.Union[int, str]
    '''

    curve: 'CurveMapping' = None
    '''Curve used for the curve mapping 

    :type: 'CurveMapping'
    '''

    expanded: bool = None
    '''True if the modifier tab is expanded 

    :type: bool
    '''

    influence: float = None
    '''Influence factor by which the modifier changes the property 

    :type: float
    '''

    invert: bool = None
    '''Invert the fade-out direction of the linear mapping 

    :type: bool
    '''

    mapping: typing.Union[int, str] = None
    '''Select the mapping type 

    :type: typing.Union[int, str]
    '''

    name: str = None
    '''Name of the modifier 

    :type: str
    '''

    period: float = None
    '''Period of the noise 

    :type: float
    '''

    seed: int = None
    '''Seed for the noise generation 

    :type: int
    '''

    type: typing.Union[int, str] = None
    '''Type of the modifier 

    :type: typing.Union[int, str]
    '''

    use: bool = None
    '''Enable or disable this modifier during stroke rendering 

    :type: bool
    '''


class LineStyleAlphaModifier_Tangent:
    '''Alpha transparency based on the direction of the stroke '''

    blend: typing.Union[int, str] = None
    '''Specify how the modifier value is blended into the base value 

    :type: typing.Union[int, str]
    '''

    curve: 'CurveMapping' = None
    '''Curve used for the curve mapping 

    :type: 'CurveMapping'
    '''

    expanded: bool = None
    '''True if the modifier tab is expanded 

    :type: bool
    '''

    influence: float = None
    '''Influence factor by which the modifier changes the property 

    :type: float
    '''

    invert: bool = None
    '''Invert the fade-out direction of the linear mapping 

    :type: bool
    '''

    mapping: typing.Union[int, str] = None
    '''Select the mapping type 

    :type: typing.Union[int, str]
    '''

    name: str = None
    '''Name of the modifier 

    :type: str
    '''

    type: typing.Union[int, str] = None
    '''Type of the modifier 

    :type: typing.Union[int, str]
    '''

    use: bool = None
    '''Enable or disable this modifier during stroke rendering 

    :type: bool
    '''


class LineStyleAlphaModifiers:
    '''Alpha modifiers for changing line alphas '''

    def new(self, name: str,
            type: typing.Union[int, str]) -> 'LineStyleAlphaModifier':
        '''Add a alpha modifier to line style 

        :param name: New name for the alpha modifier (not unique) 
        :type name: str
        :param type: Alpha modifier type to add 
        :type type: typing.Union[int, str]
        :rtype: 'LineStyleAlphaModifier'
        :return:  Newly added alpha modifier 
        '''
        pass

    def remove(self, modifier: 'LineStyleAlphaModifier'):
        '''Remove a alpha modifier from line style 

        :param modifier: Alpha modifier to remove 
        :type modifier: 'LineStyleAlphaModifier'
        '''
        pass


class LineStyleColorModifier:
    '''Base type to define line color modifiers '''

    pass


class LineStyleColorModifier_AlongStroke:
    '''Change line color along stroke '''

    blend: typing.Union[int, str] = None
    '''Specify how the modifier value is blended into the base value 

    :type: typing.Union[int, str]
    '''

    color_ramp: 'ColorRamp' = None
    '''Color ramp used to change line color 

    :type: 'ColorRamp'
    '''

    expanded: bool = None
    '''True if the modifier tab is expanded 

    :type: bool
    '''

    influence: float = None
    '''Influence factor by which the modifier changes the property 

    :type: float
    '''

    name: str = None
    '''Name of the modifier 

    :type: str
    '''

    type: typing.Union[int, str] = None
    '''Type of the modifier 

    :type: typing.Union[int, str]
    '''

    use: bool = None
    '''Enable or disable this modifier during stroke rendering 

    :type: bool
    '''


class LineStyleColorModifier_CreaseAngle:
    '''Change line color based on the underlying crease angle '''

    angle_max: float = None
    '''Maximum angle to modify thickness 

    :type: float
    '''

    angle_min: float = None
    '''Minimum angle to modify thickness 

    :type: float
    '''

    blend: typing.Union[int, str] = None
    '''Specify how the modifier value is blended into the base value 

    :type: typing.Union[int, str]
    '''

    color_ramp: 'ColorRamp' = None
    '''Color ramp used to change line color 

    :type: 'ColorRamp'
    '''

    expanded: bool = None
    '''True if the modifier tab is expanded 

    :type: bool
    '''

    influence: float = None
    '''Influence factor by which the modifier changes the property 

    :type: float
    '''

    name: str = None
    '''Name of the modifier 

    :type: str
    '''

    type: typing.Union[int, str] = None
    '''Type of the modifier 

    :type: typing.Union[int, str]
    '''

    use: bool = None
    '''Enable or disable this modifier during stroke rendering 

    :type: bool
    '''


class LineStyleColorModifier_Curvature_3D:
    '''Change line color based on the radial curvature of 3D mesh surfaces '''

    blend: typing.Union[int, str] = None
    '''Specify how the modifier value is blended into the base value 

    :type: typing.Union[int, str]
    '''

    color_ramp: 'ColorRamp' = None
    '''Color ramp used to change line color 

    :type: 'ColorRamp'
    '''

    curvature_max: float = None
    '''Maximum Curvature 

    :type: float
    '''

    curvature_min: float = None
    '''Minimum Curvature 

    :type: float
    '''

    expanded: bool = None
    '''True if the modifier tab is expanded 

    :type: bool
    '''

    influence: float = None
    '''Influence factor by which the modifier changes the property 

    :type: float
    '''

    name: str = None
    '''Name of the modifier 

    :type: str
    '''

    type: typing.Union[int, str] = None
    '''Type of the modifier 

    :type: typing.Union[int, str]
    '''

    use: bool = None
    '''Enable or disable this modifier during stroke rendering 

    :type: bool
    '''


class LineStyleColorModifier_DistanceFromCamera:
    '''Change line color based on the distance from the camera '''

    blend: typing.Union[int, str] = None
    '''Specify how the modifier value is blended into the base value 

    :type: typing.Union[int, str]
    '''

    color_ramp: 'ColorRamp' = None
    '''Color ramp used to change line color 

    :type: 'ColorRamp'
    '''

    expanded: bool = None
    '''True if the modifier tab is expanded 

    :type: bool
    '''

    influence: float = None
    '''Influence factor by which the modifier changes the property 

    :type: float
    '''

    name: str = None
    '''Name of the modifier 

    :type: str
    '''

    range_max: float = None
    '''Upper bound of the input range the mapping is applied 

    :type: float
    '''

    range_min: float = None
    '''Lower bound of the input range the mapping is applied 

    :type: float
    '''

    type: typing.Union[int, str] = None
    '''Type of the modifier 

    :type: typing.Union[int, str]
    '''

    use: bool = None
    '''Enable or disable this modifier during stroke rendering 

    :type: bool
    '''


class LineStyleColorModifier_DistanceFromObject:
    '''Change line color based on the distance from an object '''

    blend: typing.Union[int, str] = None
    '''Specify how the modifier value is blended into the base value 

    :type: typing.Union[int, str]
    '''

    color_ramp: 'ColorRamp' = None
    '''Color ramp used to change line color 

    :type: 'ColorRamp'
    '''

    expanded: bool = None
    '''True if the modifier tab is expanded 

    :type: bool
    '''

    influence: float = None
    '''Influence factor by which the modifier changes the property 

    :type: float
    '''

    name: str = None
    '''Name of the modifier 

    :type: str
    '''

    range_max: float = None
    '''Upper bound of the input range the mapping is applied 

    :type: float
    '''

    range_min: float = None
    '''Lower bound of the input range the mapping is applied 

    :type: float
    '''

    target: 'Object' = None
    '''Target object from which the distance is measured 

    :type: 'Object'
    '''

    type: typing.Union[int, str] = None
    '''Type of the modifier 

    :type: typing.Union[int, str]
    '''

    use: bool = None
    '''Enable or disable this modifier during stroke rendering 

    :type: bool
    '''


class LineStyleColorModifier_Material:
    '''Change line color based on a material attribute '''

    blend: typing.Union[int, str] = None
    '''Specify how the modifier value is blended into the base value 

    :type: typing.Union[int, str]
    '''

    color_ramp: 'ColorRamp' = None
    '''Color ramp used to change line color 

    :type: 'ColorRamp'
    '''

    expanded: bool = None
    '''True if the modifier tab is expanded 

    :type: bool
    '''

    influence: float = None
    '''Influence factor by which the modifier changes the property 

    :type: float
    '''

    material_attribute: typing.Union[int, str] = None
    '''Specify which material attribute is used 

    :type: typing.Union[int, str]
    '''

    name: str = None
    '''Name of the modifier 

    :type: str
    '''

    type: typing.Union[int, str] = None
    '''Type of the modifier 

    :type: typing.Union[int, str]
    '''

    use: bool = None
    '''Enable or disable this modifier during stroke rendering 

    :type: bool
    '''

    use_ramp: bool = None
    '''Use color ramp to map the BW average into an RGB color 

    :type: bool
    '''


class LineStyleColorModifier_Noise:
    '''Change line color based on random noise '''

    amplitude: float = None
    '''Amplitude of the noise 

    :type: float
    '''

    blend: typing.Union[int, str] = None
    '''Specify how the modifier value is blended into the base value 

    :type: typing.Union[int, str]
    '''

    color_ramp: 'ColorRamp' = None
    '''Color ramp used to change line color 

    :type: 'ColorRamp'
    '''

    expanded: bool = None
    '''True if the modifier tab is expanded 

    :type: bool
    '''

    influence: float = None
    '''Influence factor by which the modifier changes the property 

    :type: float
    '''

    name: str = None
    '''Name of the modifier 

    :type: str
    '''

    period: float = None
    '''Period of the noise 

    :type: float
    '''

    seed: int = None
    '''Seed for the noise generation 

    :type: int
    '''

    type: typing.Union[int, str] = None
    '''Type of the modifier 

    :type: typing.Union[int, str]
    '''

    use: bool = None
    '''Enable or disable this modifier during stroke rendering 

    :type: bool
    '''


class LineStyleColorModifier_Tangent:
    '''Change line color based on the direction of a stroke '''

    blend: typing.Union[int, str] = None
    '''Specify how the modifier value is blended into the base value 

    :type: typing.Union[int, str]
    '''

    color_ramp: 'ColorRamp' = None
    '''Color ramp used to change line color 

    :type: 'ColorRamp'
    '''

    expanded: bool = None
    '''True if the modifier tab is expanded 

    :type: bool
    '''

    influence: float = None
    '''Influence factor by which the modifier changes the property 

    :type: float
    '''

    name: str = None
    '''Name of the modifier 

    :type: str
    '''

    type: typing.Union[int, str] = None
    '''Type of the modifier 

    :type: typing.Union[int, str]
    '''

    use: bool = None
    '''Enable or disable this modifier during stroke rendering 

    :type: bool
    '''


class LineStyleColorModifiers:
    '''Color modifiers for changing line colors '''

    def new(self, name: str,
            type: typing.Union[int, str]) -> 'LineStyleColorModifier':
        '''Add a color modifier to line style 

        :param name: New name for the color modifier (not unique) 
        :type name: str
        :param type: Color modifier type to add 
        :type type: typing.Union[int, str]
        :rtype: 'LineStyleColorModifier'
        :return:  Newly added color modifier 
        '''
        pass

    def remove(self, modifier: 'LineStyleColorModifier'):
        '''Remove a color modifier from line style 

        :param modifier: Color modifier to remove 
        :type modifier: 'LineStyleColorModifier'
        '''
        pass


class LineStyleGeometryModifier:
    '''Base type to define stroke geometry modifiers '''

    pass


class LineStyleGeometryModifier_2DOffset:
    '''Add two-dimensional offsets to stroke backbone geometry '''

    end: float = None
    '''Displacement that is applied from the end of the stroke 

    :type: float
    '''

    expanded: bool = None
    '''True if the modifier tab is expanded 

    :type: bool
    '''

    name: str = None
    '''Name of the modifier 

    :type: str
    '''

    start: float = None
    '''Displacement that is applied from the beginning of the stroke 

    :type: float
    '''

    type: typing.Union[int, str] = None
    '''Type of the modifier 

    :type: typing.Union[int, str]
    '''

    use: bool = None
    '''Enable or disable this modifier during stroke rendering 

    :type: bool
    '''

    x: float = None
    '''Displacement that is applied to the X coordinates of stroke vertices 

    :type: float
    '''

    y: float = None
    '''Displacement that is applied to the Y coordinates of stroke vertices 

    :type: float
    '''


class LineStyleGeometryModifier_2DTransform:
    '''Apply two-dimensional scaling and rotation to stroke backbone geometry '''

    angle: float = None
    '''Rotation angle 

    :type: float
    '''

    expanded: bool = None
    '''True if the modifier tab is expanded 

    :type: bool
    '''

    name: str = None
    '''Name of the modifier 

    :type: str
    '''

    pivot: typing.Union[int, str] = None
    '''Pivot of scaling and rotation operations 

    :type: typing.Union[int, str]
    '''

    pivot_u: float = None
    '''Pivot in terms of the stroke point parameter u (0 <= u <= 1) 

    :type: float
    '''

    pivot_x: float = None
    '''2D X coordinate of the absolute pivot 

    :type: float
    '''

    pivot_y: float = None
    '''2D Y coordinate of the absolute pivot 

    :type: float
    '''

    scale_x: float = None
    '''Scaling factor that is applied along the X axis 

    :type: float
    '''

    scale_y: float = None
    '''Scaling factor that is applied along the Y axis 

    :type: float
    '''

    type: typing.Union[int, str] = None
    '''Type of the modifier 

    :type: typing.Union[int, str]
    '''

    use: bool = None
    '''Enable or disable this modifier during stroke rendering 

    :type: bool
    '''


class LineStyleGeometryModifier_BackboneStretcher:
    '''Stretch the beginning and the end of stroke backbone '''

    backbone_length: float = None
    '''Amount of backbone stretching 

    :type: float
    '''

    expanded: bool = None
    '''True if the modifier tab is expanded 

    :type: bool
    '''

    name: str = None
    '''Name of the modifier 

    :type: str
    '''

    type: typing.Union[int, str] = None
    '''Type of the modifier 

    :type: typing.Union[int, str]
    '''

    use: bool = None
    '''Enable or disable this modifier during stroke rendering 

    :type: bool
    '''


class LineStyleGeometryModifier_BezierCurve:
    '''Replace stroke backbone geometry by a Bezier curve approximation of the original backbone geometry '''

    error: float = None
    '''Maximum distance allowed between the new Bezier curve and the original backbone geometry 

    :type: float
    '''

    expanded: bool = None
    '''True if the modifier tab is expanded 

    :type: bool
    '''

    name: str = None
    '''Name of the modifier 

    :type: str
    '''

    type: typing.Union[int, str] = None
    '''Type of the modifier 

    :type: typing.Union[int, str]
    '''

    use: bool = None
    '''Enable or disable this modifier during stroke rendering 

    :type: bool
    '''


class LineStyleGeometryModifier_Blueprint:
    '''Produce a blueprint using circular, elliptic, and square contour strokes '''

    backbone_length: float = None
    '''Amount of backbone stretching 

    :type: float
    '''

    expanded: bool = None
    '''True if the modifier tab is expanded 

    :type: bool
    '''

    name: str = None
    '''Name of the modifier 

    :type: str
    '''

    random_backbone: int = None
    '''Randomness of the backbone stretching 

    :type: int
    '''

    random_center: int = None
    '''Randomness of the center 

    :type: int
    '''

    random_radius: int = None
    '''Randomness of the radius 

    :type: int
    '''

    rounds: int = None
    '''Number of rounds in contour strokes 

    :type: int
    '''

    shape: typing.Union[int, str] = None
    '''Select the shape of blueprint contour strokes 

    :type: typing.Union[int, str]
    '''

    type: typing.Union[int, str] = None
    '''Type of the modifier 

    :type: typing.Union[int, str]
    '''

    use: bool = None
    '''Enable or disable this modifier during stroke rendering 

    :type: bool
    '''


class LineStyleGeometryModifier_GuidingLines:
    '''Modify the stroke geometry so that it corresponds to its main direction line '''

    expanded: bool = None
    '''True if the modifier tab is expanded 

    :type: bool
    '''

    name: str = None
    '''Name of the modifier 

    :type: str
    '''

    offset: float = None
    '''Displacement that is applied to the main direction line along its normal 

    :type: float
    '''

    type: typing.Union[int, str] = None
    '''Type of the modifier 

    :type: typing.Union[int, str]
    '''

    use: bool = None
    '''Enable or disable this modifier during stroke rendering 

    :type: bool
    '''


class LineStyleGeometryModifier_PerlinNoise1D:
    '''Add one-dimensional Perlin noise to stroke backbone geometry '''

    amplitude: float = None
    '''Amplitude of the Perlin noise 

    :type: float
    '''

    angle: float = None
    '''Displacement direction 

    :type: float
    '''

    expanded: bool = None
    '''True if the modifier tab is expanded 

    :type: bool
    '''

    frequency: float = None
    '''Frequency of the Perlin noise 

    :type: float
    '''

    name: str = None
    '''Name of the modifier 

    :type: str
    '''

    octaves: int = None
    '''Number of octaves (i.e., the amount of detail of the Perlin noise) 

    :type: int
    '''

    seed: int = None
    '''Seed for random number generation (if negative, time is used as a seed instead) 

    :type: int
    '''

    type: typing.Union[int, str] = None
    '''Type of the modifier 

    :type: typing.Union[int, str]
    '''

    use: bool = None
    '''Enable or disable this modifier during stroke rendering 

    :type: bool
    '''


class LineStyleGeometryModifier_PerlinNoise2D:
    '''Add two-dimensional Perlin noise to stroke backbone geometry '''

    amplitude: float = None
    '''Amplitude of the Perlin noise 

    :type: float
    '''

    angle: float = None
    '''Displacement direction 

    :type: float
    '''

    expanded: bool = None
    '''True if the modifier tab is expanded 

    :type: bool
    '''

    frequency: float = None
    '''Frequency of the Perlin noise 

    :type: float
    '''

    name: str = None
    '''Name of the modifier 

    :type: str
    '''

    octaves: int = None
    '''Number of octaves (i.e., the amount of detail of the Perlin noise) 

    :type: int
    '''

    seed: int = None
    '''Seed for random number generation (if negative, time is used as a seed instead) 

    :type: int
    '''

    type: typing.Union[int, str] = None
    '''Type of the modifier 

    :type: typing.Union[int, str]
    '''

    use: bool = None
    '''Enable or disable this modifier during stroke rendering 

    :type: bool
    '''


class LineStyleGeometryModifier_Polygonalization:
    '''Modify the stroke geometry so that it looks more ‘polygonal’ '''

    error: float = None
    '''Maximum distance between the original stroke and its polygonal approximation 

    :type: float
    '''

    expanded: bool = None
    '''True if the modifier tab is expanded 

    :type: bool
    '''

    name: str = None
    '''Name of the modifier 

    :type: str
    '''

    type: typing.Union[int, str] = None
    '''Type of the modifier 

    :type: typing.Union[int, str]
    '''

    use: bool = None
    '''Enable or disable this modifier during stroke rendering 

    :type: bool
    '''


class LineStyleGeometryModifier_Sampling:
    '''Specify a new sampling value that determines the resolution of stroke polylines '''

    expanded: bool = None
    '''True if the modifier tab is expanded 

    :type: bool
    '''

    name: str = None
    '''Name of the modifier 

    :type: str
    '''

    sampling: float = None
    '''New sampling value to be used for subsequent modifiers 

    :type: float
    '''

    type: typing.Union[int, str] = None
    '''Type of the modifier 

    :type: typing.Union[int, str]
    '''

    use: bool = None
    '''Enable or disable this modifier during stroke rendering 

    :type: bool
    '''


class LineStyleGeometryModifier_Simplification:
    '''Simplify the stroke set '''

    expanded: bool = None
    '''True if the modifier tab is expanded 

    :type: bool
    '''

    name: str = None
    '''Name of the modifier 

    :type: str
    '''

    tolerance: float = None
    '''Distance below which segments will be merged 

    :type: float
    '''

    type: typing.Union[int, str] = None
    '''Type of the modifier 

    :type: typing.Union[int, str]
    '''

    use: bool = None
    '''Enable or disable this modifier during stroke rendering 

    :type: bool
    '''


class LineStyleGeometryModifier_SinusDisplacement:
    '''Add sinus displacement to stroke backbone geometry '''

    amplitude: float = None
    '''Amplitude of the sinus displacement 

    :type: float
    '''

    expanded: bool = None
    '''True if the modifier tab is expanded 

    :type: bool
    '''

    name: str = None
    '''Name of the modifier 

    :type: str
    '''

    phase: float = None
    '''Phase of the sinus displacement 

    :type: float
    '''

    type: typing.Union[int, str] = None
    '''Type of the modifier 

    :type: typing.Union[int, str]
    '''

    use: bool = None
    '''Enable or disable this modifier during stroke rendering 

    :type: bool
    '''

    wavelength: float = None
    '''Wavelength of the sinus displacement 

    :type: float
    '''


class LineStyleGeometryModifier_SpatialNoise:
    '''Add spatial noise to stroke backbone geometry '''

    amplitude: float = None
    '''Amplitude of the spatial noise 

    :type: float
    '''

    expanded: bool = None
    '''True if the modifier tab is expanded 

    :type: bool
    '''

    name: str = None
    '''Name of the modifier 

    :type: str
    '''

    octaves: int = None
    '''Number of octaves (i.e., the amount of detail of the spatial noise) 

    :type: int
    '''

    scale: float = None
    '''Scale of the spatial noise 

    :type: float
    '''

    smooth: bool = None
    '''If true, the spatial noise is smooth 

    :type: bool
    '''

    type: typing.Union[int, str] = None
    '''Type of the modifier 

    :type: typing.Union[int, str]
    '''

    use: bool = None
    '''Enable or disable this modifier during stroke rendering 

    :type: bool
    '''

    use_pure_random: bool = None
    '''If true, the spatial noise does not show any coherence 

    :type: bool
    '''


class LineStyleGeometryModifier_TipRemover:
    '''Remove a piece of stroke at the beginning and the end of stroke backbone '''

    expanded: bool = None
    '''True if the modifier tab is expanded 

    :type: bool
    '''

    name: str = None
    '''Name of the modifier 

    :type: str
    '''

    tip_length: float = None
    '''Length of tips to be removed 

    :type: float
    '''

    type: typing.Union[int, str] = None
    '''Type of the modifier 

    :type: typing.Union[int, str]
    '''

    use: bool = None
    '''Enable or disable this modifier during stroke rendering 

    :type: bool
    '''


class LineStyleGeometryModifiers:
    '''Geometry modifiers for changing line geometries '''

    def new(self, name: str,
            type: typing.Union[int, str]) -> 'LineStyleGeometryModifier':
        '''Add a geometry modifier to line style 

        :param name: New name for the geometry modifier (not unique) 
        :type name: str
        :param type: Geometry modifier type to add 
        :type type: typing.Union[int, str]
        :rtype: 'LineStyleGeometryModifier'
        :return:  Newly added geometry modifier 
        '''
        pass

    def remove(self, modifier: 'LineStyleGeometryModifier'):
        '''Remove a geometry modifier from line style 

        :param modifier: Geometry modifier to remove 
        :type modifier: 'LineStyleGeometryModifier'
        '''
        pass


class LineStyleModifier:
    '''Base type to define modifiers '''

    pass


class LineStyleTextureSlot:
    '''Texture slot for textures in a LineStyle data-block '''

    alpha_factor: float = None
    '''Amount texture affects alpha 

    :type: float
    '''

    diffuse_color_factor: float = None
    '''Amount texture affects diffuse color 

    :type: float
    '''

    mapping: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    mapping_x: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    mapping_y: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    mapping_z: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    texture_coords: typing.Union[int, str] = None
    '''Texture coordinates used to map the texture onto the background 

    :type: typing.Union[int, str]
    '''

    use_map_alpha: bool = None
    '''The texture affects the alpha value 

    :type: bool
    '''

    use_map_color_diffuse: bool = None
    '''The texture affects basic color of the stroke 

    :type: bool
    '''

    use_tips: bool = None
    '''Lower half of the texture is for tips of the stroke 

    :type: bool
    '''


class LineStyleTextureSlots:
    '''Collection of texture slots '''

    pass


class LineStyleThicknessModifier:
    '''Base type to define line thickness modifiers '''

    pass


class LineStyleThicknessModifier_AlongStroke:
    '''Change line thickness along stroke '''

    blend: typing.Union[int, str] = None
    '''Specify how the modifier value is blended into the base value 

    :type: typing.Union[int, str]
    '''

    curve: 'CurveMapping' = None
    '''Curve used for the curve mapping 

    :type: 'CurveMapping'
    '''

    expanded: bool = None
    '''True if the modifier tab is expanded 

    :type: bool
    '''

    influence: float = None
    '''Influence factor by which the modifier changes the property 

    :type: float
    '''

    invert: bool = None
    '''Invert the fade-out direction of the linear mapping 

    :type: bool
    '''

    mapping: typing.Union[int, str] = None
    '''Select the mapping type 

    :type: typing.Union[int, str]
    '''

    name: str = None
    '''Name of the modifier 

    :type: str
    '''

    type: typing.Union[int, str] = None
    '''Type of the modifier 

    :type: typing.Union[int, str]
    '''

    use: bool = None
    '''Enable or disable this modifier during stroke rendering 

    :type: bool
    '''

    value_max: float = None
    '''Maximum output value of the mapping 

    :type: float
    '''

    value_min: float = None
    '''Minimum output value of the mapping 

    :type: float
    '''


class LineStyleThicknessModifier_Calligraphy:
    '''Change line thickness so that stroke looks like made with a calligraphic pen '''

    blend: typing.Union[int, str] = None
    '''Specify how the modifier value is blended into the base value 

    :type: typing.Union[int, str]
    '''

    expanded: bool = None
    '''True if the modifier tab is expanded 

    :type: bool
    '''

    influence: float = None
    '''Influence factor by which the modifier changes the property 

    :type: float
    '''

    name: str = None
    '''Name of the modifier 

    :type: str
    '''

    orientation: float = None
    '''Angle of the main direction 

    :type: float
    '''

    thickness_max: float = None
    '''Maximum thickness in the main direction 

    :type: float
    '''

    thickness_min: float = None
    '''Minimum thickness in the direction perpendicular to the main direction 

    :type: float
    '''

    type: typing.Union[int, str] = None
    '''Type of the modifier 

    :type: typing.Union[int, str]
    '''

    use: bool = None
    '''Enable or disable this modifier during stroke rendering 

    :type: bool
    '''


class LineStyleThicknessModifier_CreaseAngle:
    '''Line thickness based on the angle between two adjacent faces '''

    angle_max: float = None
    '''Maximum angle to modify thickness 

    :type: float
    '''

    angle_min: float = None
    '''Minimum angle to modify thickness 

    :type: float
    '''

    blend: typing.Union[int, str] = None
    '''Specify how the modifier value is blended into the base value 

    :type: typing.Union[int, str]
    '''

    curve: 'CurveMapping' = None
    '''Curve used for the curve mapping 

    :type: 'CurveMapping'
    '''

    expanded: bool = None
    '''True if the modifier tab is expanded 

    :type: bool
    '''

    influence: float = None
    '''Influence factor by which the modifier changes the property 

    :type: float
    '''

    invert: bool = None
    '''Invert the fade-out direction of the linear mapping 

    :type: bool
    '''

    mapping: typing.Union[int, str] = None
    '''Select the mapping type 

    :type: typing.Union[int, str]
    '''

    name: str = None
    '''Name of the modifier 

    :type: str
    '''

    thickness_max: float = None
    '''Maximum thickness 

    :type: float
    '''

    thickness_min: float = None
    '''Minimum thickness 

    :type: float
    '''

    type: typing.Union[int, str] = None
    '''Type of the modifier 

    :type: typing.Union[int, str]
    '''

    use: bool = None
    '''Enable or disable this modifier during stroke rendering 

    :type: bool
    '''


class LineStyleThicknessModifier_Curvature_3D:
    '''Line thickness based on the radial curvature of 3D mesh surfaces '''

    blend: typing.Union[int, str] = None
    '''Specify how the modifier value is blended into the base value 

    :type: typing.Union[int, str]
    '''

    curvature_max: float = None
    '''Maximum Curvature 

    :type: float
    '''

    curvature_min: float = None
    '''Minimum Curvature 

    :type: float
    '''

    curve: 'CurveMapping' = None
    '''Curve used for the curve mapping 

    :type: 'CurveMapping'
    '''

    expanded: bool = None
    '''True if the modifier tab is expanded 

    :type: bool
    '''

    influence: float = None
    '''Influence factor by which the modifier changes the property 

    :type: float
    '''

    invert: bool = None
    '''Invert the fade-out direction of the linear mapping 

    :type: bool
    '''

    mapping: typing.Union[int, str] = None
    '''Select the mapping type 

    :type: typing.Union[int, str]
    '''

    name: str = None
    '''Name of the modifier 

    :type: str
    '''

    thickness_max: float = None
    '''Maximum thickness 

    :type: float
    '''

    thickness_min: float = None
    '''Minimum thickness 

    :type: float
    '''

    type: typing.Union[int, str] = None
    '''Type of the modifier 

    :type: typing.Union[int, str]
    '''

    use: bool = None
    '''Enable or disable this modifier during stroke rendering 

    :type: bool
    '''


class LineStyleThicknessModifier_DistanceFromCamera:
    '''Change line thickness based on the distance from the camera '''

    blend: typing.Union[int, str] = None
    '''Specify how the modifier value is blended into the base value 

    :type: typing.Union[int, str]
    '''

    curve: 'CurveMapping' = None
    '''Curve used for the curve mapping 

    :type: 'CurveMapping'
    '''

    expanded: bool = None
    '''True if the modifier tab is expanded 

    :type: bool
    '''

    influence: float = None
    '''Influence factor by which the modifier changes the property 

    :type: float
    '''

    invert: bool = None
    '''Invert the fade-out direction of the linear mapping 

    :type: bool
    '''

    mapping: typing.Union[int, str] = None
    '''Select the mapping type 

    :type: typing.Union[int, str]
    '''

    name: str = None
    '''Name of the modifier 

    :type: str
    '''

    range_max: float = None
    '''Upper bound of the input range the mapping is applied 

    :type: float
    '''

    range_min: float = None
    '''Lower bound of the input range the mapping is applied 

    :type: float
    '''

    type: typing.Union[int, str] = None
    '''Type of the modifier 

    :type: typing.Union[int, str]
    '''

    use: bool = None
    '''Enable or disable this modifier during stroke rendering 

    :type: bool
    '''

    value_max: float = None
    '''Maximum output value of the mapping 

    :type: float
    '''

    value_min: float = None
    '''Minimum output value of the mapping 

    :type: float
    '''


class LineStyleThicknessModifier_DistanceFromObject:
    '''Change line thickness based on the distance from an object '''

    blend: typing.Union[int, str] = None
    '''Specify how the modifier value is blended into the base value 

    :type: typing.Union[int, str]
    '''

    curve: 'CurveMapping' = None
    '''Curve used for the curve mapping 

    :type: 'CurveMapping'
    '''

    expanded: bool = None
    '''True if the modifier tab is expanded 

    :type: bool
    '''

    influence: float = None
    '''Influence factor by which the modifier changes the property 

    :type: float
    '''

    invert: bool = None
    '''Invert the fade-out direction of the linear mapping 

    :type: bool
    '''

    mapping: typing.Union[int, str] = None
    '''Select the mapping type 

    :type: typing.Union[int, str]
    '''

    name: str = None
    '''Name of the modifier 

    :type: str
    '''

    range_max: float = None
    '''Upper bound of the input range the mapping is applied 

    :type: float
    '''

    range_min: float = None
    '''Lower bound of the input range the mapping is applied 

    :type: float
    '''

    target: 'Object' = None
    '''Target object from which the distance is measured 

    :type: 'Object'
    '''

    type: typing.Union[int, str] = None
    '''Type of the modifier 

    :type: typing.Union[int, str]
    '''

    use: bool = None
    '''Enable or disable this modifier during stroke rendering 

    :type: bool
    '''

    value_max: float = None
    '''Maximum output value of the mapping 

    :type: float
    '''

    value_min: float = None
    '''Minimum output value of the mapping 

    :type: float
    '''


class LineStyleThicknessModifier_Material:
    '''Change line thickness based on a material attribute '''

    blend: typing.Union[int, str] = None
    '''Specify how the modifier value is blended into the base value 

    :type: typing.Union[int, str]
    '''

    curve: 'CurveMapping' = None
    '''Curve used for the curve mapping 

    :type: 'CurveMapping'
    '''

    expanded: bool = None
    '''True if the modifier tab is expanded 

    :type: bool
    '''

    influence: float = None
    '''Influence factor by which the modifier changes the property 

    :type: float
    '''

    invert: bool = None
    '''Invert the fade-out direction of the linear mapping 

    :type: bool
    '''

    mapping: typing.Union[int, str] = None
    '''Select the mapping type 

    :type: typing.Union[int, str]
    '''

    material_attribute: typing.Union[int, str] = None
    '''Specify which material attribute is used 

    :type: typing.Union[int, str]
    '''

    name: str = None
    '''Name of the modifier 

    :type: str
    '''

    type: typing.Union[int, str] = None
    '''Type of the modifier 

    :type: typing.Union[int, str]
    '''

    use: bool = None
    '''Enable or disable this modifier during stroke rendering 

    :type: bool
    '''

    value_max: float = None
    '''Maximum output value of the mapping 

    :type: float
    '''

    value_min: float = None
    '''Minimum output value of the mapping 

    :type: float
    '''


class LineStyleThicknessModifier_Noise:
    '''Line thickness based on random noise '''

    amplitude: float = None
    '''Amplitude of the noise 

    :type: float
    '''

    blend: typing.Union[int, str] = None
    '''Specify how the modifier value is blended into the base value 

    :type: typing.Union[int, str]
    '''

    expanded: bool = None
    '''True if the modifier tab is expanded 

    :type: bool
    '''

    influence: float = None
    '''Influence factor by which the modifier changes the property 

    :type: float
    '''

    name: str = None
    '''Name of the modifier 

    :type: str
    '''

    period: float = None
    '''Period of the noise 

    :type: float
    '''

    seed: int = None
    '''Seed for the noise generation 

    :type: int
    '''

    type: typing.Union[int, str] = None
    '''Type of the modifier 

    :type: typing.Union[int, str]
    '''

    use: bool = None
    '''Enable or disable this modifier during stroke rendering 

    :type: bool
    '''

    use_asymmetric: bool = None
    '''Allow thickness to be assigned asymmetrically 

    :type: bool
    '''


class LineStyleThicknessModifier_Tangent:
    '''Thickness based on the direction of the stroke '''

    blend: typing.Union[int, str] = None
    '''Specify how the modifier value is blended into the base value 

    :type: typing.Union[int, str]
    '''

    curve: 'CurveMapping' = None
    '''Curve used for the curve mapping 

    :type: 'CurveMapping'
    '''

    expanded: bool = None
    '''True if the modifier tab is expanded 

    :type: bool
    '''

    influence: float = None
    '''Influence factor by which the modifier changes the property 

    :type: float
    '''

    invert: bool = None
    '''Invert the fade-out direction of the linear mapping 

    :type: bool
    '''

    mapping: typing.Union[int, str] = None
    '''Select the mapping type 

    :type: typing.Union[int, str]
    '''

    name: str = None
    '''Name of the modifier 

    :type: str
    '''

    thickness_max: float = None
    '''Maximum thickness 

    :type: float
    '''

    thickness_min: float = None
    '''Minimum thickness 

    :type: float
    '''

    type: typing.Union[int, str] = None
    '''Type of the modifier 

    :type: typing.Union[int, str]
    '''

    use: bool = None
    '''Enable or disable this modifier during stroke rendering 

    :type: bool
    '''


class LineStyleThicknessModifiers:
    '''Thickness modifiers for changing line thickness '''

    def new(self, name: str,
            type: typing.Union[int, str]) -> 'LineStyleThicknessModifier':
        '''Add a thickness modifier to line style 

        :param name: New name for the thickness modifier (not unique) 
        :type name: str
        :param type: Thickness modifier type to add 
        :type type: typing.Union[int, str]
        :rtype: 'LineStyleThicknessModifier'
        :return:  Newly added thickness modifier 
        '''
        pass

    def remove(self, modifier: 'LineStyleThicknessModifier'):
        '''Remove a thickness modifier from line style 

        :param modifier: Thickness modifier to remove 
        :type modifier: 'LineStyleThicknessModifier'
        '''
        pass


class Linesets:
    '''Line sets for associating lines and style parameters '''

    active: 'FreestyleLineSet' = None
    '''Active line set being displayed 

    :type: 'FreestyleLineSet'
    '''

    active_index: int = None
    '''Index of active line set slot 

    :type: int
    '''

    def new(self, name: str) -> 'FreestyleLineSet':
        '''Add a line set to scene render layer Freestyle settings 

        :param name: New name for the line set (not unique) 
        :type name: str
        :rtype: 'FreestyleLineSet'
        :return:  Newly created line set 
        '''
        pass

    def remove(self, lineset: 'FreestyleLineSet'):
        '''Remove a line set from scene render layer Freestyle settings 

        :param lineset: Line set to remove 
        :type lineset: 'FreestyleLineSet'
        '''
        pass


class LocRotScale:
    def generate(self, context, ks, data):
        '''

        '''
        pass


class Location:
    pass


class LockedTrackConstraint:
    '''Point toward the target along the track axis, while locking the other axis '''

    head_tail: float = None
    '''Target along length of bone: Head=0, Tail=1 

    :type: float
    '''

    lock_axis: typing.Union[int, str] = None
    '''Axis that points upward 

    :type: typing.Union[int, str]
    '''

    subtarget: str = None
    '''

    :type: str
    '''

    target: 'Object' = None
    '''Target Object 

    :type: 'Object'
    '''

    track_axis: typing.Union[int, str] = None
    '''Axis that points to the target object 

    :type: typing.Union[int, str]
    '''

    use_bbone_shape: bool = None
    '''Follow shape of B-Bone segments when calculating Head/Tail position 

    :type: bool
    '''


class LodLevel:
    distance: float = None
    '''Distance to begin using this level of detail 

    :type: float
    '''

    object: 'Object' = None
    '''Object to use for this level of detail 

    :type: 'Object'
    '''

    object_hysteresis_percentage: int = None
    '''Minimum distance change required to transition to the previous level of detail 

    :type: int
    '''

    use_material: bool = None
    '''Use the material from this object at this level of detail 

    :type: bool
    '''

    use_mesh: bool = None
    '''Use the mesh from this object at this level of detail 

    :type: bool
    '''

    use_object_hysteresis: bool = None
    '''Override LoD Hysteresis scene setting for this LoD level 

    :type: bool
    '''


class LoopColors:
    '''Collection of vertex colors '''

    active: 'MeshLoopColorLayer' = None
    '''Active vertex color layer 

    :type: 'MeshLoopColorLayer'
    '''

    active_index: int = None
    '''Active vertex color index 

    :type: int
    '''

    def new(self, name: str = "Col") -> 'MeshLoopColorLayer':
        '''Add a vertex color layer to Mesh 

        :param name: Vertex color name 
        :type name: str
        :rtype: 'MeshLoopColorLayer'
        :return:  The newly created layer 
        '''
        pass

    def remove(self, layer: 'MeshLoopColorLayer'):
        '''Remove a vertex color layer 

        :param layer: The layer to remove 
        :type layer: 'MeshLoopColorLayer'
        '''
        pass


class MASK_UL_layers:
    def draw_item(self, context, layout, data, item, icon, active_data,
                  active_propname, index):
        '''

        '''
        pass


class MATERIAL_UL_matslots:
    def draw_item(self, context, layout, data, item, icon, active_data,
                  active_propname, index):
        '''

        '''
        pass


class MESH_UL_shape_keys:
    def draw_item(self, context, layout, data, item, icon, active_data,
                  active_propname, index):
        '''

        '''
        pass


class MESH_UL_uvmaps_vcols:
    def draw_item(self, context, layout, data, item, icon, active_data,
                  active_propname, index):
        '''

        '''
        pass


class MESH_UL_vgroups:
    def draw_item(self, context, layout, data, item, icon, active_data,
                  active_propname, index):
        '''

        '''
        pass


class Macro:
    '''Storage of a macro operator being executed, or registered after execution '''

    bl_description: str = None
    '''

    :type: str
    '''

    bl_idname: str = None
    '''

    :type: str
    '''

    bl_label: str = None
    '''

    :type: str
    '''

    bl_options: typing.Set[typing.Union[int, str]] = None
    '''Options for this operator type 

    :type: typing.Set[typing.Union[int, str]]
    '''

    bl_translation_context: str = None
    '''

    :type: str
    '''

    bl_undo_group: str = None
    '''

    :type: str
    '''

    name: str = None
    '''

    :type: str
    '''

    properties: 'OperatorProperties' = None
    '''

    :type: 'OperatorProperties'
    '''

    def report(self, type: typing.Set[typing.Union[int, str]], message: str):
        '''report 

        :param type: Type 
        :type type: typing.Set[typing.Union[int, str]]
        :param message: Report Message 
        :type message: str
        '''
        pass

    def draw(self, context):
        '''Draw function for the operator 

        '''
        pass


class MagicTexture:
    '''Procedural noise texture '''

    noise_depth: int = None
    '''Depth of the noise 

    :type: int
    '''

    turbulence: float = None
    '''Turbulence of the noise 

    :type: float
    '''

    users_material = None
    '''Materials that use this texture (readonly) '''

    users_object_modifier = None
    '''Object modifiers that use this texture (readonly) '''


class MaintainVolumeConstraint:
    '''Maintain a constant volume along a single scaling axis '''

    free_axis: typing.Union[int, str] = None
    '''The free scaling axis of the object 

    :type: typing.Union[int, str]
    '''

    volume: float = None
    '''Volume of the bone at rest 

    :type: float
    '''


class MarbleTexture:
    '''Procedural noise texture '''

    marble_type: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    nabla: float = None
    '''Size of derivative offset used for calculating normal 

    :type: float
    '''

    noise_basis: typing.Union[int, str] = None
    '''Noise basis used for turbulence 

    :type: typing.Union[int, str]
    '''

    noise_basis_2: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    noise_depth: int = None
    '''Depth of the cloud calculation 

    :type: int
    '''

    noise_scale: float = None
    '''Scaling for noise input 

    :type: float
    '''

    noise_type: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    turbulence: float = None
    '''Turbulence of the bandnoise and ringnoise types 

    :type: float
    '''

    users_material = None
    '''Materials that use this texture (readonly) '''

    users_object_modifier = None
    '''Object modifiers that use this texture (readonly) '''


class Mask:
    '''Mask data-block defining mask for compositing '''

    active_layer_index: int = None
    '''Index of active layer in list of all mask’s layers 

    :type: int
    '''

    animation_data: 'AnimData' = None
    '''Animation data for this data-block 

    :type: 'AnimData'
    '''

    frame_end: int = None
    '''Final frame of the mask (used for sequencer) 

    :type: int
    '''

    frame_start: int = None
    '''First frame of the mask (used for sequencer) 

    :type: int
    '''

    layers: typing.List['MaskLayer'] = None
    '''Collection of layers which defines this mask 

    :type: typing.List['MaskLayer']
    '''


class MaskLayer:
    '''Single layer used for masking pixels '''

    alpha: float = None
    '''Render Opacity 

    :type: float
    '''

    blend: typing.Union[int, str] = None
    '''Method of blending mask layers 

    :type: typing.Union[int, str]
    '''

    falloff: typing.Union[int, str] = None
    '''Falloff type the feather 

    :type: typing.Union[int, str]
    '''

    hide: bool = None
    '''Restrict visibility in the viewport 

    :type: bool
    '''

    hide_render: bool = None
    '''Restrict renderability 

    :type: bool
    '''

    hide_select: bool = None
    '''Restrict selection in the viewport 

    :type: bool
    '''

    invert: bool = None
    '''Invert the mask black/white 

    :type: bool
    '''

    name: str = None
    '''Unique name of layer 

    :type: str
    '''

    select: bool = None
    '''Layer is selected for editing in the Dope Sheet 

    :type: bool
    '''

    splines: typing.List['MaskSplines'] = None
    '''Collection of splines which defines this layer 

    :type: typing.List['MaskSplines']
    '''

    use_fill_holes: bool = None
    '''Calculate holes when filling overlapping curves 

    :type: bool
    '''

    use_fill_overlap: bool = None
    '''Calculate self intersections and overlap before filling 

    :type: bool
    '''


class MaskLayers:
    '''Collection of layers used by mask '''

    active: 'MaskLayer' = None
    '''Active layer in this mask 

    :type: 'MaskLayer'
    '''

    def new(self, name: str = "") -> 'MaskLayer':
        '''Add layer to this mask 

        :param name: Name, Name of new layer 
        :type name: str
        :rtype: 'MaskLayer'
        :return:  New mask layer 
        '''
        pass

    def remove(self, layer: 'MaskLayer'):
        '''Remove layer from this mask 

        :param layer: Shape to be removed 
        :type layer: 'MaskLayer'
        '''
        pass

    def clear(self, ):
        '''Remove all mask layers 

        '''
        pass


class MaskModifier:
    '''Mask modifier to hide parts of the mesh '''

    armature: 'Object' = None
    '''Armature to use as source of bones to mask 

    :type: 'Object'
    '''

    invert_vertex_group: bool = None
    '''Use vertices that are not part of region defined 

    :type: bool
    '''

    mode: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    vertex_group: str = None
    '''Vertex group name 

    :type: str
    '''


class MaskParent:
    '''Parenting settings for masking element '''

    id: 'ID' = None
    '''ID-block to which masking element would be parented to or to it’s property 

    :type: 'ID'
    '''

    id_type: typing.Union[int, str] = None
    '''Type of ID-block that can be used 

    :type: typing.Union[int, str]
    '''

    parent: str = None
    '''Name of parent object in specified data-block to which parenting happens 

    :type: str
    '''

    sub_parent: str = None
    '''Name of parent sub-object in specified data-block to which parenting happens 

    :type: str
    '''

    type: typing.Union[int, str] = None
    '''Parent Type 

    :type: typing.Union[int, str]
    '''


class MaskSequence:
    '''Sequence strip to load a video from a mask '''

    alpha_mode: typing.Union[int, str] = None
    '''Representation of alpha information in the RGBA pixels 

    :type: typing.Union[int, str]
    '''

    animation_offset_end: int = None
    '''Animation end offset (trim end) 

    :type: int
    '''

    animation_offset_start: int = None
    '''Animation start offset (trim start) 

    :type: int
    '''

    color_multiply: float = None
    '''

    :type: float
    '''

    color_saturation: float = None
    '''Adjust the intensity of the input’s color 

    :type: float
    '''

    crop: 'SequenceCrop' = None
    '''

    :type: 'SequenceCrop'
    '''

    mask: 'Mask' = None
    '''Mask that this sequence uses 

    :type: 'Mask'
    '''

    strobe: float = None
    '''Only display every nth frame 

    :type: float
    '''

    transform: 'SequenceTransform' = None
    '''

    :type: 'SequenceTransform'
    '''

    use_crop: bool = None
    '''Crop image before processing 

    :type: bool
    '''

    use_deinterlace: bool = None
    '''Remove fields from video movies 

    :type: bool
    '''

    use_flip_x: bool = None
    '''Flip on the X axis 

    :type: bool
    '''

    use_flip_y: bool = None
    '''Flip on the Y axis 

    :type: bool
    '''

    use_float: bool = None
    '''Convert input to float data 

    :type: bool
    '''

    use_reverse_frames: bool = None
    '''Reverse frame order 

    :type: bool
    '''

    use_translation: bool = None
    '''Translate image before processing 

    :type: bool
    '''


class MaskSpline:
    '''Single spline used for defining mask shape '''

    offset_mode: typing.Union[int, str] = None
    '''The method used for calculating the feather offset 

    :type: typing.Union[int, str]
    '''

    points: typing.List['MaskSplinePoints'] = None
    '''Collection of points 

    :type: typing.List['MaskSplinePoints']
    '''

    use_cyclic: bool = None
    '''Make this spline a closed loop 

    :type: bool
    '''

    use_fill: bool = None
    '''Make this spline filled 

    :type: bool
    '''

    use_self_intersection_check: bool = None
    '''Prevent feather from self-intersections 

    :type: bool
    '''

    weight_interpolation: typing.Union[int, str] = None
    '''The type of weight interpolation for spline 

    :type: typing.Union[int, str]
    '''


class MaskSplinePoint:
    '''Single point in spline used for defining mask '''

    co: float = None
    '''Coordinates of the control point 

    :type: float
    '''

    feather_points: typing.List['MaskSplinePointUW'] = None
    '''Points defining feather 

    :type: typing.List['MaskSplinePointUW']
    '''

    handle_left: float = None
    '''Coordinates of the first handle 

    :type: float
    '''

    handle_left_type: typing.Union[int, str] = None
    '''Handle type 

    :type: typing.Union[int, str]
    '''

    handle_right: float = None
    '''Coordinates of the second handle 

    :type: float
    '''

    handle_right_type: typing.Union[int, str] = None
    '''Handle type 

    :type: typing.Union[int, str]
    '''

    handle_type: typing.Union[int, str] = None
    '''Handle type 

    :type: typing.Union[int, str]
    '''

    parent: 'MaskParent' = None
    '''

    :type: 'MaskParent'
    '''

    select: bool = None
    '''Selection status 

    :type: bool
    '''

    weight: float = None
    '''Weight of the point 

    :type: float
    '''


class MaskSplinePointUW:
    '''Single point in spline segment defining feather '''

    select: bool = None
    '''Selection status 

    :type: bool
    '''

    u: float = None
    '''U coordinate of point along spline segment 

    :type: float
    '''

    weight: float = None
    '''Weight of feather point 

    :type: float
    '''


class MaskSplinePoints:
    '''Collection of masking spline points '''

    def add(self, count: int = 1):
        '''Add a number of point to this spline 

        :param count: Number, Number of points to add to the spline 
        :type count: int
        '''
        pass

    def remove(self, point: 'MaskSplinePoint'):
        '''Remove a point from a spline 

        :param point: The point to remove 
        :type point: 'MaskSplinePoint'
        '''
        pass


class MaskSplines:
    '''Collection of masking splines '''

    active: 'MaskSpline' = None
    '''Active spline of masking layer 

    :type: 'MaskSpline'
    '''

    active_point: 'MaskSplinePoint' = None
    '''Active spline of masking layer 

    :type: 'MaskSplinePoint'
    '''

    def new(self, ) -> 'MaskSpline':
        '''Add a new spline to the layer 

        :rtype: 'MaskSpline'
        :return:  The newly created spline 
        '''
        pass

    def remove(self, spline: 'MaskSpline'):
        '''Remove a spline from a layer 

        :param spline: The spline to remove 
        :type spline: 'MaskSpline'
        '''
        pass


class Material:
    '''Material data-block to define the appearance of geometric objects for rendering '''

    active_node_material: 'Material' = None
    '''Active node material 

    :type: 'Material'
    '''

    active_texture: 'Texture' = None
    '''Active texture slot being displayed 

    :type: 'Texture'
    '''

    active_texture_index: int = None
    '''Index of active texture slot 

    :type: int
    '''

    alpha: float = None
    '''Alpha transparency of the material 

    :type: float
    '''

    ambient: float = None
    '''Amount of global ambient color the material receives 

    :type: float
    '''

    animation_data: 'AnimData' = None
    '''Animation data for this data-block 

    :type: 'AnimData'
    '''

    cycles: 'CyclesMaterialSettings' = None
    '''Cycles material settings 

    :type: 'CyclesMaterialSettings'
    '''

    darkness: float = None
    '''Minnaert darkness 

    :type: float
    '''

    diffuse_color: float = None
    '''Diffuse color of the material 

    :type: float
    '''

    diffuse_fresnel: float = None
    '''Power of Fresnel 

    :type: float
    '''

    diffuse_fresnel_factor: float = None
    '''Blending factor of Fresnel 

    :type: float
    '''

    diffuse_intensity: float = None
    '''Amount of diffuse reflection 

    :type: float
    '''

    diffuse_ramp: 'ColorRamp' = None
    '''Color ramp used to affect diffuse shading 

    :type: 'ColorRamp'
    '''

    diffuse_ramp_blend: typing.Union[int, str] = None
    '''Blending method of the ramp and the diffuse color 

    :type: typing.Union[int, str]
    '''

    diffuse_ramp_factor: float = None
    '''Blending factor (also uses alpha in Colorband) 

    :type: float
    '''

    diffuse_ramp_input: typing.Union[int, str] = None
    '''How the ramp maps on the surface 

    :type: typing.Union[int, str]
    '''

    diffuse_shader: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    diffuse_toon_size: float = None
    '''Size of diffuse toon area 

    :type: float
    '''

    diffuse_toon_smooth: float = None
    '''Smoothness of diffuse toon area 

    :type: float
    '''

    emit: float = None
    '''Amount of light to emit 

    :type: float
    '''

    game_settings: 'MaterialGameSettings' = None
    '''Game material settings 

    :type: 'MaterialGameSettings'
    '''

    halo: 'MaterialHalo' = None
    '''Halo settings for the material 

    :type: 'MaterialHalo'
    '''

    invert_z: bool = None
    '''Render material’s faces with an inverted Z buffer (scanline only) 

    :type: bool
    '''

    light_group: 'Group' = None
    '''Limit lighting to lamps in this Group 

    :type: 'Group'
    '''

    line_color: float = None
    '''Line color used for Freestyle line rendering 

    :type: float
    '''

    line_priority: int = None
    '''The line color of a higher priority is used at material boundaries 

    :type: int
    '''

    mirror_color: float = None
    '''Mirror color of the material 

    :type: float
    '''

    node_tree: 'NodeTree' = None
    '''Node tree for node based materials 

    :type: 'NodeTree'
    '''

    offset_z: float = None
    '''Give faces an artificial offset in the Z buffer for Z transparency 

    :type: float
    '''

    paint_active_slot: int = None
    '''Index of active texture paint slot 

    :type: int
    '''

    paint_clone_slot: int = None
    '''Index of clone texture paint slot 

    :type: int
    '''

    pass_index: int = None
    '''Index number for the “Material Index” render pass 

    :type: int
    '''

    physics: 'MaterialPhysics' = None
    '''Game physics settings 

    :type: 'MaterialPhysics'
    '''

    preview_render_type: typing.Union[int, str] = None
    '''Type of preview render 

    :type: typing.Union[int, str]
    '''

    raytrace_mirror: 'MaterialRaytraceMirror' = None
    '''Raytraced reflection settings for the material 

    :type: 'MaterialRaytraceMirror'
    '''

    raytrace_transparency: 'MaterialRaytraceTransparency' = None
    '''Raytraced transparency settings for the material 

    :type: 'MaterialRaytraceTransparency'
    '''

    roughness: float = None
    '''Oren-Nayar Roughness 

    :type: float
    '''

    shadow_buffer_bias: float = None
    '''Factor to multiply shadow buffer bias with (0 is ignore) 

    :type: float
    '''

    shadow_cast_alpha: float = None
    '''Shadow casting alpha, in use for Irregular and Deep shadow buffer 

    :type: float
    '''

    shadow_only_type: typing.Union[int, str] = None
    '''How to draw shadows 

    :type: typing.Union[int, str]
    '''

    shadow_ray_bias: float = None
    '''Shadow raytracing bias to prevent terminator problems on shadow boundary 

    :type: float
    '''

    specular_alpha: float = None
    '''Alpha transparency for specular areas 

    :type: float
    '''

    specular_color: float = None
    '''Specular color of the material 

    :type: float
    '''

    specular_hardness: int = None
    '''How hard (sharp) the specular reflection is 

    :type: int
    '''

    specular_intensity: float = None
    '''How intense (bright) the specular reflection is 

    :type: float
    '''

    specular_ior: float = None
    '''Specular index of refraction 

    :type: float
    '''

    specular_ramp: 'ColorRamp' = None
    '''Color ramp used to affect specular shading 

    :type: 'ColorRamp'
    '''

    specular_ramp_blend: typing.Union[int, str] = None
    '''Blending method of the ramp and the specular color 

    :type: typing.Union[int, str]
    '''

    specular_ramp_factor: float = None
    '''Blending factor (also uses alpha in Colorband) 

    :type: float
    '''

    specular_ramp_input: typing.Union[int, str] = None
    '''How the ramp maps on the surface 

    :type: typing.Union[int, str]
    '''

    specular_shader: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    specular_slope: float = None
    '''The standard deviation of surface slope 

    :type: float
    '''

    specular_toon_size: float = None
    '''Size of specular toon area 

    :type: float
    '''

    specular_toon_smooth: float = None
    '''Smoothness of specular toon area 

    :type: float
    '''

    strand: 'MaterialStrand' = None
    '''Strand settings for the material 

    :type: 'MaterialStrand'
    '''

    subsurface_scattering: 'MaterialSubsurfaceScattering' = None
    '''Subsurface scattering settings for the material 

    :type: 'MaterialSubsurfaceScattering'
    '''

    texture_paint_images: typing.List['Image'] = None
    '''Texture images used for texture painting 

    :type: typing.List['Image']
    '''

    texture_paint_slots: typing.List['TexPaintSlot'] = None
    '''Texture slots defining the mapping and influence of textures 

    :type: typing.List['TexPaintSlot']
    '''

    texture_slots: typing.List['MaterialTextureSlot'] = None
    '''Texture slots defining the mapping and influence of textures 

    :type: typing.List['MaterialTextureSlot']
    '''

    translucency: float = None
    '''Amount of diffuse shading on the back side 

    :type: float
    '''

    transparency_method: typing.Union[int, str] = None
    '''Method to use for rendering transparency 

    :type: typing.Union[int, str]
    '''

    type: typing.Union[int, str] = None
    '''Material type defining how the object is rendered 

    :type: typing.Union[int, str]
    '''

    use_cast_approximate: bool = None
    '''Allow this material to cast shadows when using approximate ambient occlusion 

    :type: bool
    '''

    use_cast_buffer_shadows: bool = None
    '''Allow this material to cast shadows from shadow buffer lamps 

    :type: bool
    '''

    use_cast_shadows: bool = None
    '''Allow this material to cast shadows 

    :type: bool
    '''

    use_cast_shadows_only: bool = None
    '''Make objects with this material appear invisible (not rendered), only casting shadows 

    :type: bool
    '''

    use_cubic: bool = None
    '''Use cubic interpolation for diffuse values, for smoother transitions 

    :type: bool
    '''

    use_diffuse_ramp: bool = None
    '''Toggle diffuse ramp operations 

    :type: bool
    '''

    use_face_texture: bool = None
    '''Replace the object’s base color with color from UV map image textures 

    :type: bool
    '''

    use_face_texture_alpha: bool = None
    '''Replace the object’s base alpha value with alpha from UV map image textures 

    :type: bool
    '''

    use_full_oversampling: bool = None
    '''Force this material to render full shading/textures for all anti-aliasing samples 

    :type: bool
    '''

    use_light_group_exclusive: bool = None
    '''Material uses the light group exclusively - these lamps are excluded from other scene lighting 

    :type: bool
    '''

    use_light_group_local: bool = None
    '''When linked in, material uses local light group with the same name 

    :type: bool
    '''

    use_mist: bool = None
    '''Use mist with this material (in world settings) 

    :type: bool
    '''

    use_nodes: bool = None
    '''Use shader nodes to render the material 

    :type: bool
    '''

    use_object_color: bool = None
    '''Modulate the result with a per-object color 

    :type: bool
    '''

    use_only_shadow: bool = None
    '''Render shadows as the material’s alpha value, making the material transparent except for shadowed areas 

    :type: bool
    '''

    use_ray_shadow_bias: bool = None
    '''Prevent raytraced shadow errors on surfaces with smooth shaded normals (terminator problem) 

    :type: bool
    '''

    use_raytrace: bool = None
    '''Include this material and geometry that uses it in raytracing calculations 

    :type: bool
    '''

    use_shadeless: bool = None
    '''Make this material insensitive to light or shadow 

    :type: bool
    '''

    use_shadows: bool = None
    '''Allow this material to receive shadows 

    :type: bool
    '''

    use_sky: bool = None
    '''Render this material with zero alpha, with sky background in place (scanline only) 

    :type: bool
    '''

    use_specular_ramp: bool = None
    '''Toggle specular ramp operations 

    :type: bool
    '''

    use_tangent_shading: bool = None
    '''Use the material’s tangent vector instead of the normal for shading - for anisotropic shading effects 

    :type: bool
    '''

    use_textures: bool = None
    '''Enable/Disable each texture 

    :type: bool
    '''

    use_transparency: bool = None
    '''Render material as transparent 

    :type: bool
    '''

    use_transparent_shadows: bool = None
    '''Allow this object to receive transparent shadows cast through other objects 

    :type: bool
    '''

    use_uv_project: bool = None
    '''Use to ensure UV interpolation is correct for camera projections (use with UV project modifier) 

    :type: bool
    '''

    use_vertex_color_light: bool = None
    '''Add vertex colors as additional lighting 

    :type: bool
    '''

    use_vertex_color_paint: bool = None
    '''Replace object base color with vertex colors (multiply with ‘texture face’ face assigned textures) 

    :type: bool
    '''

    volume: 'MaterialVolume' = None
    '''Volume settings for the material 

    :type: 'MaterialVolume'
    '''


class MaterialGameSettings:
    '''Game Engine settings for a Material data-block '''

    alpha_blend: typing.Union[int, str] = None
    '''Blend Mode for Transparent Faces 

    :type: typing.Union[int, str]
    '''

    face_orientation: typing.Union[int, str] = None
    '''Especial face orientation options 

    :type: typing.Union[int, str]
    '''

    invisible: bool = None
    '''Make face invisible 

    :type: bool
    '''

    physics: bool = None
    '''Use physics properties of materials 

    :type: bool
    '''

    text: bool = None
    '''Use material as text in Game Engine 

    :type: bool
    '''

    use_backface_culling: bool = None
    '''Hide Back of the face in Game Engine 

    :type: bool
    '''


class MaterialHalo:
    '''Halo particle effect settings for a Material data-block '''

    add: float = None
    '''Strength of the add effect 

    :type: float
    '''

    flare_boost: float = None
    '''Give the flare extra strength 

    :type: float
    '''

    flare_seed: int = None
    '''Offset in the flare seed table 

    :type: int
    '''

    flare_size: float = None
    '''Factor by which the flare is larger than the halo 

    :type: float
    '''

    flare_subflare_count: int = None
    '''Number of sub-flares 

    :type: int
    '''

    flare_subflare_size: float = None
    '''Dimension of the sub-flares, dots and circles 

    :type: float
    '''

    hardness: int = None
    '''Hardness of the halo 

    :type: int
    '''

    line_count: int = None
    '''Number of star shaped lines rendered over the halo 

    :type: int
    '''

    ring_count: int = None
    '''Number of rings rendered over the halo 

    :type: int
    '''

    seed: int = None
    '''Randomize ring dimension and line location 

    :type: int
    '''

    size: float = None
    '''Dimension of the halo 

    :type: float
    '''

    star_tip_count: int = None
    '''Number of points on the star shaped halo 

    :type: int
    '''

    use_extreme_alpha: bool = None
    '''Use extreme alpha 

    :type: bool
    '''

    use_flare_mode: bool = None
    '''Render halo as a lens flare 

    :type: bool
    '''

    use_lines: bool = None
    '''Render star shaped lines over halo 

    :type: bool
    '''

    use_ring: bool = None
    '''Render rings over halo 

    :type: bool
    '''

    use_shaded: bool = None
    '''Let halo receive light and shadows from external objects 

    :type: bool
    '''

    use_soft: bool = None
    '''Soften the edges of halos at intersections with other geometry 

    :type: bool
    '''

    use_star: bool = None
    '''Render halo as a star 

    :type: bool
    '''

    use_texture: bool = None
    '''Give halo a texture 

    :type: bool
    '''

    use_vertex_normal: bool = None
    '''Use the vertex normal to specify the dimension of the halo 

    :type: bool
    '''


class MaterialPhysics:
    '''Physics settings for a Material data-block '''

    elasticity: float = None
    '''Elasticity of collisions 

    :type: float
    '''

    fh_damping: float = None
    '''Damping of the spring force, when inside the physics distance area 

    :type: float
    '''

    fh_distance: float = None
    '''Distance of the physics area 

    :type: float
    '''

    fh_force: float = None
    '''Upward spring force, when inside the physics distance area 

    :type: float
    '''

    friction: float = None
    '''Coulomb friction coefficient, when inside the physics distance area 

    :type: float
    '''

    use_fh_normal: bool = None
    '''Align dynamic game objects along the surface normal, when inside the physics distance area 

    :type: bool
    '''


class MaterialRaytraceMirror:
    '''Raytraced reflection settings for a Material data-block '''

    depth: int = None
    '''Maximum allowed number of light inter-reflections 

    :type: int
    '''

    distance: float = None
    '''Maximum distance of reflected rays (reflections further than this range fade to sky color or material color) 

    :type: float
    '''

    fade_to: typing.Union[int, str] = None
    '''The color that rays with no intersection within the Max Distance take (material color can be best for indoor scenes, sky color for outdoor) 

    :type: typing.Union[int, str]
    '''

    fresnel: float = None
    '''Power of Fresnel for mirror reflection 

    :type: float
    '''

    fresnel_factor: float = None
    '''Blending factor for Fresnel 

    :type: float
    '''

    gloss_anisotropic: float = None
    '''The shape of the reflection, from 0.0 (circular) to 1.0 (fully stretched along the tangent 

    :type: float
    '''

    gloss_factor: float = None
    '''The shininess of the reflection (values < 1.0 give diffuse, blurry reflections) 

    :type: float
    '''

    gloss_samples: int = None
    '''Number of cone samples averaged for blurry reflections 

    :type: int
    '''

    gloss_threshold: float = None
    '''Threshold for adaptive sampling (if a sample contributes less than this amount [as a percentage], sampling is stopped) 

    :type: float
    '''

    reflect_factor: float = None
    '''Amount of mirror reflection for raytrace 

    :type: float
    '''

    use: bool = None
    '''Enable raytraced reflections 

    :type: bool
    '''


class MaterialRaytraceTransparency:
    '''Raytraced refraction settings for a Material data-block '''

    depth: int = None
    '''Maximum allowed number of light inter-refractions 

    :type: int
    '''

    depth_max: float = None
    '''Maximum depth for light to travel through the transparent material before becoming fully filtered (0.0 is disabled) 

    :type: float
    '''

    falloff: float = None
    '''Falloff power for transmissivity filter effect (1.0 is linear) 

    :type: float
    '''

    filter: float = None
    '''Amount to blend in the material’s diffuse color in raytraced transparency (simulating absorption) 

    :type: float
    '''

    fresnel: float = None
    '''Power of Fresnel for transparency (Ray or ZTransp) 

    :type: float
    '''

    fresnel_factor: float = None
    '''Blending factor for Fresnel 

    :type: float
    '''

    gloss_factor: float = None
    '''The clarity of the refraction. Values < 1.0 give diffuse, blurry refractions 

    :type: float
    '''

    gloss_samples: int = None
    '''Number of cone samples averaged for blurry refractions 

    :type: int
    '''

    gloss_threshold: float = None
    '''Threshold for adaptive sampling. If a sample contributes less than this amount (as a percentage), sampling is stopped 

    :type: float
    '''

    ior: float = None
    '''Angular index of refraction for raytraced refraction 

    :type: float
    '''


class MaterialSlot:
    '''Material slot in an object '''

    link: typing.Union[int, str] = None
    '''Link material to object or the object’s data 

    :type: typing.Union[int, str]
    '''

    material: 'Material' = None
    '''Material data-block used by this material slot 

    :type: 'Material'
    '''

    name: str = None
    '''Material slot name 

    :type: str
    '''


class MaterialStrand:
    '''Strand settings for a Material data-block '''

    blend_distance: float = None
    '''Worldspace distance over which to blend in the surface normal 

    :type: float
    '''

    root_size: float = None
    '''Start size of strands in pixels or Blender units 

    :type: float
    '''

    shape: float = None
    '''Positive values make strands rounder, negative ones make strands spiky 

    :type: float
    '''

    size_min: float = None
    '''Minimum size of strands in pixels 

    :type: float
    '''

    tip_size: float = None
    '''End size of strands in pixels or Blender units 

    :type: float
    '''

    use_blender_units: bool = None
    '''Use Blender units for widths instead of pixels 

    :type: bool
    '''

    use_surface_diffuse: bool = None
    '''Make diffuse shading more similar to shading the surface 

    :type: bool
    '''

    use_tangent_shading: bool = None
    '''Use direction of strands as normal for tangent-shading 

    :type: bool
    '''

    uv_layer: str = None
    '''Name of UV map to override 

    :type: str
    '''

    width_fade: float = None
    '''Transparency along the width of the strand 

    :type: float
    '''


class MaterialSubsurfaceScattering:
    '''Diffuse subsurface scattering settings for a Material data-block '''

    back: float = None
    '''Back scattering weight 

    :type: float
    '''

    color: float = None
    '''Scattering color 

    :type: float
    '''

    color_factor: float = None
    '''Blend factor for SSS colors 

    :type: float
    '''

    error_threshold: float = None
    '''Error tolerance (low values are slower and higher quality) 

    :type: float
    '''

    front: float = None
    '''Front scattering weight 

    :type: float
    '''

    ior: float = None
    '''Index of refraction (higher values are denser) 

    :type: float
    '''

    radius: float = None
    '''Mean red/green/blue scattering path length 

    :type: float
    '''

    scale: float = None
    '''Object scale factor 

    :type: float
    '''

    texture_factor: float = None
    '''Texture scattering blend factor 

    :type: float
    '''

    use: bool = None
    '''Enable diffuse subsurface scattering effects in a material 

    :type: bool
    '''


class MaterialTextureSlot:
    '''Texture slot for textures in a Material data-block '''

    alpha_factor: float = None
    '''Amount texture affects alpha 

    :type: float
    '''

    ambient_factor: float = None
    '''Amount texture affects ambient 

    :type: float
    '''

    bump_method: typing.Union[int, str] = None
    '''Method to use for bump mapping 

    :type: typing.Union[int, str]
    '''

    bump_objectspace: typing.Union[int, str] = None
    '''Space to apply bump mapping in 

    :type: typing.Union[int, str]
    '''

    density_factor: float = None
    '''Amount texture affects density 

    :type: float
    '''

    diffuse_color_factor: float = None
    '''Amount texture affects diffuse color 

    :type: float
    '''

    diffuse_factor: float = None
    '''Amount texture affects diffuse reflectivity 

    :type: float
    '''

    displacement_factor: float = None
    '''Amount texture displaces the surface 

    :type: float
    '''

    emission_color_factor: float = None
    '''Amount texture affects emission color 

    :type: float
    '''

    emission_factor: float = None
    '''Amount texture affects emission 

    :type: float
    '''

    emit_factor: float = None
    '''Amount texture affects emission 

    :type: float
    '''

    hardness_factor: float = None
    '''Amount texture affects hardness 

    :type: float
    '''

    mapping: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    mapping_x: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    mapping_y: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    mapping_z: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    mirror_factor: float = None
    '''Amount texture affects mirror color 

    :type: float
    '''

    normal_factor: float = None
    '''Amount texture affects normal values 

    :type: float
    '''

    normal_map_space: typing.Union[int, str] = None
    '''Set space of normal map image 

    :type: typing.Union[int, str]
    '''

    object: 'Object' = None
    '''Object to use for mapping with Object texture coordinates 

    :type: 'Object'
    '''

    raymir_factor: float = None
    '''Amount texture affects ray mirror 

    :type: float
    '''

    reflection_color_factor: float = None
    '''Amount texture affects color of out-scattered light 

    :type: float
    '''

    reflection_factor: float = None
    '''Amount texture affects brightness of out-scattered light 

    :type: float
    '''

    scattering_factor: float = None
    '''Amount texture affects scattering 

    :type: float
    '''

    specular_color_factor: float = None
    '''Amount texture affects specular color 

    :type: float
    '''

    specular_factor: float = None
    '''Amount texture affects specular reflectivity 

    :type: float
    '''

    texture_coords: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    translucency_factor: float = None
    '''Amount texture affects translucency 

    :type: float
    '''

    transmission_color_factor: float = None
    '''Amount texture affects result color after light has been scattered/absorbed 

    :type: float
    '''

    use: bool = None
    '''Enable this material texture slot 

    :type: bool
    '''

    use_from_dupli: bool = None
    '''Dupli’s instanced from verts, faces or particles, inherit texture coordinate from their parent 

    :type: bool
    '''

    use_from_original: bool = None
    '''Dupli’s derive their object coordinates from the original object’s transformation 

    :type: bool
    '''

    use_map_alpha: bool = None
    '''The texture affects the alpha value 

    :type: bool
    '''

    use_map_ambient: bool = None
    '''The texture affects the value of ambient 

    :type: bool
    '''

    use_map_color_diffuse: bool = None
    '''The texture affects basic color of the material 

    :type: bool
    '''

    use_map_color_emission: bool = None
    '''The texture affects the color of emission 

    :type: bool
    '''

    use_map_color_reflection: bool = None
    '''The texture affects the color of scattered light 

    :type: bool
    '''

    use_map_color_spec: bool = None
    '''The texture affects the specularity color 

    :type: bool
    '''

    use_map_color_transmission: bool = None
    '''The texture affects the result color after other light has been scattered/absorbed 

    :type: bool
    '''

    use_map_density: bool = None
    '''The texture affects the volume’s density 

    :type: bool
    '''

    use_map_diffuse: bool = None
    '''The texture affects the value of diffuse reflectivity 

    :type: bool
    '''

    use_map_displacement: bool = None
    '''Let the texture displace the surface 

    :type: bool
    '''

    use_map_emission: bool = None
    '''The texture affects the volume’s emission 

    :type: bool
    '''

    use_map_emit: bool = None
    '''The texture affects the emit value 

    :type: bool
    '''

    use_map_hardness: bool = None
    '''The texture affects the hardness value 

    :type: bool
    '''

    use_map_mirror: bool = None
    '''The texture affects the mirror color 

    :type: bool
    '''

    use_map_normal: bool = None
    '''The texture affects the rendered normal 

    :type: bool
    '''

    use_map_raymir: bool = None
    '''The texture affects the ray-mirror value 

    :type: bool
    '''

    use_map_reflect: bool = None
    '''The texture affects the reflected light’s brightness 

    :type: bool
    '''

    use_map_scatter: bool = None
    '''The texture affects the volume’s scattering 

    :type: bool
    '''

    use_map_specular: bool = None
    '''The texture affects the value of specular reflectivity 

    :type: bool
    '''

    use_map_to_bounds: bool = None
    '''Map coordinates in object bounds 

    :type: bool
    '''

    use_map_translucency: bool = None
    '''The texture affects the translucency value 

    :type: bool
    '''

    use_map_warp: bool = None
    '''Let the texture warp texture coordinates of next channels 

    :type: bool
    '''

    uv_layer: str = None
    '''UV map to use for mapping with UV texture coordinates 

    :type: str
    '''

    warp_factor: float = None
    '''Amount texture affects texture coordinates of next channels 

    :type: float
    '''


class MaterialTextureSlots:
    '''Collection of texture slots '''

    pass


class MaterialVolume:
    '''Volume rendering settings for a Material data-block '''

    asymmetry: float = None
    '''Back scattering (-1.0) to Forward scattering (1.0) and the range in between 

    :type: float
    '''

    cache_resolution: int = None
    '''Resolution of the voxel grid, low resolutions are faster, high resolutions use more memory 

    :type: int
    '''

    density: float = None
    '''The base density of the volume 

    :type: float
    '''

    density_scale: float = None
    '''Multiplier for the material’s density 

    :type: float
    '''

    depth_threshold: float = None
    '''Stop ray marching early if transmission drops below this luminance - higher values give speedups in dense volumes at the expense of accuracy 

    :type: float
    '''

    emission: float = None
    '''Amount of light that gets emitted by the volume 

    :type: float
    '''

    emission_color: float = None
    '''Color of emitted light 

    :type: float
    '''

    light_method: typing.Union[int, str] = None
    '''Method of shading, attenuating, and scattering light through the volume 

    :type: typing.Union[int, str]
    '''

    ms_diffusion: float = None
    '''Diffusion factor, the strength of the blurring effect 

    :type: float
    '''

    ms_intensity: float = None
    '''Multiplier for multiple scattered light energy 

    :type: float
    '''

    ms_spread: float = None
    '''Proportional distance over which the light is diffused 

    :type: float
    '''

    reflection: float = None
    '''Multiplier to make out-scattered light brighter or darker (non-physically correct) 

    :type: float
    '''

    reflection_color: float = None
    '''Color of light scattered out of the volume (does not affect transmission) 

    :type: float
    '''

    scattering: float = None
    '''Amount of light that gets scattered out by the volume - the more out-scattering, the shallower the light will penetrate 

    :type: float
    '''

    step_method: typing.Union[int, str] = None
    '''Method of calculating the steps through the volume 

    :type: typing.Union[int, str]
    '''

    step_size: float = None
    '''Distance between subsequent volume depth samples 

    :type: float
    '''

    transmission_color: float = None
    '''Result color of the volume, after other light has been scattered/absorbed 

    :type: float
    '''

    use_external_shadows: bool = None
    '''Receive shadows from sources outside the volume (temporary) 

    :type: bool
    '''

    use_light_cache: bool = None
    '''Pre-calculate the shading information into a voxel grid, speeds up shading at slightly less accuracy 

    :type: bool
    '''


class Menu:
    '''Editor menu containing buttons '''

    bl_description: str = None
    '''

    :type: str
    '''

    bl_idname: str = None
    '''If this is set, the menu gets a custom ID, otherwise it takes the name of the class used to define the menu (for example, if the class name is “OBJECT_MT_hello”, and bl_idname is not set by the script, then bl_idname = “OBJECT_MT_hello”) 

    :type: str
    '''

    bl_label: str = None
    '''The menu label 

    :type: str
    '''

    bl_translation_context: str = None
    '''

    :type: str
    '''

    layout: 'UILayout' = None
    '''Defines the structure of the menu in the UI 

    :type: 'UILayout'
    '''

    def draw(self, context):
        '''Draw UI elements into the menu UI layout 

        '''
        pass

    def draw_preset(self, context):
        '''Optionally: - preset_extensions (set of strings) - preset_operator_defaults (dict of keyword args) 

        '''
        pass

    def path_menu(self,
                  searchpaths: list,
                  operator: str,
                  *,
                  props_default: dict = None,
                  prop_filepath: str = 'filepath',
                  filter_ext: str = None,
                  filter_path=None,
                  display_name: str = None):
        '''Populate a menu from a list of paths. 

        :param searchpaths: Paths to scan. 
        :type searchpaths: list
        :param operator: The operator id to use with each file. 
        :type operator: str
        :param prop_filepath: Optional operator filepath property (defaults to “filepath”). 
        :type prop_filepath: str
        :param props_default: Properties to assign to each operator. 
        :type props_default: dict
        :param filter_ext: Optional callback that takes the file extensions.Returning false excludes the file from the list. 
        :type filter_ext: str
        :param display_name: Optional callback that takes the full path, returns the name to display. 
        :type display_name: str
        '''
        pass


class Mesh:
    '''Mesh data-block defining geometric surfaces '''

    animation_data: 'AnimData' = None
    '''Animation data for this data-block 

    :type: 'AnimData'
    '''

    auto_smooth_angle: float = None
    '''Maximum angle between face normals that will be considered as smooth (unused if custom split normals data are available) 

    :type: float
    '''

    auto_texspace: bool = None
    '''Adjust active object’s texture space automatically when transforming object 

    :type: bool
    '''

    cycles: 'CyclesMeshSettings' = None
    '''Cycles mesh settings 

    :type: 'CyclesMeshSettings'
    '''

    edges: typing.List['MeshEdge'] = None
    '''Edges of the mesh 

    :type: typing.List['MeshEdge']
    '''

    has_custom_normals: bool = None
    '''True if there are custom split normals data in this mesh 

    :type: bool
    '''

    is_editmode: bool = None
    '''True when used in editmode 

    :type: bool
    '''

    loops: typing.List['MeshLoops'] = None
    '''Loops of the mesh (polygon corners) 

    :type: typing.List['MeshLoops']
    '''

    materials: typing.List['Material'] = None
    '''

    :type: typing.List['Material']
    '''

    polygon_layers_float: typing.List['MeshPolygonFloatPropertyLayer'] = None
    '''

    :type: typing.List['MeshPolygonFloatPropertyLayer']
    '''

    polygon_layers_int: typing.List['MeshPolygonIntPropertyLayer'] = None
    '''

    :type: typing.List['MeshPolygonIntPropertyLayer']
    '''

    polygon_layers_string: typing.List['MeshPolygonStringPropertyLayer'] = None
    '''

    :type: typing.List['MeshPolygonStringPropertyLayer']
    '''

    polygons: typing.List['MeshPolygons'] = None
    '''Polygons of the mesh 

    :type: typing.List['MeshPolygons']
    '''

    shape_keys: 'Key' = None
    '''

    :type: 'Key'
    '''

    show_double_sided: bool = None
    '''Display the mesh with double or single sided lighting (OpenGL only) 

    :type: bool
    '''

    show_edge_bevel_weight: bool = None
    '''Display weights created for the Bevel modifier 

    :type: bool
    '''

    show_edge_crease: bool = None
    '''Display creases created for Subdivision Surface modifier 

    :type: bool
    '''

    show_edge_seams: bool = None
    '''Display UV unwrapping seams 

    :type: bool
    '''

    show_edge_sharp: bool = None
    '''Display sharp edges, used with the Edge Split modifier 

    :type: bool
    '''

    show_edges: bool = None
    '''Display selected edges using highlights in the 3D view and UV editor 

    :type: bool
    '''

    show_extra_edge_angle: bool = None
    '''Display selected edge angle, using global values when set in the transform panel 

    :type: bool
    '''

    show_extra_edge_length: bool = None
    '''Display selected edge lengths, using global values when set in the transform panel 

    :type: bool
    '''

    show_extra_face_angle: bool = None
    '''Display the angles in the selected edges, using global values when set in the transform panel 

    :type: bool
    '''

    show_extra_face_area: bool = None
    '''Display the area of selected faces, using global values when set in the transform panel 

    :type: bool
    '''

    show_extra_indices: bool = None
    '''Display the index numbers of selected vertices, edges, and faces 

    :type: bool
    '''

    show_faces: bool = None
    '''Display all faces as shades in the 3D view and UV editor 

    :type: bool
    '''

    show_freestyle_edge_marks: bool = None
    '''Display Freestyle edge marks, used with the Freestyle renderer 

    :type: bool
    '''

    show_freestyle_face_marks: bool = None
    '''Display Freestyle face marks, used with the Freestyle renderer 

    :type: bool
    '''

    show_normal_face: bool = None
    '''Display face normals as lines 

    :type: bool
    '''

    show_normal_loop: bool = None
    '''Display vertex-per-face normals as lines 

    :type: bool
    '''

    show_normal_vertex: bool = None
    '''Display vertex normals as lines 

    :type: bool
    '''

    show_statvis: bool = None
    '''Display statistical information about the mesh 

    :type: bool
    '''

    show_weight: bool = None
    '''Draw weights in editmode 

    :type: bool
    '''

    skin_vertices: typing.List['MeshSkinVertexLayer'] = None
    '''All skin vertices 

    :type: typing.List['MeshSkinVertexLayer']
    '''

    tessface_uv_textures: typing.List['TessfaceUVTextures'] = None
    '''All UV maps for tessellated faces (read-only, for use by renderers) 

    :type: typing.List['TessfaceUVTextures']
    '''

    tessface_vertex_colors: typing.List['VertexColors'] = None
    '''All tessellated face colors (read-only, for use by renderers) 

    :type: typing.List['VertexColors']
    '''

    tessfaces: typing.List['MeshTessFaces'] = None
    '''Tessellated faces of the mesh (derived from polygons) 

    :type: typing.List['MeshTessFaces']
    '''

    texco_mesh: 'Mesh' = None
    '''Derive texture coordinates from another mesh 

    :type: 'Mesh'
    '''

    texspace_location: float = None
    '''Texture space location 

    :type: float
    '''

    texspace_size: float = None
    '''Texture space size 

    :type: float
    '''

    texture_mesh: 'Mesh' = None
    '''Use another mesh for texture indices (vertex indices must be aligned) 

    :type: 'Mesh'
    '''

    total_edge_sel: int = None
    '''Selected edge count in editmode 

    :type: int
    '''

    total_face_sel: int = None
    '''Selected face count in editmode 

    :type: int
    '''

    total_vert_sel: int = None
    '''Selected vertex count in editmode 

    :type: int
    '''

    use_auto_smooth: bool = None
    '''Auto smooth (based on smooth/sharp faces/edges and angle between faces), or use custom split normals data if available 

    :type: bool
    '''

    use_auto_texspace: bool = None
    '''Adjust active object’s texture space automatically when transforming object 

    :type: bool
    '''

    use_customdata_edge_bevel: bool = None
    '''

    :type: bool
    '''

    use_customdata_edge_crease: bool = None
    '''

    :type: bool
    '''

    use_customdata_vertex_bevel: bool = None
    '''

    :type: bool
    '''

    use_mirror_topology: bool = None
    '''Use topology based mirroring (for when both sides of mesh have matching, unique topology) 

    :type: bool
    '''

    use_mirror_x: bool = None
    '''X Axis mirror editing 

    :type: bool
    '''

    use_paint_mask: bool = None
    '''Face selection masking for painting 

    :type: bool
    '''

    use_paint_mask_vertex: bool = None
    '''Vertex selection masking for painting (weight paint only) 

    :type: bool
    '''

    uv_layer_clone: 'MeshUVLoopLayer' = None
    '''UV loop layer to be used as cloning source 

    :type: 'MeshUVLoopLayer'
    '''

    uv_layer_clone_index: int = None
    '''Clone UV loop layer index 

    :type: int
    '''

    uv_layer_stencil: 'MeshUVLoopLayer' = None
    '''UV loop layer to mask the painted area 

    :type: 'MeshUVLoopLayer'
    '''

    uv_layer_stencil_index: int = None
    '''Mask UV loop layer index 

    :type: int
    '''

    uv_layers: typing.List['MeshUVLoopLayer'] = None
    '''All UV loop layers 

    :type: typing.List['MeshUVLoopLayer']
    '''

    uv_texture_clone: 'MeshTexturePolyLayer' = None
    '''UV map to be used as cloning source 

    :type: 'MeshTexturePolyLayer'
    '''

    uv_texture_clone_index: int = None
    '''Clone UV map index 

    :type: int
    '''

    uv_texture_stencil: 'MeshTexturePolyLayer' = None
    '''UV map to mask the painted area 

    :type: 'MeshTexturePolyLayer'
    '''

    uv_texture_stencil_index: int = None
    '''Mask UV map index 

    :type: int
    '''

    uv_textures: typing.List['MeshTexturePolyLayer'] = None
    '''All UV maps 

    :type: typing.List['MeshTexturePolyLayer']
    '''

    vertex_colors: typing.List['MeshLoopColorLayer'] = None
    '''All vertex colors 

    :type: typing.List['MeshLoopColorLayer']
    '''

    vertex_layers_float: typing.List['MeshVertexFloatPropertyLayer'] = None
    '''

    :type: typing.List['MeshVertexFloatPropertyLayer']
    '''

    vertex_layers_int: typing.List['VertexIntProperties'] = None
    '''

    :type: typing.List['VertexIntProperties']
    '''

    vertex_layers_string: typing.List['MeshVertexStringPropertyLayer'] = None
    '''

    :type: typing.List['MeshVertexStringPropertyLayer']
    '''

    vertex_paint_masks: typing.List['MeshPaintMaskLayer'] = None
    '''Vertex paint mask 

    :type: typing.List['MeshPaintMaskLayer']
    '''

    vertices: typing.List['MeshVertex'] = None
    '''Vertices of the mesh 

    :type: typing.List['MeshVertex']
    '''

    edge_keys = None
    '''(readonly) '''

    def transform(self, matrix: float, shape_keys: bool = False):
        '''Transform mesh vertices by a matrix (Warning: inverts normals if matrix is negative) 

        :param matrix: Matrix 
        :type matrix: float
        :param shape_keys: Transform Shape Keys 
        :type shape_keys: bool
        '''
        pass

    def flip_normals(self, ):
        '''Invert winding of all polygons (clears tessellation, does not handle custom normals) 

        '''
        pass

    def calc_normals(self, ):
        '''Calculate vertex normals 

        '''
        pass

    def create_normals_split(self, ):
        '''Empty split vertex normals 

        '''
        pass

    def calc_normals_split(self, ):
        '''Calculate split vertex normals, which preserve sharp edges 

        '''
        pass

    def free_normals_split(self, ):
        '''Free split vertex normals 

        '''
        pass

    def split_faces(self, free_loop_normals: bool = True):
        '''Split faces based on the edge angle 

        :param free_loop_normals: Free Loop Notmals, Free loop normals custom data layer 
        :type free_loop_normals: bool
        '''
        pass

    def calc_tangents(self, uvmap: str = ""):
        '''Compute tangents and bitangent signs, to be used together with the split normals to get a complete tangent space for normal mapping (split normals are also computed if not yet present) 

        :param uvmap: Name of the UV map to use for tangent space computation 
        :type uvmap: str
        '''
        pass

    def free_tangents(self, ):
        '''Free tangents 

        '''
        pass

    def calc_tessface(self, free_mpoly: bool = False):
        '''Calculate face tessellation (supports editmode too) 

        :param free_mpoly: Free MPoly, Free data used by polygons and loops. WARNING: This destructive operation removes regular faces, only used on temporary mesh data-blocks to reduce memory footprint of render engines and export scripts 
        :type free_mpoly: bool
        '''
        pass

    def calc_smooth_groups(self, use_bitflags: bool = False):
        '''Calculate smooth groups from sharp edges 

        :param use_bitflags: Produce bitflags groups instead of simple numeric values 
        :type use_bitflags: bool
        '''
        pass

    def normals_split_custom_set(self, normals: float):
        '''Define custom split normals of this mesh (use zero-vectors to keep auto ones) 

        :param normals: Normals 
        :type normals: float
        '''
        pass

    def normals_split_custom_set_from_vertices(self, normals: float):
        '''Define custom split normals of this mesh, from vertices’ normals (use zero-vectors to keep auto ones) 

        :param normals: Normals 
        :type normals: float
        '''
        pass

    def update(self, calc_edges: bool = False, calc_tessface: bool = False):
        '''update 

        :param calc_edges: Calculate Edges, Force recalculation of edges 
        :type calc_edges: bool
        :param calc_tessface: Calculate Tessellation, Force recalculation of tessellation faces 
        :type calc_tessface: bool
        '''
        pass

    def unit_test_compare(self, mesh: 'Mesh' = None) -> str:
        '''unit_test_compare 

        :param mesh: Mesh to compare to 
        :type mesh: 'Mesh'
        :rtype: str
        :return:  Return value, String description of result of comparison 
        '''
        pass

    def validate(self, verbose: bool = False,
                 clean_customdata: bool = True) -> bool:
        '''Validate geometry, return True when the mesh has had invalid geometry corrected/removed 

        :param verbose: Verbose, Output information about the errors found 
        :type verbose: bool
        :param clean_customdata: Clean Custom Data, Remove temp/cached custom-data layers, like e.g. normals… 
        :type clean_customdata: bool
        :rtype: bool
        :return:  Result 
        '''
        pass

    def validate_material_indices(self, ) -> bool:
        '''Validate material indices of polygons, return True when the mesh has had invalid indices corrected (to default 0) 

        :rtype: bool
        :return:  Result 
        '''
        pass

    def from_pydata(self, vertices: 'bpy.context.object',
                    edges: 'bpy.context.object', faces: 'bpy.context.object'):
        '''Make a mesh from a list of vertices/edges/faces Until we have a nicer way to make geometry, use this. 

        :param vertices: float triplets each representing (X, Y, Z) eg: [(0.0, 1.0, 0.5), …]. 
        :type vertices: 'bpy.context.object'
        :param edges: int pairs, each pair contains two indices to the vertices argument. eg: [(1, 2), …] 
        :type edges: 'bpy.context.object'
        :param faces: iterator of faces, each faces contains three or more indices to the vertices argument. eg: [(5, 6, 8, 9), (1, 2, 3), …] 
        :type faces: 'bpy.context.object'
        '''
        pass


class MeshCacheModifier:
    '''Cache Mesh '''

    cache_format: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    deform_mode: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    eval_factor: float = None
    '''Evaluation time in seconds 

    :type: float
    '''

    eval_frame: float = None
    '''The frame to evaluate (starting at 0) 

    :type: float
    '''

    eval_time: float = None
    '''Evaluation time in seconds 

    :type: float
    '''

    factor: float = None
    '''Influence of the deformation 

    :type: float
    '''

    filepath: str = None
    '''Path to external displacements file 

    :type: str
    '''

    flip_axis: typing.Set[typing.Union[int, str]] = None
    '''

    :type: typing.Set[typing.Union[int, str]]
    '''

    forward_axis: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    frame_scale: float = None
    '''Evaluation time in seconds 

    :type: float
    '''

    frame_start: float = None
    '''Add this to the start frame 

    :type: float
    '''

    interpolation: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    play_mode: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    time_mode: typing.Union[int, str] = None
    '''Method to control playback time 

    :type: typing.Union[int, str]
    '''

    up_axis: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''


class MeshColor:
    '''Vertex colors for a face in a Mesh '''

    color1: float = None
    '''

    :type: float
    '''

    color2: float = None
    '''

    :type: float
    '''

    color3: float = None
    '''

    :type: float
    '''

    color4: float = None
    '''

    :type: float
    '''


class MeshColorLayer:
    '''Layer of vertex colors in a Mesh data-block '''

    active: bool = None
    '''Sets the layer as active for display and editing 

    :type: bool
    '''

    active_render: bool = None
    '''Sets the layer as active for rendering 

    :type: bool
    '''

    data: typing.List['MeshColor'] = None
    '''

    :type: typing.List['MeshColor']
    '''

    name: str = None
    '''Name of Vertex color layer 

    :type: str
    '''


class MeshDeformModifier:
    '''Mesh deformation modifier to deform with other meshes '''

    invert_vertex_group: bool = None
    '''Invert vertex group influence 

    :type: bool
    '''

    is_bound: bool = None
    '''Whether geometry has been bound to control cage 

    :type: bool
    '''

    object: 'Object' = None
    '''Mesh object to deform with 

    :type: 'Object'
    '''

    precision: int = None
    '''The grid size for binding 

    :type: int
    '''

    use_dynamic_bind: bool = None
    '''Recompute binding dynamically on top of other deformers (slower and more memory consuming) 

    :type: bool
    '''

    vertex_group: str = None
    '''Vertex group name 

    :type: str
    '''


class MeshEdge:
    '''Edge in a Mesh data-block '''

    bevel_weight: float = None
    '''Weight used by the Bevel modifier 

    :type: float
    '''

    crease: float = None
    '''Weight used by the Subdivision Surface modifier for creasing 

    :type: float
    '''

    hide: bool = None
    '''

    :type: bool
    '''

    index: int = None
    '''Index of this edge 

    :type: int
    '''

    is_loose: bool = None
    '''Loose edge 

    :type: bool
    '''

    select: bool = None
    '''

    :type: bool
    '''

    use_edge_sharp: bool = None
    '''Sharp edge for the Edge Split modifier 

    :type: bool
    '''

    use_freestyle_mark: bool = None
    '''Edge mark for Freestyle line rendering 

    :type: bool
    '''

    use_seam: bool = None
    '''Seam edge for UV unwrapping 

    :type: bool
    '''

    vertices: int = None
    '''Vertex indices 

    :type: int
    '''

    key = None
    '''(readonly) '''


class MeshEdges:
    '''Collection of mesh edges '''

    def add(self, count: int = 0):
        '''add 

        :param count: Count, Number of edges to add 
        :type count: int
        '''
        pass


class MeshLoop:
    '''Loop in a Mesh data-block '''

    bitangent: float = None
    '''Bitangent vector of this vertex for this polygon (must be computed beforehand using calc_tangents, use it only if really needed, slower access than bitangent_sign) 

    :type: float
    '''

    bitangent_sign: float = None
    '''Sign of the bitangent vector of this vertex for this polygon (must be computed beforehand using calc_tangents, bitangent = bitangent_sign * cross(normal, tangent)) 

    :type: float
    '''

    edge_index: int = None
    '''Edge index 

    :type: int
    '''

    index: int = None
    '''Index of this loop 

    :type: int
    '''

    normal: float = None
    '''Local space unit length split normal vector of this vertex for this polygon (must be computed beforehand using calc_normals_split or calc_tangents) 

    :type: float
    '''

    tangent: float = None
    '''Local space unit length tangent vector of this vertex for this polygon (must be computed beforehand using calc_tangents) 

    :type: float
    '''

    vertex_index: int = None
    '''Vertex index 

    :type: int
    '''


class MeshLoopColor:
    '''Vertex loop colors in a Mesh '''

    color: float = None
    '''

    :type: float
    '''


class MeshLoopColorLayer:
    '''Layer of vertex colors in a Mesh data-block '''

    active: bool = None
    '''Sets the layer as active for display and editing 

    :type: bool
    '''

    active_render: bool = None
    '''Sets the layer as active for rendering 

    :type: bool
    '''

    data: typing.List['MeshLoopColor'] = None
    '''

    :type: typing.List['MeshLoopColor']
    '''

    name: str = None
    '''Name of Vertex color layer 

    :type: str
    '''


class MeshLoops:
    '''Collection of mesh loops '''

    def add(self, count: int = 0):
        '''add 

        :param count: Count, Number of loops to add 
        :type count: int
        '''
        pass


class MeshPaintMaskLayer:
    '''Per-vertex paint mask data '''

    data: typing.List['MeshPaintMaskProperty'] = None
    '''

    :type: typing.List['MeshPaintMaskProperty']
    '''


class MeshPaintMaskProperty:
    '''Floating point paint mask value '''

    value: float = None
    '''

    :type: float
    '''


class MeshPolygon:
    '''Polygon in a Mesh data-block '''

    area: float = None
    '''Read only area of this polygon 

    :type: float
    '''

    center: float = None
    '''Center of this polygon 

    :type: float
    '''

    hide: bool = None
    '''

    :type: bool
    '''

    index: int = None
    '''Index of this polygon 

    :type: int
    '''

    loop_start: int = None
    '''Index of the first loop of this polygon 

    :type: int
    '''

    loop_total: int = None
    '''Number of loops used by this polygon 

    :type: int
    '''

    material_index: int = None
    '''

    :type: int
    '''

    normal: float = None
    '''Local space unit length normal vector for this polygon 

    :type: float
    '''

    select: bool = None
    '''

    :type: bool
    '''

    use_freestyle_mark: bool = None
    '''Face mark for Freestyle line rendering 

    :type: bool
    '''

    use_smooth: bool = None
    '''

    :type: bool
    '''

    vertices: int = None
    '''Vertex indices 

    :type: int
    '''

    edge_keys = None
    '''(readonly) '''

    loop_indices = None
    '''(readonly) '''

    def flip(self, ):
        '''Invert winding of this polygon (flip its normal) 

        '''
        pass


class MeshPolygonFloatProperty:
    '''User defined floating point number value in a float properties layer '''

    value: float = None
    '''

    :type: float
    '''


class MeshPolygonFloatPropertyLayer:
    '''User defined layer of floating point number values '''

    data: typing.List['MeshPolygonFloatProperty'] = None
    '''

    :type: typing.List['MeshPolygonFloatProperty']
    '''

    name: str = None
    '''

    :type: str
    '''


class MeshPolygonIntProperty:
    '''User defined integer number value in an integer properties layer '''

    value: int = None
    '''

    :type: int
    '''


class MeshPolygonIntPropertyLayer:
    '''User defined layer of integer number values '''

    data: typing.List['MeshPolygonIntProperty'] = None
    '''

    :type: typing.List['MeshPolygonIntProperty']
    '''

    name: str = None
    '''

    :type: str
    '''


class MeshPolygonStringProperty:
    '''User defined string text value in a string properties layer '''

    value: str = None
    '''

    :type: str
    '''


class MeshPolygonStringPropertyLayer:
    '''User defined layer of string text values '''

    data: typing.List['MeshPolygonStringProperty'] = None
    '''

    :type: typing.List['MeshPolygonStringProperty']
    '''

    name: str = None
    '''

    :type: str
    '''


class MeshPolygons:
    '''Collection of mesh polygons '''

    active: int = None
    '''The active polygon for this mesh 

    :type: int
    '''

    def add(self, count: int = 0):
        '''add 

        :param count: Count, Number of polygons to add 
        :type count: int
        '''
        pass


class MeshSequenceCacheModifier:
    '''Cache Mesh '''

    cache_file: 'CacheFile' = None
    '''

    :type: 'CacheFile'
    '''

    object_path: str = None
    '''Path to the object in the Alembic archive used to lookup geometric data 

    :type: str
    '''

    read_data: typing.Set[typing.Union[int, str]] = None
    '''

    :type: typing.Set[typing.Union[int, str]]
    '''


class MeshSkinVertex:
    '''Per-vertex skin data for use with the Skin modifier '''

    radius: float = None
    '''Radius of the skin 

    :type: float
    '''

    use_loose: bool = None
    '''If vertex has multiple adjacent edges, it is hulled to them directly 

    :type: bool
    '''

    use_root: bool = None
    '''Vertex is a root for rotation calculations and armature generation 

    :type: bool
    '''


class MeshSkinVertexLayer:
    '''Per-vertex skin data for use with the Skin modifier '''

    data: typing.List['MeshSkinVertex'] = None
    '''

    :type: typing.List['MeshSkinVertex']
    '''

    name: str = None
    '''Name of skin layer 

    :type: str
    '''


class MeshStatVis:
    distort_max: float = None
    '''Maximum angle to display 

    :type: float
    '''

    distort_min: float = None
    '''Minimum angle to display 

    :type: float
    '''

    overhang_axis: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    overhang_max: float = None
    '''Maximum angle to display 

    :type: float
    '''

    overhang_min: float = None
    '''Minimum angle to display 

    :type: float
    '''

    sharp_max: float = None
    '''Maximum angle to display 

    :type: float
    '''

    sharp_min: float = None
    '''Minimum angle to display 

    :type: float
    '''

    thickness_max: float = None
    '''Maximum for measuring thickness 

    :type: float
    '''

    thickness_min: float = None
    '''Minimum for measuring thickness 

    :type: float
    '''

    thickness_samples: int = None
    '''Number of samples to test per face 

    :type: int
    '''

    type: typing.Union[int, str] = None
    '''Type of data to visualize/check 

    :type: typing.Union[int, str]
    '''


class MeshTessFace:
    '''TessFace in a Mesh data-block '''

    area: float = None
    '''Read only area of this face 

    :type: float
    '''

    hide: bool = None
    '''

    :type: bool
    '''

    index: int = None
    '''Index of this face 

    :type: int
    '''

    material_index: int = None
    '''

    :type: int
    '''

    normal: float = None
    '''Local space unit length normal vector for this face 

    :type: float
    '''

    select: bool = None
    '''

    :type: bool
    '''

    split_normals: float = None
    '''Local space unit length split normals vectors of the vertices of this face (must be computed beforehand using calc_normals_split or calc_tangents, and then calc_tessface) 

    :type: float
    '''

    use_smooth: bool = None
    '''

    :type: bool
    '''

    vertices: int = None
    '''Vertex indices 

    :type: int
    '''

    vertices_raw: int = None
    '''Fixed size vertex indices array 

    :type: int
    '''

    center = None
    '''The midpoint of the face. (readonly) '''

    edge_keys = None
    '''(readonly) '''


class MeshTessFaces:
    '''Collection of mesh faces '''

    active: int = None
    '''The active face for this mesh 

    :type: int
    '''

    def add(self, count: int = 0):
        '''add 

        :param count: Count, Number of faces to add 
        :type count: int
        '''
        pass


class MeshTextureFace:
    '''UV map and image texture for a face '''

    image: 'Image' = None
    '''

    :type: 'Image'
    '''

    uv: float = None
    '''

    :type: float
    '''

    uv1: float = None
    '''

    :type: float
    '''

    uv2: float = None
    '''

    :type: float
    '''

    uv3: float = None
    '''

    :type: float
    '''

    uv4: float = None
    '''

    :type: float
    '''

    uv_raw: float = None
    '''Fixed size UV coordinates array 

    :type: float
    '''


class MeshTextureFaceLayer:
    '''UV map with assigned image textures in a Mesh data-block '''

    active: bool = None
    '''Set the map as active for display and editing 

    :type: bool
    '''

    active_clone: bool = None
    '''Set the map as active for cloning 

    :type: bool
    '''

    active_render: bool = None
    '''Set the map as active for rendering 

    :type: bool
    '''

    data: typing.List['MeshTextureFace'] = None
    '''

    :type: typing.List['MeshTextureFace']
    '''

    name: str = None
    '''Name of UV map 

    :type: str
    '''


class MeshTexturePoly:
    '''UV map and image texture for a face '''

    image: 'Image' = None
    '''

    :type: 'Image'
    '''


class MeshTexturePolyLayer:
    '''UV map with assigned image textures in a Mesh data-block '''

    active: bool = None
    '''Set the map as active for display and editing 

    :type: bool
    '''

    active_clone: bool = None
    '''Set the map as active for cloning 

    :type: bool
    '''

    active_render: bool = None
    '''Set the map as active for rendering 

    :type: bool
    '''

    data: typing.List['MeshTexturePoly'] = None
    '''

    :type: typing.List['MeshTexturePoly']
    '''

    name: str = None
    '''Name of UV map 

    :type: str
    '''


class MeshUVLoop:
    pin_uv: bool = None
    '''

    :type: bool
    '''

    select: bool = None
    '''

    :type: bool
    '''

    select_edge: bool = None
    '''

    :type: bool
    '''

    uv: float = None
    '''

    :type: float
    '''


class MeshUVLoopLayer:
    data: typing.List['MeshUVLoop'] = None
    '''

    :type: typing.List['MeshUVLoop']
    '''

    name: str = None
    '''Name of UV map 

    :type: str
    '''


class MeshVertex:
    '''Vertex in a Mesh data-block '''

    bevel_weight: float = None
    '''Weight used by the Bevel modifier ‘Only Vertices’ option 

    :type: float
    '''

    co: float = None
    '''

    :type: float
    '''

    groups: typing.List['VertexGroupElement'] = None
    '''Weights for the vertex groups this vertex is member of 

    :type: typing.List['VertexGroupElement']
    '''

    hide: bool = None
    '''

    :type: bool
    '''

    index: int = None
    '''Index of this vertex 

    :type: int
    '''

    normal: float = None
    '''Vertex Normal 

    :type: float
    '''

    select: bool = None
    '''

    :type: bool
    '''

    undeformed_co: float = None
    '''For meshes with modifiers applied, the coordinate of the vertex with no deforming modifiers applied, as used for generated texture coordinates 

    :type: float
    '''


class MeshVertexFloatProperty:
    '''User defined floating point number value in a float properties layer '''

    value: float = None
    '''

    :type: float
    '''


class MeshVertexFloatPropertyLayer:
    '''User defined layer of floating point number values '''

    data: typing.List['MeshVertexFloatProperty'] = None
    '''

    :type: typing.List['MeshVertexFloatProperty']
    '''

    name: str = None
    '''

    :type: str
    '''


class MeshVertexIntProperty:
    '''User defined integer number value in an integer properties layer '''

    value: int = None
    '''

    :type: int
    '''


class MeshVertexIntPropertyLayer:
    '''User defined layer of integer number values '''

    data: typing.List['MeshVertexIntProperty'] = None
    '''

    :type: typing.List['MeshVertexIntProperty']
    '''

    name: str = None
    '''

    :type: str
    '''


class MeshVertexStringProperty:
    '''User defined string text value in a string properties layer '''

    value: str = None
    '''

    :type: str
    '''


class MeshVertexStringPropertyLayer:
    '''User defined layer of string text values '''

    data: typing.List['MeshVertexStringProperty'] = None
    '''

    :type: typing.List['MeshVertexStringProperty']
    '''

    name: str = None
    '''

    :type: str
    '''


class MeshVertices:
    '''Collection of mesh vertices '''

    def add(self, count: int = 0):
        '''add 

        :param count: Count, Number of vertices to add 
        :type count: int
        '''
        pass


class MessageActuator:
    body_message: str = None
    '''Optional, message body Text 

    :type: str
    '''

    body_property: str = None
    '''The message body will be set by the Property Value 

    :type: str
    '''

    body_type: typing.Union[int, str] = None
    '''Toggle message type: either Text or a PropertyName 

    :type: typing.Union[int, str]
    '''

    subject: str = None
    '''Optional, message subject (this is what can be filtered on) 

    :type: str
    '''

    to_property: str = None
    '''Optional, send message to objects with this name only, or empty to broadcast 

    :type: str
    '''


class MessageSensor:
    '''Sensor to detect incoming messages '''

    subject: str = None
    '''Optional subject filter: only accept messages with this subject, or empty to accept all 

    :type: str
    '''


class MetaBall:
    '''Metaball data-block to defined blobby surfaces '''

    animation_data: 'AnimData' = None
    '''Animation data for this data-block 

    :type: 'AnimData'
    '''

    cycles: 'CyclesMeshSettings' = None
    '''Cycles mesh settings 

    :type: 'CyclesMeshSettings'
    '''

    elements: typing.List['MetaElement'] = None
    '''Meta elements 

    :type: typing.List['MetaElement']
    '''

    is_editmode: bool = None
    '''True when used in editmode 

    :type: bool
    '''

    materials: typing.List['Material'] = None
    '''

    :type: typing.List['Material']
    '''

    render_resolution: float = None
    '''Polygonization resolution in rendering 

    :type: float
    '''

    resolution: float = None
    '''Polygonization resolution in the 3D viewport 

    :type: float
    '''

    texspace_location: float = None
    '''Texture space location 

    :type: float
    '''

    texspace_size: float = None
    '''Texture space size 

    :type: float
    '''

    threshold: float = None
    '''Influence of meta elements 

    :type: float
    '''

    update_method: typing.Union[int, str] = None
    '''Metaball edit update behavior 

    :type: typing.Union[int, str]
    '''

    use_auto_texspace: bool = None
    '''Adjust active object’s texture space automatically when transforming object 

    :type: bool
    '''

    def transform(self, matrix: float):
        '''Transform meta elements by a matrix 

        :param matrix: Matrix 
        :type matrix: float
        '''
        pass


class MetaBallElements:
    '''Collection of metaball elements '''

    active: 'MetaElement' = None
    '''Last selected element 

    :type: 'MetaElement'
    '''

    def new(self, type: typing.Union[int, str] = 'BALL') -> 'MetaElement':
        '''Add a new element to the metaball 

        :param type: type for the new meta-element 
        :type type: typing.Union[int, str]
        :rtype: 'MetaElement'
        :return:  The newly created meta-element 
        '''
        pass

    def remove(self, element: 'MetaElement'):
        '''Remove an element from the metaball 

        :param element: The element to remove 
        :type element: 'MetaElement'
        '''
        pass

    def clear(self, ):
        '''Remove all elements from the metaball 

        '''
        pass


class MetaElement:
    '''Blobby element in a Metaball data-block '''

    co: float = None
    '''

    :type: float
    '''

    hide: bool = None
    '''Hide element 

    :type: bool
    '''

    radius: float = None
    '''

    :type: float
    '''

    rotation: float = None
    '''Normalized quaternion rotation 

    :type: float
    '''

    size_x: float = None
    '''Size of element, use of components depends on element type 

    :type: float
    '''

    size_y: float = None
    '''Size of element, use of components depends on element type 

    :type: float
    '''

    size_z: float = None
    '''Size of element, use of components depends on element type 

    :type: float
    '''

    stiffness: float = None
    '''Stiffness defines how much of the element to fill 

    :type: float
    '''

    type: typing.Union[int, str] = None
    '''Metaball types 

    :type: typing.Union[int, str]
    '''

    use_negative: bool = None
    '''Set metaball as negative one 

    :type: bool
    '''


class MetaSequence:
    '''Sequence strip to group other strips as a single sequence strip '''

    alpha_mode: typing.Union[int, str] = None
    '''Representation of alpha information in the RGBA pixels 

    :type: typing.Union[int, str]
    '''

    animation_offset_end: int = None
    '''Animation end offset (trim end) 

    :type: int
    '''

    animation_offset_start: int = None
    '''Animation start offset (trim start) 

    :type: int
    '''

    color_multiply: float = None
    '''

    :type: float
    '''

    color_saturation: float = None
    '''Adjust the intensity of the input’s color 

    :type: float
    '''

    crop: 'SequenceCrop' = None
    '''

    :type: 'SequenceCrop'
    '''

    proxy: 'SequenceProxy' = None
    '''

    :type: 'SequenceProxy'
    '''

    sequences: typing.List['Sequence'] = None
    '''

    :type: typing.List['Sequence']
    '''

    strobe: float = None
    '''Only display every nth frame 

    :type: float
    '''

    transform: 'SequenceTransform' = None
    '''

    :type: 'SequenceTransform'
    '''

    use_crop: bool = None
    '''Crop image before processing 

    :type: bool
    '''

    use_deinterlace: bool = None
    '''Remove fields from video movies 

    :type: bool
    '''

    use_flip_x: bool = None
    '''Flip on the X axis 

    :type: bool
    '''

    use_flip_y: bool = None
    '''Flip on the Y axis 

    :type: bool
    '''

    use_float: bool = None
    '''Convert input to float data 

    :type: bool
    '''

    use_proxy: bool = None
    '''Use a preview proxy and/or timecode index for this strip 

    :type: bool
    '''

    use_reverse_frames: bool = None
    '''Reverse frame order 

    :type: bool
    '''

    use_translation: bool = None
    '''Translate image before processing 

    :type: bool
    '''


class MirrorModifier:
    '''Mirroring modifier '''

    merge_threshold: float = None
    '''Distance within which mirrored vertices are merged 

    :type: float
    '''

    mirror_object: 'Object' = None
    '''Object to use as mirror 

    :type: 'Object'
    '''

    mirror_offset_u: float = None
    '''Amount to offset mirrored UVs from the 0.5 point on the U axis 

    :type: float
    '''

    mirror_offset_v: float = None
    '''Amount to offset mirrored UVs from the 0.5 point on the V axis 

    :type: float
    '''

    use_clip: bool = None
    '''Prevent vertices from going through the mirror during transform 

    :type: bool
    '''

    use_mirror_merge: bool = None
    '''Merge vertices within the merge threshold 

    :type: bool
    '''

    use_mirror_u: bool = None
    '''Mirror the U texture coordinate around the 0.5 point 

    :type: bool
    '''

    use_mirror_v: bool = None
    '''Mirror the V texture coordinate around the 0.5 point 

    :type: bool
    '''

    use_mirror_vertex_groups: bool = None
    '''Mirror vertex groups (e.g. .R->.L) 

    :type: bool
    '''

    use_x: bool = None
    '''Enable X axis mirror 

    :type: bool
    '''

    use_y: bool = None
    '''Enable Y axis mirror 

    :type: bool
    '''

    use_z: bool = None
    '''Enable Z axis mirror 

    :type: bool
    '''


class Modifier:
    '''Modifier affecting the geometry data of an object '''

    name: str = None
    '''Modifier name 

    :type: str
    '''

    show_expanded: bool = None
    '''Set modifier expanded in the user interface 

    :type: bool
    '''

    show_in_editmode: bool = None
    '''Display modifier in Edit mode 

    :type: bool
    '''

    show_on_cage: bool = None
    '''Adjust edit cage to modifier result 

    :type: bool
    '''

    show_render: bool = None
    '''Use modifier during render 

    :type: bool
    '''

    show_viewport: bool = None
    '''Display modifier in viewport 

    :type: bool
    '''

    type: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    use_apply_on_spline: bool = None
    '''Apply this and all preceding deformation modifiers on splines’ points rather than on filled curve/surface 

    :type: bool
    '''


class MotionPath:
    '''Cache of the worldspace positions of an element over a frame range '''

    color: float = None
    '''Custom color for motion path 

    :type: float
    '''

    frame_end: int = None
    '''End frame of the stored range 

    :type: int
    '''

    frame_start: int = None
    '''Starting frame of the stored range 

    :type: int
    '''

    is_modified: bool = None
    '''Path is being edited 

    :type: bool
    '''

    length: int = None
    '''Number of frames cached 

    :type: int
    '''

    line_thickness: int = None
    '''Line thickness for drawing path 

    :type: int
    '''

    lines: bool = None
    '''Draw straight lines between keyframe points 

    :type: bool
    '''

    points: typing.List['MotionPathVert'] = None
    '''Cached positions per frame 

    :type: typing.List['MotionPathVert']
    '''

    use_bone_head: bool = None
    '''For PoseBone paths, use the bone head location when calculating this path 

    :type: bool
    '''

    use_custom_color: bool = None
    '''Use custom color for this motion path 

    :type: bool
    '''


class MotionPathVert:
    '''Cached location on path '''

    co: float = None
    '''

    :type: float
    '''

    select: bool = None
    '''Path point is selected for editing 

    :type: bool
    '''


class MouseActuator:
    local_x: bool = None
    '''Apply rotation locally 

    :type: bool
    '''

    local_y: bool = None
    '''Apply rotation locally 

    :type: bool
    '''

    max_x: float = None
    '''Maximum positive rotation allowed by X mouse movement (0 for infinite) 

    :type: float
    '''

    max_y: float = None
    '''Maximum positive rotation allowed by Y mouse movement (0 for infinite) 

    :type: float
    '''

    min_x: float = None
    '''Maximum negative rotation allowed by X mouse movement (0 for infinite) 

    :type: float
    '''

    min_y: float = None
    '''Maximum negative rotation allowed by Y mouse movement (0 for infinite) 

    :type: float
    '''

    mode: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    object_axis_x: typing.Union[int, str] = None
    '''Local object axis mouse movement in the X direction will apply to 

    :type: typing.Union[int, str]
    '''

    object_axis_y: typing.Union[int, str] = None
    '''Local object axis mouse movement in the Y direction will apply to 

    :type: typing.Union[int, str]
    '''

    reset_x: bool = None
    '''Reset the cursor’s X position to the center of the screen space after calculating 

    :type: bool
    '''

    reset_y: bool = None
    '''Reset the cursor’s Y position to the center of the screen space after calculating 

    :type: bool
    '''

    sensitivity_x: float = None
    '''Sensitivity of the X axis 

    :type: float
    '''

    sensitivity_y: float = None
    '''Sensitivity of the Y axis 

    :type: float
    '''

    threshold_x: float = None
    '''Amount of X motion before mouse movement will register 

    :type: float
    '''

    threshold_y: float = None
    '''Amount of Y motion before mouse movement will register 

    :type: float
    '''

    use_axis_x: bool = None
    '''Calculate mouse movement on the X axis 

    :type: bool
    '''

    use_axis_y: bool = None
    '''Calculate mouse movement on the Y axis 

    :type: bool
    '''

    visible: bool = None
    '''Make mouse cursor visible 

    :type: bool
    '''


class MouseSensor:
    '''Sensor to detect mouse events '''

    material: str = None
    '''Only look for objects with this material (blank = all objects) 

    :type: str
    '''

    mouse_event: typing.Union[int, str] = None
    '''Type of event this mouse sensor should trigger on 

    :type: typing.Union[int, str]
    '''

    property: str = None
    '''Only look for objects with this property (blank = all objects) 

    :type: str
    '''

    use_material: typing.Union[int, str] = None
    '''Toggle collision on material or property 

    :type: typing.Union[int, str]
    '''

    use_pulse: bool = None
    '''Moving the mouse over a different object generates a pulse 

    :type: bool
    '''

    use_x_ray: bool = None
    '''Toggle X-Ray option (see through objects that don’t have the property) 

    :type: bool
    '''


class MovieClip:
    '''MovieClip data-block referencing an external movie file '''

    animation_data: 'AnimData' = None
    '''Animation data for this data-block 

    :type: 'AnimData'
    '''

    colorspace_settings: 'ColorManagedInputColorspaceSettings' = None
    '''Input color space settings 

    :type: 'ColorManagedInputColorspaceSettings'
    '''

    display_aspect: float = None
    '''Display Aspect for this clip, does not affect rendering 

    :type: float
    '''

    filepath: str = None
    '''Filename of the movie or sequence file 

    :type: str
    '''

    frame_duration: int = None
    '''Detected duration of movie clip in frames 

    :type: int
    '''

    frame_offset: int = None
    '''Offset of footage first frame relative to it’s file name (affects only how footage is loading, does not change data associated with a clip) 

    :type: int
    '''

    frame_start: int = None
    '''Global scene frame number at which this movie starts playing (affects all data associated with a clip) 

    :type: int
    '''

    grease_pencil: 'GreasePencil' = None
    '''Grease pencil data for this movie clip 

    :type: 'GreasePencil'
    '''

    proxy: 'MovieClipProxy' = None
    '''

    :type: 'MovieClipProxy'
    '''

    size: int = None
    '''Width and height in pixels, zero when image data cant be loaded 

    :type: int
    '''

    source: typing.Union[int, str] = None
    '''Where the clip comes from 

    :type: typing.Union[int, str]
    '''

    tracking: 'MovieTracking' = None
    '''

    :type: 'MovieTracking'
    '''

    use_proxy: bool = None
    '''Use a preview proxy and/or timecode index for this clip 

    :type: bool
    '''

    use_proxy_custom_directory: bool = None
    '''Create proxy images in a custom directory (default is movie location) 

    :type: bool
    '''


class MovieClipProxy:
    '''Proxy parameters for a movie clip '''

    build_100: bool = None
    '''Build proxy resolution 100% of the original footage dimension 

    :type: bool
    '''

    build_25: bool = None
    '''Build proxy resolution 25% of the original footage dimension 

    :type: bool
    '''

    build_50: bool = None
    '''Build proxy resolution 50% of the original footage dimension 

    :type: bool
    '''

    build_75: bool = None
    '''Build proxy resolution 75% of the original footage dimension 

    :type: bool
    '''

    build_free_run: bool = None
    '''Build free run time code index 

    :type: bool
    '''

    build_free_run_rec_date: bool = None
    '''Build free run time code index using Record Date/Time 

    :type: bool
    '''

    build_record_run: bool = None
    '''Build record run time code index 

    :type: bool
    '''

    build_undistorted_100: bool = None
    '''Build proxy resolution 100% of the original undistorted footage dimension 

    :type: bool
    '''

    build_undistorted_25: bool = None
    '''Build proxy resolution 25% of the original undistorted footage dimension 

    :type: bool
    '''

    build_undistorted_50: bool = None
    '''Build proxy resolution 50% of the original undistorted footage dimension 

    :type: bool
    '''

    build_undistorted_75: bool = None
    '''Build proxy resolution 75% of the original undistorted footage dimension 

    :type: bool
    '''

    directory: str = None
    '''Location to store the proxy files 

    :type: str
    '''

    quality: int = None
    '''JPEG quality of proxy images 

    :type: int
    '''

    timecode: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''


class MovieClipScopes:
    '''Scopes for statistical view of a movie clip '''

    pass


class MovieClipSequence:
    '''Sequence strip to load a video from the clip editor '''

    alpha_mode: typing.Union[int, str] = None
    '''Representation of alpha information in the RGBA pixels 

    :type: typing.Union[int, str]
    '''

    animation_offset_end: int = None
    '''Animation end offset (trim end) 

    :type: int
    '''

    animation_offset_start: int = None
    '''Animation start offset (trim start) 

    :type: int
    '''

    color_multiply: float = None
    '''

    :type: float
    '''

    color_saturation: float = None
    '''Adjust the intensity of the input’s color 

    :type: float
    '''

    crop: 'SequenceCrop' = None
    '''

    :type: 'SequenceCrop'
    '''

    stabilize2d: bool = None
    '''Use the 2D stabilized version of the clip 

    :type: bool
    '''

    strobe: float = None
    '''Only display every nth frame 

    :type: float
    '''

    transform: 'SequenceTransform' = None
    '''

    :type: 'SequenceTransform'
    '''

    undistort: bool = None
    '''Use the undistorted version of the clip 

    :type: bool
    '''

    use_crop: bool = None
    '''Crop image before processing 

    :type: bool
    '''

    use_deinterlace: bool = None
    '''Remove fields from video movies 

    :type: bool
    '''

    use_flip_x: bool = None
    '''Flip on the X axis 

    :type: bool
    '''

    use_flip_y: bool = None
    '''Flip on the Y axis 

    :type: bool
    '''

    use_float: bool = None
    '''Convert input to float data 

    :type: bool
    '''

    use_reverse_frames: bool = None
    '''Reverse frame order 

    :type: bool
    '''

    use_translation: bool = None
    '''Translate image before processing 

    :type: bool
    '''


class MovieClipUser:
    '''Parameters defining how a MovieClip data-block is used by another data-block '''

    frame_current: int = None
    '''Current frame number in movie or image sequence 

    :type: int
    '''

    proxy_render_size: typing.Union[int, str] = None
    '''Draw preview using full resolution or different proxy resolutions 

    :type: typing.Union[int, str]
    '''

    use_render_undistorted: bool = None
    '''Render preview using undistorted proxy 

    :type: bool
    '''


class MovieReconstructedCamera:
    '''Match-moving reconstructed camera data from tracker '''

    average_error: float = None
    '''Average error of reconstruction 

    :type: float
    '''

    frame: int = None
    '''Frame number marker is keyframed on 

    :type: int
    '''

    matrix: float = None
    '''Worldspace transformation matrix 

    :type: float
    '''


class MovieSequence:
    '''Sequence strip to load a video '''

    alpha_mode: typing.Union[int, str] = None
    '''Representation of alpha information in the RGBA pixels 

    :type: typing.Union[int, str]
    '''

    animation_offset_end: int = None
    '''Animation end offset (trim end) 

    :type: int
    '''

    animation_offset_start: int = None
    '''Animation start offset (trim start) 

    :type: int
    '''

    color_multiply: float = None
    '''

    :type: float
    '''

    color_saturation: float = None
    '''Adjust the intensity of the input’s color 

    :type: float
    '''

    colorspace_settings: 'ColorManagedInputColorspaceSettings' = None
    '''Input color space settings 

    :type: 'ColorManagedInputColorspaceSettings'
    '''

    crop: 'SequenceCrop' = None
    '''

    :type: 'SequenceCrop'
    '''

    elements: typing.List['SequenceElement'] = None
    '''

    :type: typing.List['SequenceElement']
    '''

    filepath: str = None
    '''

    :type: str
    '''

    mpeg_preseek: int = None
    '''For MPEG movies, preseek this many frames 

    :type: int
    '''

    proxy: 'SequenceProxy' = None
    '''

    :type: 'SequenceProxy'
    '''

    stereo_3d_format: 'Stereo3dFormat' = None
    '''Settings for stereo 3d 

    :type: 'Stereo3dFormat'
    '''

    stream_index: int = None
    '''For files with several movie streams, use the stream with the given index 

    :type: int
    '''

    strobe: float = None
    '''Only display every nth frame 

    :type: float
    '''

    transform: 'SequenceTransform' = None
    '''

    :type: 'SequenceTransform'
    '''

    use_crop: bool = None
    '''Crop image before processing 

    :type: bool
    '''

    use_deinterlace: bool = None
    '''Remove fields from video movies 

    :type: bool
    '''

    use_flip_x: bool = None
    '''Flip on the X axis 

    :type: bool
    '''

    use_flip_y: bool = None
    '''Flip on the Y axis 

    :type: bool
    '''

    use_float: bool = None
    '''Convert input to float data 

    :type: bool
    '''

    use_multiview: bool = None
    '''Use Multiple Views (when available) 

    :type: bool
    '''

    use_proxy: bool = None
    '''Use a preview proxy and/or timecode index for this strip 

    :type: bool
    '''

    use_reverse_frames: bool = None
    '''Reverse frame order 

    :type: bool
    '''

    use_translation: bool = None
    '''Translate image before processing 

    :type: bool
    '''

    views_format: typing.Union[int, str] = None
    '''Mode to load movie views 

    :type: typing.Union[int, str]
    '''


class MovieTracking:
    '''Match-moving data for tracking '''

    active_object_index: int = None
    '''Index of active object 

    :type: int
    '''

    camera: 'MovieTrackingCamera' = None
    '''

    :type: 'MovieTrackingCamera'
    '''

    dopesheet: 'MovieTrackingDopesheet' = None
    '''

    :type: 'MovieTrackingDopesheet'
    '''

    objects: typing.List['MovieTrackingObjects'] = None
    '''Collection of objects in this tracking data object 

    :type: typing.List['MovieTrackingObjects']
    '''

    plane_tracks: typing.List['MovieTrackingPlaneTrack'] = None
    '''Collection of plane tracks in this tracking data object 

    :type: typing.List['MovieTrackingPlaneTrack']
    '''

    reconstruction: 'MovieTrackingReconstruction' = None
    '''

    :type: 'MovieTrackingReconstruction'
    '''

    settings: 'MovieTrackingSettings' = None
    '''

    :type: 'MovieTrackingSettings'
    '''

    stabilization: 'MovieTrackingStabilization' = None
    '''

    :type: 'MovieTrackingStabilization'
    '''

    tracks: typing.List['MovieTrackingTracks'] = None
    '''Collection of tracks in this tracking data object 

    :type: typing.List['MovieTrackingTracks']
    '''


class MovieTrackingCamera:
    '''Match-moving camera data for tracking '''

    distortion_model: typing.Union[int, str] = None
    '''Distortion model used for camera lenses 

    :type: typing.Union[int, str]
    '''

    division_k1: float = None
    '''First coefficient of second order division distortion 

    :type: float
    '''

    division_k2: float = None
    '''First coefficient of second order division distortion 

    :type: float
    '''

    focal_length: float = None
    '''Camera’s focal length 

    :type: float
    '''

    focal_length_pixels: float = None
    '''Camera’s focal length 

    :type: float
    '''

    k1: float = None
    '''First coefficient of third order polynomial radial distortion 

    :type: float
    '''

    k2: float = None
    '''Second coefficient of third order polynomial radial distortion 

    :type: float
    '''

    k3: float = None
    '''Third coefficient of third order polynomial radial distortion 

    :type: float
    '''

    pixel_aspect: float = None
    '''Pixel aspect ratio 

    :type: float
    '''

    principal: float = None
    '''Optical center of lens 

    :type: float
    '''

    sensor_width: float = None
    '''Width of CCD sensor in millimeters 

    :type: float
    '''

    units: typing.Union[int, str] = None
    '''Units used for camera focal length 

    :type: typing.Union[int, str]
    '''


class MovieTrackingDopesheet:
    '''Match-moving dopesheet data '''

    show_hidden: bool = None
    '''Include channels from objects/bone that aren’t visible 

    :type: bool
    '''

    show_only_selected: bool = None
    '''Only include channels relating to selected objects and data 

    :type: bool
    '''

    sort_method: typing.Union[int, str] = None
    '''Method to be used to sort channels in dopesheet view 

    :type: typing.Union[int, str]
    '''

    use_invert_sort: bool = None
    '''Invert sort order of dopesheet channels 

    :type: bool
    '''


class MovieTrackingMarker:
    '''Match-moving marker data for tracking '''

    co: float = None
    '''Marker position at frame in normalized coordinates 

    :type: float
    '''

    frame: int = None
    '''Frame number marker is keyframed on 

    :type: int
    '''

    is_keyed: bool = None
    '''Whether the position of the marker is keyframed or tracked 

    :type: bool
    '''

    mute: bool = None
    '''Is marker muted for current frame 

    :type: bool
    '''

    pattern_bound_box: float = None
    '''Pattern area bounding box in normalized coordinates 

    :type: float
    '''

    pattern_corners: float = None
    '''Array of coordinates which represents pattern’s corners in normalized coordinates relative to marker position 

    :type: float
    '''

    search_max: float = None
    '''Right-bottom corner of search area in normalized coordinates relative to marker position 

    :type: float
    '''

    search_min: float = None
    '''Left-bottom corner of search area in normalized coordinates relative to marker position 

    :type: float
    '''


class MovieTrackingMarkers:
    '''Collection of markers for movie tracking track '''

    def find_frame(self, frame: int,
                   exact: bool = True) -> 'MovieTrackingMarker':
        '''Get marker for specified frame 

        :param frame: Frame, Frame number to find marker for 
        :type frame: int
        :param exact: Exact, Get marker at exact frame number rather than get estimated marker 
        :type exact: bool
        :rtype: 'MovieTrackingMarker'
        :return:  Marker for specified frame 
        '''
        pass

    def insert_frame(self, frame: int,
                     co: float = (0.0, 0.0)) -> 'MovieTrackingMarker':
        '''Insert a new marker at the specified frame 

        :param frame: Frame, Frame number to insert marker to 
        :type frame: int
        :param co: Coordinate, Place new marker at the given frame using specified in normalized space coordinates 
        :type co: float
        :rtype: 'MovieTrackingMarker'
        :return:  Newly created marker 
        '''
        pass

    def delete_frame(self, frame: int):
        '''Delete marker at specified frame 

        :param frame: Frame, Frame number to delete marker from 
        :type frame: int
        '''
        pass


class MovieTrackingObject:
    '''Match-moving object tracking and reconstruction data '''

    is_camera: bool = None
    '''Object is used for camera tracking 

    :type: bool
    '''

    keyframe_a: int = None
    '''First keyframe used for reconstruction initialization 

    :type: int
    '''

    keyframe_b: int = None
    '''Second keyframe used for reconstruction initialization 

    :type: int
    '''

    name: str = None
    '''Unique name of object 

    :type: str
    '''

    plane_tracks: typing.List['MovieTrackingPlaneTrack'] = None
    '''Collection of plane tracks in this tracking data object 

    :type: typing.List['MovieTrackingPlaneTrack']
    '''

    reconstruction: 'MovieTrackingReconstruction' = None
    '''

    :type: 'MovieTrackingReconstruction'
    '''

    scale: float = None
    '''Scale of object solution in camera space 

    :type: float
    '''

    tracks: typing.List['MovieTrackingTrack'] = None
    '''Collection of tracks in this tracking data object 

    :type: typing.List['MovieTrackingTrack']
    '''


class MovieTrackingObjectPlaneTracks:
    '''Collection of tracking plane tracks '''

    active: 'MovieTrackingTrack' = None
    '''Active track in this tracking data object 

    :type: 'MovieTrackingTrack'
    '''


class MovieTrackingObjectTracks:
    '''Collection of movie tracking tracks '''

    active: 'MovieTrackingTrack' = None
    '''Active track in this tracking data object 

    :type: 'MovieTrackingTrack'
    '''

    def new(self, name: str = "", frame: int = 1) -> 'MovieTrackingTrack':
        '''create new motion track in this movie clip 

        :param name: Name of new track 
        :type name: str
        :param frame: Frame, Frame number to add tracks on 
        :type frame: int
        :rtype: 'MovieTrackingTrack'
        :return:  Newly created track 
        '''
        pass


class MovieTrackingObjects:
    '''Collection of movie tracking objects '''

    active: 'MovieTrackingObject' = None
    '''Active object in this tracking data object 

    :type: 'MovieTrackingObject'
    '''

    def new(self, name: str) -> 'MovieTrackingObject':
        '''Add tracking object to this movie clip 

        :param name: Name of new object 
        :type name: str
        :rtype: 'MovieTrackingObject'
        :return:  New motion tracking object 
        '''
        pass

    def remove(self, object: 'MovieTrackingObject'):
        '''Remove tracking object from this movie clip 

        :param object: Motion tracking object to be removed 
        :type object: 'MovieTrackingObject'
        '''
        pass


class MovieTrackingPlaneMarker:
    '''Match-moving plane marker data for tracking '''

    corners: float = None
    '''Array of coordinates which represents UI rectangle corners in frame normalized coordinates 

    :type: float
    '''

    frame: int = None
    '''Frame number marker is keyframed on 

    :type: int
    '''

    mute: bool = None
    '''Is marker muted for current frame 

    :type: bool
    '''


class MovieTrackingPlaneMarkers:
    '''Collection of markers for movie tracking plane track '''

    def find_frame(self, frame: int,
                   exact: bool = True) -> 'MovieTrackingPlaneMarker':
        '''Get plane marker for specified frame 

        :param frame: Frame, Frame number to find marker for 
        :type frame: int
        :param exact: Exact, Get plane marker at exact frame number rather than get estimated marker 
        :type exact: bool
        :rtype: 'MovieTrackingPlaneMarker'
        :return:  Plane marker for specified frame 
        '''
        pass

    def insert_frame(self, frame: int) -> 'MovieTrackingPlaneMarker':
        '''Insert a new plane marker at the specified frame 

        :param frame: Frame, Frame number to insert marker to 
        :type frame: int
        :rtype: 'MovieTrackingPlaneMarker'
        :return:  Newly created plane marker 
        '''
        pass

    def delete_frame(self, frame: int):
        '''Delete plane marker at specified frame 

        :param frame: Frame, Frame number to delete plane marker from 
        :type frame: int
        '''
        pass


class MovieTrackingPlaneTrack:
    '''Match-moving plane track data for tracking '''

    image: 'Image' = None
    '''Image displayed in the track during editing in clip editor 

    :type: 'Image'
    '''

    image_opacity: float = None
    '''Opacity of the image 

    :type: float
    '''

    markers: typing.List['MovieTrackingPlaneMarker'] = None
    '''Collection of markers in track 

    :type: typing.List['MovieTrackingPlaneMarker']
    '''

    name: str = None
    '''Unique name of track 

    :type: str
    '''

    select: bool = None
    '''Plane track is selected 

    :type: bool
    '''

    use_auto_keying: bool = None
    '''Automatic keyframe insertion when moving plane corners 

    :type: bool
    '''


class MovieTrackingPlaneTracks:
    '''Collection of movie tracking plane tracks '''

    active: 'MovieTrackingPlaneTrack' = None
    '''Active plane track in this tracking data object 

    :type: 'MovieTrackingPlaneTrack'
    '''


class MovieTrackingReconstructedCameras:
    '''Collection of solved cameras '''

    def find_frame(self, frame: int = 1) -> 'MovieReconstructedCamera':
        '''Find a reconstructed camera for a give frame number 

        :param frame: Frame, Frame number to find camera for 
        :type frame: int
        :rtype: 'MovieReconstructedCamera'
        :return:  Camera for a given frame 
        '''
        pass

    def matrix_from_frame(self, frame: int = 1) -> float:
        '''Return interpolated camera matrix for a given frame 

        :param frame: Frame, Frame number to find camera for 
        :type frame: int
        :rtype: float
        :return:  Matrix, Interpolated camera matrix for a given frame 
        '''
        pass


class MovieTrackingReconstruction:
    '''Match-moving reconstruction data from tracker '''

    average_error: float = None
    '''Average error of reconstruction 

    :type: float
    '''

    cameras: typing.List['MovieTrackingReconstructedCameras'] = None
    '''Collection of solved cameras 

    :type: typing.List['MovieTrackingReconstructedCameras']
    '''

    is_valid: bool = None
    '''Is tracking data contains valid reconstruction information 

    :type: bool
    '''


class MovieTrackingSettings:
    '''Match moving settings '''

    clean_action: typing.Union[int, str] = None
    '''Cleanup action to execute 

    :type: typing.Union[int, str]
    '''

    clean_error: float = None
    '''Effect on tracks which have a larger re-projection error 

    :type: float
    '''

    clean_frames: int = None
    '''Effect on tracks which are tracked less than the specified amount of frames 

    :type: int
    '''

    default_correlation_min: float = None
    '''Default minimum value of correlation between matched pattern and reference that is still treated as successful tracking 

    :type: float
    '''

    default_frames_limit: int = None
    '''Every tracking cycle, this number of frames are tracked 

    :type: int
    '''

    default_margin: int = None
    '''Default distance from image boundary at which marker stops tracking 

    :type: int
    '''

    default_motion_model: typing.Union[int, str] = None
    '''Default motion model to use for tracking 

    :type: typing.Union[int, str]
    '''

    default_pattern_match: typing.Union[int, str] = None
    '''Track pattern from given frame when tracking marker to next frame 

    :type: typing.Union[int, str]
    '''

    default_pattern_size: int = None
    '''Size of pattern area for newly created tracks 

    :type: int
    '''

    default_search_size: int = None
    '''Size of search area for newly created tracks 

    :type: int
    '''

    default_weight: float = None
    '''Influence of newly created track on a final solution 

    :type: float
    '''

    distance: float = None
    '''Distance between two bundles used for scene scaling 

    :type: float
    '''

    object_distance: float = None
    '''Distance between two bundles used for object scaling 

    :type: float
    '''

    refine_intrinsics: typing.Union[int, str] = None
    '''Refine intrinsics during camera solving 

    :type: typing.Union[int, str]
    '''

    show_default_expanded: bool = None
    '''Show default options expanded in the user interface 

    :type: bool
    '''

    show_extra_expanded: bool = None
    '''Show extra options expanded in the user interface 

    :type: bool
    '''

    speed: typing.Union[int, str] = None
    '''Limit speed of tracking to make visual feedback easier (this does not affect the tracking quality) 

    :type: typing.Union[int, str]
    '''

    use_default_blue_channel: bool = None
    '''Use blue channel from footage for tracking 

    :type: bool
    '''

    use_default_brute: bool = None
    '''Use a brute-force translation-only initialization when tracking 

    :type: bool
    '''

    use_default_green_channel: bool = None
    '''Use green channel from footage for tracking 

    :type: bool
    '''

    use_default_mask: bool = None
    '''Use a grease pencil data-block as a mask to use only specified areas of pattern when tracking 

    :type: bool
    '''

    use_default_normalization: bool = None
    '''Normalize light intensities while tracking (slower) 

    :type: bool
    '''

    use_default_red_channel: bool = None
    '''Use red channel from footage for tracking 

    :type: bool
    '''

    use_keyframe_selection: bool = None
    '''Automatically select keyframes when solving camera/object motion 

    :type: bool
    '''

    use_tripod_solver: bool = None
    '''Use special solver to track a stable camera position, such as a tripod 

    :type: bool
    '''


class MovieTrackingStabilization:
    '''2D stabilization based on tracking markers '''

    active_rotation_track_index: int = None
    '''Index of active track in rotation stabilization tracks list 

    :type: int
    '''

    active_track_index: int = None
    '''Index of active track in translation stabilization tracks list 

    :type: int
    '''

    anchor_frame: int = None
    '''Reference point to anchor stabilization (other frames will be adjusted relative to this frame’s position) 

    :type: int
    '''

    filter_type: typing.Union[int, str] = None
    '''Interpolation to use for sub-pixel shifts and rotations due to stabilization 

    :type: typing.Union[int, str]
    '''

    influence_location: float = None
    '''Influence of stabilization algorithm on footage location 

    :type: float
    '''

    influence_rotation: float = None
    '''Influence of stabilization algorithm on footage rotation 

    :type: float
    '''

    influence_scale: float = None
    '''Influence of stabilization algorithm on footage scale 

    :type: float
    '''

    rotation_tracks: typing.List['MovieTrackingTrack'] = None
    '''Collection of tracks used for 2D stabilization (translation) 

    :type: typing.List['MovieTrackingTrack']
    '''

    scale_max: float = None
    '''Limit the amount of automatic scaling 

    :type: float
    '''

    show_tracks_expanded: bool = None
    '''Show UI list of tracks participating in stabilization 

    :type: bool
    '''

    target_position: float = None
    '''Known relative offset of original shot, will be subtracted (e.g. for panning shot, can be animated) 

    :type: float
    '''

    target_rotation: float = None
    '''Rotation present on original shot, will be compensated (e.g. for deliberate tilting) 

    :type: float
    '''

    target_scale: float = None
    '''Explicitly scale resulting frame to compensate zoom of original shot 

    :type: float
    '''

    tracks: typing.List['MovieTrackingTrack'] = None
    '''Collection of tracks used for 2D stabilization (translation) 

    :type: typing.List['MovieTrackingTrack']
    '''

    use_2d_stabilization: bool = None
    '''Use 2D stabilization for footage 

    :type: bool
    '''

    use_autoscale: bool = None
    '''Automatically scale footage to cover unfilled areas when stabilizing 

    :type: bool
    '''

    use_stabilize_rotation: bool = None
    '''Stabilize detected rotation around center of frame 

    :type: bool
    '''

    use_stabilize_scale: bool = None
    '''Compensate any scale changes relative to center of rotation 

    :type: bool
    '''


class MovieTrackingTrack:
    '''Match-moving track data for tracking '''

    average_error: float = None
    '''Average error of re-projection 

    :type: float
    '''

    bundle: float = None
    '''Position of bundle reconstructed from this track 

    :type: float
    '''

    color: float = None
    '''Color of the track in the Movie Clip Editor and the 3D viewport after a solve 

    :type: float
    '''

    correlation_min: float = None
    '''Minimal value of correlation between matched pattern and reference that is still treated as successful tracking 

    :type: float
    '''

    frames_limit: int = None
    '''Every tracking cycle, this number of frames are tracked 

    :type: int
    '''

    grease_pencil: 'GreasePencil' = None
    '''Grease pencil data for this track 

    :type: 'GreasePencil'
    '''

    has_bundle: bool = None
    '''True if track has a valid bundle 

    :type: bool
    '''

    hide: bool = None
    '''Track is hidden 

    :type: bool
    '''

    lock: bool = None
    '''Track is locked and all changes to it are disabled 

    :type: bool
    '''

    margin: int = None
    '''Distance from image boundary at which marker stops tracking 

    :type: int
    '''

    markers: typing.List['MovieTrackingMarker'] = None
    '''Collection of markers in track 

    :type: typing.List['MovieTrackingMarker']
    '''

    motion_model: typing.Union[int, str] = None
    '''Default motion model to use for tracking 

    :type: typing.Union[int, str]
    '''

    name: str = None
    '''Unique name of track 

    :type: str
    '''

    offset: float = None
    '''Offset of track from the parenting point 

    :type: float
    '''

    pattern_match: typing.Union[int, str] = None
    '''Track pattern from given frame when tracking marker to next frame 

    :type: typing.Union[int, str]
    '''

    select: bool = None
    '''Track is selected 

    :type: bool
    '''

    select_anchor: bool = None
    '''Track’s anchor point is selected 

    :type: bool
    '''

    select_pattern: bool = None
    '''Track’s pattern area is selected 

    :type: bool
    '''

    select_search: bool = None
    '''Track’s search area is selected 

    :type: bool
    '''

    use_alpha_preview: bool = None
    '''Apply track’s mask on displaying preview 

    :type: bool
    '''

    use_blue_channel: bool = None
    '''Use blue channel from footage for tracking 

    :type: bool
    '''

    use_brute: bool = None
    '''Use a brute-force translation only pre-track before refinement 

    :type: bool
    '''

    use_custom_color: bool = None
    '''Use custom color instead of theme-defined 

    :type: bool
    '''

    use_grayscale_preview: bool = None
    '''Display what the tracking algorithm sees in the preview 

    :type: bool
    '''

    use_green_channel: bool = None
    '''Use green channel from footage for tracking 

    :type: bool
    '''

    use_mask: bool = None
    '''Use a grease pencil data-block as a mask to use only specified areas of pattern when tracking 

    :type: bool
    '''

    use_normalization: bool = None
    '''Normalize light intensities while tracking. Slower 

    :type: bool
    '''

    use_red_channel: bool = None
    '''Use red channel from footage for tracking 

    :type: bool
    '''

    weight: float = None
    '''Influence of this track on a final solution 

    :type: float
    '''

    weight_stab: float = None
    '''Influence of this track on 2D stabilization 

    :type: float
    '''


class MovieTrackingTracks:
    '''Collection of movie tracking tracks '''

    active: 'MovieTrackingTrack' = None
    '''Active track in this tracking data object 

    :type: 'MovieTrackingTrack'
    '''

    def new(self, name: str = "", frame: int = 1) -> 'MovieTrackingTrack':
        '''Create new motion track in this movie clip 

        :param name: Name of new track 
        :type name: str
        :param frame: Frame, Frame number to add track on 
        :type frame: int
        :rtype: 'MovieTrackingTrack'
        :return:  Newly created track 
        '''
        pass


class MulticamSequence:
    '''Sequence strip to perform multicam editing '''

    animation_offset_end: int = None
    '''Animation end offset (trim end) 

    :type: int
    '''

    animation_offset_start: int = None
    '''Animation start offset (trim start) 

    :type: int
    '''

    input_count: int = None
    '''

    :type: int
    '''

    multicam_source: int = None
    '''

    :type: int
    '''


class MultiplySequence:
    '''Multiply Sequence '''

    input_1: 'Sequence' = None
    '''First input for the effect strip 

    :type: 'Sequence'
    '''

    input_2: 'Sequence' = None
    '''Second input for the effect strip 

    :type: 'Sequence'
    '''

    input_count: int = None
    '''

    :type: int
    '''


class MultiresModifier:
    '''Multiresolution mesh modifier '''

    filepath: str = None
    '''Path to external displacements file 

    :type: str
    '''

    is_external: bool = None
    '''Store multires displacements outside the .blend file, to save memory 

    :type: bool
    '''

    levels: int = None
    '''Number of subdivisions to use in the viewport 

    :type: int
    '''

    render_levels: int = None
    '''The subdivision level visible at render time 

    :type: int
    '''

    sculpt_levels: int = None
    '''Number of subdivisions to use in sculpt mode 

    :type: int
    '''

    show_only_control_edges: bool = None
    '''Skip drawing/rendering of interior subdivided edges 

    :type: bool
    '''

    subdivision_type: typing.Union[int, str] = None
    '''Select type of subdivision algorithm 

    :type: typing.Union[int, str]
    '''

    total_levels: int = None
    '''Number of subdivisions for which displacements are stored 

    :type: int
    '''

    use_subsurf_uv: bool = None
    '''Use subsurf to subdivide UVs 

    :type: bool
    '''


class MusgraveTexture:
    '''Procedural musgrave texture '''

    dimension_max: float = None
    '''Highest fractal dimension 

    :type: float
    '''

    gain: float = None
    '''The gain multiplier 

    :type: float
    '''

    lacunarity: float = None
    '''Gap between successive frequencies 

    :type: float
    '''

    musgrave_type: typing.Union[int, str] = None
    '''Fractal noise algorithm 

    :type: typing.Union[int, str]
    '''

    nabla: float = None
    '''Size of derivative offset used for calculating normal 

    :type: float
    '''

    noise_basis: typing.Union[int, str] = None
    '''Noise basis used for turbulence 

    :type: typing.Union[int, str]
    '''

    noise_intensity: float = None
    '''Intensity of the noise 

    :type: float
    '''

    noise_scale: float = None
    '''Scaling for noise input 

    :type: float
    '''

    octaves: float = None
    '''Number of frequencies used 

    :type: float
    '''

    offset: float = None
    '''The fractal offset 

    :type: float
    '''

    users_material = None
    '''Materials that use this texture (readonly) '''

    users_object_modifier = None
    '''Object modifiers that use this texture (readonly) '''


class NODE_MT_add:
    pass


class NODE_PT_quality:
    pass


class NODE_UL_interface_sockets:
    def draw_item(self, context, layout, data, item, icon, active_data,
                  active_propname, index):
        '''

        '''
        pass


class NandController:
    '''Controller passing on events based on a logical NAND operation '''

    pass


class NearSensor:
    '''Sensor to detect nearby objects '''

    distance: float = None
    '''Trigger distance 

    :type: float
    '''

    property: str = None
    '''Only look for objects with this property (blank = all objects) 

    :type: str
    '''

    reset_distance: float = None
    '''The distance where the sensor forgets the actor 

    :type: float
    '''


class NlaStrip:
    '''A container referencing an existing Action '''

    action: 'Action' = None
    '''Action referenced by this strip 

    :type: 'Action'
    '''

    action_frame_end: float = None
    '''Last frame from action to use 

    :type: float
    '''

    action_frame_start: float = None
    '''First frame from action to use 

    :type: float
    '''

    active: bool = None
    '''NLA Strip is active 

    :type: bool
    '''

    blend_in: float = None
    '''Number of frames at start of strip to fade in influence 

    :type: float
    '''

    blend_out: float = None
    '''

    :type: float
    '''

    blend_type: typing.Union[int, str] = None
    '''Method used for combining strip’s result with accumulated result 

    :type: typing.Union[int, str]
    '''

    extrapolation: typing.Union[int, str] = None
    '''Action to take for gaps past the strip extents 

    :type: typing.Union[int, str]
    '''

    fcurves: typing.List['NlaStripFCurves'] = None
    '''F-Curves for controlling the strip’s influence and timing 

    :type: typing.List['NlaStripFCurves']
    '''

    frame_end: float = None
    '''

    :type: float
    '''

    frame_start: float = None
    '''

    :type: float
    '''

    influence: float = None
    '''Amount the strip contributes to the current result 

    :type: float
    '''

    modifiers: typing.List['FModifier'] = None
    '''Modifiers affecting all the F-Curves in the referenced Action 

    :type: typing.List['FModifier']
    '''

    mute: bool = None
    '''NLA Strip is not evaluated 

    :type: bool
    '''

    name: str = None
    '''

    :type: str
    '''

    repeat: float = None
    '''Number of times to repeat the action range 

    :type: float
    '''

    scale: float = None
    '''Scaling factor for action 

    :type: float
    '''

    select: bool = None
    '''NLA Strip is selected 

    :type: bool
    '''

    strip_time: float = None
    '''Frame of referenced Action to evaluate 

    :type: float
    '''

    strips: typing.List['NlaStrip'] = None
    '''NLA Strips that this strip acts as a container for (if it is of type Meta) 

    :type: typing.List['NlaStrip']
    '''

    type: typing.Union[int, str] = None
    '''Type of NLA Strip 

    :type: typing.Union[int, str]
    '''

    use_animated_influence: bool = None
    '''Influence setting is controlled by an F-Curve rather than automatically determined 

    :type: bool
    '''

    use_animated_time: bool = None
    '''Strip time is controlled by an F-Curve rather than automatically determined 

    :type: bool
    '''

    use_animated_time_cyclic: bool = None
    '''Cycle the animated time within the action start & end 

    :type: bool
    '''

    use_auto_blend: bool = None
    '''Number of frames for Blending In/Out is automatically determined from overlapping strips 

    :type: bool
    '''

    use_reverse: bool = None
    '''NLA Strip is played back in reverse order (only when timing is automatically determined) 

    :type: bool
    '''

    use_sync_length: bool = None
    '''Update range of frames referenced from action after tweaking strip and its keyframes 

    :type: bool
    '''


class NlaStripFCurves:
    '''Collection of NLA strip F-Curves '''

    def find(self, data_path: str, index: int = 0) -> 'FCurve':
        '''Find an F-Curve. Note that this function performs a linear scan of all F-Curves in the NLA strip. 

        :param data_path: Data Path, F-Curve data path 
        :type data_path: str
        :param index: Index, Array index 
        :type index: int
        :rtype: 'FCurve'
        :return:  The found F-Curve, or None if it doesn’t exist 
        '''
        pass


class NlaStrips:
    '''Collection of Nla Strips '''

    def new(self, name: str, start: int, action: 'Action') -> 'NlaStrip':
        '''Add a new Action-Clip strip to the track 

        :param name: Name for the NLA Strips 
        :type name: str
        :param start: Start Frame, Start frame for this strip 
        :type start: int
        :param action: Action to assign to this strip 
        :type action: 'Action'
        :rtype: 'NlaStrip'
        :return:  New NLA Strip 
        '''
        pass

    def remove(self, strip: 'NlaStrip'):
        '''Remove a NLA Strip 

        :param strip: NLA Strip to remove 
        :type strip: 'NlaStrip'
        '''
        pass


class NlaTrack:
    '''A animation layer containing Actions referenced as NLA strips '''

    active: bool = None
    '''NLA Track is active 

    :type: bool
    '''

    is_solo: bool = None
    '''NLA Track is evaluated itself (i.e. active Action and all other NLA Tracks in the same AnimData block are disabled) 

    :type: bool
    '''

    lock: bool = None
    '''NLA Track is locked 

    :type: bool
    '''

    mute: bool = None
    '''NLA Track is not evaluated 

    :type: bool
    '''

    name: str = None
    '''

    :type: str
    '''

    select: bool = None
    '''NLA Track is selected 

    :type: bool
    '''

    strips: typing.List['NlaStrips'] = None
    '''NLA Strips on this NLA-track 

    :type: typing.List['NlaStrips']
    '''


class NlaTracks:
    '''Collection of NLA Tracks '''

    active: 'NlaTrack' = None
    '''Active Object constraint 

    :type: 'NlaTrack'
    '''

    def new(self, prev: 'NlaTrack' = None) -> 'NlaTrack':
        '''Add a new NLA Track 

        :param prev: NLA Track to add the new one after 
        :type prev: 'NlaTrack'
        :rtype: 'NlaTrack'
        :return:  New NLA Track 
        '''
        pass

    def remove(self, track: 'NlaTrack'):
        '''Remove a NLA Track 

        :param track: NLA Track to remove 
        :type track: 'NlaTrack'
        '''
        pass


class Node:
    '''Node in a node tree '''

    bl_description: str = None
    '''

    :type: str
    '''

    bl_height_default: float = None
    '''

    :type: float
    '''

    bl_height_max: float = None
    '''

    :type: float
    '''

    bl_height_min: float = None
    '''

    :type: float
    '''

    bl_icon: typing.Union[int, str] = None
    '''The node icon 

    :type: typing.Union[int, str]
    '''

    bl_idname: str = None
    '''

    :type: str
    '''

    bl_label: str = None
    '''The node label 

    :type: str
    '''

    bl_static_type: typing.Union[int, str] = None
    '''Node type (deprecated, use with care) 

    :type: typing.Union[int, str]
    '''

    bl_width_default: float = None
    '''

    :type: float
    '''

    bl_width_max: float = None
    '''

    :type: float
    '''

    bl_width_min: float = None
    '''

    :type: float
    '''

    color: float = None
    '''Custom color of the node body 

    :type: float
    '''

    dimensions: float = None
    '''Absolute bounding box dimensions of the node 

    :type: float
    '''

    height: float = None
    '''Height of the node 

    :type: float
    '''

    hide: bool = None
    '''

    :type: bool
    '''

    inputs: typing.List['NodeInputs'] = None
    '''

    :type: typing.List['NodeInputs']
    '''

    internal_links: typing.List['NodeLink'] = None
    '''Internal input-to-output connections for muting 

    :type: typing.List['NodeLink']
    '''

    label: str = None
    '''Optional custom node label 

    :type: str
    '''

    location: float = None
    '''

    :type: float
    '''

    mute: bool = None
    '''

    :type: bool
    '''

    name: str = None
    '''Unique node identifier 

    :type: str
    '''

    outputs: typing.List['NodeSocket'] = None
    '''

    :type: typing.List['NodeSocket']
    '''

    parent: 'Node' = None
    '''Parent this node is attached to 

    :type: 'Node'
    '''

    select: bool = None
    '''Node selection state 

    :type: bool
    '''

    shading_compatibility: typing.Set[typing.Union[int, str]] = None
    '''

    :type: typing.Set[typing.Union[int, str]]
    '''

    show_options: bool = None
    '''

    :type: bool
    '''

    show_preview: bool = None
    '''

    :type: bool
    '''

    show_texture: bool = None
    '''Draw node in viewport textured draw mode 

    :type: bool
    '''

    type: typing.Union[int, str] = None
    '''Node type (deprecated, use bl_static_type or bl_idname for the actual identifier string) 

    :type: typing.Union[int, str]
    '''

    use_custom_color: bool = None
    '''Use custom color for the node 

    :type: bool
    '''

    width: float = None
    '''Width of the node 

    :type: float
    '''

    width_hidden: float = None
    '''Width of the node in hidden state 

    :type: float
    '''

    def socket_value_update(self, context):
        '''Update after property changes 

        '''
        pass

    def poll_instance(self, node_tree: 'NodeTree') -> bool:
        '''If non-null output is returned, the node can be added to the tree 

        :param node_tree: Node Tree 
        :type node_tree: 'NodeTree'
        :rtype: bool
        '''
        pass

    def update(self, ):
        '''Update on editor changes 

        '''
        pass

    def insert_link(self, link: 'NodeLink'):
        '''Handle creation of a link to or from the node 

        :param link: Link, Node link that will be inserted 
        :type link: 'NodeLink'
        '''
        pass

    def init(self, context):
        '''Initialize a new instance of this node 

        '''
        pass

    def copy(self, node: 'Node'):
        '''Initialize a new instance of this node from an existing node 

        :param node: Node, Existing node to copy 
        :type node: 'Node'
        '''
        pass

    def free(self, ):
        '''Clean up node on removal 

        '''
        pass

    def draw_buttons(self, context, layout: 'UILayout'):
        '''Draw node buttons 

        :param layout: Layout, Layout in the UI 
        :type layout: 'UILayout'
        '''
        pass

    def draw_buttons_ext(self, context, layout: 'UILayout'):
        '''Draw node buttons in the sidebar 

        :param layout: Layout, Layout in the UI 
        :type layout: 'UILayout'
        '''
        pass

    def draw_label(self, ) -> str:
        '''Returns a dynamic label string 

        :rtype: str
        :return:  Label 
        '''
        pass


class NodeCustomGroup:
    '''Base node type for custom registered node group types '''

    interface: 'PropertyGroup' = None
    '''Interface socket data 

    :type: 'PropertyGroup'
    '''

    node_tree: 'NodeTree' = None
    '''

    :type: 'NodeTree'
    '''


class NodeFrame:
    label_size: int = None
    '''Font size to use for displaying the label 

    :type: int
    '''

    shrink: bool = None
    '''Shrink the frame to minimal bounding box 

    :type: bool
    '''

    text: 'Text' = None
    '''

    :type: 'Text'
    '''


class NodeGroup:
    interface: 'PropertyGroup' = None
    '''Interface socket data 

    :type: 'PropertyGroup'
    '''

    node_tree: 'NodeTree' = None
    '''

    :type: 'NodeTree'
    '''


class NodeGroupInput:
    interface: 'PropertyGroup' = None
    '''Interface socket data 

    :type: 'PropertyGroup'
    '''


class NodeGroupOutput:
    interface: 'PropertyGroup' = None
    '''Interface socket data 

    :type: 'PropertyGroup'
    '''

    is_active_output: bool = None
    '''True if this node is used as the active group output 

    :type: bool
    '''


class NodeInputs:
    '''Collection of Node Sockets '''

    def new(self, type: str, name: str, identifier: str = "") -> 'NodeSocket':
        '''Add a socket to this node 

        :param type: Type, Data type 
        :type type: str
        :param name: Name 
        :type name: str
        :param identifier: Identifier, Unique socket identifier 
        :type identifier: str
        :rtype: 'NodeSocket'
        :return:  New socket 
        '''
        pass

    def remove(self, socket: 'NodeSocket'):
        '''Remove a socket from this node 

        :param socket: The socket to remove 
        :type socket: 'NodeSocket'
        '''
        pass

    def clear(self, ):
        '''Remove all sockets from this node 

        '''
        pass

    def move(self, from_index: int, to_index: int):
        '''Move a socket to another position 

        :param from_index: From Index, Index of the socket to move 
        :type from_index: int
        :param to_index: To Index, Target index for the socket 
        :type to_index: int
        '''
        pass


class NodeInstanceHash:
    '''Hash table containing node instance data '''

    pass


class NodeInternal:
    def poll_instance(self, node_tree: 'NodeTree') -> bool:
        '''If non-null output is returned, the node can be added to the tree 

        :param node_tree: Node Tree 
        :type node_tree: 'NodeTree'
        :rtype: bool
        '''
        pass

    def update(self, ):
        '''Update on editor changes 

        '''
        pass

    def draw_buttons(self, context, layout: 'UILayout'):
        '''Draw node buttons 

        :param layout: Layout, Layout in the UI 
        :type layout: 'UILayout'
        '''
        pass

    def draw_buttons_ext(self, context, layout: 'UILayout'):
        '''Draw node buttons in the sidebar 

        :param layout: Layout, Layout in the UI 
        :type layout: 'UILayout'
        '''
        pass


class NodeInternalSocketTemplate:
    '''Type and default value of a node socket '''

    identifier: str = None
    '''Identifier of the socket 

    :type: str
    '''

    name: str = None
    '''Name of the socket 

    :type: str
    '''

    type: typing.Union[int, str] = None
    '''Data type of the socket 

    :type: typing.Union[int, str]
    '''


class NodeLink:
    '''Link is valid '''

    from_node: 'Node' = None
    '''

    :type: 'Node'
    '''

    from_socket: 'NodeSocket' = None
    '''

    :type: 'NodeSocket'
    '''

    is_hidden: bool = None
    '''Link is hidden due to invisible sockets 

    :type: bool
    '''

    is_valid: bool = None
    '''

    :type: bool
    '''

    to_node: 'Node' = None
    '''

    :type: 'Node'
    '''

    to_socket: 'NodeSocket' = None
    '''

    :type: 'NodeSocket'
    '''


class NodeLinks:
    '''Collection of Node Links '''

    def new(self,
            input: 'NodeSocket',
            output: 'NodeSocket',
            verify_limits: bool = True) -> 'NodeLink':
        '''Add a node link to this node tree 

        :param input: The input socket 
        :type input: 'NodeSocket'
        :param output: The output socket 
        :type output: 'NodeSocket'
        :param verify_limits: Verify Limits, Remove existing links if connection limit is exceeded 
        :type verify_limits: bool
        :rtype: 'NodeLink'
        :return:  New node link 
        '''
        pass

    def remove(self, link: 'NodeLink'):
        '''remove a node link from the node tree 

        :param link: The node link to remove 
        :type link: 'NodeLink'
        '''
        pass

    def clear(self, ):
        '''remove all node links from the node tree 

        '''
        pass


class NodeOutputFileSlotFile:
    '''Single layer file slot of the file output node '''

    format: 'ImageFormatSettings' = None
    '''

    :type: 'ImageFormatSettings'
    '''

    path: str = None
    '''Subpath used for this slot 

    :type: str
    '''

    use_node_format: bool = None
    '''

    :type: bool
    '''


class NodeOutputFileSlotLayer:
    '''Multilayer slot of the file output node '''

    name: str = None
    '''OpenEXR layer name used for this slot 

    :type: str
    '''


class NodeOutputs:
    '''Collection of Node Sockets '''

    def new(self, type: str, name: str, identifier: str = "") -> 'NodeSocket':
        '''Add a socket to this node 

        :param type: Type, Data type 
        :type type: str
        :param name: Name 
        :type name: str
        :param identifier: Identifier, Unique socket identifier 
        :type identifier: str
        :rtype: 'NodeSocket'
        :return:  New socket 
        '''
        pass

    def remove(self, socket: 'NodeSocket'):
        '''Remove a socket from this node 

        :param socket: The socket to remove 
        :type socket: 'NodeSocket'
        '''
        pass

    def clear(self, ):
        '''Remove all sockets from this node 

        '''
        pass

    def move(self, from_index: int, to_index: int):
        '''Move a socket to another position 

        :param from_index: From Index, Index of the socket to move 
        :type from_index: int
        :param to_index: To Index, Target index for the socket 
        :type to_index: int
        '''
        pass


class NodeReroute:
    pass


class NodeSetting:
    value: str = None
    '''Python expression to be evaluated as the initial node setting 

    :type: str
    '''


class NodeSocket:
    '''Input or output socket of a node '''

    bl_idname: str = None
    '''

    :type: str
    '''

    enabled: bool = None
    '''Enable the socket 

    :type: bool
    '''

    hide: bool = None
    '''Hide the socket 

    :type: bool
    '''

    hide_value: bool = None
    '''Hide the socket input value 

    :type: bool
    '''

    identifier: str = None
    '''Unique identifier for mapping sockets 

    :type: str
    '''

    is_linked: bool = None
    '''True if the socket is connected 

    :type: bool
    '''

    is_output: bool = None
    '''True if the socket is an output, otherwise input 

    :type: bool
    '''

    link_limit: int = None
    '''Max number of links allowed for this socket 

    :type: int
    '''

    name: str = None
    '''Socket name 

    :type: str
    '''

    node: 'Node' = None
    '''Node owning this socket 

    :type: 'Node'
    '''

    show_expanded: bool = None
    '''Socket links are expanded in the user interface 

    :type: bool
    '''

    type: typing.Union[int, str] = None
    '''Data type 

    :type: typing.Union[int, str]
    '''

    links = None
    '''List of node links from or to this socket (readonly) '''

    def draw(self, context, layout: 'UILayout', node: 'Node', text: str):
        '''Draw socket 

        :param layout: Layout, Layout in the UI 
        :type layout: 'UILayout'
        :param node: Node, Node the socket belongs to 
        :type node: 'Node'
        :param text: Text, Text label to draw alongside properties 
        :type text: str
        '''
        pass

    def draw_color(self, context, node: 'Node') -> float:
        '''Color of the socket icon 

        :param node: Node, Node the socket belongs to 
        :type node: 'Node'
        :rtype: float
        :return:  Color 
        '''
        pass


class NodeSocketBool:
    '''Boolean value socket of a node '''

    default_value: bool = None
    '''Input value used for unconnected socket 

    :type: bool
    '''

    links = None
    '''List of node links from or to this socket (readonly) '''


class NodeSocketColor:
    '''RGBA color socket of a node '''

    default_value: float = None
    '''Input value used for unconnected socket 

    :type: float
    '''

    links = None
    '''List of node links from or to this socket (readonly) '''


class NodeSocketFloat:
    '''Floating point number socket of a node '''

    default_value: float = None
    '''Input value used for unconnected socket 

    :type: float
    '''

    links = None
    '''List of node links from or to this socket (readonly) '''


class NodeSocketFloatAngle:
    '''Floating point number socket of a node '''

    default_value: float = None
    '''Input value used for unconnected socket 

    :type: float
    '''

    links = None
    '''List of node links from or to this socket (readonly) '''


class NodeSocketFloatFactor:
    '''Floating point number socket of a node '''

    default_value: float = None
    '''Input value used for unconnected socket 

    :type: float
    '''

    links = None
    '''List of node links from or to this socket (readonly) '''


class NodeSocketFloatPercentage:
    '''Floating point number socket of a node '''

    default_value: float = None
    '''Input value used for unconnected socket 

    :type: float
    '''

    links = None
    '''List of node links from or to this socket (readonly) '''


class NodeSocketFloatTime:
    '''Floating point number socket of a node '''

    default_value: float = None
    '''Input value used for unconnected socket 

    :type: float
    '''

    links = None
    '''List of node links from or to this socket (readonly) '''


class NodeSocketFloatUnsigned:
    '''Floating point number socket of a node '''

    default_value: float = None
    '''Input value used for unconnected socket 

    :type: float
    '''

    links = None
    '''List of node links from or to this socket (readonly) '''


class NodeSocketInt:
    '''Integer number socket of a node '''

    default_value: int = None
    '''Input value used for unconnected socket 

    :type: int
    '''

    links = None
    '''List of node links from or to this socket (readonly) '''


class NodeSocketIntFactor:
    '''Integer number socket of a node '''

    default_value: int = None
    '''Input value used for unconnected socket 

    :type: int
    '''

    links = None
    '''List of node links from or to this socket (readonly) '''


class NodeSocketIntPercentage:
    '''Integer number socket of a node '''

    default_value: int = None
    '''Input value used for unconnected socket 

    :type: int
    '''

    links = None
    '''List of node links from or to this socket (readonly) '''


class NodeSocketIntUnsigned:
    '''Integer number socket of a node '''

    default_value: int = None
    '''Input value used for unconnected socket 

    :type: int
    '''

    links = None
    '''List of node links from or to this socket (readonly) '''


class NodeSocketInterface:
    '''Parameters to define node sockets '''

    bl_socket_idname: str = None
    '''

    :type: str
    '''

    identifier: str = None
    '''Unique identifier for mapping sockets 

    :type: str
    '''

    is_output: bool = None
    '''True if the socket is an output, otherwise input 

    :type: bool
    '''

    name: str = None
    '''Socket name 

    :type: str
    '''

    def draw(self, context, layout: 'UILayout'):
        '''Draw template settings 

        :param layout: Layout, Layout in the UI 
        :type layout: 'UILayout'
        '''
        pass

    def draw_color(self, context) -> float:
        '''Color of the socket icon 

        :rtype: float
        :return:  Color 
        '''
        pass

    def register_properties(self, data_rna_type: 'Struct'):
        '''Define RNA properties of a socket 

        :param data_rna_type: Data RNA Type, RNA type for special socket properties 
        :type data_rna_type: 'Struct'
        '''
        pass

    def init_socket(self, node: 'Node', socket: 'NodeSocket', data_path: str):
        '''Initialize a node socket instance 

        :param node: Node, Node of the socket to initialize 
        :type node: 'Node'
        :param socket: Socket, Socket to initialize 
        :type socket: 'NodeSocket'
        :param data_path: Data Path, Path to specialized socket data 
        :type data_path: str
        '''
        pass

    def from_socket(self, node: 'Node', socket: 'NodeSocket'):
        '''Setup template parameters from an existing socket 

        :param node: Node, Node of the original socket 
        :type node: 'Node'
        :param socket: Socket, Original socket 
        :type socket: 'NodeSocket'
        '''
        pass


class NodeSocketInterfaceBool:
    '''Boolean value socket of a node '''

    default_value: bool = None
    '''Input value used for unconnected socket 

    :type: bool
    '''


class NodeSocketInterfaceColor:
    '''RGBA color socket of a node '''

    default_value: float = None
    '''Input value used for unconnected socket 

    :type: float
    '''


class NodeSocketInterfaceFloat:
    '''Floating point number socket of a node '''

    default_value: float = None
    '''Input value used for unconnected socket 

    :type: float
    '''

    max_value: float = None
    '''Maximum value 

    :type: float
    '''

    min_value: float = None
    '''Minimum value 

    :type: float
    '''


class NodeSocketInterfaceFloatAngle:
    '''Floating point number socket of a node '''

    default_value: float = None
    '''Input value used for unconnected socket 

    :type: float
    '''

    max_value: float = None
    '''Maximum value 

    :type: float
    '''

    min_value: float = None
    '''Minimum value 

    :type: float
    '''


class NodeSocketInterfaceFloatFactor:
    '''Floating point number socket of a node '''

    default_value: float = None
    '''Input value used for unconnected socket 

    :type: float
    '''

    max_value: float = None
    '''Maximum value 

    :type: float
    '''

    min_value: float = None
    '''Minimum value 

    :type: float
    '''


class NodeSocketInterfaceFloatPercentage:
    '''Floating point number socket of a node '''

    default_value: float = None
    '''Input value used for unconnected socket 

    :type: float
    '''

    max_value: float = None
    '''Maximum value 

    :type: float
    '''

    min_value: float = None
    '''Minimum value 

    :type: float
    '''


class NodeSocketInterfaceFloatTime:
    '''Floating point number socket of a node '''

    default_value: float = None
    '''Input value used for unconnected socket 

    :type: float
    '''

    max_value: float = None
    '''Maximum value 

    :type: float
    '''

    min_value: float = None
    '''Minimum value 

    :type: float
    '''


class NodeSocketInterfaceFloatUnsigned:
    '''Floating point number socket of a node '''

    default_value: float = None
    '''Input value used for unconnected socket 

    :type: float
    '''

    max_value: float = None
    '''Maximum value 

    :type: float
    '''

    min_value: float = None
    '''Minimum value 

    :type: float
    '''


class NodeSocketInterfaceInt:
    '''Integer number socket of a node '''

    default_value: int = None
    '''Input value used for unconnected socket 

    :type: int
    '''

    max_value: int = None
    '''Maximum value 

    :type: int
    '''

    min_value: int = None
    '''Minimum value 

    :type: int
    '''


class NodeSocketInterfaceIntFactor:
    '''Integer number socket of a node '''

    default_value: int = None
    '''Input value used for unconnected socket 

    :type: int
    '''

    max_value: int = None
    '''Maximum value 

    :type: int
    '''

    min_value: int = None
    '''Minimum value 

    :type: int
    '''


class NodeSocketInterfaceIntPercentage:
    '''Integer number socket of a node '''

    default_value: int = None
    '''Input value used for unconnected socket 

    :type: int
    '''

    max_value: int = None
    '''Maximum value 

    :type: int
    '''

    min_value: int = None
    '''Minimum value 

    :type: int
    '''


class NodeSocketInterfaceIntUnsigned:
    '''Integer number socket of a node '''

    default_value: int = None
    '''Input value used for unconnected socket 

    :type: int
    '''

    max_value: int = None
    '''Maximum value 

    :type: int
    '''

    min_value: int = None
    '''Minimum value 

    :type: int
    '''


class NodeSocketInterfaceShader:
    '''Shader socket of a node '''

    pass


class NodeSocketInterfaceStandard:
    type: typing.Union[int, str] = None
    '''Data type 

    :type: typing.Union[int, str]
    '''

    def draw(self, context, layout: 'UILayout'):
        '''Draw template settings 

        :param layout: Layout, Layout in the UI 
        :type layout: 'UILayout'
        '''
        pass

    def draw_color(self, context) -> float:
        '''Color of the socket icon 

        :rtype: float
        :return:  Color 
        '''
        pass


class NodeSocketInterfaceString:
    '''String socket of a node '''

    default_value: str = None
    '''Input value used for unconnected socket 

    :type: str
    '''


class NodeSocketInterfaceVector:
    '''3D vector socket of a node '''

    default_value: float = None
    '''Input value used for unconnected socket 

    :type: float
    '''

    max_value: float = None
    '''Maximum value 

    :type: float
    '''

    min_value: float = None
    '''Minimum value 

    :type: float
    '''


class NodeSocketInterfaceVectorAcceleration:
    '''3D vector socket of a node '''

    default_value: float = None
    '''Input value used for unconnected socket 

    :type: float
    '''

    max_value: float = None
    '''Maximum value 

    :type: float
    '''

    min_value: float = None
    '''Minimum value 

    :type: float
    '''


class NodeSocketInterfaceVectorDirection:
    '''3D vector socket of a node '''

    default_value: float = None
    '''Input value used for unconnected socket 

    :type: float
    '''

    max_value: float = None
    '''Maximum value 

    :type: float
    '''

    min_value: float = None
    '''Minimum value 

    :type: float
    '''


class NodeSocketInterfaceVectorEuler:
    '''3D vector socket of a node '''

    default_value: float = None
    '''Input value used for unconnected socket 

    :type: float
    '''

    max_value: float = None
    '''Maximum value 

    :type: float
    '''

    min_value: float = None
    '''Minimum value 

    :type: float
    '''


class NodeSocketInterfaceVectorTranslation:
    '''3D vector socket of a node '''

    default_value: float = None
    '''Input value used for unconnected socket 

    :type: float
    '''

    max_value: float = None
    '''Maximum value 

    :type: float
    '''

    min_value: float = None
    '''Minimum value 

    :type: float
    '''


class NodeSocketInterfaceVectorVelocity:
    '''3D vector socket of a node '''

    default_value: float = None
    '''Input value used for unconnected socket 

    :type: float
    '''

    max_value: float = None
    '''Maximum value 

    :type: float
    '''

    min_value: float = None
    '''Minimum value 

    :type: float
    '''


class NodeSocketInterfaceVectorXYZ:
    '''3D vector socket of a node '''

    default_value: float = None
    '''Input value used for unconnected socket 

    :type: float
    '''

    max_value: float = None
    '''Maximum value 

    :type: float
    '''

    min_value: float = None
    '''Minimum value 

    :type: float
    '''


class NodeSocketShader:
    '''Shader socket of a node '''

    links = None
    '''List of node links from or to this socket (readonly) '''


class NodeSocketStandard:
    links = None
    '''List of node links from or to this socket (readonly) '''

    def draw(self, context, layout: 'UILayout', node: 'Node', text: str):
        '''Draw socket 

        :param layout: Layout, Layout in the UI 
        :type layout: 'UILayout'
        :param node: Node, Node the socket belongs to 
        :type node: 'Node'
        :param text: Text, Text label to draw alongside properties 
        :type text: str
        '''
        pass

    def draw_color(self, context, node: 'Node') -> float:
        '''Color of the socket icon 

        :param node: Node, Node the socket belongs to 
        :type node: 'Node'
        :rtype: float
        :return:  Color 
        '''
        pass


class NodeSocketString:
    '''String socket of a node '''

    default_value: str = None
    '''Input value used for unconnected socket 

    :type: str
    '''

    links = None
    '''List of node links from or to this socket (readonly) '''


class NodeSocketVector:
    '''3D vector socket of a node '''

    default_value: float = None
    '''Input value used for unconnected socket 

    :type: float
    '''

    links = None
    '''List of node links from or to this socket (readonly) '''


class NodeSocketVectorAcceleration:
    '''3D vector socket of a node '''

    default_value: float = None
    '''Input value used for unconnected socket 

    :type: float
    '''

    links = None
    '''List of node links from or to this socket (readonly) '''


class NodeSocketVectorDirection:
    '''3D vector socket of a node '''

    default_value: float = None
    '''Input value used for unconnected socket 

    :type: float
    '''

    links = None
    '''List of node links from or to this socket (readonly) '''


class NodeSocketVectorEuler:
    '''3D vector socket of a node '''

    default_value: float = None
    '''Input value used for unconnected socket 

    :type: float
    '''

    links = None
    '''List of node links from or to this socket (readonly) '''


class NodeSocketVectorTranslation:
    '''3D vector socket of a node '''

    default_value: float = None
    '''Input value used for unconnected socket 

    :type: float
    '''

    links = None
    '''List of node links from or to this socket (readonly) '''


class NodeSocketVectorVelocity:
    '''3D vector socket of a node '''

    default_value: float = None
    '''Input value used for unconnected socket 

    :type: float
    '''

    links = None
    '''List of node links from or to this socket (readonly) '''


class NodeSocketVectorXYZ:
    '''3D vector socket of a node '''

    default_value: float = None
    '''Input value used for unconnected socket 

    :type: float
    '''

    links = None
    '''List of node links from or to this socket (readonly) '''


class NodeSocketVirtual:
    '''Virtual socket of a node '''

    links = None
    '''List of node links from or to this socket (readonly) '''


class NodeTree:
    '''Node tree consisting of linked nodes used for shading, textures and compositing '''

    active_input: int = None
    '''Index of the active input 

    :type: int
    '''

    active_output: int = None
    '''Index of the active output 

    :type: int
    '''

    animation_data: 'AnimData' = None
    '''Animation data for this data-block 

    :type: 'AnimData'
    '''

    bl_description: str = None
    '''

    :type: str
    '''

    bl_icon: typing.Union[int, str] = None
    '''The node tree icon 

    :type: typing.Union[int, str]
    '''

    bl_idname: str = None
    '''

    :type: str
    '''

    bl_label: str = None
    '''The node tree label 

    :type: str
    '''

    grease_pencil: 'GreasePencil' = None
    '''Grease Pencil data-block 

    :type: 'GreasePencil'
    '''

    inputs: typing.List['NodeTreeInputs'] = None
    '''Node tree inputs 

    :type: typing.List['NodeTreeInputs']
    '''

    links: typing.List['NodeLinks'] = None
    '''

    :type: typing.List['NodeLinks']
    '''

    nodes: typing.List['Nodes'] = None
    '''

    :type: typing.List['Nodes']
    '''

    outputs: typing.List['NodeSocketInterface'] = None
    '''Node tree outputs 

    :type: typing.List['NodeSocketInterface']
    '''

    type: typing.Union[int, str] = None
    '''Node Tree type (deprecated, bl_idname is the actual node tree type identifier) 

    :type: typing.Union[int, str]
    '''

    view_center: float = None
    '''

    :type: float
    '''

    def interface_update(self, context):
        '''Updated node group interface 

        '''
        pass

    def update(self, ):
        '''Update on editor changes 

        '''
        pass


class NodeTreeInputs:
    '''Collection of Node Tree Sockets '''

    def new(self, type: str, name: str) -> 'NodeSocketInterface':
        '''Add a socket to this node tree 

        :param type: Type, Data type 
        :type type: str
        :param name: Name 
        :type name: str
        :rtype: 'NodeSocketInterface'
        :return:  New socket 
        '''
        pass

    def remove(self, socket: 'NodeSocketInterface'):
        '''Remove a socket from this node tree 

        :param socket: The socket to remove 
        :type socket: 'NodeSocketInterface'
        '''
        pass

    def clear(self, ):
        '''Remove all sockets from this node tree 

        '''
        pass

    def move(self, from_index: int, to_index: int):
        '''Move a socket to another position 

        :param from_index: From Index, Index of the socket to move 
        :type from_index: int
        :param to_index: To Index, Target index for the socket 
        :type to_index: int
        '''
        pass


class NodeTreeOutputs:
    '''Collection of Node Tree Sockets '''

    def new(self, type: str, name: str) -> 'NodeSocketInterface':
        '''Add a socket to this node tree 

        :param type: Type, Data type 
        :type type: str
        :param name: Name 
        :type name: str
        :rtype: 'NodeSocketInterface'
        :return:  New socket 
        '''
        pass

    def remove(self, socket: 'NodeSocketInterface'):
        '''Remove a socket from this node tree 

        :param socket: The socket to remove 
        :type socket: 'NodeSocketInterface'
        '''
        pass

    def clear(self, ):
        '''Remove all sockets from this node tree 

        '''
        pass

    def move(self, from_index: int, to_index: int):
        '''Move a socket to another position 

        :param from_index: From Index, Index of the socket to move 
        :type from_index: int
        :param to_index: To Index, Target index for the socket 
        :type to_index: int
        '''
        pass


class NodeTreePath:
    '''Element of the node space tree path '''

    node_tree: 'NodeTree' = None
    '''Base node tree from context 

    :type: 'NodeTree'
    '''


class Nodes:
    '''Collection of Nodes '''

    active: 'Node' = None
    '''Active node in this tree 

    :type: 'Node'
    '''

    def new(self, type: str) -> 'Node':
        '''Add a node to this node tree 

        :param type: Type, Type of node to add (Warning: should be same as node.bl_idname, not node.type!) 
        :type type: str
        :rtype: 'Node'
        :return:  New node 
        '''
        pass

    def remove(self, node: 'Node'):
        '''Remove a node from this node tree 

        :param node: The node to remove 
        :type node: 'Node'
        '''
        pass

    def clear(self, ):
        '''Remove all nodes from this node tree 

        '''
        pass


class NoiseTexture:
    '''Procedural noise texture '''

    users_material = None
    '''Materials that use this texture (readonly) '''

    users_object_modifier = None
    '''Object modifiers that use this texture (readonly) '''


class NorController:
    '''Controller passing on events based on a logical NOR operation '''

    pass


class NormalEditModifier:
    '''Modifier affecting/generating custom normals '''

    invert_vertex_group: bool = None
    '''Invert vertex group influence 

    :type: bool
    '''

    mix_factor: float = None
    '''How much of generated normals to mix with exiting ones 

    :type: float
    '''

    mix_limit: float = None
    '''Maximum angle between old and new normals 

    :type: float
    '''

    mix_mode: typing.Union[int, str] = None
    '''How to mix generated normals with existing ones 

    :type: typing.Union[int, str]
    '''

    mode: typing.Union[int, str] = None
    '''How to affect (generate) normals 

    :type: typing.Union[int, str]
    '''

    offset: float = None
    '''Offset from object’s center 

    :type: float
    '''

    target: 'Object' = None
    '''Target object used to affect normals 

    :type: 'Object'
    '''

    use_direction_parallel: bool = None
    '''Use same direction for all normals, from origin to target’s center (Directional mode only) 

    :type: bool
    '''

    vertex_group: str = None
    '''Vertex group name for selecting/weighting the affected areas 

    :type: str
    '''


class Object:
    '''Object data-block defining an object in a scene '''

    active_material: 'Material' = None
    '''Active material being displayed 

    :type: 'Material'
    '''

    active_material_index: int = None
    '''Index of active material slot 

    :type: int
    '''

    active_shape_key: 'ShapeKey' = None
    '''Current shape key 

    :type: 'ShapeKey'
    '''

    active_shape_key_index: int = None
    '''Current shape key index 

    :type: int
    '''

    animation_data: 'AnimData' = None
    '''Animation data for this data-block 

    :type: 'AnimData'
    '''

    animation_visualization: 'AnimViz' = None
    '''Animation data for this data-block 

    :type: 'AnimViz'
    '''

    bound_box: float = None
    '''Object’s bounding box in object-space coordinates, all values are -1.0 when not available 

    :type: float
    '''

    collision: 'CollisionSettings' = None
    '''Settings for using the object as a collider in physics simulation 

    :type: 'CollisionSettings'
    '''

    color: float = None
    '''Object color and alpha, used when faces have the ObColor mode enabled 

    :type: float
    '''

    constraints: typing.List['ObjectConstraints'] = None
    '''Constraints affecting the transformation of the object 

    :type: typing.List['ObjectConstraints']
    '''

    cycles: 'CyclesObjectSettings' = None
    '''Cycles object settings 

    :type: 'CyclesObjectSettings'
    '''

    cycles_visibility: 'CyclesVisibilitySettings' = None
    '''Cycles visibility settings 

    :type: 'CyclesVisibilitySettings'
    '''

    data: 'ID' = None
    '''Object data 

    :type: 'ID'
    '''

    delta_location: float = None
    '''Extra translation added to the location of the object 

    :type: float
    '''

    delta_rotation_euler: float = None
    '''Extra rotation added to the rotation of the object (when using Euler rotations) 

    :type: float
    '''

    delta_rotation_quaternion: float = None
    '''Extra rotation added to the rotation of the object (when using Quaternion rotations) 

    :type: float
    '''

    delta_scale: float = None
    '''Extra scaling added to the scale of the object 

    :type: float
    '''

    dimensions: float = None
    '''Absolute bounding box dimensions of the object 

    :type: float
    '''

    draw_bounds_type: typing.Union[int, str] = None
    '''Object boundary display type 

    :type: typing.Union[int, str]
    '''

    draw_type: typing.Union[int, str] = None
    '''Maximum draw type to display object with in viewport 

    :type: typing.Union[int, str]
    '''

    dupli_faces_scale: float = None
    '''Scale the DupliFace objects 

    :type: float
    '''

    dupli_frames_end: int = None
    '''End frame for DupliFrames 

    :type: int
    '''

    dupli_frames_off: int = None
    '''Recurring frames to exclude from the Dupliframes 

    :type: int
    '''

    dupli_frames_on: int = None
    '''Number of frames to use between DupOff frames 

    :type: int
    '''

    dupli_frames_start: int = None
    '''Start frame for DupliFrames 

    :type: int
    '''

    dupli_group: 'Group' = None
    '''Instance an existing group 

    :type: 'Group'
    '''

    dupli_list: typing.List['DupliObject'] = None
    '''Object duplis 

    :type: typing.List['DupliObject']
    '''

    dupli_type: typing.Union[int, str] = None
    '''If not None, object duplication method to use 

    :type: typing.Union[int, str]
    '''

    empty_draw_size: float = None
    '''Size of display for empties in the viewport 

    :type: float
    '''

    empty_draw_type: typing.Union[int, str] = None
    '''Viewport display style for empties 

    :type: typing.Union[int, str]
    '''

    empty_image_offset: float = None
    '''Origin offset distance 

    :type: float
    '''

    field: 'FieldSettings' = None
    '''Settings for using the object as a field in physics simulation 

    :type: 'FieldSettings'
    '''

    game: 'GameObjectSettings' = None
    '''Game engine related settings for the object 

    :type: 'GameObjectSettings'
    '''

    grease_pencil: 'GreasePencil' = None
    '''Grease Pencil data-block 

    :type: 'GreasePencil'
    '''

    hide: bool = None
    '''Restrict visibility in the viewport 

    :type: bool
    '''

    hide_render: bool = None
    '''Restrict renderability 

    :type: bool
    '''

    hide_select: bool = None
    '''Restrict selection in the viewport 

    :type: bool
    '''

    image_user: 'ImageUser' = None
    '''Parameters defining which layer, pass and frame of the image is displayed 

    :type: 'ImageUser'
    '''

    is_duplicator: bool = None
    '''

    :type: bool
    '''

    layers: bool = None
    '''Layers the object is on 

    :type: bool
    '''

    layers_local_view: bool = None
    '''3D local view layers the object is on 

    :type: bool
    '''

    location: float = None
    '''Location of the object 

    :type: float
    '''

    lock_location: bool = None
    '''Lock editing of location in the interface 

    :type: bool
    '''

    lock_rotation: bool = None
    '''Lock editing of rotation in the interface 

    :type: bool
    '''

    lock_rotation_w: bool = None
    '''Lock editing of ‘angle’ component of four-component rotations in the interface 

    :type: bool
    '''

    lock_rotations_4d: bool = None
    '''Lock editing of four component rotations by components (instead of as Eulers) 

    :type: bool
    '''

    lock_scale: bool = None
    '''Lock editing of scale in the interface 

    :type: bool
    '''

    lod_levels: typing.List['LodLevel'] = None
    '''A collection of detail levels to automatically switch between 

    :type: typing.List['LodLevel']
    '''

    material_slots: typing.List['MaterialSlot'] = None
    '''Material slots in the object 

    :type: typing.List['MaterialSlot']
    '''

    matrix_basis: float = None
    '''Matrix access to location, rotation and scale (including deltas), before constraints and parenting are applied 

    :type: float
    '''

    matrix_local: float = None
    '''Parent relative transformation matrix - WARNING: Only takes into account ‘Object’ parenting, so e.g. in case of bone parenting you get a matrix relative to the Armature object, not to the actual parent bone 

    :type: float
    '''

    matrix_parent_inverse: float = None
    '''Inverse of object’s parent matrix at time of parenting 

    :type: float
    '''

    matrix_world: float = None
    '''Worldspace transformation matrix 

    :type: float
    '''

    mode: typing.Union[int, str] = None
    '''Object interaction mode 

    :type: typing.Union[int, str]
    '''

    modifiers: typing.List['ObjectModifiers'] = None
    '''Modifiers affecting the geometric data of the object 

    :type: typing.List['ObjectModifiers']
    '''

    motion_path: 'MotionPath' = None
    '''Motion Path for this element 

    :type: 'MotionPath'
    '''

    parent: 'Object' = None
    '''Parent Object 

    :type: 'Object'
    '''

    parent_bone: str = None
    '''Name of parent bone in case of a bone parenting relation 

    :type: str
    '''

    parent_type: typing.Union[int, str] = None
    '''Type of parent relation 

    :type: typing.Union[int, str]
    '''

    parent_vertices: int = None
    '''Indices of vertices in case of a vertex parenting relation 

    :type: int
    '''

    particle_systems: typing.List['ParticleSystem'] = None
    '''Particle systems emitted from the object 

    :type: typing.List['ParticleSystem']
    '''

    pass_index: int = None
    '''Index number for the “Object Index” render pass 

    :type: int
    '''

    pose: 'Pose' = None
    '''Current pose for armatures 

    :type: 'Pose'
    '''

    pose_library: 'Action' = None
    '''Action used as a pose library for armatures 

    :type: 'Action'
    '''

    proxy: 'Object' = None
    '''Library object this proxy object controls 

    :type: 'Object'
    '''

    proxy_group: 'Object' = None
    '''Library group duplicator object this proxy object controls 

    :type: 'Object'
    '''

    rigid_body: 'RigidBodyObject' = None
    '''Settings for rigid body simulation 

    :type: 'RigidBodyObject'
    '''

    rigid_body_constraint: 'RigidBodyConstraint' = None
    '''Constraint constraining rigid bodies 

    :type: 'RigidBodyConstraint'
    '''

    rotation_axis_angle: float = None
    '''Angle of Rotation for Axis-Angle rotation representation 

    :type: float
    '''

    rotation_euler: float = None
    '''Rotation in Eulers 

    :type: float
    '''

    rotation_mode: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    rotation_quaternion: float = None
    '''Rotation in Quaternions 

    :type: float
    '''

    scale: float = None
    '''Scaling of the object 

    :type: float
    '''

    select: bool = None
    '''Object selection state 

    :type: bool
    '''

    show_all_edges: bool = None
    '''Display all edges for mesh objects 

    :type: bool
    '''

    show_axis: bool = None
    '''Display the object’s origin and axes 

    :type: bool
    '''

    show_bounds: bool = None
    '''Display the object’s bounds 

    :type: bool
    '''

    show_name: bool = None
    '''Display the object’s name 

    :type: bool
    '''

    show_only_shape_key: bool = None
    '''Always show the current Shape for this Object 

    :type: bool
    '''

    show_texture_space: bool = None
    '''Display the object’s texture space 

    :type: bool
    '''

    show_transparent: bool = None
    '''Display material transparency in the object (unsupported for duplicator drawing) 

    :type: bool
    '''

    show_wire: bool = None
    '''Add the object’s wireframe over solid drawing 

    :type: bool
    '''

    show_x_ray: bool = None
    '''Make the object draw in front of others (unsupported for duplicator drawing) 

    :type: bool
    '''

    slow_parent_offset: float = None
    '''Delay in the parent relationship 

    :type: float
    '''

    soft_body: 'SoftBodySettings' = None
    '''Settings for soft body simulation 

    :type: 'SoftBodySettings'
    '''

    track_axis: typing.Union[int, str] = None
    '''Axis that points in ‘forward’ direction (applies to DupliFrame when parent ‘Follow’ is enabled) 

    :type: typing.Union[int, str]
    '''

    type: typing.Union[int, str] = None
    '''Type of Object 

    :type: typing.Union[int, str]
    '''

    up_axis: typing.Union[int, str] = None
    '''Axis that points in the upward direction (applies to DupliFrame when parent ‘Follow’ is enabled) 

    :type: typing.Union[int, str]
    '''

    use_dupli_faces_scale: bool = None
    '''Scale dupli based on face size 

    :type: bool
    '''

    use_dupli_frames_speed: bool = None
    '''Set dupliframes to use the current frame instead of parent curve’s evaluation time 

    :type: bool
    '''

    use_dupli_vertices_rotation: bool = None
    '''Rotate dupli according to vertex normal 

    :type: bool
    '''

    use_dynamic_topology_sculpting: bool = None
    '''

    :type: bool
    '''

    use_extra_recalc_data: bool = None
    '''Refresh this object’s data again on frame changes, dependency graph hack 

    :type: bool
    '''

    use_extra_recalc_object: bool = None
    '''Refresh this object again on frame changes, dependency graph hack 

    :type: bool
    '''

    use_shape_key_edit_mode: bool = None
    '''Apply shape keys in edit mode (for Meshes only) 

    :type: bool
    '''

    use_slow_parent: bool = None
    '''Create a delay in the parent relationship (beware: this isn’t renderfarm safe and may be invalid after jumping around the timeline) 

    :type: bool
    '''

    vertex_groups: typing.List['VertexGroups'] = None
    '''Vertex groups of the object 

    :type: typing.List['VertexGroups']
    '''

    children = None
    '''All the children of this object (readonly) '''

    users_group = None
    '''The groups this object is in (readonly) '''

    users_scene = None
    '''The scenes this object is in (readonly) '''

    def convert_space(self,
                      pose_bone: 'PoseBone' = None,
                      matrix: float = (0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                                       0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0),
                      from_space: typing.Union[int, str] = 'WORLD',
                      to_space: typing.Union[int, str] = 'WORLD') -> float:
        '''Convert (transform) the given matrix from one space to another 

        :param pose_bone: Bone to use to define spaces (may be None, in which case only the two ‘WORLD’ and ‘LOCAL’ spaces are usable) 
        :type pose_bone: 'PoseBone'
        :param matrix: The matrix to transform 
        :type matrix: float
        :param from_space: The space in which ‘matrix’ is currentlyWORLD World Space, The most gobal space in Blender.POSE Pose Space, The pose space of a bone (its armature’s object space).LOCAL_WITH_PARENT Local With Parent, The local space of a bone’s parent bone.LOCAL Local Space, The local space of an object/bone. 
        :type from_space: typing.Union[int, str]
        :param to_space: The space to which you want to transform ‘matrix’WORLD World Space, The most gobal space in Blender.POSE Pose Space, The pose space of a bone (its armature’s object space).LOCAL_WITH_PARENT Local With Parent, The local space of a bone’s parent bone.LOCAL Local Space, The local space of an object/bone. 
        :type to_space: typing.Union[int, str]
        :rtype: float
        :return:  The transformed matrix 
        '''
        pass

    def calc_matrix_camera(self,
                           x: int = 1,
                           y: int = 1,
                           scale_x: float = 1.0,
                           scale_y: float = 1.0) -> float:
        '''Generate the camera projection matrix of this object (mostly useful for Camera and Lamp types) 

        :param x: Width of the render area 
        :type x: int
        :param y: Height of the render area 
        :type y: int
        :param scale_x: Width scaling factor 
        :type scale_x: float
        :param scale_y: height scaling factor 
        :type scale_y: float
        :rtype: float
        :return:  The camera projection matrix 
        '''
        pass

    def camera_fit_coords(self, scene: 'Scene', coordinates: float):
        '''Compute the coordinate (and scale for ortho cameras) given object should be to ‘see’ all given coordinates 

        :param scene: Scene to get render size information from, if available 
        :type scene: 'Scene'
        :param coordinates: Coordinates to fit in 
        :type coordinates: float
        '''
        pass

    def to_mesh(self,
                scene: 'Scene',
                apply_modifiers: bool,
                settings: typing.Union[int, str],
                calc_tessface: bool = True,
                calc_undeformed: bool = False) -> 'Mesh':
        '''Create a Mesh data-block with modifiers applied 

        :param scene: Scene within which to evaluate modifiers 
        :type scene: 'Scene'
        :param apply_modifiers: Apply modifiers 
        :type apply_modifiers: bool
        :param settings: Modifier settings to applyPREVIEW Preview, Apply modifier preview settings.RENDER Render, Apply modifier render settings. 
        :type settings: typing.Union[int, str]
        :param calc_tessface: Calculate Tessellation, Calculate tessellation faces 
        :type calc_tessface: bool
        :param calc_undeformed: Calculate Undeformed, Calculate undeformed vertex coordinates 
        :type calc_undeformed: bool
        :rtype: 'Mesh'
        :return:  Mesh created from object, remove it if it is only used for export 
        '''
        pass

    def dupli_list_create(self,
                          scene: 'Scene',
                          settings: typing.Union[int, str] = 'VIEWPORT'):
        '''Create a list of dupli objects for this object, needs to be freed manually with free_dupli_list to restore the objects real matrix and layers 

        :param scene: Scene within which to evaluate duplis 
        :type scene: 'Scene'
        :param settings: Generate texture coordinates for renderingVIEWPORT Viewport, Generate duplis using viewport settings.PREVIEW Preview, Generate duplis using preview settings.RENDER Render, Generate duplis using render settings. 
        :type settings: typing.Union[int, str]
        '''
        pass

    def dupli_list_clear(self, ):
        '''Free the list of dupli objects 

        '''
        pass

    def find_armature(self, ) -> 'Object':
        '''Find armature influencing this object as a parent or via a modifier 

        :rtype: 'Object'
        :return:  Armature object influencing this object or NULL 
        '''
        pass

    def shape_key_add(self, name: str = "Key",
                      from_mix: bool = True) -> 'ShapeKey':
        '''Add shape key to this object 

        :param name: Unique name for the new keyblock 
        :type name: str
        :param from_mix: Create new shape from existing mix of shapes 
        :type from_mix: bool
        :rtype: 'ShapeKey'
        :return:  New shape keyblock 
        '''
        pass

    def shape_key_remove(self, key: 'ShapeKey'):
        '''Remove a Shape Key from this object 

        :param key: Keyblock to be removed 
        :type key: 'ShapeKey'
        '''
        pass

    def ray_cast(self, origin, direction, distance: float = 1.70141e+38):
        '''Cast a ray onto in object space 

        :param distance: Maximum distance 
        :type distance: float
        '''
        pass

    def closest_point_on_mesh(self, origin, distance: float = 1.84467e+19):
        '''Find the nearest point in object space 

        :param distance: Maximum distance 
        :type distance: float
        '''
        pass

    def is_visible(self, scene) -> bool:
        '''Determine if object is visible in a given scene 

        :rtype: bool
        :return:  Object visibility 
        '''
        pass

    def is_modified(self, scene, settings: typing.Union[int, str]) -> bool:
        '''Determine if this object is modified from the base mesh data 

        :param settings: Modifier settings to applyPREVIEW Preview, Apply modifier preview settings.RENDER Render, Apply modifier render settings. 
        :type settings: typing.Union[int, str]
        :rtype: bool
        :return:  Object visibility 
        '''
        pass

    def is_deform_modified(self, scene,
                           settings: typing.Union[int, str]) -> bool:
        '''Determine if this object is modified by a deformation from the base mesh data 

        :param settings: Modifier settings to applyPREVIEW Preview, Apply modifier preview settings.RENDER Render, Apply modifier render settings. 
        :type settings: typing.Union[int, str]
        :rtype: bool
        :return:  Object visibility 
        '''
        pass

    def update_from_editmode(self, ) -> bool:
        '''Load the objects edit-mode data into the object data 

        :rtype: bool
        :return:  Success 
        '''
        pass

    def cache_release(self, ):
        '''Release memory used by caches associated with this object. Intended to be used by render engines only 

        '''
        pass


class ObjectActuator:
    '''Actuator to control the object movement '''

    angular_velocity: float = None
    '''Angular velocity 

    :type: float
    '''

    damping: int = None
    '''Number of frames to reach the target velocity 

    :type: int
    '''

    derivate_coefficient: float = None
    '''Not required, high values can cause instability 

    :type: float
    '''

    force: float = None
    '''Force 

    :type: float
    '''

    force_max_x: float = None
    '''Upper limit for X force 

    :type: float
    '''

    force_max_y: float = None
    '''Upper limit for Y force 

    :type: float
    '''

    force_max_z: float = None
    '''Upper limit for Z force 

    :type: float
    '''

    force_min_x: float = None
    '''Lower limit for X force 

    :type: float
    '''

    force_min_y: float = None
    '''Lower limit for Y force 

    :type: float
    '''

    force_min_z: float = None
    '''Lower limit for Z force 

    :type: float
    '''

    integral_coefficient: float = None
    '''Low value (0.01) for slow response, high value (0.5) for fast response 

    :type: float
    '''

    linear_velocity: float = None
    '''Linear velocity (in Servo mode it sets the target relative linear velocity, it will be achieved by automatic application of force - Null velocity is a valid target) 

    :type: float
    '''

    mode: typing.Union[int, str] = None
    '''Specify the motion system 

    :type: typing.Union[int, str]
    '''

    offset_location: float = None
    '''Location 

    :type: float
    '''

    offset_rotation: float = None
    '''Rotation 

    :type: float
    '''

    proportional_coefficient: float = None
    '''Typical value is 60x integral coefficient 

    :type: float
    '''

    reference_object: 'Object' = None
    '''Reference object for velocity calculation, leave empty for world reference 

    :type: 'Object'
    '''

    torque: float = None
    '''Torque 

    :type: float
    '''

    use_add_character_location: bool = None
    '''Toggle between ADD and SET character location 

    :type: bool
    '''

    use_add_linear_velocity: bool = None
    '''Toggles between ADD and SET linV 

    :type: bool
    '''

    use_character_jump: bool = None
    '''Make the character jump using the settings in the physics properties 

    :type: bool
    '''

    use_local_angular_velocity: bool = None
    '''Angular velocity is defined in local coordinates 

    :type: bool
    '''

    use_local_force: bool = None
    '''Force is defined in local coordinates 

    :type: bool
    '''

    use_local_linear_velocity: bool = None
    '''Velocity is defined in local coordinates 

    :type: bool
    '''

    use_local_location: bool = None
    '''Location is defined in local coordinates 

    :type: bool
    '''

    use_local_rotation: bool = None
    '''Rotation is defined in local coordinates 

    :type: bool
    '''

    use_local_torque: bool = None
    '''Torque is defined in local coordinates 

    :type: bool
    '''

    use_servo_limit_x: bool = None
    '''Set limit to force along the X axis 

    :type: bool
    '''

    use_servo_limit_y: bool = None
    '''Set limit to force along the Y axis 

    :type: bool
    '''

    use_servo_limit_z: bool = None
    '''Set limit to force along the Z axis 

    :type: bool
    '''


class ObjectBase:
    '''An object instance in a scene '''

    layers: bool = None
    '''Layers the object base is on 

    :type: bool
    '''

    layers_local_view: bool = None
    '''3D local view layers the object base is on 

    :type: bool
    '''

    object: 'Object' = None
    '''Object this base links to 

    :type: 'Object'
    '''

    select: bool = None
    '''Object base selection state 

    :type: bool
    '''

    def layers_from_view(self, view):
        '''Sets the object layers from a 3D View (use when adding an object in local view) 

        '''
        pass


class ObjectConstraints:
    '''Collection of object constraints '''

    active: 'Constraint' = None
    '''Active Object constraint 

    :type: 'Constraint'
    '''

    def new(self, type: typing.Union[int, str]) -> 'Constraint':
        '''Add a new constraint to this object 

        :param type: Constraint type to addCAMERA_SOLVER Camera Solver.FOLLOW_TRACK Follow Track.OBJECT_SOLVER Object Solver.COPY_LOCATION Copy Location, Copy the location of a target (with an optional offset), so that they move together.COPY_ROTATION Copy Rotation, Copy the rotation of a target (with an optional offset), so that they rotate together.COPY_SCALE Copy Scale, Copy the scale factors of a target (with an optional offset), so that they are scaled by the same amount.COPY_TRANSFORMS Copy Transforms, Copy all the transformations of a target, so that they move together.LIMIT_DISTANCE Limit Distance, Restrict movements to within a certain distance of a target (at the time of constraint evaluation only).LIMIT_LOCATION Limit Location, Restrict movement along each axis within given ranges.LIMIT_ROTATION Limit Rotation, Restrict rotation along each axis within given ranges.LIMIT_SCALE Limit Scale, Restrict scaling along each axis with given ranges.MAINTAIN_VOLUME Maintain Volume, Compensate for scaling one axis by applying suitable scaling to the other two axes.TRANSFORM Transformation, Use one transform property from target to control another (or same) property on owner.TRANSFORM_CACHE Transform Cache, Look up the transformation matrix from an external file.CLAMP_TO Clamp To, Restrict movements to lie along a curve by remapping location along curve’s longest axis.DAMPED_TRACK Damped Track, Point towards a target by performing the smallest rotation necessary.IK Inverse Kinematics, Control a chain of bones by specifying the endpoint target (Bones only).LOCKED_TRACK Locked Track, Rotate around the specified (‘locked’) axis to point towards a target.SPLINE_IK Spline IK, Align chain of bones along a curve (Bones only).STRETCH_TO Stretch To, Stretch along Y-Axis to point towards a target.TRACK_TO Track To, Legacy tracking constraint prone to twisting artifacts.ACTION Action, Use transform property of target to look up pose for owner from an Action.CHILD_OF Child Of, Make target the ‘detachable’ parent of owner.FLOOR Floor, Use position (and optionally rotation) of target to define a ‘wall’ or ‘floor’ that the owner can not cross.FOLLOW_PATH Follow Path, Use to animate an object/bone following a path.PIVOT Pivot, Change pivot point for transforms (buggy).RIGID_BODY_JOINT Rigid Body Joint, Use to define a Rigid Body Constraint (for Game Engine use only).SHRINKWRAP Shrinkwrap, Restrict movements to surface of target mesh. 
        :type type: typing.Union[int, str]
        :rtype: 'Constraint'
        :return:  New constraint 
        '''
        pass

    def remove(self, constraint: 'Constraint'):
        '''Remove a constraint from this object 

        :param constraint: Removed constraint 
        :type constraint: 'Constraint'
        '''
        pass

    def clear(self, ):
        '''Remove all constraint from this object 

        '''
        pass


class ObjectModifiers:
    '''Collection of object modifiers '''

    def new(self, name: str, type: typing.Union[int, str]) -> 'Modifier':
        '''Add a new modifier 

        :param name: New name for the modifier 
        :type name: str
        :param type: Modifier type to addDATA_TRANSFER Data Transfer.MESH_CACHE Mesh Cache.MESH_SEQUENCE_CACHE Mesh Sequence Cache.NORMAL_EDIT Normal Edit.UV_PROJECT UV Project.UV_WARP UV Warp.VERTEX_WEIGHT_EDIT Vertex Weight Edit.VERTEX_WEIGHT_MIX Vertex Weight Mix.VERTEX_WEIGHT_PROXIMITY Vertex Weight Proximity.ARRAY Array.BEVEL Bevel.BOOLEAN Boolean.BUILD Build.DECIMATE Decimate.EDGE_SPLIT Edge Split.MASK Mask.MIRROR Mirror.MULTIRES Multiresolution.REMESH Remesh.SCREW Screw.SKIN Skin.SOLIDIFY Solidify.SUBSURF Subdivision Surface.TRIANGULATE Triangulate.WIREFRAME Wireframe, Generate a wireframe on the edges of a mesh.ARMATURE Armature.CAST Cast.CORRECTIVE_SMOOTH Corrective Smooth.CURVE Curve.DISPLACE Displace.HOOK Hook.LAPLACIANSMOOTH Laplacian Smooth.LAPLACIANDEFORM Laplacian Deform.LATTICE Lattice.MESH_DEFORM Mesh Deform.SHRINKWRAP Shrinkwrap.SIMPLE_DEFORM Simple Deform.SMOOTH Smooth.SURFACE_DEFORM Surface Deform.WARP Warp.WAVE Wave.CLOTH Cloth.COLLISION Collision.DYNAMIC_PAINT Dynamic Paint.EXPLODE Explode.FLUID_SIMULATION Fluid Simulation.OCEAN Ocean.PARTICLE_INSTANCE Particle Instance.PARTICLE_SYSTEM Particle System.SMOKE Smoke.SOFT_BODY Soft Body.SURFACE Surface. 
        :type type: typing.Union[int, str]
        :rtype: 'Modifier'
        :return:  Newly created modifier 
        '''
        pass

    def remove(self, modifier: 'Modifier'):
        '''Remove an existing modifier from the object 

        :param modifier: Modifier to remove 
        :type modifier: 'Modifier'
        '''
        pass

    def clear(self, ):
        '''Remove all modifiers from the object 

        '''
        pass


class ObjectSolverConstraint:
    '''Lock motion to the reconstructed object movement '''

    camera: 'Object' = None
    '''Camera to which motion is parented (if empty active scene camera is used) 

    :type: 'Object'
    '''

    clip: 'MovieClip' = None
    '''Movie Clip to get tracking data from 

    :type: 'MovieClip'
    '''

    object: str = None
    '''Movie tracking object to follow 

    :type: str
    '''

    use_active_clip: bool = None
    '''Use active clip defined in scene 

    :type: bool
    '''


class ObstacleFluidSettings:
    '''Fluid simulation settings for obstacles in the simulation '''

    impact_factor: float = None
    '''This is an unphysical value for moving objects - it controls the impact an obstacle has on the fluid, =0 behaves a bit like outflow (deleting fluid), =1 is default, while >1 results in high forces (can be used to tweak total mass) 

    :type: float
    '''

    partial_slip_factor: float = None
    '''Amount of mixing between no- and free-slip, 0 is no slip and 1 is free slip 

    :type: float
    '''

    slip_type: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    use: bool = None
    '''Object contributes to the fluid simulation 

    :type: bool
    '''

    use_animated_mesh: bool = None
    '''Export this mesh as an animated one (slower and enforces No Slip, only use if really necessary [e.g. armatures or parented objects], animated pos/rot/scale F-Curves do not require it) 

    :type: bool
    '''

    volume_initialization: typing.Union[int, str] = None
    '''Volume initialization type (WARNING: complex volumes might require too much memory and break simulation) 

    :type: typing.Union[int, str]
    '''


class OceanModifier:
    '''Simulate an ocean surface '''

    bake_foam_fade: float = None
    '''How much foam accumulates over time (baked ocean only) 

    :type: float
    '''

    choppiness: float = None
    '''Choppiness of the wave’s crest (adds some horizontal component to the displacement) 

    :type: float
    '''

    damping: float = None
    '''Damp reflected waves going in opposite direction to the wind 

    :type: float
    '''

    depth: float = None
    '''Depth of the solid ground below the water surface 

    :type: float
    '''

    filepath: str = None
    '''Path to a folder to store external baked images 

    :type: str
    '''

    foam_coverage: float = None
    '''Amount of generated foam 

    :type: float
    '''

    foam_layer_name: str = None
    '''Name of the vertex color layer used for foam 

    :type: str
    '''

    frame_end: int = None
    '''End frame of the ocean baking 

    :type: int
    '''

    frame_start: int = None
    '''Start frame of the ocean baking 

    :type: int
    '''

    geometry_mode: typing.Union[int, str] = None
    '''Method of modifying geometry 

    :type: typing.Union[int, str]
    '''

    is_cached: bool = None
    '''Whether the ocean is using cached data or simulating 

    :type: bool
    '''

    random_seed: int = None
    '''Seed of the random generator 

    :type: int
    '''

    repeat_x: int = None
    '''Repetitions of the generated surface in X 

    :type: int
    '''

    repeat_y: int = None
    '''Repetitions of the generated surface in Y 

    :type: int
    '''

    resolution: int = None
    '''Resolution of the generated surface 

    :type: int
    '''

    size: float = None
    '''Surface scale factor (does not affect the height of the waves) 

    :type: float
    '''

    spatial_size: int = None
    '''Size of the simulation domain (in meters), and of the generated geometry (in BU) 

    :type: int
    '''

    time: float = None
    '''Current time of the simulation 

    :type: float
    '''

    use_foam: bool = None
    '''Generate foam mask as a vertex color channel 

    :type: bool
    '''

    use_normals: bool = None
    '''Output normals for bump mapping - disabling can speed up performance if its not needed 

    :type: bool
    '''

    wave_alignment: float = None
    '''How much the waves are aligned to each other 

    :type: float
    '''

    wave_direction: float = None
    '''Main direction of the waves when they are (partially) aligned 

    :type: float
    '''

    wave_scale: float = None
    '''Scale of the displacement effect 

    :type: float
    '''

    wave_scale_min: float = None
    '''Shortest allowed wavelength 

    :type: float
    '''

    wind_velocity: float = None
    '''Wind speed 

    :type: float
    '''


class OceanTexData:
    '''Ocean Texture settings '''

    ocean_object: 'Object' = None
    '''Object containing the ocean modifier 

    :type: 'Object'
    '''

    output: typing.Union[int, str] = None
    '''The data that is output by the texture 

    :type: typing.Union[int, str]
    '''


class OceanTexture:
    '''Settings for the Ocean texture '''

    ocean: 'OceanTexData' = None
    '''The ocean data associated with this texture 

    :type: 'OceanTexData'
    '''

    users_material = None
    '''Materials that use this texture (readonly) '''

    users_object_modifier = None
    '''Object modifiers that use this texture (readonly) '''


class Operator:
    '''Storage of an operator being executed, or registered after execution '''

    bl_description: str = None
    '''

    :type: str
    '''

    bl_idname: str = None
    '''

    :type: str
    '''

    bl_label: str = None
    '''

    :type: str
    '''

    bl_options: typing.Set[typing.Union[int, str]] = None
    '''Options for this operator type 

    :type: typing.Set[typing.Union[int, str]]
    '''

    bl_translation_context: str = None
    '''

    :type: str
    '''

    bl_undo_group: str = None
    '''

    :type: str
    '''

    has_reports: bool = None
    '''Operator has a set of reports (warnings and errors) from last execution 

    :type: bool
    '''

    layout: 'UILayout' = None
    '''

    :type: 'UILayout'
    '''

    macros: typing.List['Macro'] = None
    '''

    :type: typing.List['Macro']
    '''

    name: str = None
    '''

    :type: str
    '''

    options: 'OperatorOptions' = None
    '''Runtime options 

    :type: 'OperatorOptions'
    '''

    properties: 'OperatorProperties' = None
    '''

    :type: 'OperatorProperties'
    '''

    bl_property = None
    '''The name of a property to use as this operators primary property. Currently this is only used to select the default property when expanding an operator into a menu. :type: string '''

    def report(self, type: typing.Set[typing.Union[int, str]], message: str):
        '''report 

        :param type: Type 
        :type type: typing.Set[typing.Union[int, str]]
        :param message: Report Message 
        :type message: str
        '''
        pass

    def is_repeat(self, ) -> bool:
        '''is_repeat 

        :rtype: bool
        :return:  result 
        '''
        pass

    def execute(self, context) -> typing.Set[typing.Union[int, str]]:
        '''Execute the operator 

        :rtype: typing.Set[typing.Union[int, str]]
        :return:  resultRUNNING_MODAL Running Modal, Keep the operator running with blender.CANCELLED Cancelled, When no action has been taken, operator exits.FINISHED Finished, When the operator is complete, operator exits.PASS_THROUGH Pass Through, Do nothing and pass the event on.INTERFACE Interface, Handled but not executed (popup menus). 
        '''
        pass

    def check(self, context) -> bool:
        '''Check the operator settings, return True to signal a change to redraw 

        :rtype: bool
        :return:  result 
        '''
        pass

    def invoke(self, context, event) -> typing.Set[typing.Union[int, str]]:
        '''Invoke the operator 

        :rtype: typing.Set[typing.Union[int, str]]
        :return:  resultRUNNING_MODAL Running Modal, Keep the operator running with blender.CANCELLED Cancelled, When no action has been taken, operator exits.FINISHED Finished, When the operator is complete, operator exits.PASS_THROUGH Pass Through, Do nothing and pass the event on.INTERFACE Interface, Handled but not executed (popup menus). 
        '''
        pass

    def modal(self, context, event) -> typing.Set[typing.Union[int, str]]:
        '''Modal operator function 

        :rtype: typing.Set[typing.Union[int, str]]
        :return:  resultRUNNING_MODAL Running Modal, Keep the operator running with blender.CANCELLED Cancelled, When no action has been taken, operator exits.FINISHED Finished, When the operator is complete, operator exits.PASS_THROUGH Pass Through, Do nothing and pass the event on.INTERFACE Interface, Handled but not executed (popup menus). 
        '''
        pass

    def draw(self, context):
        '''Draw function for the operator 

        '''
        pass

    def cancel(self, context):
        '''Called when the operator is canceled 

        '''
        pass

    def as_keywords(self, ignore=()):
        '''Return a copy of the properties as a dictionary 

        '''
        pass


class OperatorFileListElement:
    name: str = None
    '''Name of a file or directory within a file list 

    :type: str
    '''


class OperatorMacro:
    '''Storage of a sub operator in a macro after it has been added '''

    properties: 'OperatorProperties' = None
    '''

    :type: 'OperatorProperties'
    '''


class OperatorMousePath:
    '''Mouse path values for operators that record such paths '''

    loc: float = None
    '''Mouse location 

    :type: float
    '''

    time: float = None
    '''Time of mouse location 

    :type: float
    '''


class OperatorOptions:
    '''Runtime options '''

    is_grab_cursor: bool = None
    '''True when the cursor is grabbed 

    :type: bool
    '''

    is_invoke: bool = None
    '''True when invoked (even if only the execute callbacks available) 

    :type: bool
    '''

    use_cursor_region: bool = None
    '''Enable to use the region under the cursor for modal execution 

    :type: bool
    '''


class OperatorProperties:
    '''Input properties of an Operator '''

    pass


class OperatorStrokeElement:
    is_start: bool = None
    '''

    :type: bool
    '''

    location: float = None
    '''

    :type: float
    '''

    mouse: float = None
    '''

    :type: float
    '''

    pen_flip: bool = None
    '''

    :type: bool
    '''

    pressure: float = None
    '''Tablet pressure 

    :type: float
    '''

    size: float = None
    '''Brush Size in screen space 

    :type: float
    '''

    time: float = None
    '''

    :type: float
    '''


class OrController:
    '''Controller passing on events based on a logical OR operation '''

    pass


class OutflowFluidSettings:
    '''Fluid simulation settings for objects removing fluids from the simulation '''

    use: bool = None
    '''Object contributes to the fluid simulation 

    :type: bool
    '''

    use_animated_mesh: bool = None
    '''Export this mesh as an animated one (slower and enforces No Slip, only use if really necessary [e.g. armatures or parented objects], animated pos/rot/scale F-Curves do not require it) 

    :type: bool
    '''

    volume_initialization: typing.Union[int, str] = None
    '''Volume initialization type (WARNING: complex volumes might require too much memory and break simulation) 

    :type: typing.Union[int, str]
    '''


class OverDropSequence:
    '''Over Drop Sequence '''

    input_1: 'Sequence' = None
    '''First input for the effect strip 

    :type: 'Sequence'
    '''

    input_2: 'Sequence' = None
    '''Second input for the effect strip 

    :type: 'Sequence'
    '''

    input_count: int = None
    '''

    :type: int
    '''


class PARTICLE_UL_particle_systems:
    def draw_item(self, context, layout, data, item, icon, active_data,
                  active_propname, index, flt_flag):
        '''

        '''
        pass


class PHYSICS_UL_dynapaint_surfaces:
    def draw_item(self, context, layout, data, item, icon, active_data,
                  active_propname, index):
        '''

        '''
        pass


class PackedFile:
    '''External file packed into the .blend file '''

    data: str = None
    '''Raw data (bytes, exact content of the embedded file) 

    :type: str
    '''

    size: int = None
    '''Size of packed file in bytes 

    :type: int
    '''


class Paint:
    brush: 'Brush' = None
    '''Active Brush 

    :type: 'Brush'
    '''

    cavity_curve: 'CurveMapping' = None
    '''Editable cavity curve 

    :type: 'CurveMapping'
    '''

    input_samples: int = None
    '''Average multiple input samples together to smooth the brush stroke 

    :type: int
    '''

    palette: 'Palette' = None
    '''Active Palette 

    :type: 'Palette'
    '''

    show_brush: bool = None
    '''

    :type: bool
    '''

    show_brush_on_surface: bool = None
    '''

    :type: bool
    '''

    show_low_resolution: bool = None
    '''For multires, show low resolution while navigating the view 

    :type: bool
    '''

    tile_offset: float = None
    '''Stride at which tiled strokes are copied 

    :type: float
    '''

    tile_x: bool = None
    '''Tile along X axis 

    :type: bool
    '''

    tile_y: bool = None
    '''Tile along Y axis 

    :type: bool
    '''

    tile_z: bool = None
    '''Tile along Z axis 

    :type: bool
    '''

    use_cavity: bool = None
    '''Mask painting according to mesh geometry cavity 

    :type: bool
    '''

    use_symmetry_feather: bool = None
    '''Reduce the strength of the brush where it overlaps symmetrical daubs 

    :type: bool
    '''

    use_symmetry_x: bool = None
    '''Mirror brush across the X axis 

    :type: bool
    '''

    use_symmetry_y: bool = None
    '''Mirror brush across the Y axis 

    :type: bool
    '''

    use_symmetry_z: bool = None
    '''Mirror brush across the Z axis 

    :type: bool
    '''


class PaintCurve:
    pass


class Palette:
    colors: typing.List['PaletteColors'] = None
    '''

    :type: typing.List['PaletteColors']
    '''


class PaletteColor:
    color: float = None
    '''

    :type: float
    '''

    strength: float = None
    '''

    :type: float
    '''

    weight: float = None
    '''

    :type: float
    '''


class PaletteColors:
    '''Collection of palette colors '''

    active: 'PaletteColor' = None
    '''

    :type: 'PaletteColor'
    '''

    def new(self, ) -> 'PaletteColor':
        '''Add a new color to the palette 

        :rtype: 'PaletteColor'
        :return:  The newly created color 
        '''
        pass

    def remove(self, color: 'PaletteColor'):
        '''Remove a color from the palette 

        :param color: The color to remove 
        :type color: 'PaletteColor'
        '''
        pass

    def clear(self, ):
        '''Remove all colors from the palette 

        '''
        pass


class Panel:
    '''Panel containing UI elements '''

    bl_category: str = None
    '''

    :type: str
    '''

    bl_context: str = None
    '''The context in which the panel belongs to. (TODO: explain the possible combinations bl_context/bl_region_type/bl_space_type) 

    :type: str
    '''

    bl_idname: str = None
    '''If this is set, the panel gets a custom ID, otherwise it takes the name of the class used to define the panel. For example, if the class name is “OBJECT_PT_hello”, and bl_idname is not set by the script, then bl_idname = “OBJECT_PT_hello” 

    :type: str
    '''

    bl_label: str = None
    '''The panel label, shows up in the panel header at the right of the triangle used to collapse the panel 

    :type: str
    '''

    bl_options: typing.Set[typing.Union[int, str]] = None
    '''Options for this panel type 

    :type: typing.Set[typing.Union[int, str]]
    '''

    bl_region_type: typing.Union[int, str] = None
    '''The region where the panel is going to be used in 

    :type: typing.Union[int, str]
    '''

    bl_space_type: typing.Union[int, str] = None
    '''The space where the panel is going to be used in 

    :type: typing.Union[int, str]
    '''

    bl_translation_context: str = None
    '''

    :type: str
    '''

    layout: 'UILayout' = None
    '''Defines the structure of the panel in the UI 

    :type: 'UILayout'
    '''

    text: str = None
    '''XXX todo 

    :type: str
    '''

    use_pin: bool = None
    '''

    :type: bool
    '''

    def draw(self, context):
        '''Draw UI elements into the panel UI layout 

        '''
        pass

    def draw_header(self, context):
        '''Draw UI elements into the panel’s header UI layout 

        '''
        pass


class ParentActuator:
    mode: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    object: 'Object' = None
    '''Set this object as parent 

    :type: 'Object'
    '''

    use_compound: bool = None
    '''Add this object shape to the parent shape (only if the parent shape is already compound) 

    :type: bool
    '''

    use_ghost: bool = None
    '''Make this object ghost while parented 

    :type: bool
    '''


class Particle:
    '''Particle in a particle system '''

    alive_state: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    angular_velocity: float = None
    '''

    :type: float
    '''

    birth_time: float = None
    '''

    :type: float
    '''

    die_time: float = None
    '''

    :type: float
    '''

    hair_keys: typing.List['ParticleHairKey'] = None
    '''

    :type: typing.List['ParticleHairKey']
    '''

    is_exist: bool = None
    '''

    :type: bool
    '''

    is_visible: bool = None
    '''

    :type: bool
    '''

    lifetime: float = None
    '''

    :type: float
    '''

    location: float = None
    '''

    :type: float
    '''

    particle_keys: typing.List['ParticleKey'] = None
    '''

    :type: typing.List['ParticleKey']
    '''

    prev_angular_velocity: float = None
    '''

    :type: float
    '''

    prev_location: float = None
    '''

    :type: float
    '''

    prev_rotation: float = None
    '''

    :type: float
    '''

    prev_velocity: float = None
    '''

    :type: float
    '''

    rotation: float = None
    '''

    :type: float
    '''

    size: float = None
    '''

    :type: float
    '''

    velocity: float = None
    '''

    :type: float
    '''

    def uv_on_emitter(self, modifier: 'ParticleSystemModifier') -> float:
        '''Obtain uv for particle on derived mesh 

        :param modifier: Particle modifier 
        :type modifier: 'ParticleSystemModifier'
        :rtype: float
        :return:  uv 
        '''
        pass


class ParticleBrush:
    '''Particle editing brush '''

    count: int = None
    '''Particle count 

    :type: int
    '''

    curve: 'CurveMapping' = None
    '''

    :type: 'CurveMapping'
    '''

    length_mode: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    puff_mode: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    size: int = None
    '''Radius of the brush in pixels 

    :type: int
    '''

    steps: int = None
    '''Brush steps 

    :type: int
    '''

    strength: float = None
    '''Brush strength 

    :type: float
    '''

    use_puff_volume: bool = None
    '''Apply puff to unselected end-points (helps maintain hair volume when puffing root) 

    :type: bool
    '''


class ParticleDupliWeight:
    '''Weight of a particle dupliobject in a group '''

    count: int = None
    '''The number of times this object is repeated with respect to other objects 

    :type: int
    '''

    name: str = None
    '''Particle dupliobject name 

    :type: str
    '''


class ParticleEdit:
    '''Properties of particle editing mode '''

    brush: 'ParticleBrush' = None
    '''

    :type: 'ParticleBrush'
    '''

    default_key_count: int = None
    '''How many keys to make new particles with 

    :type: int
    '''

    draw_step: int = None
    '''How many steps to draw the path with 

    :type: int
    '''

    emitter_distance: float = None
    '''Distance to keep particles away from the emitter 

    :type: float
    '''

    fade_frames: int = None
    '''How many frames to fade 

    :type: int
    '''

    is_editable: bool = None
    '''A valid edit mode exists 

    :type: bool
    '''

    is_hair: bool = None
    '''Editing hair 

    :type: bool
    '''

    object: 'Object' = None
    '''The edited object 

    :type: 'Object'
    '''

    select_mode: typing.Union[int, str] = None
    '''Particle select and display mode 

    :type: typing.Union[int, str]
    '''

    shape_object: 'Object' = None
    '''Outer shape to use for tools 

    :type: 'Object'
    '''

    show_particles: bool = None
    '''Draw actual particles 

    :type: bool
    '''

    tool: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    type: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    use_auto_velocity: bool = None
    '''Calculate point velocities automatically 

    :type: bool
    '''

    use_default_interpolate: bool = None
    '''Interpolate new particles from the existing ones 

    :type: bool
    '''

    use_emitter_deflect: bool = None
    '''Keep paths from intersecting the emitter 

    :type: bool
    '''

    use_fade_time: bool = None
    '''Fade paths and keys further away from current frame 

    :type: bool
    '''

    use_preserve_length: bool = None
    '''Keep path lengths constant 

    :type: bool
    '''

    use_preserve_root: bool = None
    '''Keep root keys unmodified 

    :type: bool
    '''


class ParticleFluidSettings:
    '''Fluid simulation settings for objects storing fluid particles generated by the simulation '''

    alpha_influence: float = None
    '''Amount of particle alpha change, inverse of size influence: 0=off (all same alpha), 1=full (larger particles get lower alphas, smaller ones higher values) 

    :type: float
    '''

    filepath: str = None
    '''Directory (and/or filename prefix) to store and load particles from 

    :type: str
    '''

    particle_influence: float = None
    '''Amount of particle size scaling: 0=off (all same size), 1=full (range 0.2-2.0), >1=stronger 

    :type: float
    '''

    show_tracer: bool = None
    '''Show tracer particles 

    :type: bool
    '''

    use_drops: bool = None
    '''Show drop particles 

    :type: bool
    '''

    use_floats: bool = None
    '''Show floating foam particles 

    :type: bool
    '''


class ParticleHairKey:
    '''Particle key for hair particle system '''

    co: float = None
    '''Location of the hair key in object space 

    :type: float
    '''

    co_local: float = None
    '''Location of the hair key in its local coordinate system, relative to the emitting face 

    :type: float
    '''

    time: float = None
    '''Relative time of key over hair length 

    :type: float
    '''

    weight: float = None
    '''Weight for cloth simulation 

    :type: float
    '''

    def co_object(self, object: 'Object', modifier: 'ParticleSystemModifier',
                  particle: 'Particle') -> float:
        '''Obtain hairkey location with particle and modifier data 

        :param object: Object 
        :type object: 'Object'
        :param modifier: Particle modifier 
        :type modifier: 'ParticleSystemModifier'
        :param particle: hair particle 
        :type particle: 'Particle'
        :rtype: float
        :return:  Co, Exported hairkey location 
        '''
        pass


class ParticleInstanceModifier:
    '''Particle system instancing modifier '''

    axis: typing.Union[int, str] = None
    '''Pole axis for rotation 

    :type: typing.Union[int, str]
    '''

    object: 'Object' = None
    '''Object that has the particle system 

    :type: 'Object'
    '''

    particle_system_index: int = None
    '''

    :type: int
    '''

    position: float = None
    '''Position along path 

    :type: float
    '''

    random_position: float = None
    '''Randomize position along path 

    :type: float
    '''

    show_alive: bool = None
    '''Show instances when particles are alive 

    :type: bool
    '''

    show_dead: bool = None
    '''Show instances when particles are dead 

    :type: bool
    '''

    show_unborn: bool = None
    '''Show instances when particles are unborn 

    :type: bool
    '''

    use_children: bool = None
    '''Create instances from child particles 

    :type: bool
    '''

    use_normal: bool = None
    '''Create instances from normal particles 

    :type: bool
    '''

    use_path: bool = None
    '''Create instances along particle paths 

    :type: bool
    '''

    use_preserve_shape: bool = None
    '''Don’t stretch the object 

    :type: bool
    '''

    use_size: bool = None
    '''Use particle size to scale the instances 

    :type: bool
    '''


class ParticleKey:
    '''Key location for a particle over time '''

    angular_velocity: float = None
    '''Key angular velocity 

    :type: float
    '''

    location: float = None
    '''Key location 

    :type: float
    '''

    rotation: float = None
    '''Key rotation quaternion 

    :type: float
    '''

    time: float = None
    '''Time of key over the simulation 

    :type: float
    '''

    velocity: float = None
    '''Key velocity 

    :type: float
    '''


class ParticleSettings:
    '''Particle settings, reusable by multiple particle systems '''

    active_dupliweight: 'ParticleDupliWeight' = None
    '''

    :type: 'ParticleDupliWeight'
    '''

    active_dupliweight_index: int = None
    '''

    :type: int
    '''

    active_texture: 'Texture' = None
    '''Active texture slot being displayed 

    :type: 'Texture'
    '''

    active_texture_index: int = None
    '''Index of active texture slot 

    :type: int
    '''

    adaptive_angle: int = None
    '''How many degrees path has to curve to make another render segment 

    :type: int
    '''

    adaptive_pixel: int = None
    '''How many pixels path has to cover to make another render segment 

    :type: int
    '''

    angular_velocity_factor: float = None
    '''Angular velocity amount (in radians per second) 

    :type: float
    '''

    angular_velocity_mode: typing.Union[int, str] = None
    '''What axis is used to change particle rotation with time 

    :type: typing.Union[int, str]
    '''

    animation_data: 'AnimData' = None
    '''Animation data for this data-block 

    :type: 'AnimData'
    '''

    apply_effector_to_children: bool = None
    '''Apply effectors to children 

    :type: bool
    '''

    apply_guide_to_children: bool = None
    '''

    :type: bool
    '''

    bending_random: float = None
    '''Random stiffness of hairs 

    :type: float
    '''

    billboard_align: typing.Union[int, str] = None
    '''In respect to what the billboards are aligned 

    :type: typing.Union[int, str]
    '''

    billboard_animation: typing.Union[int, str] = None
    '''How to animate billboard textures 

    :type: typing.Union[int, str]
    '''

    billboard_object: 'Object' = None
    '''Billboards face this object (default is active camera) 

    :type: 'Object'
    '''

    billboard_offset: float = None
    '''

    :type: float
    '''

    billboard_offset_split: typing.Union[int, str] = None
    '''How to offset billboard textures 

    :type: typing.Union[int, str]
    '''

    billboard_size: float = None
    '''Scale billboards relative to particle size 

    :type: float
    '''

    billboard_tilt: float = None
    '''Tilt of the billboards 

    :type: float
    '''

    billboard_tilt_random: float = None
    '''Random tilt of the billboards 

    :type: float
    '''

    billboard_uv_split: int = None
    '''Number of rows/columns to split UV coordinates for billboards 

    :type: int
    '''

    billboard_velocity_head: float = None
    '''Scale billboards by velocity 

    :type: float
    '''

    billboard_velocity_tail: float = None
    '''Scale billboards by velocity 

    :type: float
    '''

    boids: 'BoidSettings' = None
    '''

    :type: 'BoidSettings'
    '''

    branch_threshold: float = None
    '''Threshold of branching 

    :type: float
    '''

    brownian_factor: float = None
    '''Amount of random, erratic particle movement 

    :type: float
    '''

    child_length: float = None
    '''Length of child paths 

    :type: float
    '''

    child_length_threshold: float = None
    '''Amount of particles left untouched by child path length 

    :type: float
    '''

    child_nbr: int = None
    '''Number of children/parent 

    :type: int
    '''

    child_parting_factor: float = None
    '''Create parting in the children based on parent strands 

    :type: float
    '''

    child_parting_max: float = None
    '''Maximum root to tip angle (tip distance/root distance for long hair) 

    :type: float
    '''

    child_parting_min: float = None
    '''Minimum root to tip angle (tip distance/root distance for long hair) 

    :type: float
    '''

    child_radius: float = None
    '''Radius of children around parent 

    :type: float
    '''

    child_roundness: float = None
    '''Roundness of children around parent 

    :type: float
    '''

    child_size: float = None
    '''A multiplier for the child particle size 

    :type: float
    '''

    child_size_random: float = None
    '''Random variation to the size of the child particles 

    :type: float
    '''

    child_type: typing.Union[int, str] = None
    '''Create child particles 

    :type: typing.Union[int, str]
    '''

    clump_curve: 'CurveMapping' = None
    '''Curve defining clump tapering 

    :type: 'CurveMapping'
    '''

    clump_factor: float = None
    '''Amount of clumping 

    :type: float
    '''

    clump_noise_size: float = None
    '''Size of clump noise 

    :type: float
    '''

    clump_shape: float = None
    '''Shape of clumping 

    :type: float
    '''

    collision_group: 'Group' = None
    '''Limit colliders to this Group 

    :type: 'Group'
    '''

    color_maximum: float = None
    '''Maximum length of the particle color vector 

    :type: float
    '''

    count: int = None
    '''Total number of particles 

    :type: int
    '''

    courant_target: float = None
    '''The relative distance a particle can move before requiring more subframes (target Courant number); 0.01-0.3 is the recommended range 

    :type: float
    '''

    create_long_hair_children: bool = None
    '''Calculate children that suit long hair well 

    :type: bool
    '''

    cycles: 'CyclesCurveSettings' = None
    '''Cycles hair settings 

    :type: 'CyclesCurveSettings'
    '''

    damping: float = None
    '''Amount of damping 

    :type: float
    '''

    distribution: typing.Union[int, str] = None
    '''How to distribute particles on selected element 

    :type: typing.Union[int, str]
    '''

    drag_factor: float = None
    '''Amount of air-drag 

    :type: float
    '''

    draw_color: typing.Union[int, str] = None
    '''Draw additional particle data as a color 

    :type: typing.Union[int, str]
    '''

    draw_method: typing.Union[int, str] = None
    '''How particles are drawn in viewport 

    :type: typing.Union[int, str]
    '''

    draw_percentage: int = None
    '''Percentage of particles to display in 3D view 

    :type: int
    '''

    draw_size: int = None
    '''Size of particles on viewport in pixels (0=default) 

    :type: int
    '''

    draw_step: int = None
    '''How many steps paths are drawn with (power of 2) 

    :type: int
    '''

    dupli_group: 'Group' = None
    '''Show Objects in this Group in place of particles 

    :type: 'Group'
    '''

    dupli_object: 'Object' = None
    '''Show this Object in place of particles 

    :type: 'Object'
    '''

    dupli_weights: typing.List['ParticleDupliWeight'] = None
    '''Weights for all of the objects in the dupli group 

    :type: typing.List['ParticleDupliWeight']
    '''

    effect_hair: float = None
    '''Hair stiffness for effectors 

    :type: float
    '''

    effector_amount: int = None
    '''How many particles are effectors (0 is all particles) 

    :type: int
    '''

    effector_weights: 'EffectorWeights' = None
    '''

    :type: 'EffectorWeights'
    '''

    emit_from: typing.Union[int, str] = None
    '''Where to emit particles from 

    :type: typing.Union[int, str]
    '''

    factor_random: float = None
    '''Give the starting velocity a random variation 

    :type: float
    '''

    fluid: 'SPHFluidSettings' = None
    '''

    :type: 'SPHFluidSettings'
    '''

    force_field_1: 'FieldSettings' = None
    '''

    :type: 'FieldSettings'
    '''

    force_field_2: 'FieldSettings' = None
    '''

    :type: 'FieldSettings'
    '''

    frame_end: float = None
    '''Frame number to stop emitting particles 

    :type: float
    '''

    frame_start: float = None
    '''Frame number to start emitting particles 

    :type: float
    '''

    grid_random: float = None
    '''Add random offset to the grid locations 

    :type: float
    '''

    grid_resolution: int = None
    '''The resolution of the particle grid 

    :type: int
    '''

    hair_length: float = None
    '''Length of the hair 

    :type: float
    '''

    hair_step: int = None
    '''Number of hair segments 

    :type: int
    '''

    hexagonal_grid: bool = None
    '''Create the grid in a hexagonal pattern 

    :type: bool
    '''

    integrator: typing.Union[int, str] = None
    '''Algorithm used to calculate physics, from the fastest to the most stable/accurate: Midpoint, Euler, Verlet, RK4 (Old) 

    :type: typing.Union[int, str]
    '''

    invert_grid: bool = None
    '''Invert what is considered object and what is not 

    :type: bool
    '''

    is_fluid: bool = None
    '''Particles were created by a fluid simulation 

    :type: bool
    '''

    jitter_factor: float = None
    '''Amount of jitter applied to the sampling 

    :type: float
    '''

    keyed_loops: int = None
    '''Number of times the keys are looped 

    :type: int
    '''

    keys_step: int = None
    '''

    :type: int
    '''

    kink: typing.Union[int, str] = None
    '''Type of periodic offset on the path 

    :type: typing.Union[int, str]
    '''

    kink_amplitude: float = None
    '''The amplitude of the offset 

    :type: float
    '''

    kink_amplitude_clump: float = None
    '''How much clump affects kink amplitude 

    :type: float
    '''

    kink_amplitude_random: float = None
    '''Random variation of the amplitude 

    :type: float
    '''

    kink_axis: typing.Union[int, str] = None
    '''Which axis to use for offset 

    :type: typing.Union[int, str]
    '''

    kink_axis_random: float = None
    '''Random variation of the orientation 

    :type: float
    '''

    kink_extra_steps: int = None
    '''Extra steps for resolution of special kink features 

    :type: int
    '''

    kink_flat: float = None
    '''How flat the hairs are 

    :type: float
    '''

    kink_frequency: float = None
    '''The frequency of the offset (1/total length) 

    :type: float
    '''

    kink_shape: float = None
    '''Adjust the offset to the beginning/end 

    :type: float
    '''

    length_random: float = None
    '''Give path length a random variation 

    :type: float
    '''

    lifetime: float = None
    '''Life span of the particles 

    :type: float
    '''

    lifetime_random: float = None
    '''Give the particle life a random variation 

    :type: float
    '''

    line_length_head: float = None
    '''Length of the line’s head 

    :type: float
    '''

    line_length_tail: float = None
    '''Length of the line’s tail 

    :type: float
    '''

    lock_billboard: bool = None
    '''Lock the billboards align axis 

    :type: bool
    '''

    lock_boids_to_surface: bool = None
    '''Constrain boids to a surface 

    :type: bool
    '''

    mass: float = None
    '''Mass of the particles 

    :type: float
    '''

    material: int = None
    '''Index of material slot used for rendering particles 

    :type: int
    '''

    material_slot: typing.Union[int, str] = None
    '''Material slot used for rendering particles 

    :type: typing.Union[int, str]
    '''

    normal_factor: float = None
    '''Let the surface normal give the particle a starting velocity 

    :type: float
    '''

    object_align_factor: float = None
    '''Let the emitter object orientation give the particle a starting velocity 

    :type: float
    '''

    object_factor: float = None
    '''Let the object give the particle a starting velocity 

    :type: float
    '''

    particle_factor: float = None
    '''Let the target particle give the particle a starting velocity 

    :type: float
    '''

    particle_size: float = None
    '''The size of the particles 

    :type: float
    '''

    path_end: float = None
    '''End time of drawn path 

    :type: float
    '''

    path_start: float = None
    '''Starting time of drawn path 

    :type: float
    '''

    phase_factor: float = None
    '''Rotation around the chosen orientation axis 

    :type: float
    '''

    phase_factor_random: float = None
    '''Randomize rotation around the chosen orientation axis 

    :type: float
    '''

    physics_type: typing.Union[int, str] = None
    '''Particle physics type 

    :type: typing.Union[int, str]
    '''

    react_event: typing.Union[int, str] = None
    '''The event of target particles to react on 

    :type: typing.Union[int, str]
    '''

    reactor_factor: float = None
    '''Let the vector away from the target particle’s location give the particle a starting velocity 

    :type: float
    '''

    regrow_hair: bool = None
    '''Regrow hair for each frame 

    :type: bool
    '''

    render_step: int = None
    '''How many steps paths are rendered with (power of 2) 

    :type: int
    '''

    render_type: typing.Union[int, str] = None
    '''How particles are rendered 

    :type: typing.Union[int, str]
    '''

    rendered_child_count: int = None
    '''Number of children/parent for rendering 

    :type: int
    '''

    rotation_factor_random: float = None
    '''Randomize particle orientation 

    :type: float
    '''

    rotation_mode: typing.Union[int, str] = None
    '''Particle orientation axis (does not affect Explode modifier’s results) 

    :type: typing.Union[int, str]
    '''

    roughness_1: float = None
    '''Amount of location dependent rough 

    :type: float
    '''

    roughness_1_size: float = None
    '''Size of location dependent rough 

    :type: float
    '''

    roughness_2: float = None
    '''Amount of random rough 

    :type: float
    '''

    roughness_2_size: float = None
    '''Size of random rough 

    :type: float
    '''

    roughness_2_threshold: float = None
    '''Amount of particles left untouched by random rough 

    :type: float
    '''

    roughness_curve: 'CurveMapping' = None
    '''Curve defining roughness 

    :type: 'CurveMapping'
    '''

    roughness_end_shape: float = None
    '''Shape of end point rough 

    :type: float
    '''

    roughness_endpoint: float = None
    '''Amount of end point rough 

    :type: float
    '''

    show_guide_hairs: bool = None
    '''Show guide hairs 

    :type: bool
    '''

    show_hair_grid: bool = None
    '''Show hair simulation grid 

    :type: bool
    '''

    show_health: bool = None
    '''Draw boid health 

    :type: bool
    '''

    show_number: bool = None
    '''Show particle number 

    :type: bool
    '''

    show_size: bool = None
    '''Show particle size 

    :type: bool
    '''

    show_unborn: bool = None
    '''Show particles before they are emitted 

    :type: bool
    '''

    show_velocity: bool = None
    '''Show particle velocity 

    :type: bool
    '''

    simplify_rate: float = None
    '''Speed of simplification 

    :type: float
    '''

    simplify_refsize: int = None
    '''Reference size in pixels, after which simplification begins 

    :type: int
    '''

    simplify_transition: float = None
    '''Transition period for fading out strands 

    :type: float
    '''

    simplify_viewport: float = None
    '''Speed of Simplification 

    :type: float
    '''

    size_random: float = None
    '''Give the particle size a random variation 

    :type: float
    '''

    subframes: int = None
    '''Subframes to simulate for improved stability and finer granularity simulations (dt = timestep / (subframes + 1)) 

    :type: int
    '''

    tangent_factor: float = None
    '''Let the surface tangent give the particle a starting velocity 

    :type: float
    '''

    tangent_phase: float = None
    '''Rotate the surface tangent 

    :type: float
    '''

    texture_slots: typing.List['ParticleSettingsTextureSlot'] = None
    '''Texture slots defining the mapping and influence of textures 

    :type: typing.List['ParticleSettingsTextureSlot']
    '''

    time_tweak: float = None
    '''A multiplier for physics timestep (1.0 means one frame = 1/25 seconds) 

    :type: float
    '''

    timestep: float = None
    '''The simulation timestep per frame (seconds per frame) 

    :type: float
    '''

    trail_count: int = None
    '''Number of trail particles 

    :type: int
    '''

    type: typing.Union[int, str] = None
    '''Particle Type 

    :type: typing.Union[int, str]
    '''

    use_absolute_path_time: bool = None
    '''Path timing is in absolute frames 

    :type: bool
    '''

    use_adaptive_subframes: bool = None
    '''Automatically set the number of subframes 

    :type: bool
    '''

    use_advanced_hair: bool = None
    '''Use full physics calculations for growing hair 

    :type: bool
    '''

    use_clump_curve: bool = None
    '''Use a curve to define clump tapering 

    :type: bool
    '''

    use_clump_noise: bool = None
    '''Create random clumps around the parent 

    :type: bool
    '''

    use_dead: bool = None
    '''Show particles after they have died 

    :type: bool
    '''

    use_die_on_collision: bool = None
    '''Particles die when they collide with a deflector object 

    :type: bool
    '''

    use_dynamic_rotation: bool = None
    '''Particle rotations are affected by collisions and effectors 

    :type: bool
    '''

    use_emit_random: bool = None
    '''Emit in random order of elements 

    :type: bool
    '''

    use_even_distribution: bool = None
    '''Use even distribution from faces based on face areas or edge lengths 

    :type: bool
    '''

    use_global_dupli: bool = None
    '''Use object’s global coordinates for duplication 

    :type: bool
    '''

    use_group_count: bool = None
    '''Use object multiple times in the same group 

    :type: bool
    '''

    use_group_pick_random: bool = None
    '''Pick objects from group randomly 

    :type: bool
    '''

    use_hair_bspline: bool = None
    '''Interpolate hair using B-Splines 

    :type: bool
    '''

    use_modifier_stack: bool = None
    '''Emit particles from mesh with modifiers applied (must use same subsurf level for viewport and render for correct results) 

    :type: bool
    '''

    use_multiply_size_mass: bool = None
    '''Multiply mass by particle size 

    :type: bool
    '''

    use_parent_particles: bool = None
    '''Render parent particles 

    :type: bool
    '''

    use_react_multiple: bool = None
    '''React multiple times 

    :type: bool
    '''

    use_react_start_end: bool = None
    '''Give birth to unreacted particles eventually 

    :type: bool
    '''

    use_render_adaptive: bool = None
    '''Draw steps of the particle path 

    :type: bool
    '''

    use_render_emitter: bool = None
    '''Render emitter Object also 

    :type: bool
    '''

    use_rotation_dupli: bool = None
    '''Use object’s rotation for duplication (global x-axis is aligned particle rotation axis) 

    :type: bool
    '''

    use_rotations: bool = None
    '''Calculate particle rotations 

    :type: bool
    '''

    use_roughness_curve: bool = None
    '''Use a curve to define roughness 

    :type: bool
    '''

    use_scale_dupli: bool = None
    '''Use object’s scale for duplication 

    :type: bool
    '''

    use_self_effect: bool = None
    '''Particle effectors affect themselves 

    :type: bool
    '''

    use_simplify: bool = None
    '''Remove child strands as the object becomes smaller on the screen 

    :type: bool
    '''

    use_simplify_viewport: bool = None
    '''

    :type: bool
    '''

    use_size_deflect: bool = None
    '''Use particle’s size in deflection 

    :type: bool
    '''

    use_strand_primitive: bool = None
    '''Use the strand primitive for rendering 

    :type: bool
    '''

    use_velocity_length: bool = None
    '''Multiply line length by particle speed 

    :type: bool
    '''

    use_whole_group: bool = None
    '''Use whole group at once 

    :type: bool
    '''

    userjit: int = None
    '''Emission locations / face (0 = automatic) 

    :type: int
    '''

    virtual_parents: float = None
    '''Relative amount of virtual parents 

    :type: float
    '''


class ParticleSettingsTextureSlot:
    '''Texture slot for textures in a Particle Settings data-block '''

    clump_factor: float = None
    '''Amount texture affects child clump 

    :type: float
    '''

    damp_factor: float = None
    '''Amount texture affects particle damping 

    :type: float
    '''

    density_factor: float = None
    '''Amount texture affects particle density 

    :type: float
    '''

    field_factor: float = None
    '''Amount texture affects particle force fields 

    :type: float
    '''

    gravity_factor: float = None
    '''Amount texture affects particle gravity 

    :type: float
    '''

    kink_amp_factor: float = None
    '''Amount texture affects child kink amplitude 

    :type: float
    '''

    kink_freq_factor: float = None
    '''Amount texture affects child kink frequency 

    :type: float
    '''

    length_factor: float = None
    '''Amount texture affects child hair length 

    :type: float
    '''

    life_factor: float = None
    '''Amount texture affects particle life time 

    :type: float
    '''

    mapping: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    mapping_x: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    mapping_y: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    mapping_z: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    object: 'Object' = None
    '''Object to use for mapping with Object texture coordinates 

    :type: 'Object'
    '''

    rough_factor: float = None
    '''Amount texture affects child roughness 

    :type: float
    '''

    size_factor: float = None
    '''Amount texture affects physical particle size 

    :type: float
    '''

    texture_coords: typing.Union[int, str] = None
    '''Texture coordinates used to map the texture onto the background 

    :type: typing.Union[int, str]
    '''

    time_factor: float = None
    '''Amount texture affects particle emission time 

    :type: float
    '''

    use_map_clump: bool = None
    '''Affect the child clumping 

    :type: bool
    '''

    use_map_damp: bool = None
    '''Affect the particle velocity damping 

    :type: bool
    '''

    use_map_density: bool = None
    '''Affect the density of the particles 

    :type: bool
    '''

    use_map_field: bool = None
    '''Affect the particle force fields 

    :type: bool
    '''

    use_map_gravity: bool = None
    '''Affect the particle gravity 

    :type: bool
    '''

    use_map_kink_amp: bool = None
    '''Affect the child kink amplitude 

    :type: bool
    '''

    use_map_kink_freq: bool = None
    '''Affect the child kink frequency 

    :type: bool
    '''

    use_map_length: bool = None
    '''Affect the child hair length 

    :type: bool
    '''

    use_map_life: bool = None
    '''Affect the life time of the particles 

    :type: bool
    '''

    use_map_rough: bool = None
    '''Affect the child rough 

    :type: bool
    '''

    use_map_size: bool = None
    '''Affect the particle size 

    :type: bool
    '''

    use_map_time: bool = None
    '''Affect the emission time of the particles 

    :type: bool
    '''

    use_map_velocity: bool = None
    '''Affect the particle initial velocity 

    :type: bool
    '''

    uv_layer: str = None
    '''UV map to use for mapping with UV texture coordinates 

    :type: str
    '''

    velocity_factor: float = None
    '''Amount texture affects particle initial velocity 

    :type: float
    '''


class ParticleSettingsTextureSlots:
    '''Collection of texture slots '''

    pass


class ParticleSystem:
    '''Particle system in an object '''

    active_particle_target: 'ParticleTarget' = None
    '''

    :type: 'ParticleTarget'
    '''

    active_particle_target_index: int = None
    '''

    :type: int
    '''

    billboard_normal_uv: str = None
    '''UV map to control billboard normals 

    :type: str
    '''

    billboard_split_uv: str = None
    '''UV map to control billboard splitting 

    :type: str
    '''

    billboard_time_index_uv: str = None
    '''UV map to control billboard time index (X-Y) 

    :type: str
    '''

    child_particles: typing.List['ChildParticle'] = None
    '''Child particles generated by the particle system 

    :type: typing.List['ChildParticle']
    '''

    child_seed: int = None
    '''Offset in the random number table for child particles, to get a different randomized result 

    :type: int
    '''

    cloth: 'ClothModifier' = None
    '''Cloth dynamics for hair 

    :type: 'ClothModifier'
    '''

    dt_frac: float = None
    '''The current simulation time step size, as a fraction of a frame 

    :type: float
    '''

    has_multiple_caches: bool = None
    '''Particle system has multiple point caches 

    :type: bool
    '''

    invert_vertex_group_clump: bool = None
    '''Negate the effect of the clump vertex group 

    :type: bool
    '''

    invert_vertex_group_density: bool = None
    '''Negate the effect of the density vertex group 

    :type: bool
    '''

    invert_vertex_group_field: bool = None
    '''Negate the effect of the field vertex group 

    :type: bool
    '''

    invert_vertex_group_kink: bool = None
    '''Negate the effect of the kink vertex group 

    :type: bool
    '''

    invert_vertex_group_length: bool = None
    '''Negate the effect of the length vertex group 

    :type: bool
    '''

    invert_vertex_group_rotation: bool = None
    '''Negate the effect of the rotation vertex group 

    :type: bool
    '''

    invert_vertex_group_roughness_1: bool = None
    '''Negate the effect of the roughness 1 vertex group 

    :type: bool
    '''

    invert_vertex_group_roughness_2: bool = None
    '''Negate the effect of the roughness 2 vertex group 

    :type: bool
    '''

    invert_vertex_group_roughness_end: bool = None
    '''Negate the effect of the roughness end vertex group 

    :type: bool
    '''

    invert_vertex_group_size: bool = None
    '''Negate the effect of the size vertex group 

    :type: bool
    '''

    invert_vertex_group_tangent: bool = None
    '''Negate the effect of the tangent vertex group 

    :type: bool
    '''

    invert_vertex_group_velocity: bool = None
    '''Negate the effect of the velocity vertex group 

    :type: bool
    '''

    is_editable: bool = None
    '''Particle system can be edited in particle mode 

    :type: bool
    '''

    is_edited: bool = None
    '''Particle system has been edited in particle mode 

    :type: bool
    '''

    is_global_hair: bool = None
    '''Hair keys are in global coordinate space 

    :type: bool
    '''

    name: str = None
    '''Particle system name 

    :type: str
    '''

    parent: 'Object' = None
    '''Use this object’s coordinate system instead of global coordinate system 

    :type: 'Object'
    '''

    particles: typing.List['Particle'] = None
    '''Particles generated by the particle system 

    :type: typing.List['Particle']
    '''

    point_cache: 'PointCache' = None
    '''

    :type: 'PointCache'
    '''

    reactor_target_object: 'Object' = None
    '''For reactor systems, the object that has the target particle system (empty if same object) 

    :type: 'Object'
    '''

    reactor_target_particle_system: int = None
    '''For reactor systems, index of particle system on the target object 

    :type: int
    '''

    seed: int = None
    '''Offset in the random number table, to get a different randomized result 

    :type: int
    '''

    settings: 'ParticleSettings' = None
    '''Particle system settings 

    :type: 'ParticleSettings'
    '''

    targets: typing.List['ParticleTarget'] = None
    '''Target particle systems 

    :type: typing.List['ParticleTarget']
    '''

    use_hair_dynamics: bool = None
    '''Enable hair dynamics using cloth simulation 

    :type: bool
    '''

    use_keyed_timing: bool = None
    '''Use key times 

    :type: bool
    '''

    vertex_group_clump: str = None
    '''Vertex group to control clump 

    :type: str
    '''

    vertex_group_density: str = None
    '''Vertex group to control density 

    :type: str
    '''

    vertex_group_field: str = None
    '''Vertex group to control field 

    :type: str
    '''

    vertex_group_kink: str = None
    '''Vertex group to control kink 

    :type: str
    '''

    vertex_group_length: str = None
    '''Vertex group to control length 

    :type: str
    '''

    vertex_group_rotation: str = None
    '''Vertex group to control rotation 

    :type: str
    '''

    vertex_group_roughness_1: str = None
    '''Vertex group to control roughness 1 

    :type: str
    '''

    vertex_group_roughness_2: str = None
    '''Vertex group to control roughness 2 

    :type: str
    '''

    vertex_group_roughness_end: str = None
    '''Vertex group to control roughness end 

    :type: str
    '''

    vertex_group_size: str = None
    '''Vertex group to control size 

    :type: str
    '''

    vertex_group_tangent: str = None
    '''Vertex group to control tangent 

    :type: str
    '''

    vertex_group_velocity: str = None
    '''Vertex group to control velocity 

    :type: str
    '''

    def set_resolution(self,
                       scene: 'Scene' = None,
                       object: 'Object' = None,
                       resolution: typing.Union[int, str] = 'PREVIEW'):
        '''Set the resolution to use for the number of particles 

        :param scene: Scene 
        :type scene: 'Scene'
        :param object: Object 
        :type object: 'Object'
        :param resolution: Resolution settings to applyPREVIEW Preview, Apply modifier preview settings.RENDER Render, Apply modifier render settings. 
        :type resolution: typing.Union[int, str]
        '''
        pass

    def co_hair(self, object: 'Object', particle_no: int = 0,
                step: int = 0) -> float:
        '''Obtain cache hair data 

        :param object: Object 
        :type object: 'Object'
        :param particle_no: Particle no 
        :type particle_no: int
        :param step: step no 
        :type step: int
        :rtype: float
        :return:  Co, Exported hairkey location 
        '''
        pass

    def uv_on_emitter(self,
                      modifier: 'ParticleSystemModifier',
                      particle: 'Particle' = None,
                      particle_no: int = 0,
                      uv_no: int = 0) -> float:
        '''Obtain uv for all particles 

        :param modifier: Particle modifier 
        :type modifier: 'ParticleSystemModifier'
        :param particle: Particle 
        :type particle: 'Particle'
        :param particle_no: Particle no 
        :type particle_no: int
        :param uv_no: UV no 
        :type uv_no: int
        :rtype: float
        :return:  uv 
        '''
        pass

    def mcol_on_emitter(self,
                        modifier: 'ParticleSystemModifier',
                        particle: 'Particle',
                        particle_no: int = 0,
                        vcol_no: int = 0) -> float:
        '''Obtain mcol for all particles 

        :param modifier: Particle modifier 
        :type modifier: 'ParticleSystemModifier'
        :param particle: Particle 
        :type particle: 'Particle'
        :param particle_no: Particle no 
        :type particle_no: int
        :param vcol_no: vcol no 
        :type vcol_no: int
        :rtype: float
        :return:  mcol 
        '''
        pass


class ParticleSystemModifier:
    '''Particle system simulation modifier '''

    particle_system: 'ParticleSystem' = None
    '''Particle System that this modifier controls 

    :type: 'ParticleSystem'
    '''


class ParticleSystems:
    '''Collection of particle systems '''

    active: 'ParticleSystem' = None
    '''Active particle system being displayed 

    :type: 'ParticleSystem'
    '''

    active_index: int = None
    '''Index of active particle system slot 

    :type: int
    '''


class ParticleTarget:
    '''Target particle system '''

    alliance: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    duration: float = None
    '''

    :type: float
    '''

    is_valid: bool = None
    '''Keyed particles target is valid 

    :type: bool
    '''

    name: str = None
    '''Particle target name 

    :type: str
    '''

    object: 'Object' = None
    '''The object that has the target particle system (empty if same object) 

    :type: 'Object'
    '''

    system: int = None
    '''The index of particle system on the target object 

    :type: int
    '''

    time: float = None
    '''

    :type: float
    '''


class PathCompare:
    '''Match paths against this value '''

    path: str = None
    '''

    :type: str
    '''

    use_glob: bool = None
    '''Enable wildcard globbing 

    :type: bool
    '''


class PathCompareCollection:
    '''Collection of paths '''

    pass


class PivotConstraint:
    '''Rotate around a different point '''

    head_tail: float = None
    '''Target along length of bone: Head=0, Tail=1 

    :type: float
    '''

    offset: float = None
    '''Offset of pivot from target (when set), or from owner’s location (when Fixed Position is off), or the absolute pivot point 

    :type: float
    '''

    rotation_range: typing.Union[int, str] = None
    '''Rotation range on which pivoting should occur 

    :type: typing.Union[int, str]
    '''

    subtarget: str = None
    '''

    :type: str
    '''

    target: 'Object' = None
    '''Target Object, defining the position of the pivot when defined 

    :type: 'Object'
    '''

    use_bbone_shape: bool = None
    '''Follow shape of B-Bone segments when calculating Head/Tail position 

    :type: bool
    '''

    use_relative_location: bool = None
    '''Offset will be an absolute point in space instead of relative to the target 

    :type: bool
    '''


class PointCache:
    '''Point cache for physics simulations '''

    compression: typing.Union[int, str] = None
    '''Compression method to be used 

    :type: typing.Union[int, str]
    '''

    filepath: str = None
    '''Cache file path 

    :type: str
    '''

    frame_end: int = None
    '''Frame on which the simulation stops 

    :type: int
    '''

    frame_start: int = None
    '''Frame on which the simulation starts 

    :type: int
    '''

    frame_step: int = None
    '''Number of frames between cached frames 

    :type: int
    '''

    index: int = None
    '''Index number of cache files 

    :type: int
    '''

    info: str = None
    '''Info on current cache status 

    :type: str
    '''

    is_baked: bool = None
    '''

    :type: bool
    '''

    is_baking: bool = None
    '''

    :type: bool
    '''

    is_frame_skip: bool = None
    '''

    :type: bool
    '''

    is_outdated: bool = None
    '''

    :type: bool
    '''

    name: str = None
    '''Cache name 

    :type: str
    '''

    point_caches: typing.List['PointCache'] = None
    '''Point cache list 

    :type: typing.List['PointCache']
    '''

    use_disk_cache: bool = None
    '''Save cache files to disk (.blend file must be saved first) 

    :type: bool
    '''

    use_external: bool = None
    '''Read cache from an external location 

    :type: bool
    '''

    use_library_path: bool = None
    '''Use this file’s path for the disk cache when library linked into another file (for local bakes per scene file, disable this option) 

    :type: bool
    '''


class PointCaches:
    '''Collection of point caches '''

    active_index: int = None
    '''

    :type: int
    '''


class PointDensity:
    '''Point density settings '''

    color_ramp: 'ColorRamp' = None
    '''

    :type: 'ColorRamp'
    '''

    falloff: typing.Union[int, str] = None
    '''Method of attenuating density by distance from the point 

    :type: typing.Union[int, str]
    '''

    falloff_curve: 'CurveMapping' = None
    '''

    :type: 'CurveMapping'
    '''

    falloff_soft: float = None
    '''Softness of the ‘soft’ falloff option 

    :type: float
    '''

    falloff_speed_scale: float = None
    '''Multiplier to bring particle speed within an acceptable range 

    :type: float
    '''

    noise_basis: typing.Union[int, str] = None
    '''Noise formula used for turbulence 

    :type: typing.Union[int, str]
    '''

    object: 'Object' = None
    '''Object to take point data from 

    :type: 'Object'
    '''

    particle_cache_space: typing.Union[int, str] = None
    '''Coordinate system to cache particles in 

    :type: typing.Union[int, str]
    '''

    particle_color_source: typing.Union[int, str] = None
    '''Data to derive color results from 

    :type: typing.Union[int, str]
    '''

    particle_system: 'ParticleSystem' = None
    '''Particle System to render as points 

    :type: 'ParticleSystem'
    '''

    point_source: typing.Union[int, str] = None
    '''Point data to use as renderable point density 

    :type: typing.Union[int, str]
    '''

    radius: float = None
    '''Radius from the shaded sample to look for points within 

    :type: float
    '''

    speed_scale: float = None
    '''Multiplier to bring particle speed within an acceptable range 

    :type: float
    '''

    turbulence_depth: int = None
    '''Level of detail in the added turbulent noise 

    :type: int
    '''

    turbulence_influence: typing.Union[int, str] = None
    '''Method for driving added turbulent noise 

    :type: typing.Union[int, str]
    '''

    turbulence_scale: float = None
    '''Scale of the added turbulent noise 

    :type: float
    '''

    turbulence_strength: float = None
    '''Strength of the added turbulent noise 

    :type: float
    '''

    use_falloff_curve: bool = None
    '''Use a custom falloff curve 

    :type: bool
    '''

    use_turbulence: bool = None
    '''Add directed noise to the density at render-time 

    :type: bool
    '''

    vertex_attribute_name: str = None
    '''Vertex attribute to use for color 

    :type: str
    '''

    vertex_cache_space: typing.Union[int, str] = None
    '''Coordinate system to cache vertices in 

    :type: typing.Union[int, str]
    '''

    vertex_color_source: typing.Union[int, str] = None
    '''Data to derive color results from 

    :type: typing.Union[int, str]
    '''


class PointDensityTexture:
    '''Settings for the Point Density texture '''

    point_density: 'PointDensity' = None
    '''The point density settings associated with this texture 

    :type: 'PointDensity'
    '''

    users_material = None
    '''Materials that use this texture (readonly) '''

    users_object_modifier = None
    '''Object modifiers that use this texture (readonly) '''


class PointLamp:
    '''Omnidirectional point lamp '''

    compression_threshold: float = None
    '''Deep shadow map compression threshold 

    :type: float
    '''

    constant_coefficient: float = None
    '''Constant distance attenuation coefficient 

    :type: float
    '''

    falloff_curve: 'CurveMapping' = None
    '''Custom Lamp Falloff Curve 

    :type: 'CurveMapping'
    '''

    falloff_type: typing.Union[int, str] = None
    '''Intensity Decay with distance 

    :type: typing.Union[int, str]
    '''

    ge_shadow_buffer_type: typing.Union[int, str] = None
    '''The shadow mapping algorithm used 

    :type: typing.Union[int, str]
    '''

    linear_attenuation: float = None
    '''Linear distance attenuation 

    :type: float
    '''

    linear_coefficient: float = None
    '''Linear distance attenuation coefficient 

    :type: float
    '''

    quadratic_attenuation: float = None
    '''Quadratic distance attenuation 

    :type: float
    '''

    quadratic_coefficient: float = None
    '''Quadratic distance attenuation coefficient 

    :type: float
    '''

    shadow_adaptive_threshold: float = None
    '''Threshold for Adaptive Sampling (Raytraced shadows) 

    :type: float
    '''

    shadow_buffer_bias: float = None
    '''Shadow buffer sampling bias 

    :type: float
    '''

    shadow_buffer_bleed_bias: float = None
    '''Bias for reducing light-bleed on variance shadow maps 

    :type: float
    '''

    shadow_buffer_clip_end: float = None
    '''Shadow map clip end, beyond which objects will not generate shadows 

    :type: float
    '''

    shadow_buffer_clip_start: float = None
    '''Shadow map clip start, below which objects will not generate shadows 

    :type: float
    '''

    shadow_buffer_samples: int = None
    '''Number of shadow buffer samples 

    :type: int
    '''

    shadow_buffer_size: int = None
    '''Resolution of the shadow buffer, higher values give crisper shadows but use more memory 

    :type: int
    '''

    shadow_buffer_soft: float = None
    '''Size of shadow buffer sampling area 

    :type: float
    '''

    shadow_buffer_type: typing.Union[int, str] = None
    '''Type of shadow buffer 

    :type: typing.Union[int, str]
    '''

    shadow_color: float = None
    '''Color of shadows cast by the lamp 

    :type: float
    '''

    shadow_filter_type: typing.Union[int, str] = None
    '''Type of shadow filter (Buffer Shadows) 

    :type: typing.Union[int, str]
    '''

    shadow_method: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    shadow_ray_sample_method: typing.Union[int, str] = None
    '''Method for generating shadow samples: Adaptive QMC is fastest, Constant QMC is less noisy but slower 

    :type: typing.Union[int, str]
    '''

    shadow_ray_samples: int = None
    '''Number of samples taken extra (samples x samples) 

    :type: int
    '''

    shadow_sample_buffers: typing.Union[int, str] = None
    '''Number of shadow buffers to render for better AA, this increases memory usage 

    :type: typing.Union[int, str]
    '''

    shadow_soft_size: float = None
    '''Light size for ray shadow sampling (Raytraced shadows) 

    :type: float
    '''

    use_auto_clip_end: bool = None
    '''Automatic calculation of clipping-end, based on visible vertices 

    :type: bool
    '''

    use_auto_clip_start: bool = None
    '''Automatic calculation of clipping-start, based on visible vertices 

    :type: bool
    '''

    use_only_shadow: bool = None
    '''Cast shadows only, without illuminating objects 

    :type: bool
    '''

    use_shadow: bool = None
    '''

    :type: bool
    '''

    use_shadow_layer: bool = None
    '''Objects on the same layers only cast shadows 

    :type: bool
    '''

    use_sphere: bool = None
    '''Set light intensity to zero beyond lamp distance 

    :type: bool
    '''


class PointerProperty:
    '''RNA pointer property to point to another RNA struct '''

    fixed_type: 'Struct' = None
    '''Fixed pointer type, empty if variable type 

    :type: 'Struct'
    '''


class PolygonFloatProperties:
    '''Collection of float properties '''

    def new(self, name: str = "FloatProp") -> 'MeshPolygonFloatPropertyLayer':
        '''Add a float property layer to Mesh 

        :param name: Float property name 
        :type name: str
        :rtype: 'MeshPolygonFloatPropertyLayer'
        :return:  The newly created layer 
        '''
        pass


class PolygonIntProperties:
    '''Collection of int properties '''

    def new(self, name: str = "IntProp") -> 'MeshPolygonIntPropertyLayer':
        '''Add a integer property layer to Mesh 

        :param name: Int property name 
        :type name: str
        :rtype: 'MeshPolygonIntPropertyLayer'
        :return:  The newly created layer 
        '''
        pass


class PolygonStringProperties:
    '''Collection of string properties '''

    def new(self,
            name: str = "StringProp") -> 'MeshPolygonStringPropertyLayer':
        '''Add a string property layer to Mesh 

        :param name: String property name 
        :type name: str
        :rtype: 'MeshPolygonStringPropertyLayer'
        :return:  The newly created layer 
        '''
        pass


class Pose:
    '''A collection of pose channels, including settings for animating bones '''

    animation_visualization: 'AnimViz' = None
    '''Animation data for this data-block 

    :type: 'AnimViz'
    '''

    bone_groups: typing.List['BoneGroups'] = None
    '''Groups of the bones 

    :type: typing.List['BoneGroups']
    '''

    bones: typing.List['PoseBone'] = None
    '''Individual pose bones for the armature 

    :type: typing.List['PoseBone']
    '''

    ik_param: 'IKParam' = None
    '''Parameters for IK solver 

    :type: 'IKParam'
    '''

    ik_solver: typing.Union[int, str] = None
    '''Selection of IK solver for IK chain 

    :type: typing.Union[int, str]
    '''


class PoseBone:
    '''Channel defining pose data for a bone in a Pose '''

    bbone_curveinx: float = None
    '''X-axis handle offset for start of the B-Bone’s curve, adjusts curvature 

    :type: float
    '''

    bbone_curveiny: float = None
    '''Y-axis handle offset for start of the B-Bone’s curve, adjusts curvature 

    :type: float
    '''

    bbone_curveoutx: float = None
    '''X-axis handle offset for end of the B-Bone’s curve, adjusts curvature 

    :type: float
    '''

    bbone_curveouty: float = None
    '''Y-axis handle offset for end of the B-Bone’s curve, adjusts curvature 

    :type: float
    '''

    bbone_custom_handle_end: 'PoseBone' = None
    '''Bone that serves as the end handle for the B-Bone curve 

    :type: 'PoseBone'
    '''

    bbone_custom_handle_start: 'PoseBone' = None
    '''Bone that serves as the start handle for the B-Bone curve 

    :type: 'PoseBone'
    '''

    bbone_rollin: float = None
    '''Roll offset for the start of the B-Bone, adjusts twist 

    :type: float
    '''

    bbone_rollout: float = None
    '''Roll offset for the end of the B-Bone, adjusts twist 

    :type: float
    '''

    bbone_scalein: float = None
    '''Scale factor for start of the B-Bone, adjusts thickness (for tapering effects) 

    :type: float
    '''

    bbone_scaleout: float = None
    '''Scale factor for end of the B-Bone, adjusts thickness (for tapering effects) 

    :type: float
    '''

    bone: 'Bone' = None
    '''Bone associated with this PoseBone 

    :type: 'Bone'
    '''

    bone_group: 'BoneGroup' = None
    '''Bone Group this pose channel belongs to 

    :type: 'BoneGroup'
    '''

    bone_group_index: int = None
    '''Bone Group this pose channel belongs to (0=no group) 

    :type: int
    '''

    child: 'PoseBone' = None
    '''Child of this pose bone 

    :type: 'PoseBone'
    '''

    constraints: typing.List['PoseBoneConstraints'] = None
    '''Constraints that act on this PoseChannel 

    :type: typing.List['PoseBoneConstraints']
    '''

    custom_shape: 'Object' = None
    '''Object that defines custom draw type for this bone 

    :type: 'Object'
    '''

    custom_shape_scale: float = None
    '''Adjust the size of the custom shape 

    :type: float
    '''

    custom_shape_transform: 'PoseBone' = None
    '''Bone that defines the display transform of this custom shape 

    :type: 'PoseBone'
    '''

    head: float = None
    '''Location of head of the channel’s bone 

    :type: float
    '''

    ik_linear_weight: float = None
    '''Weight of scale constraint for IK 

    :type: float
    '''

    ik_max_x: float = None
    '''Maximum angles for IK Limit 

    :type: float
    '''

    ik_max_y: float = None
    '''Maximum angles for IK Limit 

    :type: float
    '''

    ik_max_z: float = None
    '''Maximum angles for IK Limit 

    :type: float
    '''

    ik_min_x: float = None
    '''Minimum angles for IK Limit 

    :type: float
    '''

    ik_min_y: float = None
    '''Minimum angles for IK Limit 

    :type: float
    '''

    ik_min_z: float = None
    '''Minimum angles for IK Limit 

    :type: float
    '''

    ik_rotation_weight: float = None
    '''Weight of rotation constraint for IK 

    :type: float
    '''

    ik_stiffness_x: float = None
    '''IK stiffness around the X axis 

    :type: float
    '''

    ik_stiffness_y: float = None
    '''IK stiffness around the Y axis 

    :type: float
    '''

    ik_stiffness_z: float = None
    '''IK stiffness around the Z axis 

    :type: float
    '''

    ik_stretch: float = None
    '''Allow scaling of the bone for IK 

    :type: float
    '''

    is_in_ik_chain: bool = None
    '''Is part of an IK chain 

    :type: bool
    '''

    location: float = None
    '''

    :type: float
    '''

    lock_ik_x: bool = None
    '''Disallow movement around the X axis 

    :type: bool
    '''

    lock_ik_y: bool = None
    '''Disallow movement around the Y axis 

    :type: bool
    '''

    lock_ik_z: bool = None
    '''Disallow movement around the Z axis 

    :type: bool
    '''

    lock_location: bool = None
    '''Lock editing of location in the interface 

    :type: bool
    '''

    lock_rotation: bool = None
    '''Lock editing of rotation in the interface 

    :type: bool
    '''

    lock_rotation_w: bool = None
    '''Lock editing of ‘angle’ component of four-component rotations in the interface 

    :type: bool
    '''

    lock_rotations_4d: bool = None
    '''Lock editing of four component rotations by components (instead of as Eulers) 

    :type: bool
    '''

    lock_scale: bool = None
    '''Lock editing of scale in the interface 

    :type: bool
    '''

    matrix: float = None
    '''Final 4x4 matrix after constraints and drivers are applied (object space) 

    :type: float
    '''

    matrix_basis: float = None
    '''Alternative access to location/scale/rotation relative to the parent and own rest bone 

    :type: float
    '''

    matrix_channel: float = None
    '''4x4 matrix, before constraints 

    :type: float
    '''

    motion_path: 'MotionPath' = None
    '''Motion Path for this element 

    :type: 'MotionPath'
    '''

    name: str = None
    '''

    :type: str
    '''

    parent: 'PoseBone' = None
    '''Parent of this pose bone 

    :type: 'PoseBone'
    '''

    rotation_axis_angle: float = None
    '''Angle of Rotation for Axis-Angle rotation representation 

    :type: float
    '''

    rotation_euler: float = None
    '''Rotation in Eulers 

    :type: float
    '''

    rotation_mode: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    rotation_quaternion: float = None
    '''Rotation in Quaternions 

    :type: float
    '''

    scale: float = None
    '''

    :type: float
    '''

    tail: float = None
    '''Location of tail of the channel’s bone 

    :type: float
    '''

    use_bbone_custom_handles: bool = None
    '''Use custom reference bones as handles for B-Bones instead of next/previous bones, leave these blank to use only B-Bone offset properties to control the shape 

    :type: bool
    '''

    use_bbone_relative_end_handle: bool = None
    '''Treat custom end handle position as a relative value 

    :type: bool
    '''

    use_bbone_relative_start_handle: bool = None
    '''Treat custom start handle position as a relative value 

    :type: bool
    '''

    use_custom_shape_bone_size: bool = None
    '''Scale the custom object by the bone length 

    :type: bool
    '''

    use_ik_limit_x: bool = None
    '''Limit movement around the X axis 

    :type: bool
    '''

    use_ik_limit_y: bool = None
    '''Limit movement around the Y axis 

    :type: bool
    '''

    use_ik_limit_z: bool = None
    '''Limit movement around the Z axis 

    :type: bool
    '''

    use_ik_linear_control: bool = None
    '''Apply channel size as IK constraint if stretching is enabled 

    :type: bool
    '''

    use_ik_rotation_control: bool = None
    '''Apply channel rotation as IK constraint 

    :type: bool
    '''

    basename = None
    '''The name of this bone before any ‘.’ character (readonly) '''

    center = None
    '''The midpoint between the head and the tail. (readonly) '''

    children = None
    '''(readonly) '''

    children_recursive = None
    '''A list of all children from this bone. (readonly) '''

    children_recursive_basename = None
    '''Returns a chain of children with the same base name as this bone. Only direct chains are supported, forks caused by multiple children with matching base names will terminate the function and not be returned. (readonly) '''

    length = None
    '''The distance from head to tail, when set the head is moved to fit the length. '''

    parent_recursive = None
    '''A list of parents, starting with the immediate parent (readonly) '''

    vector = None
    '''The direction this bone is pointing. Utility function for (tail - head) (readonly) '''

    x_axis = None
    '''Vector pointing down the x-axis of the bone. (readonly) '''

    y_axis = None
    '''Vector pointing down the y-axis of the bone. (readonly) '''

    z_axis = None
    '''Vector pointing down the z-axis of the bone. (readonly) '''

    def evaluate_envelope(self, point: float) -> float:
        '''Calculate bone envelope at given point 

        :param point: Point, Position in 3d space to evaluate 
        :type point: float
        :rtype: float
        :return:  Factor, Envelope factor 
        '''
        pass

    def parent_index(self, parent_test):
        '''The same as ‘bone in other_bone.parent_recursive’ but saved generating a list. 

        '''
        pass

    def translate(self, vec):
        '''Utility function to add vec to the head and tail of this bone 

        '''
        pass


class PoseBoneConstraints:
    '''Collection of pose bone constraints '''

    active: 'Constraint' = None
    '''Active PoseChannel constraint 

    :type: 'Constraint'
    '''

    def new(self, type: typing.Union[int, str]) -> 'Constraint':
        '''Add a constraint to this object 

        :param type: Constraint type to addCAMERA_SOLVER Camera Solver.FOLLOW_TRACK Follow Track.OBJECT_SOLVER Object Solver.COPY_LOCATION Copy Location, Copy the location of a target (with an optional offset), so that they move together.COPY_ROTATION Copy Rotation, Copy the rotation of a target (with an optional offset), so that they rotate together.COPY_SCALE Copy Scale, Copy the scale factors of a target (with an optional offset), so that they are scaled by the same amount.COPY_TRANSFORMS Copy Transforms, Copy all the transformations of a target, so that they move together.LIMIT_DISTANCE Limit Distance, Restrict movements to within a certain distance of a target (at the time of constraint evaluation only).LIMIT_LOCATION Limit Location, Restrict movement along each axis within given ranges.LIMIT_ROTATION Limit Rotation, Restrict rotation along each axis within given ranges.LIMIT_SCALE Limit Scale, Restrict scaling along each axis with given ranges.MAINTAIN_VOLUME Maintain Volume, Compensate for scaling one axis by applying suitable scaling to the other two axes.TRANSFORM Transformation, Use one transform property from target to control another (or same) property on owner.TRANSFORM_CACHE Transform Cache, Look up the transformation matrix from an external file.CLAMP_TO Clamp To, Restrict movements to lie along a curve by remapping location along curve’s longest axis.DAMPED_TRACK Damped Track, Point towards a target by performing the smallest rotation necessary.IK Inverse Kinematics, Control a chain of bones by specifying the endpoint target (Bones only).LOCKED_TRACK Locked Track, Rotate around the specified (‘locked’) axis to point towards a target.SPLINE_IK Spline IK, Align chain of bones along a curve (Bones only).STRETCH_TO Stretch To, Stretch along Y-Axis to point towards a target.TRACK_TO Track To, Legacy tracking constraint prone to twisting artifacts.ACTION Action, Use transform property of target to look up pose for owner from an Action.CHILD_OF Child Of, Make target the ‘detachable’ parent of owner.FLOOR Floor, Use position (and optionally rotation) of target to define a ‘wall’ or ‘floor’ that the owner can not cross.FOLLOW_PATH Follow Path, Use to animate an object/bone following a path.PIVOT Pivot, Change pivot point for transforms (buggy).RIGID_BODY_JOINT Rigid Body Joint, Use to define a Rigid Body Constraint (for Game Engine use only).SHRINKWRAP Shrinkwrap, Restrict movements to surface of target mesh. 
        :type type: typing.Union[int, str]
        :rtype: 'Constraint'
        :return:  New constraint 
        '''
        pass

    def remove(self, constraint: 'Constraint'):
        '''Remove a constraint from this object 

        :param constraint: Removed constraint 
        :type constraint: 'Constraint'
        '''
        pass


class Property:
    '''RNA property definition '''

    description: str = None
    '''Description of the property for tooltips 

    :type: str
    '''

    icon: typing.Union[int, str] = None
    '''Icon of the item 

    :type: typing.Union[int, str]
    '''

    identifier: str = None
    '''Unique name used in the code and scripting 

    :type: str
    '''

    is_animatable: bool = None
    '''Property is animatable through RNA 

    :type: bool
    '''

    is_argument_optional: bool = None
    '''True when the property is optional in a Python function implementing an RNA function 

    :type: bool
    '''

    is_enum_flag: bool = None
    '''True when multiple enums 

    :type: bool
    '''

    is_hidden: bool = None
    '''True when the property is hidden 

    :type: bool
    '''

    is_library_editable: bool = None
    '''Property is editable from linked instances (changes not saved) 

    :type: bool
    '''

    is_never_none: bool = None
    '''True when this value can’t be set to None 

    :type: bool
    '''

    is_output: bool = None
    '''True when this property is an output value from an RNA function 

    :type: bool
    '''

    is_readonly: bool = None
    '''Property is editable through RNA 

    :type: bool
    '''

    is_registered: bool = None
    '''Property is registered as part of type registration 

    :type: bool
    '''

    is_registered_optional: bool = None
    '''Property is optionally registered as part of type registration 

    :type: bool
    '''

    is_required: bool = None
    '''False when this property is an optional argument in an RNA function 

    :type: bool
    '''

    is_runtime: bool = None
    '''Property has been dynamically created at runtime 

    :type: bool
    '''

    is_skip_save: bool = None
    '''True when the property is not saved in presets 

    :type: bool
    '''

    name: str = None
    '''Human readable name 

    :type: str
    '''

    srna: 'Struct' = None
    '''Struct definition used for properties assigned to this item 

    :type: 'Struct'
    '''

    subtype: typing.Union[int, str] = None
    '''Semantic interpretation of the property 

    :type: typing.Union[int, str]
    '''

    translation_context: str = None
    '''Translation context of the property’s name 

    :type: str
    '''

    type: typing.Union[int, str] = None
    '''Data type of the property 

    :type: typing.Union[int, str]
    '''

    unit: typing.Union[int, str] = None
    '''Type of units for this property 

    :type: typing.Union[int, str]
    '''


class PropertyActuator:
    '''Actuator to handle properties '''

    mode: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    object: 'Object' = None
    '''Copy from this Object 

    :type: 'Object'
    '''

    object_property: str = None
    '''Copy this property 

    :type: str
    '''

    property: str = None
    '''The name of the property 

    :type: str
    '''

    value: str = None
    '''The name of the property or the value to use (use “” around strings) 

    :type: str
    '''


class PropertyGroup:
    '''Group of ID properties '''

    name: str = None
    '''Unique name used in the code and scripting 

    :type: str
    '''


class PropertyGroupItem:
    '''Property that stores arbitrary, user defined properties '''

    collection: typing.List['PropertyGroup'] = None
    '''

    :type: typing.List['PropertyGroup']
    '''

    double: float = None
    '''

    :type: float
    '''

    double_array: float = None
    '''

    :type: float
    '''

    float: float = None
    '''

    :type: float
    '''

    float_array: float = None
    '''

    :type: float
    '''

    group: 'PropertyGroup' = None
    '''

    :type: 'PropertyGroup'
    '''

    id: 'ID' = None
    '''

    :type: 'ID'
    '''

    idp_array: typing.List['PropertyGroup'] = None
    '''

    :type: typing.List['PropertyGroup']
    '''

    int: int = None
    '''

    :type: int
    '''

    int_array: int = None
    '''

    :type: int
    '''

    string: str = None
    '''

    :type: str
    '''


class PropertySensor:
    '''Sensor to detect values and changes in values of properties '''

    evaluation_type: typing.Union[int, str] = None
    '''Type of property evaluation 

    :type: typing.Union[int, str]
    '''

    property: str = None
    '''

    :type: str
    '''

    value: str = None
    '''Check for this value in types in Equal, Not Equal, Less Than and Greater Than types 

    :type: str
    '''

    value_max: str = None
    '''Maximum value in Interval type 

    :type: str
    '''

    value_min: str = None
    '''Minimum value in Interval type 

    :type: str
    '''


class PythonConstraint:
    '''Use Python script for constraint evaluation '''

    has_script_error: bool = None
    '''The linked Python script has thrown an error 

    :type: bool
    '''

    target_count: int = None
    '''Usually only 1-3 are needed 

    :type: int
    '''

    targets: typing.List['ConstraintTarget'] = None
    '''Target Objects 

    :type: typing.List['ConstraintTarget']
    '''

    text: 'Text' = None
    '''The text object that contains the Python script 

    :type: 'Text'
    '''

    use_targets: bool = None
    '''Use the targets indicated in the constraint panel 

    :type: bool
    '''


class PythonController:
    '''Controller executing a python script '''

    mode: typing.Union[int, str] = None
    '''Python script type (textblock or module - faster) 

    :type: typing.Union[int, str]
    '''

    module: str = None
    '''Module name and function to run, e.g. “someModule.main” (internal texts and external python files can be used) 

    :type: str
    '''

    text: 'Text' = None
    '''Text data-block with the python script 

    :type: 'Text'
    '''

    use_debug: bool = None
    '''Continuously reload the module from disk for editing external modules without restarting 

    :type: bool
    '''


class RENDERLAYER_UL_linesets:
    def draw_item(self, context, layout, data, item, icon, active_data,
                  active_propname, index):
        '''

        '''
        pass


class RENDERLAYER_UL_renderlayers:
    def draw_item(self, context, layout, data, item, icon, active_data,
                  active_propname, index):
        '''

        '''
        pass


class RENDERLAYER_UL_renderviews:
    def draw_item(self, context, layout, data, item, icon, active_data,
                  active_propname, index):
        '''

        '''
        pass


class RadarSensor:
    '''Sensor to detect objects in a cone shaped radar emanating from the current object '''

    angle: float = None
    '''Opening angle of the radar cone 

    :type: float
    '''

    axis: typing.Union[int, str] = None
    '''Along which axis the radar cone is cast 

    :type: typing.Union[int, str]
    '''

    distance: float = None
    '''Depth of the radar cone 

    :type: float
    '''

    property: str = None
    '''Only look for objects with this property (blank = all objects) 

    :type: str
    '''


class RandomActuator:
    chance: float = None
    '''Pick a number between 0 and 1, success if it’s below this value 

    :type: float
    '''

    distribution: typing.Union[int, str] = None
    '''Choose the type of distribution 

    :type: typing.Union[int, str]
    '''

    float_max: float = None
    '''Choose a number from a range: upper boundary of the range 

    :type: float
    '''

    float_mean: float = None
    '''A normal distribution: mean of the distribution 

    :type: float
    '''

    float_min: float = None
    '''Choose a number from a range: lower boundary of the range 

    :type: float
    '''

    float_value: float = None
    '''Always return this number 

    :type: float
    '''

    half_life_time: float = None
    '''Negative exponential dropoff 

    :type: float
    '''

    int_max: int = None
    '''Choose a number from a range: upper boundary of the range 

    :type: int
    '''

    int_mean: float = None
    '''Expected mean value of the distribution 

    :type: float
    '''

    int_min: int = None
    '''Choose a number from a range: lower boundary of the range 

    :type: int
    '''

    int_value: int = None
    '''Always return this number 

    :type: int
    '''

    property: str = None
    '''Assign the random value to this property 

    :type: str
    '''

    seed: int = None
    '''Initial seed of the random generator, use Python for more freedom (choose 0 for not random) 

    :type: int
    '''

    standard_derivation: float = None
    '''A normal distribution: standard deviation of the distribution 

    :type: float
    '''

    use_always_true: bool = None
    '''Always false or always true 

    :type: bool
    '''


class RandomSensor:
    '''Sensor to send random events '''

    seed: int = None
    '''Initial seed of the generator (choose 0 for not random) 

    :type: int
    '''


class RaySensor:
    '''Sensor to detect intersections with a ray emanating from the current object '''

    axis: typing.Union[int, str] = None
    '''Along which axis the ray is cast 

    :type: typing.Union[int, str]
    '''

    material: str = None
    '''Only look for objects with this material (blank = all objects) 

    :type: str
    '''

    property: str = None
    '''Only look for objects with this property (blank = all objects) 

    :type: str
    '''

    range: float = None
    '''Sense objects no farther than this distance 

    :type: float
    '''

    ray_type: typing.Union[int, str] = None
    '''Toggle collision on material or property 

    :type: typing.Union[int, str]
    '''

    use_x_ray: bool = None
    '''Toggle X-Ray option (see through objects that don’t have the property) 

    :type: bool
    '''


class Region:
    '''Region in a subdivided screen area '''

    height: int = None
    '''Region height 

    :type: int
    '''

    id: int = None
    '''Unique ID for this region 

    :type: int
    '''

    type: typing.Union[int, str] = None
    '''Type of this region 

    :type: typing.Union[int, str]
    '''

    view2d: 'View2D' = None
    '''2D view of the region 

    :type: 'View2D'
    '''

    width: int = None
    '''Region width 

    :type: int
    '''

    x: int = None
    '''The window relative vertical location of the region 

    :type: int
    '''

    y: int = None
    '''The window relative horizontal location of the region 

    :type: int
    '''

    def tag_redraw(self, ):
        '''tag_redraw 

        '''
        pass


class RegionView3D:
    '''3D View region data '''

    is_perspective: bool = None
    '''

    :type: bool
    '''

    lock_rotation: bool = None
    '''Lock view rotation in side views 

    :type: bool
    '''

    perspective_matrix: float = None
    '''Current perspective matrix (window_matrix * view_matrix) 

    :type: float
    '''

    show_sync_view: bool = None
    '''Sync view position between side views 

    :type: bool
    '''

    use_box_clip: bool = None
    '''Clip objects based on what’s visible in other side views 

    :type: bool
    '''

    view_camera_offset: float = None
    '''View shift in camera view 

    :type: float
    '''

    view_camera_zoom: float = None
    '''Zoom factor in camera view 

    :type: float
    '''

    view_distance: float = None
    '''Distance to the view location 

    :type: float
    '''

    view_location: float = None
    '''View pivot location 

    :type: float
    '''

    view_matrix: float = None
    '''Current view matrix 

    :type: float
    '''

    view_perspective: typing.Union[int, str] = None
    '''View Perspective 

    :type: typing.Union[int, str]
    '''

    view_rotation: float = None
    '''Rotation in quaternions (keep normalized) 

    :type: float
    '''

    window_matrix: float = None
    '''Current window matrix 

    :type: float
    '''

    def update(self, ):
        '''Recalculate the view matrices 

        '''
        pass


class RemeshModifier:
    '''Generate a new surface with regular topology that follows the shape of the input mesh '''

    mode: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    octree_depth: int = None
    '''Resolution of the octree; higher values give finer details 

    :type: int
    '''

    scale: float = None
    '''The ratio of the largest dimension of the model over the size of the grid 

    :type: float
    '''

    sharpness: float = None
    '''Tolerance for outliers; lower values filter noise while higher values will reproduce edges closer to the input 

    :type: float
    '''

    threshold: float = None
    '''If removing disconnected pieces, minimum size of components to preserve as a ratio of the number of polygons in the largest component 

    :type: float
    '''

    use_remove_disconnected: bool = None
    '''

    :type: bool
    '''

    use_smooth_shade: bool = None
    '''Output faces with smooth shading rather than flat shaded 

    :type: bool
    '''


class RenderEngine:
    '''Render engine '''

    bl_idname: str = None
    '''

    :type: str
    '''

    bl_label: str = None
    '''

    :type: str
    '''

    bl_use_exclude_layers: bool = None
    '''

    :type: bool
    '''

    bl_use_postprocess: bool = None
    '''

    :type: bool
    '''

    bl_use_preview: bool = None
    '''

    :type: bool
    '''

    bl_use_save_buffers: bool = None
    '''

    :type: bool
    '''

    bl_use_shading_nodes: bool = None
    '''

    :type: bool
    '''

    bl_use_shading_nodes_custom: bool = None
    '''

    :type: bool
    '''

    bl_use_spherical_stereo: bool = None
    '''

    :type: bool
    '''

    bl_use_texture_preview: bool = None
    '''

    :type: bool
    '''

    camera_override: 'Object' = None
    '''

    :type: 'Object'
    '''

    is_animation: bool = None
    '''

    :type: bool
    '''

    is_preview: bool = None
    '''

    :type: bool
    '''

    layer_override: bool = None
    '''

    :type: bool
    '''

    render: 'RenderSettings' = None
    '''

    :type: 'RenderSettings'
    '''

    resolution_x: int = None
    '''

    :type: int
    '''

    resolution_y: int = None
    '''

    :type: int
    '''

    tile_x: int = None
    '''

    :type: int
    '''

    tile_y: int = None
    '''

    :type: int
    '''

    use_highlight_tiles: bool = None
    '''

    :type: bool
    '''

    def update(self, data=None, scene=None):
        '''Export scene data for render 

        '''
        pass

    def render(self, scene=None):
        '''Render scene into an image 

        '''
        pass

    def bake(self, scene, object, pass_type: typing.Union[int, str],
             pass_filter: int, object_id: int, pixel_array, num_pixels: int,
             depth: int, result):
        '''Bake passes 

        :param pass_type: Pass, Pass to bake 
        :type pass_type: typing.Union[int, str]
        :param pass_filter: Pass Filter, Filter to combined, diffuse, glossy, transmission and subsurface passes 
        :type pass_filter: int
        :param object_id: Object Id, Id of the current object being baked in relation to the others 
        :type object_id: int
        :param num_pixels: Number of Pixels, Size of the baking batch 
        :type num_pixels: int
        :param depth: Pixels depth, Number of channels 
        :type depth: int
        '''
        pass

    def view_update(self, context=None):
        '''Update on data changes for viewport render 

        '''
        pass

    def view_draw(self, context=None):
        '''Draw viewport render 

        '''
        pass

    def update_script_node(self, node=None):
        '''Compile shader script node 

        '''
        pass

    def tag_redraw(self, ):
        '''Request redraw for viewport rendering 

        '''
        pass

    def tag_update(self, ):
        '''Request update call for viewport rendering 

        '''
        pass

    def update_render_passes(self, scene=None, renderlayer=None):
        '''Update the render passes that will be generated 

        '''
        pass

    def begin_result(self,
                     x: int,
                     y: int,
                     w: int,
                     h: int,
                     layer: str = "",
                     view: str = "") -> 'RenderResult':
        '''Create render result to write linear floating point render layers and passes 

        :param x: X 
        :type x: int
        :param y: Y 
        :type y: int
        :param w: Width 
        :type w: int
        :param h: Height 
        :type h: int
        :param layer: Layer, Single layer to get render result for 
        :type layer: str
        :param view: View, Single view to get render result for 
        :type view: str
        :rtype: 'RenderResult'
        :return:  Result 
        '''
        pass

    def update_result(self, result: 'RenderResult'):
        '''Signal that pixels have been updated and can be redrawn in the user interface 

        :param result: Result 
        :type result: 'RenderResult'
        '''
        pass

    def end_result(self,
                   result: 'RenderResult',
                   cancel: bool = False,
                   highlight: bool = False,
                   do_merge_results: bool = False):
        '''All pixels in the render result have been set and are final 

        :param result: Result 
        :type result: 'RenderResult'
        :param cancel: Cancel, Don’t mark tile as done, don’t merge results unless forced 
        :type cancel: bool
        :param highlight: Highlight, Don’t mark tile as done yet 
        :type highlight: bool
        :param do_merge_results: Merge Results, Merge results even if cancel=true 
        :type do_merge_results: bool
        '''
        pass

    def add_pass(self, name: str, channels: int, chan_id: str,
                 layer: str = ""):
        '''Add a pass to the render layer 

        :param name: Name, Name of the Pass, without view or channel tag 
        :type name: str
        :param channels: Channels 
        :type channels: int
        :param chan_id: Channel IDs, Channel names, one character per channel 
        :type chan_id: str
        :param layer: Layer, Single layer to add render pass to 
        :type layer: str
        '''
        pass

    def test_break(self, ) -> bool:
        '''Test if the render operation should been canceled, this is a fast call that should be used regularly for responsiveness 

        :rtype: bool
        :return:  Break 
        '''
        pass

    def active_view_get(self, ) -> str:
        '''active_view_get 

        :rtype: str
        :return:  View, Single view active 
        '''
        pass

    def active_view_set(self, view: str):
        '''active_view_set 

        :param view: View, Single view to set as active 
        :type view: str
        '''
        pass

    def camera_shift_x(self, camera,
                       use_spherical_stereo: bool = False) -> float:
        '''camera_shift_x 

        :param use_spherical_stereo: Spherical Stereo 
        :type use_spherical_stereo: bool
        :rtype: float
        :return:  Shift X 
        '''
        pass

    def camera_model_matrix(self,
                            camera,
                            use_spherical_stereo: bool = False,
                            r_model_matrix: float = 0.0):
        '''camera_model_matrix 

        :param use_spherical_stereo: Spherical Stereo 
        :type use_spherical_stereo: bool
        :param r_model_matrix: Model Matrix, Normalized camera model matrix 
        :type r_model_matrix: float
        '''
        pass

    def use_spherical_stereo(self, camera) -> bool:
        '''use_spherical_stereo 

        :rtype: bool
        :return:  Spherical Stereo 
        '''
        pass

    def update_stats(self, stats: str, info: str):
        '''Update and signal to redraw render status text 

        :param stats: Stats 
        :type stats: str
        :param info: Info 
        :type info: str
        '''
        pass

    def frame_set(self, frame: int, subframe: float):
        '''Evaluate scene at a different frame (for motion blur) 

        :param frame: Frame 
        :type frame: int
        :param subframe: Subframe 
        :type subframe: float
        '''
        pass

    def update_progress(self, progress: float):
        '''Update progress percentage of render 

        :param progress: Percentage of render that’s done 
        :type progress: float
        '''
        pass

    def update_memory_stats(self,
                            memory_used: float = 0.0,
                            memory_peak: float = 0.0):
        '''Update memory usage statistics 

        :param memory_used: Current memory usage in megabytes 
        :type memory_used: float
        :param memory_peak: Peak memory usage in megabytes 
        :type memory_peak: float
        '''
        pass

    def report(self, type: typing.Set[typing.Union[int, str]], message: str):
        '''Report info, warning or error messages 

        :param type: Type 
        :type type: typing.Set[typing.Union[int, str]]
        :param message: Report Message 
        :type message: str
        '''
        pass

    def error_set(self, message: str):
        '''Set error message displaying after the render is finished 

        :param message: Report Message 
        :type message: str
        '''
        pass

    def bind_display_space_shader(self, scene):
        '''Bind GLSL fragment shader that converts linear colors to display space colors using scene color management settings 

        '''
        pass

    def unbind_display_space_shader(self, ):
        '''Unbind GLSL display space shader, must always be called after binding the shader 

        '''
        pass

    def support_display_space_shader(self, scene) -> bool:
        '''Test if GLSL display space shader is supported for the combination of graphics card and scene settings 

        :rtype: bool
        :return:  Supported 
        '''
        pass

    def register_pass(self,
                      scene=None,
                      srl=None,
                      name: str = "",
                      channels: int = 1,
                      chanid: str = "",
                      type: typing.Union[int, str] = 'VALUE'):
        '''Register a render pass that will be part of the render with the current settings 

        :param name: Name 
        :type name: str
        :param channels: Channels 
        :type channels: int
        :param chanid: Channel IDs 
        :type chanid: str
        :param type: Type 
        :type type: typing.Union[int, str]
        '''
        pass


class RenderLayer:
    exclude_ambient_occlusion: bool = None
    '''Exclude AO pass from combined 

    :type: bool
    '''

    exclude_emit: bool = None
    '''Exclude emission pass from combined 

    :type: bool
    '''

    exclude_environment: bool = None
    '''Exclude environment pass from combined 

    :type: bool
    '''

    exclude_indirect: bool = None
    '''Exclude indirect pass from combined 

    :type: bool
    '''

    exclude_reflection: bool = None
    '''Exclude raytraced reflection pass from combined 

    :type: bool
    '''

    exclude_refraction: bool = None
    '''Exclude raytraced refraction pass from combined 

    :type: bool
    '''

    exclude_shadow: bool = None
    '''Exclude shadow pass from combined 

    :type: bool
    '''

    exclude_specular: bool = None
    '''Exclude specular pass from combined 

    :type: bool
    '''

    invert_zmask: bool = None
    '''For Zmask, only render what is behind solid z values instead of in front 

    :type: bool
    '''

    layers: bool = None
    '''Scene layers included in this render layer 

    :type: bool
    '''

    layers_exclude: bool = None
    '''Exclude scene layers from having any influence 

    :type: bool
    '''

    layers_zmask: bool = None
    '''Zmask scene layers for solid faces 

    :type: bool
    '''

    light_override: 'Group' = None
    '''Group to override all other lights in this render layer 

    :type: 'Group'
    '''

    material_override: 'Material' = None
    '''Material to override all other materials in this render layer 

    :type: 'Material'
    '''

    name: str = None
    '''Render layer name 

    :type: str
    '''

    passes: typing.List['RenderPasses'] = None
    '''

    :type: typing.List['RenderPasses']
    '''

    use: bool = None
    '''Disable or enable the render layer 

    :type: bool
    '''

    use_all_z: bool = None
    '''Fill in Z values for solid faces in invisible layers, for masking 

    :type: bool
    '''

    use_ao: bool = None
    '''Render AO in this Layer 

    :type: bool
    '''

    use_edge_enhance: bool = None
    '''Render Edge-enhance in this Layer (only works for Solid faces) 

    :type: bool
    '''

    use_freestyle: bool = None
    '''Render stylized strokes in this Layer 

    :type: bool
    '''

    use_halo: bool = None
    '''Render Halos in this Layer (on top of Solid) 

    :type: bool
    '''

    use_pass_ambient_occlusion: bool = None
    '''Deliver AO pass 

    :type: bool
    '''

    use_pass_color: bool = None
    '''Deliver shade-less color pass 

    :type: bool
    '''

    use_pass_combined: bool = None
    '''Deliver full combined RGBA buffer 

    :type: bool
    '''

    use_pass_diffuse: bool = None
    '''Deliver diffuse pass 

    :type: bool
    '''

    use_pass_diffuse_color: bool = None
    '''Deliver diffuse color pass 

    :type: bool
    '''

    use_pass_diffuse_direct: bool = None
    '''Deliver diffuse direct pass 

    :type: bool
    '''

    use_pass_diffuse_indirect: bool = None
    '''Deliver diffuse indirect pass 

    :type: bool
    '''

    use_pass_emit: bool = None
    '''Deliver emission pass 

    :type: bool
    '''

    use_pass_environment: bool = None
    '''Deliver environment lighting pass 

    :type: bool
    '''

    use_pass_glossy_color: bool = None
    '''Deliver glossy color pass 

    :type: bool
    '''

    use_pass_glossy_direct: bool = None
    '''Deliver glossy direct pass 

    :type: bool
    '''

    use_pass_glossy_indirect: bool = None
    '''Deliver glossy indirect pass 

    :type: bool
    '''

    use_pass_indirect: bool = None
    '''Deliver indirect lighting pass 

    :type: bool
    '''

    use_pass_material_index: bool = None
    '''Deliver material index pass 

    :type: bool
    '''

    use_pass_mist: bool = None
    '''Deliver mist factor pass (0.0-1.0) 

    :type: bool
    '''

    use_pass_normal: bool = None
    '''Deliver normal pass 

    :type: bool
    '''

    use_pass_object_index: bool = None
    '''Deliver object index pass 

    :type: bool
    '''

    use_pass_reflection: bool = None
    '''Deliver raytraced reflection pass 

    :type: bool
    '''

    use_pass_refraction: bool = None
    '''Deliver raytraced refraction pass 

    :type: bool
    '''

    use_pass_shadow: bool = None
    '''Deliver shadow pass 

    :type: bool
    '''

    use_pass_specular: bool = None
    '''Deliver specular pass 

    :type: bool
    '''

    use_pass_subsurface_color: bool = None
    '''Deliver subsurface color pass 

    :type: bool
    '''

    use_pass_subsurface_direct: bool = None
    '''Deliver subsurface direct pass 

    :type: bool
    '''

    use_pass_subsurface_indirect: bool = None
    '''Deliver subsurface indirect pass 

    :type: bool
    '''

    use_pass_transmission_color: bool = None
    '''Deliver transmission color pass 

    :type: bool
    '''

    use_pass_transmission_direct: bool = None
    '''Deliver transmission direct pass 

    :type: bool
    '''

    use_pass_transmission_indirect: bool = None
    '''Deliver transmission indirect pass 

    :type: bool
    '''

    use_pass_uv: bool = None
    '''Deliver texture UV pass 

    :type: bool
    '''

    use_pass_vector: bool = None
    '''Deliver speed vector pass 

    :type: bool
    '''

    use_pass_z: bool = None
    '''Deliver Z values pass 

    :type: bool
    '''

    use_sky: bool = None
    '''Render Sky in this Layer 

    :type: bool
    '''

    use_solid: bool = None
    '''Render Solid faces in this Layer 

    :type: bool
    '''

    use_strand: bool = None
    '''Render Strands in this Layer 

    :type: bool
    '''

    use_zmask: bool = None
    '''Only render what’s in front of the solid z values 

    :type: bool
    '''

    use_ztransp: bool = None
    '''Render Z-Transparent faces in this Layer (on top of Solid and Halos) 

    :type: bool
    '''

    def load_from_file(self, filename: str, x: int = 0, y: int = 0):
        '''Copies the pixels of this renderlayer from an image file 

        :param filename: Filename, Filename to load into this render tile, must be no smaller than the renderlayer 
        :type filename: str
        :param x: Offset X, Offset the position to copy from if the image is larger than the render layer 
        :type x: int
        :param y: Offset Y, Offset the position to copy from if the image is larger than the render layer 
        :type y: int
        '''
        pass


class RenderLayers:
    '''Collection of render layers '''

    active: 'SceneRenderLayer' = None
    '''Active Render Layer 

    :type: 'SceneRenderLayer'
    '''

    active_index: int = None
    '''Active index in render layer array 

    :type: int
    '''

    def new(self, name: str) -> 'SceneRenderLayer':
        '''Add a render layer to scene 

        :param name: New name for the render layer (not unique) 
        :type name: str
        :rtype: 'SceneRenderLayer'
        :return:  Newly created render layer 
        '''
        pass

    def remove(self, layer: 'SceneRenderLayer'):
        '''Remove a render layer 

        :param layer: Render layer to remove 
        :type layer: 'SceneRenderLayer'
        '''
        pass


class RenderPass:
    channel_id: str = None
    '''

    :type: str
    '''

    channels: int = None
    '''

    :type: int
    '''

    fullname: str = None
    '''

    :type: str
    '''

    name: str = None
    '''

    :type: str
    '''

    rect: float = None
    '''

    :type: float
    '''

    view_id: int = None
    '''

    :type: int
    '''


class RenderPasses:
    '''Collection of render passes '''

    def find_by_type(self, pass_type: typing.Union[int, str],
                     view: str) -> 'RenderPass':
        '''Get the render pass for a given type and view 

        :param pass_type: Pass 
        :type pass_type: typing.Union[int, str]
        :param view: View, Render view to get pass from 
        :type view: str
        :rtype: 'RenderPass'
        :return:  The matching render pass 
        '''
        pass

    def find_by_name(self, name: str, view: str) -> 'RenderPass':
        '''Get the render pass for a given name and view 

        :param name: Pass 
        :type name: str
        :param view: View, Render view to get pass from 
        :type view: str
        :rtype: 'RenderPass'
        :return:  The matching render pass 
        '''
        pass


class RenderResult:
    '''Result of rendering, including all layers and passes '''

    layers: typing.List['RenderLayer'] = None
    '''

    :type: typing.List['RenderLayer']
    '''

    resolution_x: int = None
    '''

    :type: int
    '''

    resolution_y: int = None
    '''

    :type: int
    '''

    views: typing.List['RenderView'] = None
    '''

    :type: typing.List['RenderView']
    '''

    def load_from_file(self, filename: str):
        '''Copies the pixels of this render result from an image file 

        :param filename: File Name, Filename to load into this render tile, must be no smaller than the render result 
        :type filename: str
        '''
        pass


class RenderSettings:
    '''Rendering settings for a Scene data-block '''

    alpha_mode: typing.Union[int, str] = None
    '''Representation of alpha information in the RGBA pixels 

    :type: typing.Union[int, str]
    '''

    antialiasing_samples: typing.Union[int, str] = None
    '''Amount of anti-aliasing samples per pixel 

    :type: typing.Union[int, str]
    '''

    bake: 'BakeSettings' = None
    '''

    :type: 'BakeSettings'
    '''

    bake_aa_mode: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    bake_bias: float = None
    '''Bias towards faces further away from the object (in blender units) 

    :type: float
    '''

    bake_distance: float = None
    '''Maximum distance from active object to other object (in blender units) 

    :type: float
    '''

    bake_margin: int = None
    '''Extends the baked result as a post process filter 

    :type: int
    '''

    bake_normal_space: typing.Union[int, str] = None
    '''Choose normal space for baking 

    :type: typing.Union[int, str]
    '''

    bake_quad_split: typing.Union[int, str] = None
    '''Choose the method used to split a quad into 2 triangles for baking 

    :type: typing.Union[int, str]
    '''

    bake_samples: int = None
    '''Number of samples used for ambient occlusion baking from multires 

    :type: int
    '''

    bake_type: typing.Union[int, str] = None
    '''Choose shading information to bake into the image 

    :type: typing.Union[int, str]
    '''

    bake_user_scale: float = None
    '''Instead of automatically normalizing to 0..1, apply a user scale to the derivative map 

    :type: float
    '''

    border_max_x: float = None
    '''Maximum X value for the render border 

    :type: float
    '''

    border_max_y: float = None
    '''Maximum Y value for the render border 

    :type: float
    '''

    border_min_x: float = None
    '''Minimum X value for the render border 

    :type: float
    '''

    border_min_y: float = None
    '''Minimum Y value for the render border 

    :type: float
    '''

    display_mode: typing.Union[int, str] = None
    '''Select where rendered images will be displayed 

    :type: typing.Union[int, str]
    '''

    dither_intensity: float = None
    '''Amount of dithering noise added to the rendered image to break up banding 

    :type: float
    '''

    edge_color: float = None
    '''Edge color 

    :type: float
    '''

    edge_threshold: int = None
    '''Threshold for drawing outlines on geometry edges 

    :type: int
    '''

    engine: typing.Union[int, str] = None
    '''Engine to use for rendering 

    :type: typing.Union[int, str]
    '''

    ffmpeg: 'FFmpegSettings' = None
    '''FFmpeg related settings for the scene 

    :type: 'FFmpegSettings'
    '''

    field_order: typing.Union[int, str] = None
    '''Order of video fields (select which lines get rendered first, to create smooth motion for TV output) 

    :type: typing.Union[int, str]
    '''

    file_extension: str = None
    '''The file extension used for saving renders 

    :type: str
    '''

    filepath: str = None
    '''Directory/name to save animations, # characters defines the position and length of frame numbers 

    :type: str
    '''

    filter_size: float = None
    '''Width over which the reconstruction filter combines samples 

    :type: float
    '''

    fps: int = None
    '''Framerate, expressed in frames per second 

    :type: int
    '''

    fps_base: float = None
    '''Framerate base 

    :type: float
    '''

    frame_map_new: int = None
    '''How many frames the Map Old will last 

    :type: int
    '''

    frame_map_old: int = None
    '''Old mapping value in frames 

    :type: int
    '''

    has_multiple_engines: bool = None
    '''More than one rendering engine is available 

    :type: bool
    '''

    image_settings: 'ImageFormatSettings' = None
    '''

    :type: 'ImageFormatSettings'
    '''

    is_movie_format: bool = None
    '''When true the format is a movie 

    :type: bool
    '''

    layers: typing.List['RenderLayers'] = None
    '''

    :type: typing.List['RenderLayers']
    '''

    line_thickness: float = None
    '''Line thickness in pixels 

    :type: float
    '''

    line_thickness_mode: typing.Union[int, str] = None
    '''Line thickness mode for Freestyle line drawing 

    :type: typing.Union[int, str]
    '''

    motion_blur_samples: int = None
    '''Number of scene samples to take with motion blur 

    :type: int
    '''

    motion_blur_shutter: float = None
    '''Time taken in frames between shutter open and close 

    :type: float
    '''

    motion_blur_shutter_curve: 'CurveMapping' = None
    '''Curve defining the shutter’s openness over time 

    :type: 'CurveMapping'
    '''

    octree_resolution: typing.Union[int, str] = None
    '''Resolution of raytrace accelerator, use higher resolutions for larger scenes 

    :type: typing.Union[int, str]
    '''

    pixel_aspect_x: float = None
    '''Horizontal aspect ratio - for anamorphic or non-square pixel output 

    :type: float
    '''

    pixel_aspect_y: float = None
    '''Vertical aspect ratio - for anamorphic or non-square pixel output 

    :type: float
    '''

    pixel_filter_type: typing.Union[int, str] = None
    '''Reconstruction filter used for combining anti-aliasing samples 

    :type: typing.Union[int, str]
    '''

    preview_start_resolution: int = None
    '''Resolution to start rendering preview at, progressively increasing it to the full viewport size 

    :type: int
    '''

    raytrace_method: typing.Union[int, str] = None
    '''Type of raytrace accelerator structure 

    :type: typing.Union[int, str]
    '''

    resolution_percentage: int = None
    '''Percentage scale for render resolution 

    :type: int
    '''

    resolution_x: int = None
    '''Number of horizontal pixels in the rendered image 

    :type: int
    '''

    resolution_y: int = None
    '''Number of vertical pixels in the rendered image 

    :type: int
    '''

    sequencer_gl_preview: typing.Union[int, str] = None
    '''Method to draw in the sequencer view 

    :type: typing.Union[int, str]
    '''

    simplify_ao_sss: float = None
    '''Global approximate AO and SSS quality factor 

    :type: float
    '''

    simplify_child_particles: float = None
    '''Global child particles percentage 

    :type: float
    '''

    simplify_child_particles_render: float = None
    '''Global child particles percentage during rendering 

    :type: float
    '''

    simplify_shadow_samples: int = None
    '''Global maximum shadow samples 

    :type: int
    '''

    simplify_subdivision: int = None
    '''Global maximum subdivision level 

    :type: int
    '''

    simplify_subdivision_render: int = None
    '''Global maximum subdivision level during rendering 

    :type: int
    '''

    stamp_background: float = None
    '''Color to use behind stamp text 

    :type: float
    '''

    stamp_font_size: int = None
    '''Size of the font used when rendering stamp text 

    :type: int
    '''

    stamp_foreground: float = None
    '''Color to use for stamp text 

    :type: float
    '''

    stamp_note_text: str = None
    '''Custom text to appear in the stamp note 

    :type: str
    '''

    stereo_views: typing.List['SceneRenderView'] = None
    '''

    :type: typing.List['SceneRenderView']
    '''

    threads: int = None
    '''Number of CPU threads to use simultaneously while rendering (for multi-core/CPU systems) 

    :type: int
    '''

    threads_mode: typing.Union[int, str] = None
    '''Determine the amount of render threads used 

    :type: typing.Union[int, str]
    '''

    tile_x: int = None
    '''Horizontal tile size to use while rendering 

    :type: int
    '''

    tile_y: int = None
    '''Vertical tile size to use while rendering 

    :type: int
    '''

    use_antialiasing: bool = None
    '''Render and combine multiple samples per pixel to prevent jagged edges 

    :type: bool
    '''

    use_bake_antialiasing: bool = None
    '''Enables Anti-aliasing 

    :type: bool
    '''

    use_bake_clear: bool = None
    '''Clear Images before baking 

    :type: bool
    '''

    use_bake_lores_mesh: bool = None
    '''Calculate heights against unsubdivided low resolution mesh 

    :type: bool
    '''

    use_bake_multires: bool = None
    '''Bake directly from multires object 

    :type: bool
    '''

    use_bake_normalize: bool = None
    '''With displacement normalize to the distance, with ambient occlusion normalize without using material settings 

    :type: bool
    '''

    use_bake_selected_to_active: bool = None
    '''Bake shading on the surface of selected objects to the active object 

    :type: bool
    '''

    use_bake_to_vertex_color: bool = None
    '''Bake to vertex colors instead of to a UV-mapped image 

    :type: bool
    '''

    use_bake_user_scale: bool = None
    '''Use a user scale for the derivative map 

    :type: bool
    '''

    use_border: bool = None
    '''Render a user-defined border region, within the frame size (note that this disables save_buffers and full_sample) 

    :type: bool
    '''

    use_compositing: bool = None
    '''Process the render result through the compositing pipeline, if compositing nodes are enabled 

    :type: bool
    '''

    use_crop_to_border: bool = None
    '''Crop the rendered frame to the defined border size 

    :type: bool
    '''

    use_edge_enhance: bool = None
    '''Create a toon outline around the edges of geometry 

    :type: bool
    '''

    use_envmaps: bool = None
    '''Calculate environment maps while rendering 

    :type: bool
    '''

    use_fields: bool = None
    '''Render image to two fields per frame, for interlaced TV output 

    :type: bool
    '''

    use_fields_still: bool = None
    '''Disable the time difference between fields 

    :type: bool
    '''

    use_file_extension: bool = None
    '''Add the file format extensions to the rendered file name (eg: filename + .jpg) 

    :type: bool
    '''

    use_free_image_textures: bool = None
    '''Free all image textures from memory after render, to save memory before compositing 

    :type: bool
    '''

    use_freestyle: bool = None
    '''Draw stylized strokes using Freestyle 

    :type: bool
    '''

    use_full_sample: bool = None
    '''Save for every anti-aliasing sample the entire RenderLayer results (this solves anti-aliasing issues with compositing) 

    :type: bool
    '''

    use_game_engine: bool = None
    '''Current rendering engine is a game engine 

    :type: bool
    '''

    use_instances: bool = None
    '''Instance support leads to effective memory reduction when using duplicates 

    :type: bool
    '''

    use_local_coords: bool = None
    '''Vertex coordinates are stored locally on each primitive (increases memory usage, but may have impact on speed) 

    :type: bool
    '''

    use_lock_interface: bool = None
    '''Lock interface during rendering in favor of giving more memory to the renderer 

    :type: bool
    '''

    use_motion_blur: bool = None
    '''Use multi-sampled 3D scene motion blur 

    :type: bool
    '''

    use_multiview: bool = None
    '''Use multiple views in the scene 

    :type: bool
    '''

    use_overwrite: bool = None
    '''Overwrite existing files while rendering 

    :type: bool
    '''

    use_persistent_data: bool = None
    '''Keep render data around for faster re-renders 

    :type: bool
    '''

    use_placeholder: bool = None
    '''Create empty placeholder files while rendering frames (similar to Unix ‘touch’) 

    :type: bool
    '''

    use_raytrace: bool = None
    '''Pre-calculate the raytrace accelerator and render raytracing effects 

    :type: bool
    '''

    use_render_cache: bool = None
    '''Save render cache to EXR files (useful for heavy compositing, Note: affects indirectly rendered scenes) 

    :type: bool
    '''

    use_save_buffers: bool = None
    '''Save tiles for all RenderLayers and SceneNodes to files in the temp directory (saves memory, required for Full Sample) 

    :type: bool
    '''

    use_sequencer: bool = None
    '''Process the render (and composited) result through the video sequence editor pipeline, if sequencer strips exist 

    :type: bool
    '''

    use_sequencer_gl_textured_solid: bool = None
    '''Draw face-assigned textures in solid draw method 

    :type: bool
    '''

    use_shading_nodes: bool = None
    '''Active render engine uses new shading nodes system 

    :type: bool
    '''

    use_shadows: bool = None
    '''Calculate shadows while rendering 

    :type: bool
    '''

    use_simplify: bool = None
    '''Enable simplification of scene for quicker preview renders 

    :type: bool
    '''

    use_simplify_triangulate: bool = None
    '''Disable non-planar quads being triangulated 

    :type: bool
    '''

    use_single_layer: bool = None
    '''Only render the active layer 

    :type: bool
    '''

    use_spherical_stereo: bool = None
    '''Active render engine supports spherical stereo rendering 

    :type: bool
    '''

    use_sss: bool = None
    '''Calculate sub-surface scattering in materials rendering 

    :type: bool
    '''

    use_stamp: bool = None
    '''Render the stamp info text in the rendered image 

    :type: bool
    '''

    use_stamp_camera: bool = None
    '''Include the name of the active camera in image metadata 

    :type: bool
    '''

    use_stamp_date: bool = None
    '''Include the current date in image metadata 

    :type: bool
    '''

    use_stamp_filename: bool = None
    '''Include the .blend filename in image metadata 

    :type: bool
    '''

    use_stamp_frame: bool = None
    '''Include the frame number in image metadata 

    :type: bool
    '''

    use_stamp_labels: bool = None
    '''Draw stamp labels (“Camera” in front of camera name, etc.) 

    :type: bool
    '''

    use_stamp_lens: bool = None
    '''Include the active camera’s lens in image metadata 

    :type: bool
    '''

    use_stamp_marker: bool = None
    '''Include the name of the last marker in image metadata 

    :type: bool
    '''

    use_stamp_memory: bool = None
    '''Include the peak memory usage in image metadata 

    :type: bool
    '''

    use_stamp_note: bool = None
    '''Include a custom note in image metadata 

    :type: bool
    '''

    use_stamp_render_time: bool = None
    '''Include the render time in image metadata 

    :type: bool
    '''

    use_stamp_scene: bool = None
    '''Include the name of the active scene in image metadata 

    :type: bool
    '''

    use_stamp_sequencer_strip: bool = None
    '''Include the name of the foreground sequence strip in image metadata 

    :type: bool
    '''

    use_stamp_strip_meta: bool = None
    '''Use metadata from the strips in the sequencer 

    :type: bool
    '''

    use_stamp_time: bool = None
    '''Include the rendered frame timecode as HH:MM:SS.FF in image metadata 

    :type: bool
    '''

    use_textures: bool = None
    '''Use textures to affect material properties 

    :type: bool
    '''

    use_world_space_shading: bool = None
    '''Use world space interpretation of lighting data for node materials 

    :type: bool
    '''

    views: typing.List['RenderViews'] = None
    '''

    :type: typing.List['RenderViews']
    '''

    views_format: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    def frame_path(self,
                   frame: int = -2147483648,
                   preview: bool = False,
                   view: str = "") -> str:
        '''Return the absolute path to the filename to be written for a given frame 

        :param frame: Frame number to use, if unset the current frame will be used 
        :type frame: int
        :param preview: Preview, Use preview range 
        :type preview: bool
        :param view: View, The name of the view to use to replace the “%” chars 
        :type view: str
        :rtype: str
        :return:  File Path, The resulting filepath from the scenes render settings 
        '''
        pass


class RenderSlot:
    '''Parameters defining the render slot '''

    name: str = None
    '''Render slot name 

    :type: str
    '''


class RenderSlots:
    '''Collection of the render slots '''

    active: 'RenderSlot' = None
    '''Active render slot of the image 

    :type: 'RenderSlot'
    '''

    active_index: int = None
    '''Index of an active render slot of the image 

    :type: int
    '''


class RenderView:
    name: str = None
    '''

    :type: str
    '''


class RenderViews:
    '''Collection of render views '''

    active: 'SceneRenderView' = None
    '''Active Render View 

    :type: 'SceneRenderView'
    '''

    active_index: int = None
    '''Active index in render view array 

    :type: int
    '''

    def new(self, name: str) -> 'SceneRenderView':
        '''Add a render view to scene 

        :param name: New name for the marker (not unique) 
        :type name: str
        :rtype: 'SceneRenderView'
        :return:  Newly created render view 
        '''
        pass

    def remove(self, view: 'SceneRenderView'):
        '''Remove a render view 

        :param view: Render view to remove 
        :type view: 'SceneRenderView'
        '''
        pass


class RigidBodyConstraint:
    '''Constraint influencing Objects inside Rigid Body Simulation '''

    breaking_threshold: float = None
    '''Impulse threshold that must be reached for the constraint to break 

    :type: float
    '''

    disable_collisions: bool = None
    '''Disable collisions between constrained rigid bodies 

    :type: bool
    '''

    enabled: bool = None
    '''Enable this constraint 

    :type: bool
    '''

    limit_ang_x_lower: float = None
    '''Lower limit of X axis rotation 

    :type: float
    '''

    limit_ang_x_upper: float = None
    '''Upper limit of X axis rotation 

    :type: float
    '''

    limit_ang_y_lower: float = None
    '''Lower limit of Y axis rotation 

    :type: float
    '''

    limit_ang_y_upper: float = None
    '''Upper limit of Y axis rotation 

    :type: float
    '''

    limit_ang_z_lower: float = None
    '''Lower limit of Z axis rotation 

    :type: float
    '''

    limit_ang_z_upper: float = None
    '''Upper limit of Z axis rotation 

    :type: float
    '''

    limit_lin_x_lower: float = None
    '''Lower limit of X axis translation 

    :type: float
    '''

    limit_lin_x_upper: float = None
    '''Upper limit of X axis translation 

    :type: float
    '''

    limit_lin_y_lower: float = None
    '''Lower limit of Y axis translation 

    :type: float
    '''

    limit_lin_y_upper: float = None
    '''Upper limit of Y axis translation 

    :type: float
    '''

    limit_lin_z_lower: float = None
    '''Lower limit of Z axis translation 

    :type: float
    '''

    limit_lin_z_upper: float = None
    '''Upper limit of Z axis translation 

    :type: float
    '''

    motor_ang_max_impulse: float = None
    '''Maximum angular motor impulse 

    :type: float
    '''

    motor_ang_target_velocity: float = None
    '''Target angular motor velocity 

    :type: float
    '''

    motor_lin_max_impulse: float = None
    '''Maximum linear motor impulse 

    :type: float
    '''

    motor_lin_target_velocity: float = None
    '''Target linear motor velocity 

    :type: float
    '''

    object1: 'Object' = None
    '''First Rigid Body Object to be constrained 

    :type: 'Object'
    '''

    object2: 'Object' = None
    '''Second Rigid Body Object to be constrained 

    :type: 'Object'
    '''

    solver_iterations: int = None
    '''Number of constraint solver iterations made per simulation step (higher values are more accurate but slower) 

    :type: int
    '''

    spring_damping_ang_x: float = None
    '''Damping on the X rotational axis 

    :type: float
    '''

    spring_damping_ang_y: float = None
    '''Damping on the Y rotational axis 

    :type: float
    '''

    spring_damping_ang_z: float = None
    '''Damping on the Z rotational axis 

    :type: float
    '''

    spring_damping_x: float = None
    '''Damping on the X axis 

    :type: float
    '''

    spring_damping_y: float = None
    '''Damping on the Y axis 

    :type: float
    '''

    spring_damping_z: float = None
    '''Damping on the Z axis 

    :type: float
    '''

    spring_stiffness_ang_x: float = None
    '''Stiffness on the X rotational axis 

    :type: float
    '''

    spring_stiffness_ang_y: float = None
    '''Stiffness on the Y rotational axis 

    :type: float
    '''

    spring_stiffness_ang_z: float = None
    '''Stiffness on the Z rotational axis 

    :type: float
    '''

    spring_stiffness_x: float = None
    '''Stiffness on the X axis 

    :type: float
    '''

    spring_stiffness_y: float = None
    '''Stiffness on the Y axis 

    :type: float
    '''

    spring_stiffness_z: float = None
    '''Stiffness on the Z axis 

    :type: float
    '''

    type: typing.Union[int, str] = None
    '''Type of Rigid Body Constraint 

    :type: typing.Union[int, str]
    '''

    use_breaking: bool = None
    '''Constraint can be broken if it receives an impulse above the threshold 

    :type: bool
    '''

    use_limit_ang_x: bool = None
    '''Limit rotation around X axis 

    :type: bool
    '''

    use_limit_ang_y: bool = None
    '''Limit rotation around Y axis 

    :type: bool
    '''

    use_limit_ang_z: bool = None
    '''Limit rotation around Z axis 

    :type: bool
    '''

    use_limit_lin_x: bool = None
    '''Limit translation on X axis 

    :type: bool
    '''

    use_limit_lin_y: bool = None
    '''Limit translation on Y axis 

    :type: bool
    '''

    use_limit_lin_z: bool = None
    '''Limit translation on Z axis 

    :type: bool
    '''

    use_motor_ang: bool = None
    '''Enable angular motor 

    :type: bool
    '''

    use_motor_lin: bool = None
    '''Enable linear motor 

    :type: bool
    '''

    use_override_solver_iterations: bool = None
    '''Override the number of solver iterations for this constraint 

    :type: bool
    '''

    use_spring_ang_x: bool = None
    '''Enable spring on X rotational axis 

    :type: bool
    '''

    use_spring_ang_y: bool = None
    '''Enable spring on Y rotational axis 

    :type: bool
    '''

    use_spring_ang_z: bool = None
    '''Enable spring on Z rotational axis 

    :type: bool
    '''

    use_spring_x: bool = None
    '''Enable spring on X axis 

    :type: bool
    '''

    use_spring_y: bool = None
    '''Enable spring on Y axis 

    :type: bool
    '''

    use_spring_z: bool = None
    '''Enable spring on Z axis 

    :type: bool
    '''


class RigidBodyJointConstraint:
    '''For use with the Game Engine '''

    axis_x: float = None
    '''Rotate pivot on X axis 

    :type: float
    '''

    axis_y: float = None
    '''Rotate pivot on Y axis 

    :type: float
    '''

    axis_z: float = None
    '''Rotate pivot on Z axis 

    :type: float
    '''

    child: 'Object' = None
    '''Child object 

    :type: 'Object'
    '''

    limit_angle_max_x: float = None
    '''

    :type: float
    '''

    limit_angle_max_y: float = None
    '''

    :type: float
    '''

    limit_angle_max_z: float = None
    '''

    :type: float
    '''

    limit_angle_min_x: float = None
    '''

    :type: float
    '''

    limit_angle_min_y: float = None
    '''

    :type: float
    '''

    limit_angle_min_z: float = None
    '''

    :type: float
    '''

    limit_max_x: float = None
    '''

    :type: float
    '''

    limit_max_y: float = None
    '''

    :type: float
    '''

    limit_max_z: float = None
    '''

    :type: float
    '''

    limit_min_x: float = None
    '''

    :type: float
    '''

    limit_min_y: float = None
    '''

    :type: float
    '''

    limit_min_z: float = None
    '''

    :type: float
    '''

    pivot_type: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    pivot_x: float = None
    '''Offset pivot on X 

    :type: float
    '''

    pivot_y: float = None
    '''Offset pivot on Y 

    :type: float
    '''

    pivot_z: float = None
    '''Offset pivot on Z 

    :type: float
    '''

    show_pivot: bool = None
    '''Display the pivot point and rotation in 3D view 

    :type: bool
    '''

    target: 'Object' = None
    '''Target Object 

    :type: 'Object'
    '''

    use_angular_limit_x: bool = None
    '''Use minimum/maximum X angular limit 

    :type: bool
    '''

    use_angular_limit_y: bool = None
    '''Use minimum/maximum Y angular limit 

    :type: bool
    '''

    use_angular_limit_z: bool = None
    '''Use minimum/maximum Z angular limit 

    :type: bool
    '''

    use_limit_x: bool = None
    '''Use minimum/maximum X limit 

    :type: bool
    '''

    use_limit_y: bool = None
    '''Use minimum/maximum y limit 

    :type: bool
    '''

    use_limit_z: bool = None
    '''Use minimum/maximum z limit 

    :type: bool
    '''

    use_linked_collision: bool = None
    '''Disable collision between linked bodies 

    :type: bool
    '''


class RigidBodyObject:
    '''Settings for object participating in Rigid Body Simulation '''

    angular_damping: float = None
    '''Amount of angular velocity that is lost over time 

    :type: float
    '''

    collision_groups: bool = None
    '''Collision Groups Rigid Body belongs to 

    :type: bool
    '''

    collision_margin: float = None
    '''Threshold of distance near surface where collisions are still considered (best results when non-zero) 

    :type: float
    '''

    collision_shape: typing.Union[int, str] = None
    '''Collision Shape of object in Rigid Body Simulations 

    :type: typing.Union[int, str]
    '''

    deactivate_angular_velocity: float = None
    '''Angular Velocity below which simulation stops simulating object 

    :type: float
    '''

    deactivate_linear_velocity: float = None
    '''Linear Velocity below which simulation stops simulating object 

    :type: float
    '''

    enabled: bool = None
    '''Rigid Body actively participates to the simulation 

    :type: bool
    '''

    friction: float = None
    '''Resistance of object to movement 

    :type: float
    '''

    kinematic: bool = None
    '''Allow rigid body to be controlled by the animation system 

    :type: bool
    '''

    linear_damping: float = None
    '''Amount of linear velocity that is lost over time 

    :type: float
    '''

    mass: float = None
    '''How much the object ‘weighs’ irrespective of gravity 

    :type: float
    '''

    mesh_source: typing.Union[int, str] = None
    '''Source of the mesh used to create collision shape 

    :type: typing.Union[int, str]
    '''

    restitution: float = None
    '''Tendency of object to bounce after colliding with another (0 = stays still, 1 = perfectly elastic) 

    :type: float
    '''

    type: typing.Union[int, str] = None
    '''Role of object in Rigid Body Simulations 

    :type: typing.Union[int, str]
    '''

    use_deactivation: bool = None
    '''Enable deactivation of resting rigid bodies (increases performance and stability but can cause glitches) 

    :type: bool
    '''

    use_deform: bool = None
    '''Rigid body deforms during simulation 

    :type: bool
    '''

    use_margin: bool = None
    '''Use custom collision margin (some shapes will have a visible gap around them) 

    :type: bool
    '''

    use_start_deactivated: bool = None
    '''Deactivate rigid body at the start of the simulation 

    :type: bool
    '''


class RigidBodyWorld:
    '''Self-contained rigid body simulation environment and settings '''

    constraints: 'Group' = None
    '''Group containing rigid body constraint objects 

    :type: 'Group'
    '''

    effector_weights: 'EffectorWeights' = None
    '''

    :type: 'EffectorWeights'
    '''

    enabled: bool = None
    '''Simulation will be evaluated 

    :type: bool
    '''

    group: 'Group' = None
    '''Group containing objects participating in this simulation 

    :type: 'Group'
    '''

    point_cache: 'PointCache' = None
    '''

    :type: 'PointCache'
    '''

    solver_iterations: int = None
    '''Number of constraint solver iterations made per simulation step (higher values are more accurate but slower) 

    :type: int
    '''

    steps_per_second: int = None
    '''Number of simulation steps taken per second (higher values are more accurate but slower) 

    :type: int
    '''

    time_scale: float = None
    '''Change the speed of the simulation 

    :type: float
    '''

    use_split_impulse: bool = None
    '''Reduce extra velocity that can build up when objects collide (lowers simulation stability a little so use only when necessary) 

    :type: bool
    '''

    def convex_sweep_test(self, object: 'Object', start, end):
        '''Sweep test convex rigidbody against the current rigidbody world 

        :param object: Rigidbody object with a convex collision shape 
        :type object: 'Object'
        '''
        pass


class Rotation:
    pass


class SCENE_UL_keying_set_paths:
    def draw_item(self, context, layout, data, item, icon, active_data,
                  active_propname, index):
        '''

        '''
        pass


class SPHFluidSettings:
    '''Settings for particle fluids physics '''

    buoyancy: float = None
    '''Artificial buoyancy force in negative gravity direction based on pressure differences inside the fluid 

    :type: float
    '''

    factor_radius: bool = None
    '''Interaction radius is a factor of 4 * particle size 

    :type: bool
    '''

    factor_repulsion: bool = None
    '''Repulsion is a factor of stiffness 

    :type: bool
    '''

    factor_rest_length: bool = None
    '''Spring rest length is a factor of 2 * particle size 

    :type: bool
    '''

    factor_stiff_viscosity: bool = None
    '''Stiff viscosity is a factor of normal viscosity 

    :type: bool
    '''

    fluid_radius: float = None
    '''Fluid interaction radius 

    :type: float
    '''

    linear_viscosity: float = None
    '''Linear viscosity 

    :type: float
    '''

    plasticity: float = None
    '''How much the spring rest length can change after the elastic limit is crossed 

    :type: float
    '''

    repulsion: float = None
    '''How strongly the fluid tries to keep from clustering (factor of stiffness) 

    :type: float
    '''

    rest_density: float = None
    '''Fluid rest density 

    :type: float
    '''

    rest_length: float = None
    '''Spring rest length (factor of particle radius) 

    :type: float
    '''

    solver: typing.Union[int, str] = None
    '''The code used to calculate internal forces on particles 

    :type: typing.Union[int, str]
    '''

    spring_force: float = None
    '''Spring force 

    :type: float
    '''

    spring_frames: int = None
    '''Create springs for this number of frames since particles birth (0 is always) 

    :type: int
    '''

    stiff_viscosity: float = None
    '''Creates viscosity for expanding fluid 

    :type: float
    '''

    stiffness: float = None
    '''How incompressible the fluid is (speed of sound) 

    :type: float
    '''

    use_factor_density: bool = None
    '''Density is calculated as a factor of default density (depends on particle size) 

    :type: bool
    '''

    use_initial_rest_length: bool = None
    '''Use the initial length as spring rest length instead of 2 * particle size 

    :type: bool
    '''

    use_viscoelastic_springs: bool = None
    '''Use viscoelastic springs instead of Hooke’s springs 

    :type: bool
    '''

    yield_ratio: float = None
    '''How much the spring has to be stretched/compressed in order to change it’s rest length 

    :type: float
    '''


class Scaling:
    pass


class Scene:
    '''Scene data-block, consisting in objects and defining time and render related settings '''

    active_clip: 'MovieClip' = None
    '''Active movie clip used for constraints and viewport drawing 

    :type: 'MovieClip'
    '''

    active_layer: int = None
    '''Active scene layer index 

    :type: int
    '''

    animation_data: 'AnimData' = None
    '''Animation data for this data-block 

    :type: 'AnimData'
    '''

    audio_distance_model: typing.Union[int, str] = None
    '''Distance model for distance attenuation calculation 

    :type: typing.Union[int, str]
    '''

    audio_doppler_factor: float = None
    '''Pitch factor for Doppler effect calculation 

    :type: float
    '''

    audio_doppler_speed: float = None
    '''Speed of sound for Doppler effect calculation 

    :type: float
    '''

    audio_volume: float = None
    '''Audio volume 

    :type: float
    '''

    background_set: 'Scene' = None
    '''Background set scene 

    :type: 'Scene'
    '''

    camera: 'Object' = None
    '''Active camera, used for rendering the scene 

    :type: 'Object'
    '''

    cursor_location: float = None
    '''3D cursor location 

    :type: float
    '''

    cycles: 'CyclesRenderSettings' = None
    '''Cycles render settings 

    :type: 'CyclesRenderSettings'
    '''

    cycles_curves: 'CyclesCurveRenderSettings' = None
    '''Cycles hair rendering settings 

    :type: 'CyclesCurveRenderSettings'
    '''

    depsgraph: 'Depsgraph' = None
    '''Dependencies in the scene data 

    :type: 'Depsgraph'
    '''

    display_settings: 'ColorManagedDisplaySettings' = None
    '''Settings of device saved image would be displayed on 

    :type: 'ColorManagedDisplaySettings'
    '''

    frame_current: int = None
    '''Current Frame, to update animation data from python frame_set() instead 

    :type: int
    '''

    frame_current_final: float = None
    '''Current frame with subframe and time remapping applied 

    :type: float
    '''

    frame_end: int = None
    '''Final frame of the playback/rendering range 

    :type: int
    '''

    frame_float: float = None
    '''

    :type: float
    '''

    frame_preview_end: int = None
    '''Alternative end frame for UI playback 

    :type: int
    '''

    frame_preview_start: int = None
    '''Alternative start frame for UI playback 

    :type: int
    '''

    frame_start: int = None
    '''First frame of the playback/rendering range 

    :type: int
    '''

    frame_step: int = None
    '''Number of frames to skip forward while rendering/playing back each frame 

    :type: int
    '''

    frame_subframe: float = None
    '''

    :type: float
    '''

    game_settings: 'SceneGameData' = None
    '''

    :type: 'SceneGameData'
    '''

    gravity: float = None
    '''Constant acceleration in a given direction 

    :type: float
    '''

    grease_pencil: 'GreasePencil' = None
    '''Grease Pencil data-block 

    :type: 'GreasePencil'
    '''

    is_nla_tweakmode: bool = None
    '''Whether there is any action referenced by NLA being edited (strictly read-only) 

    :type: bool
    '''

    keying_sets: typing.List['KeyingSet'] = None
    '''Absolute Keying Sets for this Scene 

    :type: typing.List['KeyingSet']
    '''

    keying_sets_all: typing.List['KeyingSet'] = None
    '''All Keying Sets available for use (Builtins and Absolute Keying Sets for this Scene) 

    :type: typing.List['KeyingSet']
    '''

    layers: bool = None
    '''Visible layers - Shift-Click/Drag to select multiple layers 

    :type: bool
    '''

    lock_frame_selection_to_range: bool = None
    '''Don’t allow frame to be selected with mouse outside of frame range 

    :type: bool
    '''

    node_tree: 'NodeTree' = None
    '''Compositing node tree 

    :type: 'NodeTree'
    '''

    object_bases: typing.List['ObjectBase'] = None
    '''

    :type: typing.List['ObjectBase']
    '''

    objects: typing.List['SceneObjects'] = None
    '''

    :type: typing.List['SceneObjects']
    '''

    orientations: typing.List['TransformOrientation'] = None
    '''

    :type: typing.List['TransformOrientation']
    '''

    render: 'RenderSettings' = None
    '''

    :type: 'RenderSettings'
    '''

    rigidbody_world: 'RigidBodyWorld' = None
    '''

    :type: 'RigidBodyWorld'
    '''

    safe_areas: 'DisplaySafeAreas' = None
    '''

    :type: 'DisplaySafeAreas'
    '''

    sequence_editor: 'SequenceEditor' = None
    '''

    :type: 'SequenceEditor'
    '''

    sequencer_colorspace_settings: 'ColorManagedSequencerColorspaceSettings' = None
    '''Settings of color space sequencer is working in 

    :type: 'ColorManagedSequencerColorspaceSettings'
    '''

    show_keys_from_selected_only: bool = None
    '''Consider keyframes for active Object and/or its selected bones only (in timeline and when jumping between keyframes) 

    :type: bool
    '''

    show_subframe: bool = None
    '''Show current scene subframe and allow set it using interface tools 

    :type: bool
    '''

    sync_mode: typing.Union[int, str] = None
    '''How to sync playback 

    :type: typing.Union[int, str]
    '''

    timeline_markers: typing.List['TimelineMarker'] = None
    '''Markers used in all timelines for the current scene 

    :type: typing.List['TimelineMarker']
    '''

    tool_settings: 'ToolSettings' = None
    '''

    :type: 'ToolSettings'
    '''

    unit_settings: 'UnitSettings' = None
    '''Unit editing settings 

    :type: 'UnitSettings'
    '''

    use_audio: bool = None
    '''Play back of audio from Sequence Editor will be muted 

    :type: bool
    '''

    use_audio_scrub: bool = None
    '''Play audio from Sequence Editor while scrubbing 

    :type: bool
    '''

    use_audio_sync: bool = None
    '''Play back and sync with audio clock, dropping frames if frame display is too slow 

    :type: bool
    '''

    use_frame_drop: bool = None
    '''Play back dropping frames if frame display is too slow 

    :type: bool
    '''

    use_gravity: bool = None
    '''Use global gravity for all dynamics 

    :type: bool
    '''

    use_nodes: bool = None
    '''Enable the compositing node tree 

    :type: bool
    '''

    use_preview_range: bool = None
    '''Use an alternative start/end frame range for animation playback and OpenGL renders instead of the Render properties start/end frame range 

    :type: bool
    '''

    use_stamp_note: str = None
    '''User defined note for the render stamping 

    :type: str
    '''

    view_settings: 'ColorManagedViewSettings' = None
    '''Color management settings applied on image before saving 

    :type: 'ColorManagedViewSettings'
    '''

    world: 'World' = None
    '''World used for rendering the scene 

    :type: 'World'
    '''

    def sequence_editor_create(self, ) -> 'SequenceEditor':
        '''Ensure sequence editor is valid in this scene 

        :rtype: 'SequenceEditor'
        :return:  New sequence editor data or NULL 
        '''
        pass

    def sequence_editor_clear(self, ):
        '''Clear sequence editor in this scene 

        '''
        pass

    def statistics(self, ) -> str:
        '''statistics 

        :rtype: str
        :return:  Statistics 
        '''
        pass

    def frame_set(self, frame: int, subframe: float = 0.0):
        '''Set scene frame updating all objects immediately 

        :param frame: Frame number to set 
        :type frame: int
        :param subframe: Sub-frame time, between 0.0 and 1.0 
        :type subframe: float
        '''
        pass

    def update(self, ):
        '''Update data tagged to be updated from previous access to data or operators 

        '''
        pass

    def uvedit_aspect(self, object: 'Object') -> float:
        '''Get uv aspect for current object 

        :param object: Object 
        :type object: 'Object'
        :rtype: float
        :return:  aspect 
        '''
        pass

    def ray_cast(self, origin, direction, distance: float = 1.70141e+38):
        '''Cast a ray onto in object space 

        :param distance: Maximum distance 
        :type distance: float
        '''
        pass

    def collada_export(self,
                       filepath: str,
                       apply_modifiers: bool = False,
                       export_mesh_type: int = 0,
                       selected: bool = False,
                       include_children: bool = False,
                       include_armatures: bool = False,
                       include_shapekeys: bool = True,
                       deform_bones_only: bool = False,
                       active_uv_only: bool = False,
                       export_texture_type: int = 0,
                       use_texture_copies: bool = True,
                       triangulate: bool = True,
                       use_object_instantiation: bool = True,
                       use_blender_profile: bool = True,
                       sort_by_name: bool = False,
                       export_transformation_type: int = 0,
                       open_sim: bool = False,
                       limit_precision: bool = False,
                       keep_bind_info: bool = False):
        '''collada_export 

        :param filepath: File Path, File path to write Collada file 
        :type filepath: str
        :param apply_modifiers: Apply Modifiers, Apply modifiers to exported mesh (non destructive)) 
        :type apply_modifiers: bool
        :param export_mesh_type: Resolution, Modifier resolution for export 
        :type export_mesh_type: int
        :param selected: Selection Only, Export only selected elements 
        :type selected: bool
        :param include_children: Include Children, Export all children of selected objects (even if not selected) 
        :type include_children: bool
        :param include_armatures: Include Armatures, Export related armatures (even if not selected) 
        :type include_armatures: bool
        :param include_shapekeys: Include Shape Keys, Export all Shape Keys from Mesh Objects 
        :type include_shapekeys: bool
        :param deform_bones_only: Deform Bones only, Only export deforming bones with armatures 
        :type deform_bones_only: bool
        :param active_uv_only: Only Selected UV Map, Export only the selected UV Map 
        :type active_uv_only: bool
        :param export_texture_type: Texture Type, Type for exported Textures (UV or MAT) 
        :type export_texture_type: int
        :param use_texture_copies: Copy, Copy textures to same folder where the .dae file is exported 
        :type use_texture_copies: bool
        :param triangulate: Triangulate, Export Polygons (Quads & NGons) as Triangles 
        :type triangulate: bool
        :param use_object_instantiation: Use Object Instances, Instantiate multiple Objects from same Data 
        :type use_object_instantiation: bool
        :param use_blender_profile: Use Blender Profile, Export additional Blender specific information (for material, shaders, bones, etc.) 
        :type use_blender_profile: bool
        :param sort_by_name: Sort by Object name, Sort exported data by Object name 
        :type sort_by_name: bool
        :param export_transformation_type: Transform, Transformation type for translation, scale and rotation 
        :type export_transformation_type: int
        :param open_sim: Export to SL/OpenSim, Compatibility mode for SL, OpenSim and other compatible online worlds 
        :type open_sim: bool
        :param limit_precision: Limit Precision, Reduce the precision of the exported data to 6 digits 
        :type limit_precision: bool
        :param keep_bind_info: Keep Bind Info, Store bind pose information in custom bone properties for later use during Collada export 
        :type keep_bind_info: bool
        '''
        pass

    def alembic_export(self,
                       filepath: str,
                       frame_start: int = 1,
                       frame_end: int = 1,
                       xform_samples: int = 1,
                       geom_samples: int = 1,
                       shutter_open: float = 0.0,
                       shutter_close: float = 1.0,
                       selected_only: bool = False,
                       uvs: bool = True,
                       normals: bool = True,
                       vcolors: bool = False,
                       apply_subdiv: bool = True,
                       flatten: bool = False,
                       visible_layers_only: bool = False,
                       renderable_only: bool = False,
                       face_sets: bool = False,
                       subdiv_schema: bool = False,
                       export_hair: bool = True,
                       export_particles: bool = True,
                       compression_type: typing.Union[int, str] = 'OGAWA',
                       packuv: bool = False,
                       scale: float = 1.0,
                       triangulate: bool = False,
                       quad_method: typing.Union[int, str] = 'BEAUTY',
                       ngon_method: typing.Union[int, str] = 'BEAUTY'):
        '''Export to Alembic file (deprecated, use the Alembic export operator) 

        :param filepath: File Path, File path to write Alembic file 
        :type filepath: str
        :param frame_start: Start, Start Frame 
        :type frame_start: int
        :param frame_end: End, End Frame 
        :type frame_end: int
        :param xform_samples: Xform samples, Transform samples per frame 
        :type xform_samples: int
        :param geom_samples: Geom samples, Geometry samples per frame 
        :type geom_samples: int
        :param shutter_open: Shutter open 
        :type shutter_open: float
        :param shutter_close: Shutter close 
        :type shutter_close: float
        :param selected_only: Selected only, Export only selected objects 
        :type selected_only: bool
        :param uvs: UVs, Export UVs 
        :type uvs: bool
        :param normals: Normals, Export cormals 
        :type normals: bool
        :param vcolors: Vertex colors, Export vertex colors 
        :type vcolors: bool
        :param apply_subdiv: Subsurfs as meshes, Export subdivision surfaces as meshes 
        :type apply_subdiv: bool
        :param flatten: Flatten hierarchy, Flatten hierarchy 
        :type flatten: bool
        :param visible_layers_only: Visible layers only, Export only objects in visible layers 
        :type visible_layers_only: bool
        :param renderable_only: Renderable objects only, Export only objects marked renderable in the outliner 
        :type renderable_only: bool
        :param face_sets: Facesets, Export face sets 
        :type face_sets: bool
        :param subdiv_schema: Use Alembic subdivision Schema, Use Alembic subdivision Schema 
        :type subdiv_schema: bool
        :param export_hair: Export Hair, Exports hair particle systems as animated curves 
        :type export_hair: bool
        :param export_particles: Export Particles, Exports non-hair particle systems 
        :type export_particles: bool
        :param compression_type: Compression 
        :type compression_type: typing.Union[int, str]
        :param packuv: Export with packed UV islands, Export with packed UV islands 
        :type packuv: bool
        :param scale: Scale, Value by which to enlarge or shrink the objects with respect to the world’s origin 
        :type scale: float
        :param triangulate: Triangulate, Export Polygons (Quads & NGons) as Triangles 
        :type triangulate: bool
        :param quad_method: Quad Method, Method for splitting the quads into trianglesBEAUTY Beauty , Split the quads in nice triangles, slower method.FIXED Fixed, Split the quads on the first and third vertices.FIXED_ALTERNATE Fixed Alternate, Split the quads on the 2nd and 4th vertices.SHORTEST_DIAGONAL Shortest Diagonal, Split the quads based on the distance between the vertices. 
        :type quad_method: typing.Union[int, str]
        :param ngon_method: Polygon Method, Method for splitting the polygons into trianglesBEAUTY Beauty , Split the quads in nice triangles, slower method.FIXED Fixed, Split the quads on the first and third vertices.FIXED_ALTERNATE Fixed Alternate, Split the quads on the 2nd and 4th vertices.SHORTEST_DIAGONAL Shortest Diagonal, Split the quads based on the distance between the vertices. 
        :type ngon_method: typing.Union[int, str]
        '''
        pass


class SceneActuator:
    camera: 'Object' = None
    '''Set this Camera (leave empty to refer to self object) 

    :type: 'Object'
    '''

    mode: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    scene: 'Scene' = None
    '''Scene to be added/removed/paused/resumed 

    :type: 'Scene'
    '''


class SceneBases:
    '''Collection of scene bases '''

    active: 'ObjectBase' = None
    '''Active object base in the scene 

    :type: 'ObjectBase'
    '''


class SceneGameData:
    '''Game data for a Scene data-block '''

    activity_culling_box_radius: float = None
    '''Radius of the activity bubble, in Manhattan length (objects outside the box are activity-culled) 

    :type: float
    '''

    deactivation_angular_threshold: float = None
    '''Angular velocity that an object must be below before the deactivation timer can start 

    :type: float
    '''

    deactivation_linear_threshold: float = None
    '''Linear velocity that an object must be below before the deactivation timer can start 

    :type: float
    '''

    deactivation_time: float = None
    '''Amount of time (in seconds) after which objects with a velocity less than the given threshold will deactivate (0.0 means no deactivation) 

    :type: float
    '''

    depth: int = None
    '''Display bit depth of full screen display 

    :type: int
    '''

    dome_angle: int = None
    '''Field of View of the Dome - it only works in mode Fisheye and Truncated 

    :type: int
    '''

    dome_buffer_resolution: float = None
    '''Buffer Resolution - decrease it to increase speed 

    :type: float
    '''

    dome_mode: typing.Union[int, str] = None
    '''Dome physical configurations 

    :type: typing.Union[int, str]
    '''

    dome_tessellation: int = None
    '''Tessellation level - check the generated mesh in wireframe mode 

    :type: int
    '''

    dome_text: 'Text' = None
    '''Custom Warp Mesh data file 

    :type: 'Text'
    '''

    dome_tilt: int = None
    '''Camera rotation in horizontal axis 

    :type: int
    '''

    exit_key: typing.Union[int, str] = None
    '''The key that exits the Game Engine 

    :type: typing.Union[int, str]
    '''

    fps: int = None
    '''Nominal number of game frames per second (physics fixed timestep = 1/fps, independently of actual frame rate) 

    :type: int
    '''

    frame_color: float = None
    '''Set color of the bars 

    :type: float
    '''

    frame_type: typing.Union[int, str] = None
    '''Select the type of Framing you want 

    :type: typing.Union[int, str]
    '''

    frequency: int = None
    '''Display clock frequency of fullscreen display 

    :type: int
    '''

    level_height: float = None
    '''Max difference in heights of obstacles to enable their interaction 

    :type: float
    '''

    logic_step_max: int = None
    '''Maximum number of logic frame per game frame if graphics slows down the game, higher value allows better synchronization with physics 

    :type: int
    '''

    material_mode: typing.Union[int, str] = None
    '''Material mode to use for rendering 

    :type: typing.Union[int, str]
    '''

    obstacle_simulation: typing.Union[int, str] = None
    '''Simulation used for obstacle avoidance in the game engine 

    :type: typing.Union[int, str]
    '''

    occlusion_culling_resolution: int = None
    '''Size of the occlusion buffer, use higher value for better precision (slower) 

    :type: int
    '''

    physics_engine: typing.Union[int, str] = None
    '''Physics engine used for physics simulation in the game engine 

    :type: typing.Union[int, str]
    '''

    physics_gravity: float = None
    '''Gravitational constant used for physics simulation in the game engine 

    :type: float
    '''

    physics_step_max: int = None
    '''Maximum number of physics step per game frame if graphics slows down the game, higher value allows physics to keep up with realtime 

    :type: int
    '''

    physics_step_sub: int = None
    '''Number of simulation substep per physic timestep, higher value give better physics precision 

    :type: int
    '''

    raster_storage: typing.Union[int, str] = None
    '''Set the storage mode used by the rasterizer 

    :type: typing.Union[int, str]
    '''

    recast_data: 'SceneGameRecastData' = None
    '''

    :type: 'SceneGameRecastData'
    '''

    resolution_x: int = None
    '''Number of horizontal pixels in the screen 

    :type: int
    '''

    resolution_y: int = None
    '''Number of vertical pixels in the screen 

    :type: int
    '''

    samples: typing.Union[int, str] = None
    '''The number of AA Samples to use for MSAA 

    :type: typing.Union[int, str]
    '''

    scene_hysteresis_percentage: int = None
    '''Minimum distance change required to transition to the previous level of detail 

    :type: int
    '''

    show_debug_properties: bool = None
    '''Show properties marked for debugging while the game runs 

    :type: bool
    '''

    show_framerate_profile: bool = None
    '''Show framerate and profiling information while the game runs 

    :type: bool
    '''

    show_fullscreen: bool = None
    '''Start player in a new fullscreen display 

    :type: bool
    '''

    show_mouse: bool = None
    '''Start player with a visible mouse cursor 

    :type: bool
    '''

    show_obstacle_simulation: bool = None
    '''Enable debug visualization for obstacle simulation 

    :type: bool
    '''

    show_physics_visualization: bool = None
    '''Show a visualization of physics bounds and interactions 

    :type: bool
    '''

    stereo: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    stereo_eye_separation: float = None
    '''Set the distance between the eyes - the camera focal distance/30 should be fine 

    :type: float
    '''

    stereo_mode: typing.Union[int, str] = None
    '''Stereographic techniques 

    :type: typing.Union[int, str]
    '''

    use_activity_culling: bool = None
    '''Activity culling is enabled 

    :type: bool
    '''

    use_animation_record: bool = None
    '''Record animation to F-Curves 

    :type: bool
    '''

    use_auto_start: bool = None
    '''Automatically start game at load time 

    :type: bool
    '''

    use_deprecation_warnings: bool = None
    '''Print warnings when using deprecated features in the python API 

    :type: bool
    '''

    use_desktop: bool = None
    '''Use the current desktop resolution in fullscreen mode 

    :type: bool
    '''

    use_display_lists: bool = None
    '''Use display lists to speed up rendering by keeping geometry on the GPU 

    :type: bool
    '''

    use_frame_rate: bool = None
    '''Respect the frame rate from the Physics panel in the world properties rather than rendering as many frames as possible 

    :type: bool
    '''

    use_glsl_color_management: bool = None
    '''Use color management for GLSL rendering 

    :type: bool
    '''

    use_glsl_environment_lighting: bool = None
    '''Use environment lighting for GLSL rendering 

    :type: bool
    '''

    use_glsl_extra_textures: bool = None
    '''Use extra textures like normal or specular maps for GLSL rendering 

    :type: bool
    '''

    use_glsl_lights: bool = None
    '''Use lights for GLSL rendering 

    :type: bool
    '''

    use_glsl_nodes: bool = None
    '''Use nodes for GLSL rendering 

    :type: bool
    '''

    use_glsl_ramps: bool = None
    '''Use ramps for GLSL rendering 

    :type: bool
    '''

    use_glsl_shaders: bool = None
    '''Use shaders for GLSL rendering 

    :type: bool
    '''

    use_glsl_shadows: bool = None
    '''Use shadows for GLSL rendering 

    :type: bool
    '''

    use_material_caching: bool = None
    '''Cache materials in the converter (this is faster, but can cause problems with older Singletexture and Multitexture games) 

    :type: bool
    '''

    use_occlusion_culling: bool = None
    '''Use optimized Bullet DBVT tree for view frustum and occlusion culling (more efficient, but it can waste unnecessary CPU if the scene doesn’t have occluder objects) 

    :type: bool
    '''

    use_restrict_animation_updates: bool = None
    '''Restrict the number of animation updates to the animation FPS (this is better for performance, but can cause issues with smooth playback) 

    :type: bool
    '''

    use_scene_hysteresis: bool = None
    '''Use LoD Hysteresis setting for the scene 

    :type: bool
    '''

    vsync: typing.Union[int, str] = None
    '''Change vsync settings 

    :type: typing.Union[int, str]
    '''


class SceneGameRecastData:
    '''Recast data for a Game data-block '''

    agent_height: float = None
    '''Minimum height where the agent can still walk 

    :type: float
    '''

    agent_radius: float = None
    '''Radius of the agent 

    :type: float
    '''

    cell_height: float = None
    '''Rasterized cell height 

    :type: float
    '''

    cell_size: float = None
    '''Rasterized cell size 

    :type: float
    '''

    climb_max: float = None
    '''Maximum height between grid cells the agent can climb 

    :type: float
    '''

    edge_max_error: float = None
    '''Maximum distance error from contour to cells 

    :type: float
    '''

    edge_max_len: float = None
    '''Maximum contour edge length 

    :type: float
    '''

    partitioning: typing.Union[int, str] = None
    '''Choose partitioning method 

    :type: typing.Union[int, str]
    '''

    region_merge_size: float = None
    '''Minimum regions size (smaller regions will be merged) 

    :type: float
    '''

    region_min_size: float = None
    '''Minimum regions size (smaller regions will be deleted) 

    :type: float
    '''

    sample_dist: float = None
    '''Detail mesh sample spacing 

    :type: float
    '''

    sample_max_error: float = None
    '''Detail mesh simplification max sample error 

    :type: float
    '''

    slope_max: float = None
    '''Maximum walkable slope angle 

    :type: float
    '''

    verts_per_poly: int = None
    '''Max number of vertices per polygon 

    :type: int
    '''


class SceneObjects:
    '''Collection of scene objects '''

    active: 'Object' = None
    '''Active object for this scene 

    :type: 'Object'
    '''

    def link(self, object: 'Object') -> 'ObjectBase':
        '''Link object to scene, run scene.update() after 

        :param object: Object to add to scene 
        :type object: 'Object'
        :rtype: 'ObjectBase'
        :return:  The newly created base 
        '''
        pass

    def unlink(self, object: 'Object'):
        '''Unlink object from scene 

        :param object: Object to remove from scene 
        :type object: 'Object'
        '''
        pass


class SceneRenderLayer:
    '''Render layer '''

    cycles: 'CyclesRenderLayerSettings' = None
    '''Cycles SceneRenderLayer Settings 

    :type: 'CyclesRenderLayerSettings'
    '''

    exclude_ambient_occlusion: bool = None
    '''Exclude AO pass from combined 

    :type: bool
    '''

    exclude_emit: bool = None
    '''Exclude emission pass from combined 

    :type: bool
    '''

    exclude_environment: bool = None
    '''Exclude environment pass from combined 

    :type: bool
    '''

    exclude_indirect: bool = None
    '''Exclude indirect pass from combined 

    :type: bool
    '''

    exclude_reflection: bool = None
    '''Exclude raytraced reflection pass from combined 

    :type: bool
    '''

    exclude_refraction: bool = None
    '''Exclude raytraced refraction pass from combined 

    :type: bool
    '''

    exclude_shadow: bool = None
    '''Exclude shadow pass from combined 

    :type: bool
    '''

    exclude_specular: bool = None
    '''Exclude specular pass from combined 

    :type: bool
    '''

    freestyle_settings: 'FreestyleSettings' = None
    '''

    :type: 'FreestyleSettings'
    '''

    invert_zmask: bool = None
    '''For Zmask, only render what is behind solid z values instead of in front 

    :type: bool
    '''

    layers: bool = None
    '''Scene layers included in this render layer 

    :type: bool
    '''

    layers_exclude: bool = None
    '''Exclude scene layers from having any influence 

    :type: bool
    '''

    layers_zmask: bool = None
    '''Zmask scene layers for solid faces 

    :type: bool
    '''

    light_override: 'Group' = None
    '''Group to override all other lights in this render layer 

    :type: 'Group'
    '''

    material_override: 'Material' = None
    '''Material to override all other materials in this render layer 

    :type: 'Material'
    '''

    name: str = None
    '''Render layer name 

    :type: str
    '''

    pass_alpha_threshold: float = None
    '''Z, Index, normal, UV and vector passes are only affected by surfaces with alpha transparency equal to or higher than this threshold 

    :type: float
    '''

    samples: int = None
    '''Override number of render samples for this render layer, 0 will use the scene setting 

    :type: int
    '''

    use: bool = None
    '''Disable or enable the render layer 

    :type: bool
    '''

    use_all_z: bool = None
    '''Fill in Z values for solid faces in invisible layers, for masking 

    :type: bool
    '''

    use_ao: bool = None
    '''Render AO in this Layer 

    :type: bool
    '''

    use_edge_enhance: bool = None
    '''Render Edge-enhance in this Layer (only works for Solid faces) 

    :type: bool
    '''

    use_freestyle: bool = None
    '''Render stylized strokes in this Layer 

    :type: bool
    '''

    use_halo: bool = None
    '''Render Halos in this Layer (on top of Solid) 

    :type: bool
    '''

    use_pass_ambient_occlusion: bool = None
    '''Deliver AO pass 

    :type: bool
    '''

    use_pass_color: bool = None
    '''Deliver shade-less color pass 

    :type: bool
    '''

    use_pass_combined: bool = None
    '''Deliver full combined RGBA buffer 

    :type: bool
    '''

    use_pass_diffuse: bool = None
    '''Deliver diffuse pass 

    :type: bool
    '''

    use_pass_diffuse_color: bool = None
    '''Deliver diffuse color pass 

    :type: bool
    '''

    use_pass_diffuse_direct: bool = None
    '''Deliver diffuse direct pass 

    :type: bool
    '''

    use_pass_diffuse_indirect: bool = None
    '''Deliver diffuse indirect pass 

    :type: bool
    '''

    use_pass_emit: bool = None
    '''Deliver emission pass 

    :type: bool
    '''

    use_pass_environment: bool = None
    '''Deliver environment lighting pass 

    :type: bool
    '''

    use_pass_glossy_color: bool = None
    '''Deliver glossy color pass 

    :type: bool
    '''

    use_pass_glossy_direct: bool = None
    '''Deliver glossy direct pass 

    :type: bool
    '''

    use_pass_glossy_indirect: bool = None
    '''Deliver glossy indirect pass 

    :type: bool
    '''

    use_pass_indirect: bool = None
    '''Deliver indirect lighting pass 

    :type: bool
    '''

    use_pass_material_index: bool = None
    '''Deliver material index pass 

    :type: bool
    '''

    use_pass_mist: bool = None
    '''Deliver mist factor pass (0.0-1.0) 

    :type: bool
    '''

    use_pass_normal: bool = None
    '''Deliver normal pass 

    :type: bool
    '''

    use_pass_object_index: bool = None
    '''Deliver object index pass 

    :type: bool
    '''

    use_pass_reflection: bool = None
    '''Deliver raytraced reflection pass 

    :type: bool
    '''

    use_pass_refraction: bool = None
    '''Deliver raytraced refraction pass 

    :type: bool
    '''

    use_pass_shadow: bool = None
    '''Deliver shadow pass 

    :type: bool
    '''

    use_pass_specular: bool = None
    '''Deliver specular pass 

    :type: bool
    '''

    use_pass_subsurface_color: bool = None
    '''Deliver subsurface color pass 

    :type: bool
    '''

    use_pass_subsurface_direct: bool = None
    '''Deliver subsurface direct pass 

    :type: bool
    '''

    use_pass_subsurface_indirect: bool = None
    '''Deliver subsurface indirect pass 

    :type: bool
    '''

    use_pass_transmission_color: bool = None
    '''Deliver transmission color pass 

    :type: bool
    '''

    use_pass_transmission_direct: bool = None
    '''Deliver transmission direct pass 

    :type: bool
    '''

    use_pass_transmission_indirect: bool = None
    '''Deliver transmission indirect pass 

    :type: bool
    '''

    use_pass_uv: bool = None
    '''Deliver texture UV pass 

    :type: bool
    '''

    use_pass_vector: bool = None
    '''Deliver speed vector pass 

    :type: bool
    '''

    use_pass_z: bool = None
    '''Deliver Z values pass 

    :type: bool
    '''

    use_sky: bool = None
    '''Render Sky in this Layer 

    :type: bool
    '''

    use_solid: bool = None
    '''Render Solid faces in this Layer 

    :type: bool
    '''

    use_strand: bool = None
    '''Render Strands in this Layer 

    :type: bool
    '''

    use_zmask: bool = None
    '''Only render what’s in front of the solid z values 

    :type: bool
    '''

    use_ztransp: bool = None
    '''Render Z-Transparent faces in this Layer (on top of Solid and Halos) 

    :type: bool
    '''


class SceneRenderView:
    '''Render viewpoint for 3D stereo and multiview rendering '''

    camera_suffix: str = None
    '''Suffix to identify the cameras to use, and added to the render images for this view 

    :type: str
    '''

    file_suffix: str = None
    '''Suffix added to the render images for this view 

    :type: str
    '''

    name: str = None
    '''Render view name 

    :type: str
    '''

    use: bool = None
    '''Disable or enable the render view 

    :type: bool
    '''


class SceneSequence:
    '''Sequence strip to used the rendered image of a scene '''

    alpha_mode: typing.Union[int, str] = None
    '''Representation of alpha information in the RGBA pixels 

    :type: typing.Union[int, str]
    '''

    animation_offset_end: int = None
    '''Animation end offset (trim end) 

    :type: int
    '''

    animation_offset_start: int = None
    '''Animation start offset (trim start) 

    :type: int
    '''

    color_multiply: float = None
    '''

    :type: float
    '''

    color_saturation: float = None
    '''Adjust the intensity of the input’s color 

    :type: float
    '''

    crop: 'SequenceCrop' = None
    '''

    :type: 'SequenceCrop'
    '''

    proxy: 'SequenceProxy' = None
    '''

    :type: 'SequenceProxy'
    '''

    scene: 'Scene' = None
    '''Scene that this sequence uses 

    :type: 'Scene'
    '''

    scene_camera: 'Object' = None
    '''Override the scenes active camera 

    :type: 'Object'
    '''

    strobe: float = None
    '''Only display every nth frame 

    :type: float
    '''

    transform: 'SequenceTransform' = None
    '''

    :type: 'SequenceTransform'
    '''

    use_crop: bool = None
    '''Crop image before processing 

    :type: bool
    '''

    use_deinterlace: bool = None
    '''Remove fields from video movies 

    :type: bool
    '''

    use_flip_x: bool = None
    '''Flip on the X axis 

    :type: bool
    '''

    use_flip_y: bool = None
    '''Flip on the Y axis 

    :type: bool
    '''

    use_float: bool = None
    '''Convert input to float data 

    :type: bool
    '''

    use_grease_pencil: bool = None
    '''Show Grease Pencil strokes in OpenGL previews 

    :type: bool
    '''

    use_proxy: bool = None
    '''Use a preview proxy and/or timecode index for this strip 

    :type: bool
    '''

    use_reverse_frames: bool = None
    '''Reverse frame order 

    :type: bool
    '''

    use_sequence: bool = None
    '''Use scenes sequence strips directly, instead of rendering 

    :type: bool
    '''

    use_translation: bool = None
    '''Translate image before processing 

    :type: bool
    '''


class Scopes:
    '''Scopes for statistical view of an image '''

    accuracy: float = None
    '''Proportion of original image source pixel lines to sample 

    :type: float
    '''

    histogram: 'Histogram' = None
    '''Histogram for viewing image statistics 

    :type: 'Histogram'
    '''

    use_full_resolution: bool = None
    '''Sample every pixel of the image 

    :type: bool
    '''

    vectorscope_alpha: float = None
    '''Opacity of the points 

    :type: float
    '''

    waveform_alpha: float = None
    '''Opacity of the points 

    :type: float
    '''

    waveform_mode: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''


class Screen:
    '''Screen data-block, defining the layout of areas in a window '''

    areas: typing.List['Area'] = None
    '''Areas the screen is subdivided into 

    :type: typing.List['Area']
    '''

    is_animation_playing: bool = None
    '''Animation playback is active 

    :type: bool
    '''

    scene: 'Scene' = None
    '''Active scene to be edited in the screen 

    :type: 'Scene'
    '''

    show_fullscreen: bool = None
    '''An area is maximized, filling this screen 

    :type: bool
    '''

    use_follow: bool = None
    '''Follow current frame in editors 

    :type: bool
    '''

    use_play_3d_editors: bool = None
    '''

    :type: bool
    '''

    use_play_animation_editors: bool = None
    '''

    :type: bool
    '''

    use_play_clip_editors: bool = None
    '''

    :type: bool
    '''

    use_play_image_editors: bool = None
    '''

    :type: bool
    '''

    use_play_node_editors: bool = None
    '''

    :type: bool
    '''

    use_play_properties_editors: bool = None
    '''

    :type: bool
    '''

    use_play_sequence_editors: bool = None
    '''

    :type: bool
    '''

    use_play_top_left_3d_editor: bool = None
    '''

    :type: bool
    '''


class ScrewModifier:
    '''Revolve edges '''

    angle: float = None
    '''Angle of revolution 

    :type: float
    '''

    axis: typing.Union[int, str] = None
    '''Screw axis 

    :type: typing.Union[int, str]
    '''

    iterations: int = None
    '''Number of times to apply the screw operation 

    :type: int
    '''

    merge_threshold: float = None
    '''Limit below which to merge vertices 

    :type: float
    '''

    object: 'Object' = None
    '''Object to define the screw axis 

    :type: 'Object'
    '''

    render_steps: int = None
    '''Number of steps in the revolution 

    :type: int
    '''

    screw_offset: float = None
    '''Offset the revolution along its axis 

    :type: float
    '''

    steps: int = None
    '''Number of steps in the revolution 

    :type: int
    '''

    use_merge_vertices: bool = None
    '''Merge adjacent vertices (screw offset must be zero) 

    :type: bool
    '''

    use_normal_calculate: bool = None
    '''Calculate the order of edges (needed for meshes, but not curves) 

    :type: bool
    '''

    use_normal_flip: bool = None
    '''Flip normals of lathed faces 

    :type: bool
    '''

    use_object_screw_offset: bool = None
    '''Use the distance between the objects to make a screw 

    :type: bool
    '''

    use_smooth_shade: bool = None
    '''Output faces with smooth shading rather than flat shaded 

    :type: bool
    '''

    use_stretch_u: bool = None
    '''Stretch the U coordinates between 0-1 when UV’s are present 

    :type: bool
    '''

    use_stretch_v: bool = None
    '''Stretch the V coordinates between 0-1 when UV’s are present 

    :type: bool
    '''


class Sculpt:
    constant_detail_resolution: float = None
    '''Maximum edge length for dynamic topology sculpting (as divisor of blender unit - higher value means smaller edge length) 

    :type: float
    '''

    detail_percent: float = None
    '''Maximum edge length for dynamic topology sculpting (in brush percenage) 

    :type: float
    '''

    detail_refine_method: typing.Union[int, str] = None
    '''In dynamic-topology mode, how to add or remove mesh detail 

    :type: typing.Union[int, str]
    '''

    detail_size: float = None
    '''Maximum edge length for dynamic topology sculpting (in pixels) 

    :type: float
    '''

    detail_type_method: typing.Union[int, str] = None
    '''In dynamic-topology mode, how mesh detail size is calculated 

    :type: typing.Union[int, str]
    '''

    gravity: float = None
    '''Amount of gravity after each dab 

    :type: float
    '''

    gravity_object: 'Object' = None
    '''Object whose Z axis defines orientation of gravity 

    :type: 'Object'
    '''

    lock_x: bool = None
    '''Disallow changes to the X axis of vertices 

    :type: bool
    '''

    lock_y: bool = None
    '''Disallow changes to the Y axis of vertices 

    :type: bool
    '''

    lock_z: bool = None
    '''Disallow changes to the Z axis of vertices 

    :type: bool
    '''

    radial_symmetry: int = None
    '''Number of times to copy strokes across the surface 

    :type: int
    '''

    show_diffuse_color: bool = None
    '''Show diffuse color of object and overlay sculpt mask on top of it 

    :type: bool
    '''

    symmetrize_direction: typing.Union[int, str] = None
    '''Source and destination for symmetrize operator 

    :type: typing.Union[int, str]
    '''

    use_deform_only: bool = None
    '''Use only deformation modifiers (temporary disable all constructive modifiers except multi-resolution) 

    :type: bool
    '''

    use_smooth_shading: bool = None
    '''Show faces in dynamic-topology mode with smooth shading rather than flat shaded 

    :type: bool
    '''

    use_threaded: bool = None
    '''Take advantage of multiple CPU cores to improve sculpting performance 

    :type: bool
    '''


class SculptToolCapabilities:
    '''Read-only indications of which brush operations are supported by the current sculpt tool '''

    has_accumulate: bool = None
    '''

    :type: bool
    '''

    has_auto_smooth: bool = None
    '''

    :type: bool
    '''

    has_gravity: bool = None
    '''

    :type: bool
    '''

    has_height: bool = None
    '''

    :type: bool
    '''

    has_jitter: bool = None
    '''

    :type: bool
    '''

    has_normal_weight: bool = None
    '''

    :type: bool
    '''

    has_persistence: bool = None
    '''

    :type: bool
    '''

    has_pinch_factor: bool = None
    '''

    :type: bool
    '''

    has_plane_offset: bool = None
    '''

    :type: bool
    '''

    has_rake_factor: bool = None
    '''

    :type: bool
    '''

    has_random_texture_angle: bool = None
    '''

    :type: bool
    '''

    has_sculpt_plane: bool = None
    '''

    :type: bool
    '''

    has_secondary_color: bool = None
    '''

    :type: bool
    '''

    has_smooth_stroke: bool = None
    '''

    :type: bool
    '''

    has_space_attenuation: bool = None
    '''

    :type: bool
    '''

    has_strength_pressure: bool = None
    '''

    :type: bool
    '''


class SelectedUvElement:
    element_index: int = None
    '''

    :type: int
    '''

    face_index: int = None
    '''

    :type: int
    '''


class Sensor:
    '''Game engine logic brick to detect events '''

    active: bool = None
    '''Set active state of the sensor 

    :type: bool
    '''

    controllers: typing.List['Controller'] = None
    '''The list containing the controllers connected to the sensor 

    :type: typing.List['Controller']
    '''

    invert: bool = None
    '''Invert the level(output) of this sensor 

    :type: bool
    '''

    name: str = None
    '''Sensor name 

    :type: str
    '''

    pin: bool = None
    '''Display when not linked to a visible states controller 

    :type: bool
    '''

    show_expanded: bool = None
    '''Set sensor expanded in the user interface 

    :type: bool
    '''

    tick_skip: int = None
    '''Number of logic ticks skipped between 2 active pulses (0 = pulse every logic tick, 1 = skip 1 logic tick between pulses, etc.) 

    :type: int
    '''

    type: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    use_level: bool = None
    '''Level detector, trigger controllers of new states (only applicable upon logic state transition) 

    :type: bool
    '''

    use_pulse_false_level: bool = None
    '''Activate FALSE level triggering (pulse mode) 

    :type: bool
    '''

    use_pulse_true_level: bool = None
    '''Activate TRUE level triggering (pulse mode) 

    :type: bool
    '''

    use_tap: bool = None
    '''Trigger controllers only for an instant, even while the sensor remains true 

    :type: bool
    '''

    def link(self, controller: 'Controller'):
        '''Link the sensor to a controller 

        :param controller: Controller to link to 
        :type controller: 'Controller'
        '''
        pass

    def unlink(self, controller: 'Controller'):
        '''Unlink the sensor from a controller 

        :param controller: Controller to unlink from 
        :type controller: 'Controller'
        '''
        pass


class Sequence:
    '''Sequence strip in the sequence editor '''

    blend_alpha: float = None
    '''Percentage of how much the strip’s colors affect other strips 

    :type: float
    '''

    blend_type: typing.Union[int, str] = None
    '''Method for controlling how the strip combines with other strips 

    :type: typing.Union[int, str]
    '''

    channel: int = None
    '''Y position of the sequence strip 

    :type: int
    '''

    effect_fader: float = None
    '''Custom fade value 

    :type: float
    '''

    frame_duration: int = None
    '''The length of the contents of this strip before the handles are applied 

    :type: int
    '''

    frame_final_duration: int = None
    '''The length of the contents of this strip after the handles are applied 

    :type: int
    '''

    frame_final_end: int = None
    '''End frame displayed in the sequence editor after offsets are applied 

    :type: int
    '''

    frame_final_start: int = None
    '''Start frame displayed in the sequence editor after offsets are applied, setting this is equivalent to moving the handle, not the actual start frame 

    :type: int
    '''

    frame_offset_end: int = None
    '''

    :type: int
    '''

    frame_offset_start: int = None
    '''

    :type: int
    '''

    frame_start: int = None
    '''X position where the strip begins 

    :type: int
    '''

    frame_still_end: int = None
    '''

    :type: int
    '''

    frame_still_start: int = None
    '''

    :type: int
    '''

    lock: bool = None
    '''Lock strip so that it cannot be transformed 

    :type: bool
    '''

    modifiers: typing.List['SequenceModifier'] = None
    '''Modifiers affecting this strip 

    :type: typing.List['SequenceModifier']
    '''

    mute: bool = None
    '''Disable strip so that it cannot be viewed in the output 

    :type: bool
    '''

    name: str = None
    '''

    :type: str
    '''

    select: bool = None
    '''

    :type: bool
    '''

    select_left_handle: bool = None
    '''

    :type: bool
    '''

    select_right_handle: bool = None
    '''

    :type: bool
    '''

    speed_factor: float = None
    '''Multiply the current speed of the sequence with this number or remap current frame to this frame 

    :type: float
    '''

    type: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    use_default_fade: bool = None
    '''Fade effect using the built-in default (usually make transition as long as effect strip) 

    :type: bool
    '''

    use_linear_modifiers: bool = None
    '''Calculate modifiers in linear space instead of sequencer’s space 

    :type: bool
    '''

    def update(self, data: bool = False):
        '''Update the strip dimensions 

        :param data: Data, Update strip data 
        :type data: bool
        '''
        pass

    def strip_elem_from_frame(self, frame: int) -> 'SequenceElement':
        '''Return the strip element from a given frame or None 

        :param frame: Frame, The frame to get the strip element from 
        :type frame: int
        :rtype: 'SequenceElement'
        :return:  strip element of the current frame 
        '''
        pass

    def swap(self, other: 'Sequence'):
        '''swap 

        :param other: Other 
        :type other: 'Sequence'
        '''
        pass


class SequenceColorBalance:
    '''Color balance parameters for a sequence strip '''

    pass


class SequenceColorBalanceData:
    '''Color balance parameters for a sequence strip and it’s modifiers '''

    gain: float = None
    '''Color balance gain (highlights) 

    :type: float
    '''

    gamma: float = None
    '''Color balance gamma (midtones) 

    :type: float
    '''

    invert_gain: bool = None
    '''Invert the gain color` 

    :type: bool
    '''

    invert_gamma: bool = None
    '''Invert the gamma color 

    :type: bool
    '''

    invert_lift: bool = None
    '''Invert the lift color 

    :type: bool
    '''

    lift: float = None
    '''Color balance lift (shadows) 

    :type: float
    '''


class SequenceCrop:
    '''Cropping parameters for a sequence strip '''

    max_x: int = None
    '''Number of pixels to crop from the right side 

    :type: int
    '''

    max_y: int = None
    '''Number of pixels to crop from the top 

    :type: int
    '''

    min_x: int = None
    '''Number of pixels to crop from the left side 

    :type: int
    '''

    min_y: int = None
    '''Number of pixels to crop from the bottom 

    :type: int
    '''


class SequenceEditor:
    '''Sequence editing data for a Scene data-block '''

    active_strip: 'Sequence' = None
    '''Sequencer’s active strip 

    :type: 'Sequence'
    '''

    meta_stack: typing.List['Sequence'] = None
    '''Meta strip stack, last is currently edited meta strip 

    :type: typing.List['Sequence']
    '''

    overlay_frame: int = None
    '''

    :type: int
    '''

    proxy_dir: str = None
    '''

    :type: str
    '''

    proxy_storage: typing.Union[int, str] = None
    '''How to store proxies for this project 

    :type: typing.Union[int, str]
    '''

    sequences: typing.List['Sequence'] = None
    '''Top-level strips only 

    :type: typing.List['Sequence']
    '''

    sequences_all: typing.List['Sequence'] = None
    '''All strips, recursively including those inside metastrips 

    :type: typing.List['Sequence']
    '''

    show_overlay: bool = None
    '''Partial overlay on top of the sequencer 

    :type: bool
    '''

    use_overlay_lock: bool = None
    '''

    :type: bool
    '''


class SequenceElement:
    '''Sequence strip data for a single frame '''

    filename: str = None
    '''Name of the source file 

    :type: str
    '''

    orig_height: int = None
    '''Original image height 

    :type: int
    '''

    orig_width: int = None
    '''Original image width 

    :type: int
    '''


class SequenceElements:
    '''Collection of SequenceElement '''

    def append(self, filename: str) -> 'SequenceElement':
        '''Push an image from ImageSequence.directory 

        :param filename: Filepath to image 
        :type filename: str
        :rtype: 'SequenceElement'
        :return:  New SequenceElement 
        '''
        pass

    def pop(self, index: int):
        '''Pop an image off the collection 

        :param index: Index of image to remove 
        :type index: int
        '''
        pass


class SequenceModifier:
    '''Modifier for sequence strip '''

    input_mask_id: 'Mask' = None
    '''Mask ID used as mask input for the modifier 

    :type: 'Mask'
    '''

    input_mask_strip: 'Sequence' = None
    '''Strip used as mask input for the modifier 

    :type: 'Sequence'
    '''

    input_mask_type: typing.Union[int, str] = None
    '''Type of input data used for mask 

    :type: typing.Union[int, str]
    '''

    mask_time: typing.Union[int, str] = None
    '''Time to use for the Mask animation 

    :type: typing.Union[int, str]
    '''

    mute: bool = None
    '''Mute this modifier 

    :type: bool
    '''

    name: str = None
    '''

    :type: str
    '''

    show_expanded: bool = None
    '''Mute expanded settings for the modifier 

    :type: bool
    '''

    type: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''


class SequenceModifiers:
    '''Collection of strip modifiers '''

    def new(self, name: str,
            type: typing.Union[int, str]) -> 'SequenceModifier':
        '''Add a new modifier 

        :param name: New name for the modifier 
        :type name: str
        :param type: Modifier type to add 
        :type type: typing.Union[int, str]
        :rtype: 'SequenceModifier'
        :return:  Newly created modifier 
        '''
        pass

    def remove(self, modifier: 'SequenceModifier'):
        '''Remove an existing modifier from the sequence 

        :param modifier: Modifier to remove 
        :type modifier: 'SequenceModifier'
        '''
        pass

    def clear(self, ):
        '''Remove all modifiers from the sequence 

        '''
        pass


class SequenceProxy:
    '''Proxy parameters for a sequence strip '''

    build_100: bool = None
    '''Build 100% proxy resolution 

    :type: bool
    '''

    build_25: bool = None
    '''Build 25% proxy resolution 

    :type: bool
    '''

    build_50: bool = None
    '''Build 50% proxy resolution 

    :type: bool
    '''

    build_75: bool = None
    '''Build 75% proxy resolution 

    :type: bool
    '''

    build_free_run: bool = None
    '''Build free run time code index 

    :type: bool
    '''

    build_free_run_rec_date: bool = None
    '''Build free run time code index using Record Date/Time 

    :type: bool
    '''

    build_record_run: bool = None
    '''Build record run time code index 

    :type: bool
    '''

    directory: str = None
    '''Location to store the proxy files 

    :type: str
    '''

    filepath: str = None
    '''Location of custom proxy file 

    :type: str
    '''

    quality: int = None
    '''JPEG Quality of proxies to build 

    :type: int
    '''

    timecode: typing.Union[int, str] = None
    '''Method for reading the inputs timecode 

    :type: typing.Union[int, str]
    '''

    use_overwrite: bool = None
    '''Overwrite existing proxy files when building 

    :type: bool
    '''

    use_proxy_custom_directory: bool = None
    '''Use a custom directory to store data 

    :type: bool
    '''

    use_proxy_custom_file: bool = None
    '''Use a custom file to read proxy data from 

    :type: bool
    '''


class SequenceTransform:
    '''Transform parameters for a sequence strip '''

    offset_x: int = None
    '''Amount to move the input on the X axis within its boundaries 

    :type: int
    '''

    offset_y: int = None
    '''Amount to move the input on the Y axis within its boundaries 

    :type: int
    '''


class SequencerTonemapModifierData:
    '''Tone mapping modifier '''

    adaptation: float = None
    '''If 0, global; if 1, based on pixel intensity 

    :type: float
    '''

    contrast: float = None
    '''Set to 0 to use estimate from input image 

    :type: float
    '''

    correction: float = None
    '''If 0, same for all channels; if 1, each independent 

    :type: float
    '''

    gamma: float = None
    '''If not used, set to 1 

    :type: float
    '''

    intensity: float = None
    '''If less than zero, darkens image; otherwise, makes it brighter 

    :type: float
    '''

    key: float = None
    '''The value the average luminance is mapped to 

    :type: float
    '''

    offset: float = None
    '''Normally always 1, but can be used as an extra control to alter the brightness curve 

    :type: float
    '''

    tonemap_type: typing.Union[int, str] = None
    '''Tone mapping algorithm 

    :type: typing.Union[int, str]
    '''


class Sequences:
    '''Collection of Sequences '''

    def new_clip(self, name: str, clip: 'MovieClip', channel: int,
                 frame_start: int) -> 'Sequence':
        '''Add a new movie clip sequence 

        :param name: Name for the new sequence 
        :type name: str
        :param clip: Movie clip to add 
        :type clip: 'MovieClip'
        :param channel: Channel, The channel for the new sequence 
        :type channel: int
        :param frame_start: The start frame for the new sequence 
        :type frame_start: int
        :rtype: 'Sequence'
        :return:  New Sequence 
        '''
        pass

    def new_mask(self, name: str, mask: 'Mask', channel: int,
                 frame_start: int) -> 'Sequence':
        '''Add a new mask sequence 

        :param name: Name for the new sequence 
        :type name: str
        :param mask: Mask to add 
        :type mask: 'Mask'
        :param channel: Channel, The channel for the new sequence 
        :type channel: int
        :param frame_start: The start frame for the new sequence 
        :type frame_start: int
        :rtype: 'Sequence'
        :return:  New Sequence 
        '''
        pass

    def new_scene(self, name: str, scene: 'Scene', channel: int,
                  frame_start: int) -> 'Sequence':
        '''Add a new scene sequence 

        :param name: Name for the new sequence 
        :type name: str
        :param scene: Scene to add 
        :type scene: 'Scene'
        :param channel: Channel, The channel for the new sequence 
        :type channel: int
        :param frame_start: The start frame for the new sequence 
        :type frame_start: int
        :rtype: 'Sequence'
        :return:  New Sequence 
        '''
        pass

    def new_image(self, name: str, filepath: str, channel: int,
                  frame_start: int) -> 'Sequence':
        '''Add a new image sequence 

        :param name: Name for the new sequence 
        :type name: str
        :param filepath: Filepath to image 
        :type filepath: str
        :param channel: Channel, The channel for the new sequence 
        :type channel: int
        :param frame_start: The start frame for the new sequence 
        :type frame_start: int
        :rtype: 'Sequence'
        :return:  New Sequence 
        '''
        pass

    def new_movie(self, name: str, filepath: str, channel: int,
                  frame_start: int) -> 'Sequence':
        '''Add a new movie sequence 

        :param name: Name for the new sequence 
        :type name: str
        :param filepath: Filepath to movie 
        :type filepath: str
        :param channel: Channel, The channel for the new sequence 
        :type channel: int
        :param frame_start: The start frame for the new sequence 
        :type frame_start: int
        :rtype: 'Sequence'
        :return:  New Sequence 
        '''
        pass

    def new_sound(self, name: str, filepath: str, channel: int,
                  frame_start: int) -> 'Sequence':
        '''Add a new sound sequence 

        :param name: Name for the new sequence 
        :type name: str
        :param filepath: Filepath to movie 
        :type filepath: str
        :param channel: Channel, The channel for the new sequence 
        :type channel: int
        :param frame_start: The start frame for the new sequence 
        :type frame_start: int
        :rtype: 'Sequence'
        :return:  New Sequence 
        '''
        pass

    def new_effect(self,
                   name: str,
                   type: typing.Union[int, str],
                   channel: int,
                   frame_start: int,
                   frame_end: int = 0,
                   seq1: 'Sequence' = None,
                   seq2: 'Sequence' = None,
                   seq3: 'Sequence' = None) -> 'Sequence':
        '''Add a new effect sequence 

        :param name: Name for the new sequence 
        :type name: str
        :param type: Type, type for the new sequence 
        :type type: typing.Union[int, str]
        :param channel: Channel, The channel for the new sequence 
        :type channel: int
        :param frame_start: The start frame for the new sequence 
        :type frame_start: int
        :param frame_end: The end frame for the new sequence 
        :type frame_end: int
        :param seq1: Sequence 1 for effect 
        :type seq1: 'Sequence'
        :param seq2: Sequence 2 for effect 
        :type seq2: 'Sequence'
        :param seq3: Sequence 3 for effect 
        :type seq3: 'Sequence'
        :rtype: 'Sequence'
        :return:  New Sequence 
        '''
        pass

    def remove(self, sequence: 'Sequence'):
        '''Remove a Sequence 

        :param sequence: Sequence to remove 
        :type sequence: 'Sequence'
        '''
        pass


class ShaderNode:
    '''Material shader node '''

    pass


class ShaderNodeAddShader:
    pass


class ShaderNodeAmbientOcclusion:
    pass


class ShaderNodeAttribute:
    attribute_name: str = None
    '''

    :type: str
    '''


class ShaderNodeBackground:
    pass


class ShaderNodeBlackbody:
    pass


class ShaderNodeBrightContrast:
    pass


class ShaderNodeBsdfAnisotropic:
    distribution: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''


class ShaderNodeBsdfDiffuse:
    pass


class ShaderNodeBsdfGlass:
    distribution: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''


class ShaderNodeBsdfGlossy:
    distribution: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''


class ShaderNodeBsdfHair:
    component: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''


class ShaderNodeBsdfPrincipled:
    distribution: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''


class ShaderNodeBsdfRefraction:
    distribution: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''


class ShaderNodeBsdfToon:
    component: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''


class ShaderNodeBsdfTranslucent:
    pass


class ShaderNodeBsdfTransparent:
    pass


class ShaderNodeBsdfVelvet:
    pass


class ShaderNodeBump:
    invert: bool = None
    '''Invert the bump mapping direction to push into the surface instead of out 

    :type: bool
    '''


class ShaderNodeCameraData:
    pass


class ShaderNodeCombineHSV:
    pass


class ShaderNodeCombineRGB:
    pass


class ShaderNodeCombineXYZ:
    pass


class ShaderNodeEmission:
    pass


class ShaderNodeExtendedMaterial:
    invert_normal: bool = None
    '''Material Node uses inverted normal 

    :type: bool
    '''

    material: 'Material' = None
    '''

    :type: 'Material'
    '''

    use_diffuse: bool = None
    '''Material Node outputs Diffuse 

    :type: bool
    '''

    use_specular: bool = None
    '''Material Node outputs Specular 

    :type: bool
    '''


class ShaderNodeFresnel:
    pass


class ShaderNodeGamma:
    pass


class ShaderNodeGeometry:
    color_layer: str = None
    '''

    :type: str
    '''

    uv_layer: str = None
    '''

    :type: str
    '''


class ShaderNodeGroup:
    interface: 'PropertyGroup' = None
    '''Interface socket data 

    :type: 'PropertyGroup'
    '''

    node_tree: 'NodeTree' = None
    '''

    :type: 'NodeTree'
    '''


class ShaderNodeHairInfo:
    pass


class ShaderNodeHoldout:
    pass


class ShaderNodeHueSaturation:
    pass


class ShaderNodeInvert:
    pass


class ShaderNodeLampData:
    lamp_object: 'Object' = None
    '''

    :type: 'Object'
    '''


class ShaderNodeLayerWeight:
    pass


class ShaderNodeLightFalloff:
    pass


class ShaderNodeLightPath:
    pass


class ShaderNodeMapping:
    max: float = None
    '''Maximum value for clipping 

    :type: float
    '''

    min: float = None
    '''Minimum value for clipping 

    :type: float
    '''

    rotation: float = None
    '''

    :type: float
    '''

    scale: float = None
    '''

    :type: float
    '''

    translation: float = None
    '''

    :type: float
    '''

    use_max: bool = None
    '''Whether to use maximum clipping value 

    :type: bool
    '''

    use_min: bool = None
    '''Whether to use minimum clipping value 

    :type: bool
    '''

    vector_type: typing.Union[int, str] = None
    '''Type of vector that the mapping transforms 

    :type: typing.Union[int, str]
    '''


class ShaderNodeMaterial:
    invert_normal: bool = None
    '''Material Node uses inverted normal 

    :type: bool
    '''

    material: 'Material' = None
    '''

    :type: 'Material'
    '''

    use_diffuse: bool = None
    '''Material Node outputs Diffuse 

    :type: bool
    '''

    use_specular: bool = None
    '''Material Node outputs Specular 

    :type: bool
    '''


class ShaderNodeMath:
    operation: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    use_clamp: bool = None
    '''Clamp result of the node to 0..1 range 

    :type: bool
    '''


class ShaderNodeMixRGB:
    blend_type: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    use_alpha: bool = None
    '''Include alpha of second input in this operation 

    :type: bool
    '''

    use_clamp: bool = None
    '''Clamp result of the node to 0..1 range 

    :type: bool
    '''


class ShaderNodeMixShader:
    pass


class ShaderNodeNewGeometry:
    pass


class ShaderNodeNormal:
    pass


class ShaderNodeNormalMap:
    space: typing.Union[int, str] = None
    '''Space of the input normal 

    :type: typing.Union[int, str]
    '''

    uv_map: str = None
    '''UV Map for tangent space maps 

    :type: str
    '''


class ShaderNodeObjectInfo:
    pass


class ShaderNodeOutput:
    is_active_output: bool = None
    '''True if this node is used as the active output 

    :type: bool
    '''


class ShaderNodeOutputLamp:
    is_active_output: bool = None
    '''True if this node is used as the active output 

    :type: bool
    '''


class ShaderNodeOutputLineStyle:
    blend_type: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    is_active_output: bool = None
    '''True if this node is used as the active output 

    :type: bool
    '''

    use_alpha: bool = None
    '''Include alpha of second input in this operation 

    :type: bool
    '''

    use_clamp: bool = None
    '''Clamp result of the node to 0..1 range 

    :type: bool
    '''


class ShaderNodeOutputMaterial:
    is_active_output: bool = None
    '''True if this node is used as the active output 

    :type: bool
    '''


class ShaderNodeOutputWorld:
    is_active_output: bool = None
    '''True if this node is used as the active output 

    :type: bool
    '''


class ShaderNodeParticleInfo:
    pass


class ShaderNodeRGB:
    pass


class ShaderNodeRGBCurve:
    mapping: 'CurveMapping' = None
    '''

    :type: 'CurveMapping'
    '''


class ShaderNodeRGBToBW:
    pass


class ShaderNodeScript:
    bytecode: str = None
    '''Compile bytecode for shader script node 

    :type: str
    '''

    bytecode_hash: str = None
    '''Hash of compile bytecode, for quick equality checking 

    :type: str
    '''

    filepath: str = None
    '''Shader script path 

    :type: str
    '''

    mode: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    script: 'Text' = None
    '''Internal shader script to define the shader 

    :type: 'Text'
    '''

    use_auto_update: bool = None
    '''Automatically update the shader when the .osl file changes (external scripts only) 

    :type: bool
    '''


class ShaderNodeSeparateHSV:
    pass


class ShaderNodeSeparateRGB:
    pass


class ShaderNodeSeparateXYZ:
    pass


class ShaderNodeSqueeze:
    pass


class ShaderNodeSubsurfaceScattering:
    falloff: typing.Union[int, str] = None
    '''Function to determine how much light nearby points contribute based on their distance to the shading point 

    :type: typing.Union[int, str]
    '''


class ShaderNodeTangent:
    axis: typing.Union[int, str] = None
    '''Axis for radial tangents 

    :type: typing.Union[int, str]
    '''

    direction_type: typing.Union[int, str] = None
    '''Method to use for the tangent 

    :type: typing.Union[int, str]
    '''

    uv_map: str = None
    '''UV Map for tangent generated from UV 

    :type: str
    '''


class ShaderNodeTexBrick:
    color_mapping: 'ColorMapping' = None
    '''Color mapping settings 

    :type: 'ColorMapping'
    '''

    offset: float = None
    '''

    :type: float
    '''

    offset_frequency: int = None
    '''

    :type: int
    '''

    squash: float = None
    '''

    :type: float
    '''

    squash_frequency: int = None
    '''

    :type: int
    '''

    texture_mapping: 'TexMapping' = None
    '''Texture coordinate mapping settings 

    :type: 'TexMapping'
    '''


class ShaderNodeTexChecker:
    color_mapping: 'ColorMapping' = None
    '''Color mapping settings 

    :type: 'ColorMapping'
    '''

    texture_mapping: 'TexMapping' = None
    '''Texture coordinate mapping settings 

    :type: 'TexMapping'
    '''


class ShaderNodeTexCoord:
    from_dupli: bool = None
    '''Use the parent of the dupli object if possible 

    :type: bool
    '''

    object: 'Object' = None
    '''Use coordinates from this object (for object texture coordinates output) 

    :type: 'Object'
    '''


class ShaderNodeTexEnvironment:
    color_mapping: 'ColorMapping' = None
    '''Color mapping settings 

    :type: 'ColorMapping'
    '''

    color_space: typing.Union[int, str] = None
    '''Image file color space 

    :type: typing.Union[int, str]
    '''

    image: 'Image' = None
    '''

    :type: 'Image'
    '''

    image_user: 'ImageUser' = None
    '''Parameters defining which layer, pass and frame of the image is displayed 

    :type: 'ImageUser'
    '''

    interpolation: typing.Union[int, str] = None
    '''Texture interpolation 

    :type: typing.Union[int, str]
    '''

    projection: typing.Union[int, str] = None
    '''Projection of the input image 

    :type: typing.Union[int, str]
    '''

    texture_mapping: 'TexMapping' = None
    '''Texture coordinate mapping settings 

    :type: 'TexMapping'
    '''


class ShaderNodeTexGradient:
    color_mapping: 'ColorMapping' = None
    '''Color mapping settings 

    :type: 'ColorMapping'
    '''

    gradient_type: typing.Union[int, str] = None
    '''Style of the color blending 

    :type: typing.Union[int, str]
    '''

    texture_mapping: 'TexMapping' = None
    '''Texture coordinate mapping settings 

    :type: 'TexMapping'
    '''


class ShaderNodeTexImage:
    color_mapping: 'ColorMapping' = None
    '''Color mapping settings 

    :type: 'ColorMapping'
    '''

    color_space: typing.Union[int, str] = None
    '''Image file color space 

    :type: typing.Union[int, str]
    '''

    extension: typing.Union[int, str] = None
    '''How the image is extrapolated past its original bounds 

    :type: typing.Union[int, str]
    '''

    image: 'Image' = None
    '''

    :type: 'Image'
    '''

    image_user: 'ImageUser' = None
    '''Parameters defining which layer, pass and frame of the image is displayed 

    :type: 'ImageUser'
    '''

    interpolation: typing.Union[int, str] = None
    '''Texture interpolation 

    :type: typing.Union[int, str]
    '''

    projection: typing.Union[int, str] = None
    '''Method to project 2D image on object with a 3D texture vector 

    :type: typing.Union[int, str]
    '''

    projection_blend: float = None
    '''For box projection, amount of blend to use between sides 

    :type: float
    '''

    texture_mapping: 'TexMapping' = None
    '''Texture coordinate mapping settings 

    :type: 'TexMapping'
    '''


class ShaderNodeTexMagic:
    color_mapping: 'ColorMapping' = None
    '''Color mapping settings 

    :type: 'ColorMapping'
    '''

    texture_mapping: 'TexMapping' = None
    '''Texture coordinate mapping settings 

    :type: 'TexMapping'
    '''

    turbulence_depth: int = None
    '''Level of detail in the added turbulent noise 

    :type: int
    '''


class ShaderNodeTexMusgrave:
    color_mapping: 'ColorMapping' = None
    '''Color mapping settings 

    :type: 'ColorMapping'
    '''

    musgrave_type: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    texture_mapping: 'TexMapping' = None
    '''Texture coordinate mapping settings 

    :type: 'TexMapping'
    '''


class ShaderNodeTexNoise:
    color_mapping: 'ColorMapping' = None
    '''Color mapping settings 

    :type: 'ColorMapping'
    '''

    texture_mapping: 'TexMapping' = None
    '''Texture coordinate mapping settings 

    :type: 'TexMapping'
    '''


class ShaderNodeTexPointDensity:
    interpolation: typing.Union[int, str] = None
    '''Texture interpolation 

    :type: typing.Union[int, str]
    '''

    object: 'Object' = None
    '''Object to take point data from 

    :type: 'Object'
    '''

    particle_color_source: typing.Union[int, str] = None
    '''Data to derive color results from 

    :type: typing.Union[int, str]
    '''

    particle_system: 'ParticleSystem' = None
    '''Particle System to render as points 

    :type: 'ParticleSystem'
    '''

    point_source: typing.Union[int, str] = None
    '''Point data to use as renderable point density 

    :type: typing.Union[int, str]
    '''

    radius: float = None
    '''Radius from the shaded sample to look for points within 

    :type: float
    '''

    resolution: int = None
    '''Resolution used by the texture holding the point density 

    :type: int
    '''

    space: typing.Union[int, str] = None
    '''Coordinate system to calculate voxels in 

    :type: typing.Union[int, str]
    '''

    vertex_attribute_name: str = None
    '''Vertex attribute to use for color 

    :type: str
    '''

    vertex_color_source: typing.Union[int, str] = None
    '''Data to derive color results from 

    :type: typing.Union[int, str]
    '''

    def cache_point_density(self,
                            scene=None,
                            settings: typing.Union[int, str] = 'RENDER'):
        '''Cache point density data for later calculation 

        :param settings: Calculate density for renderingVIEWPORT Viewport, Canculate density using viewport settings.RENDER Render, Canculate duplis using render settings. 
        :type settings: typing.Union[int, str]
        '''
        pass

    def calc_point_density(self,
                           scene=None,
                           settings: typing.Union[int, str] = 'RENDER'
                           ) -> float:
        '''Calculate point density 

        :param settings: Calculate density for renderingVIEWPORT Viewport, Canculate density using viewport settings.RENDER Render, Canculate duplis using render settings. 
        :type settings: typing.Union[int, str]
        :rtype: float
        :return:  RGBA Values 
        '''
        pass

    def calc_point_density_minmax(self,
                                  scene=None,
                                  settings: typing.Union[int, str] = 'RENDER'):
        '''Calculate point density 

        :param settings: Calculate density for renderingVIEWPORT Viewport, Canculate density using viewport settings.RENDER Render, Canculate duplis using render settings. 
        :type settings: typing.Union[int, str]
        '''
        pass


class ShaderNodeTexSky:
    color_mapping: 'ColorMapping' = None
    '''Color mapping settings 

    :type: 'ColorMapping'
    '''

    ground_albedo: float = None
    '''Ground color that is subtly reflected in the sky 

    :type: float
    '''

    sky_type: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    sun_direction: float = None
    '''Direction from where the sun is shining 

    :type: float
    '''

    texture_mapping: 'TexMapping' = None
    '''Texture coordinate mapping settings 

    :type: 'TexMapping'
    '''

    turbidity: float = None
    '''Atmospheric turbidity 

    :type: float
    '''


class ShaderNodeTexVoronoi:
    color_mapping: 'ColorMapping' = None
    '''Color mapping settings 

    :type: 'ColorMapping'
    '''

    coloring: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    texture_mapping: 'TexMapping' = None
    '''Texture coordinate mapping settings 

    :type: 'TexMapping'
    '''


class ShaderNodeTexWave:
    color_mapping: 'ColorMapping' = None
    '''Color mapping settings 

    :type: 'ColorMapping'
    '''

    texture_mapping: 'TexMapping' = None
    '''Texture coordinate mapping settings 

    :type: 'TexMapping'
    '''

    wave_profile: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    wave_type: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''


class ShaderNodeTexture:
    node_output: int = None
    '''For node-based textures, which output node to use 

    :type: int
    '''

    texture: 'Texture' = None
    '''

    :type: 'Texture'
    '''


class ShaderNodeTree:
    '''Node tree consisting of linked nodes used for materials (and other shading data-blocks) '''

    pass


class ShaderNodeUVAlongStroke:
    use_tips: bool = None
    '''Lower half of the texture is for tips of the stroke 

    :type: bool
    '''


class ShaderNodeUVMap:
    from_dupli: bool = None
    '''Use the parent of the dupli object if possible 

    :type: bool
    '''

    uv_map: str = None
    '''UV coordinates to be used for mapping 

    :type: str
    '''


class ShaderNodeValToRGB:
    color_ramp: 'ColorRamp' = None
    '''

    :type: 'ColorRamp'
    '''


class ShaderNodeValue:
    pass


class ShaderNodeVectorCurve:
    mapping: 'CurveMapping' = None
    '''

    :type: 'CurveMapping'
    '''


class ShaderNodeVectorMath:
    operation: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''


class ShaderNodeVectorTransform:
    convert_from: typing.Union[int, str] = None
    '''Space to convert from 

    :type: typing.Union[int, str]
    '''

    convert_to: typing.Union[int, str] = None
    '''Space to convert to 

    :type: typing.Union[int, str]
    '''

    vector_type: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''


class ShaderNodeVolumeAbsorption:
    pass


class ShaderNodeVolumeScatter:
    pass


class ShaderNodeWavelength:
    pass


class ShaderNodeWireframe:
    use_pixel_size: bool = None
    '''Use screen pixel size instead of world units 

    :type: bool
    '''


class ShapeKey:
    '''Shape key in a shape keys data-block '''

    data: typing.List['UnknownType'] = None
    '''

    :type: typing.List['UnknownType']
    '''

    frame: float = None
    '''Frame for absolute keys 

    :type: float
    '''

    interpolation: typing.Union[int, str] = None
    '''Interpolation type for absolute shape keys 

    :type: typing.Union[int, str]
    '''

    mute: bool = None
    '''Mute this shape key 

    :type: bool
    '''

    name: str = None
    '''Name of Shape Key 

    :type: str
    '''

    relative_key: 'ShapeKey' = None
    '''Shape used as a relative key 

    :type: 'ShapeKey'
    '''

    slider_max: float = None
    '''Maximum for slider 

    :type: float
    '''

    slider_min: float = None
    '''Minimum for slider 

    :type: float
    '''

    value: float = None
    '''Value of shape key at the current frame 

    :type: float
    '''

    vertex_group: str = None
    '''Vertex weight group, to blend with basis shape 

    :type: str
    '''

    def normals_vertex_get(self, ) -> float:
        '''Compute local space vertices’ normals for this shape key 

        :rtype: float
        :return:  normals 
        '''
        pass

    def normals_polygon_get(self, ) -> float:
        '''Compute local space faces’ normals for this shape key 

        :rtype: float
        :return:  normals 
        '''
        pass

    def normals_split_get(self, ) -> float:
        '''Compute local space face corners’ normals for this shape key 

        :rtype: float
        :return:  normals 
        '''
        pass


class ShapeKeyBezierPoint:
    '''Point in a shape key for Bezier curves '''

    co: float = None
    '''

    :type: float
    '''

    handle_left: float = None
    '''

    :type: float
    '''

    handle_right: float = None
    '''

    :type: float
    '''


class ShapeKeyCurvePoint:
    '''Point in a shape key for curves '''

    co: float = None
    '''

    :type: float
    '''

    tilt: float = None
    '''

    :type: float
    '''


class ShapeKeyPoint:
    '''Point in a shape key '''

    co: float = None
    '''

    :type: float
    '''


class ShrinkwrapConstraint:
    '''Create constraint-based shrinkwrap relationship '''

    distance: float = None
    '''Distance to Target 

    :type: float
    '''

    project_axis: typing.Union[int, str] = None
    '''Axis constrain to 

    :type: typing.Union[int, str]
    '''

    project_axis_space: typing.Union[int, str] = None
    '''Space for the projection axis 

    :type: typing.Union[int, str]
    '''

    project_limit: float = None
    '''Limit the distance used for projection (zero disables) 

    :type: float
    '''

    shrinkwrap_type: typing.Union[int, str] = None
    '''Select type of shrinkwrap algorithm for target position 

    :type: typing.Union[int, str]
    '''

    target: 'Object' = None
    '''Target Object 

    :type: 'Object'
    '''


class ShrinkwrapModifier:
    '''Shrink wrapping modifier to shrink wrap and object to a target '''

    auxiliary_target: 'Object' = None
    '''Additional mesh target to shrink to 

    :type: 'Object'
    '''

    cull_face: typing.Union[int, str] = None
    '''Stop vertices from projecting to a face on the target when facing towards/away 

    :type: typing.Union[int, str]
    '''

    invert_vertex_group: bool = None
    '''Invert vertex group influence 

    :type: bool
    '''

    offset: float = None
    '''Distance to keep from the target 

    :type: float
    '''

    project_limit: float = None
    '''Limit the distance used for projection (zero disables) 

    :type: float
    '''

    subsurf_levels: int = None
    '''Number of subdivisions that must be performed before extracting vertices’ positions and normals 

    :type: int
    '''

    target: 'Object' = None
    '''Mesh target to shrink to 

    :type: 'Object'
    '''

    use_keep_above_surface: bool = None
    '''

    :type: bool
    '''

    use_negative_direction: bool = None
    '''Allow vertices to move in the negative direction of axis 

    :type: bool
    '''

    use_positive_direction: bool = None
    '''Allow vertices to move in the positive direction of axis 

    :type: bool
    '''

    use_project_x: bool = None
    '''

    :type: bool
    '''

    use_project_y: bool = None
    '''

    :type: bool
    '''

    use_project_z: bool = None
    '''

    :type: bool
    '''

    vertex_group: str = None
    '''Vertex group name 

    :type: str
    '''

    wrap_method: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''


class SimpleDeformModifier:
    '''Simple deformation modifier to apply effects such as twisting and bending '''

    angle: float = None
    '''Angle of deformation 

    :type: float
    '''

    deform_method: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    factor: float = None
    '''Amount to deform object 

    :type: float
    '''

    invert_vertex_group: bool = None
    '''Invert vertex group influence 

    :type: bool
    '''

    limits: float = None
    '''Lower/Upper limits for deform 

    :type: float
    '''

    lock_x: bool = None
    '''Do not allow deformation along the X axis 

    :type: bool
    '''

    lock_y: bool = None
    '''Do not allow deformation along the Y axis 

    :type: bool
    '''

    origin: 'Object' = None
    '''Offset the origin and orientation of the deformation 

    :type: 'Object'
    '''

    vertex_group: str = None
    '''Vertex group name 

    :type: str
    '''


class SkinModifier:
    '''Generate Skin '''

    branch_smoothing: float = None
    '''Smooth complex geometry around branches 

    :type: float
    '''

    use_smooth_shade: bool = None
    '''Output faces with smooth shading rather than flat shaded 

    :type: bool
    '''

    use_x_symmetry: bool = None
    '''Avoid making unsymmetrical quads across the X axis 

    :type: bool
    '''

    use_y_symmetry: bool = None
    '''Avoid making unsymmetrical quads across the Y axis 

    :type: bool
    '''

    use_z_symmetry: bool = None
    '''Avoid making unsymmetrical quads across the Z axis 

    :type: bool
    '''


class SmokeCollSettings:
    '''Smoke collision settings '''

    collision_type: typing.Union[int, str] = None
    '''Collision type 

    :type: typing.Union[int, str]
    '''


class SmokeDomainSettings:
    '''Smoke domain settings '''

    adapt_margin: int = None
    '''Margin added around fluid to minimize boundary interference 

    :type: int
    '''

    adapt_threshold: float = None
    '''Maximum amount of fluid cell can contain before it is considered empty 

    :type: float
    '''

    additional_res: int = None
    '''Maximum number of additional cells 

    :type: int
    '''

    alpha: float = None
    '''How much density affects smoke motion (higher value results in faster rising smoke) 

    :type: float
    '''

    amplify: int = None
    '''Enhance the resolution of smoke by this factor using noise 

    :type: int
    '''

    axis_slice_method: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    beta: float = None
    '''How much heat affects smoke motion (higher value results in faster rising smoke) 

    :type: float
    '''

    burning_rate: float = None
    '''Speed of the burning reaction (use larger values for smaller flame) 

    :type: float
    '''

    cache_file_format: typing.Union[int, str] = None
    '''Select the file format to be used for caching 

    :type: typing.Union[int, str]
    '''

    cell_size: float = None
    '''Cell Size 

    :type: float
    '''

    coba_field: typing.Union[int, str] = None
    '''Simulation field to color map 

    :type: typing.Union[int, str]
    '''

    collision_extents: typing.Union[int, str] = None
    '''Select which domain border will be treated as collision object 

    :type: typing.Union[int, str]
    '''

    collision_group: 'Group' = None
    '''Limit collisions to this group 

    :type: 'Group'
    '''

    color_grid: float = None
    '''Smoke color grid 

    :type: float
    '''

    color_ramp: 'ColorRamp' = None
    '''

    :type: 'ColorRamp'
    '''

    data_depth: typing.Union[int, str] = None
    '''Bit depth for writing all scalar (including vector) lower values reduce file size 

    :type: typing.Union[int, str]
    '''

    density_grid: float = None
    '''Smoke density grid 

    :type: float
    '''

    display_thickness: float = None
    '''Thickness of smoke drawing in the viewport 

    :type: float
    '''

    dissolve_speed: int = None
    '''Dissolve Speed 

    :type: int
    '''

    domain_resolution: int = None
    '''Smoke Grid Resolution 

    :type: int
    '''

    draw_velocity: bool = None
    '''Toggle visualization of the velocity field as needles 

    :type: bool
    '''

    effector_group: 'Group' = None
    '''Limit effectors to this group 

    :type: 'Group'
    '''

    effector_weights: 'EffectorWeights' = None
    '''

    :type: 'EffectorWeights'
    '''

    flame_grid: float = None
    '''Smoke flame grid 

    :type: float
    '''

    flame_ignition: float = None
    '''Minimum temperature of flames 

    :type: float
    '''

    flame_max_temp: float = None
    '''Maximum temperature of flames 

    :type: float
    '''

    flame_smoke: float = None
    '''Amount of smoke created by burning fuel 

    :type: float
    '''

    flame_smoke_color: float = None
    '''Color of smoke emitted from burning fuel 

    :type: float
    '''

    flame_vorticity: float = None
    '''Additional vorticity for the flames 

    :type: float
    '''

    fluid_group: 'Group' = None
    '''Limit fluid objects to this group 

    :type: 'Group'
    '''

    heat_grid: float = None
    '''Smoke heat grid 

    :type: float
    '''

    highres_sampling: typing.Union[int, str] = None
    '''Method for sampling the high resolution flow 

    :type: typing.Union[int, str]
    '''

    noise_type: typing.Union[int, str] = None
    '''Noise method which is used for creating the high resolution 

    :type: typing.Union[int, str]
    '''

    openvdb_cache_compress_type: typing.Union[int, str] = None
    '''Compression method to be used 

    :type: typing.Union[int, str]
    '''

    point_cache: 'PointCache' = None
    '''

    :type: 'PointCache'
    '''

    point_cache_compress_type: typing.Union[int, str] = None
    '''Compression method to be used 

    :type: typing.Union[int, str]
    '''

    resolution_max: int = None
    '''Maximal resolution used in the fluid domain 

    :type: int
    '''

    show_high_resolution: bool = None
    '''Show high resolution (using amplification) 

    :type: bool
    '''

    slice_axis: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    slice_depth: float = None
    '''Position of the slice 

    :type: float
    '''

    slice_method: typing.Union[int, str] = None
    '''How to slice the volume for viewport rendering 

    :type: typing.Union[int, str]
    '''

    slice_per_voxel: float = None
    '''How many slices per voxel should be generated 

    :type: float
    '''

    start_point: float = None
    '''Start point 

    :type: float
    '''

    strength: float = None
    '''Strength of noise 

    :type: float
    '''

    time_scale: float = None
    '''Adjust simulation speed 

    :type: float
    '''

    use_adaptive_domain: bool = None
    '''Adapt simulation resolution and size to fluid 

    :type: bool
    '''

    use_color_ramp: bool = None
    '''Render a simulation field while mapping its voxels values to the colors of a ramp 

    :type: bool
    '''

    use_dissolve_smoke: bool = None
    '''Enable smoke to disappear over time 

    :type: bool
    '''

    use_dissolve_smoke_log: bool = None
    '''Using 1/x 

    :type: bool
    '''

    use_high_resolution: bool = None
    '''Enable high resolution (using amplification) 

    :type: bool
    '''

    vector_draw_type: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    vector_scale: float = None
    '''Multiplier for scaling the vectors 

    :type: float
    '''

    velocity_grid: float = None
    '''Smoke velocity grid 

    :type: float
    '''

    vorticity: float = None
    '''Amount of turbulence/rotation in fluid 

    :type: float
    '''


class SmokeFlowSettings:
    '''Smoke flow settings '''

    density: float = None
    '''

    :type: float
    '''

    density_vertex_group: str = None
    '''Name of vertex group which determines surface emission rate 

    :type: str
    '''

    fuel_amount: float = None
    '''

    :type: float
    '''

    noise_texture: 'Texture' = None
    '''Texture that controls emission strength 

    :type: 'Texture'
    '''

    particle_size: float = None
    '''Particle size in simulation cells 

    :type: float
    '''

    particle_system: 'ParticleSystem' = None
    '''Particle systems emitted from the object 

    :type: 'ParticleSystem'
    '''

    smoke_color: float = None
    '''Color of smoke 

    :type: float
    '''

    smoke_flow_source: typing.Union[int, str] = None
    '''Change how smoke is emitted 

    :type: typing.Union[int, str]
    '''

    smoke_flow_type: typing.Union[int, str] = None
    '''Change how flow affects the simulation 

    :type: typing.Union[int, str]
    '''

    subframes: int = None
    '''Number of additional samples to take between frames to improve quality of fast moving flows 

    :type: int
    '''

    surface_distance: float = None
    '''Maximum distance from mesh surface to emit smoke 

    :type: float
    '''

    temperature: float = None
    '''Temperature difference to ambient temperature 

    :type: float
    '''

    texture_map_type: typing.Union[int, str] = None
    '''Texture mapping type 

    :type: typing.Union[int, str]
    '''

    texture_offset: float = None
    '''Z-offset of texture mapping 

    :type: float
    '''

    texture_size: float = None
    '''Size of texture mapping 

    :type: float
    '''

    use_absolute: bool = None
    '''Only allow given density value in emitter area 

    :type: bool
    '''

    use_initial_velocity: bool = None
    '''Smoke has some initial velocity when it is emitted 

    :type: bool
    '''

    use_particle_size: bool = None
    '''Set particle size in simulation cells or use nearest cell 

    :type: bool
    '''

    use_texture: bool = None
    '''Use a texture to control emission strength 

    :type: bool
    '''

    uv_layer: str = None
    '''UV map name 

    :type: str
    '''

    velocity_factor: float = None
    '''Multiplier of source velocity passed to smoke 

    :type: float
    '''

    velocity_normal: float = None
    '''Amount of normal directional velocity 

    :type: float
    '''

    velocity_random: float = None
    '''Amount of random velocity 

    :type: float
    '''

    volume_density: float = None
    '''Factor for smoke emitted from inside the mesh volume 

    :type: float
    '''


class SmokeModifier:
    '''Smoke simulation modifier '''

    coll_settings: 'SmokeCollSettings' = None
    '''

    :type: 'SmokeCollSettings'
    '''

    domain_settings: 'SmokeDomainSettings' = None
    '''

    :type: 'SmokeDomainSettings'
    '''

    flow_settings: 'SmokeFlowSettings' = None
    '''

    :type: 'SmokeFlowSettings'
    '''

    smoke_type: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''


class SmoothModifier:
    '''Smoothing effect modifier '''

    factor: float = None
    '''Strength of modifier effect 

    :type: float
    '''

    iterations: int = None
    '''

    :type: int
    '''

    use_x: bool = None
    '''Smooth object along X axis 

    :type: bool
    '''

    use_y: bool = None
    '''Smooth object along Y axis 

    :type: bool
    '''

    use_z: bool = None
    '''Smooth object along Z axis 

    :type: bool
    '''

    vertex_group: str = None
    '''Name of Vertex Group which determines influence of modifier per point 

    :type: str
    '''


class SoftBodyModifier:
    '''Soft body simulation modifier '''

    point_cache: 'PointCache' = None
    '''

    :type: 'PointCache'
    '''

    settings: 'SoftBodySettings' = None
    '''

    :type: 'SoftBodySettings'
    '''


class SoftBodySettings:
    '''Soft body simulation settings for an object '''

    aero: int = None
    '''Make edges ‘sail’ 

    :type: int
    '''

    aerodynamics_type: typing.Union[int, str] = None
    '''Method of calculating aerodynamic interaction 

    :type: typing.Union[int, str]
    '''

    ball_damp: float = None
    '''Blending to inelastic collision 

    :type: float
    '''

    ball_size: float = None
    '''Absolute ball size or factor if not manually adjusted 

    :type: float
    '''

    ball_stiff: float = None
    '''Ball inflating pressure 

    :type: float
    '''

    bend: float = None
    '''Bending Stiffness 

    :type: float
    '''

    choke: int = None
    '''‘Viscosity’ inside collision target 

    :type: int
    '''

    collision_group: 'Group' = None
    '''Limit colliders to this Group 

    :type: 'Group'
    '''

    collision_type: typing.Union[int, str] = None
    '''Choose Collision Type 

    :type: typing.Union[int, str]
    '''

    damping: float = None
    '''Edge spring friction 

    :type: float
    '''

    effector_weights: 'EffectorWeights' = None
    '''

    :type: 'EffectorWeights'
    '''

    error_threshold: float = None
    '''The Runge-Kutta ODE solver error limit, low value gives more precision, high values speed 

    :type: float
    '''

    friction: float = None
    '''General media friction for point movements 

    :type: float
    '''

    fuzzy: int = None
    '''Fuzziness while on collision, high values make collision handling faster but less stable 

    :type: int
    '''

    goal_default: float = None
    '''Default Goal (vertex target position) value 

    :type: float
    '''

    goal_friction: float = None
    '''Goal (vertex target position) friction 

    :type: float
    '''

    goal_max: float = None
    '''Goal maximum, vertex weights are scaled to match this range 

    :type: float
    '''

    goal_min: float = None
    '''Goal minimum, vertex weights are scaled to match this range 

    :type: float
    '''

    goal_spring: float = None
    '''Goal (vertex target position) spring stiffness 

    :type: float
    '''

    gravity: float = None
    '''Apply gravitation to point movement 

    :type: float
    '''

    location_mass_center: float = None
    '''Location of Center of mass 

    :type: float
    '''

    mass: float = None
    '''General Mass value 

    :type: float
    '''

    plastic: int = None
    '''Permanent deform 

    :type: int
    '''

    pull: float = None
    '''Edge spring stiffness when longer than rest length 

    :type: float
    '''

    push: float = None
    '''Edge spring stiffness when shorter than rest length 

    :type: float
    '''

    rotation_estimate: float = None
    '''Estimated rotation matrix 

    :type: float
    '''

    scale_estimate: float = None
    '''Estimated scale matrix 

    :type: float
    '''

    shear: float = None
    '''Shear Stiffness 

    :type: float
    '''

    speed: float = None
    '''Tweak timing for physics to control frequency and speed 

    :type: float
    '''

    spring_length: int = None
    '''Alter spring length to shrink/blow up (unit %) 0 to disable 

    :type: int
    '''

    step_max: int = None
    '''Maximal # solver steps/frame 

    :type: int
    '''

    step_min: int = None
    '''Minimal # solver steps/frame 

    :type: int
    '''

    use_auto_step: bool = None
    '''Use velocities for automagic step sizes 

    :type: bool
    '''

    use_diagnose: bool = None
    '''Turn on SB diagnose console prints 

    :type: bool
    '''

    use_edge_collision: bool = None
    '''Edges collide too 

    :type: bool
    '''

    use_edges: bool = None
    '''Use Edges as springs 

    :type: bool
    '''

    use_estimate_matrix: bool = None
    '''Estimate matrix… split to COM, ROT, SCALE 

    :type: bool
    '''

    use_face_collision: bool = None
    '''Faces collide too, can be very slow 

    :type: bool
    '''

    use_goal: bool = None
    '''Define forces for vertices to stick to animated position 

    :type: bool
    '''

    use_self_collision: bool = None
    '''Enable naive vertex ball self collision 

    :type: bool
    '''

    use_stiff_quads: bool = None
    '''Add diagonal springs on 4-gons 

    :type: bool
    '''

    vertex_group_goal: str = None
    '''Control point weight values 

    :type: str
    '''

    vertex_group_mass: str = None
    '''Control point mass values 

    :type: str
    '''

    vertex_group_spring: str = None
    '''Control point spring strength values 

    :type: str
    '''


class SolidifyModifier:
    '''Create a solid skin by extruding, compensating for sharp angles '''

    edge_crease_inner: float = None
    '''Assign a crease to inner edges 

    :type: float
    '''

    edge_crease_outer: float = None
    '''Assign a crease to outer edges 

    :type: float
    '''

    edge_crease_rim: float = None
    '''Assign a crease to the edges making up the rim 

    :type: float
    '''

    invert_vertex_group: bool = None
    '''Invert the vertex group influence 

    :type: bool
    '''

    material_offset: int = None
    '''Offset material index of generated faces 

    :type: int
    '''

    material_offset_rim: int = None
    '''Offset material index of generated rim faces 

    :type: int
    '''

    offset: float = None
    '''Offset the thickness from the center 

    :type: float
    '''

    thickness: float = None
    '''Thickness of the shell 

    :type: float
    '''

    thickness_clamp: float = None
    '''Offset clamp based on geometry scale 

    :type: float
    '''

    thickness_vertex_group: float = None
    '''Thickness factor to use for zero vertex group influence 

    :type: float
    '''

    use_even_offset: bool = None
    '''Maintain thickness by adjusting for sharp corners (slow, disable when not needed) 

    :type: bool
    '''

    use_flip_normals: bool = None
    '''Invert the face direction 

    :type: bool
    '''

    use_quality_normals: bool = None
    '''Calculate normals which result in more even thickness (slow, disable when not needed) 

    :type: bool
    '''

    use_rim: bool = None
    '''Create edge loops between the inner and outer surfaces on face edges (slow, disable when not needed) 

    :type: bool
    '''

    use_rim_only: bool = None
    '''Only add the rim to the original data 

    :type: bool
    '''

    vertex_group: str = None
    '''Vertex group name 

    :type: str
    '''


class Sound:
    '''Sound data-block referencing an external or packed sound file '''

    filepath: str = None
    '''Sound sample file used by this Sound data-block 

    :type: str
    '''

    packed_file: 'PackedFile' = None
    '''

    :type: 'PackedFile'
    '''

    use_memory_cache: bool = None
    '''The sound file is decoded and loaded into RAM 

    :type: bool
    '''

    use_mono: bool = None
    '''If the file contains multiple audio channels they are rendered to a single one 

    :type: bool
    '''

    factory = None
    '''The aud.Factory object of the sound. (readonly) '''

    def pack(self, ):
        '''Pack the sound into the current blend file 

        '''
        pass

    def unpack(self, method: typing.Union[int, str] = 'USE_LOCAL'):
        '''Unpack the sound to the samples filename 

        :param method: method, How to unpack 
        :type method: typing.Union[int, str]
        '''
        pass


class SoundActuator:
    '''Sound file '''

    cone_inner_angle_3d: float = None
    '''The angle of the inner cone 

    :type: float
    '''

    cone_outer_angle_3d: float = None
    '''The angle of the outer cone 

    :type: float
    '''

    cone_outer_gain_3d: float = None
    '''The gain outside the outer cone (the gain in the outer cone will be interpolated between this value and the normal gain in the inner cone) 

    :type: float
    '''

    distance_3d_max: float = None
    '''The maximum distance at which you can hear the sound 

    :type: float
    '''

    distance_3d_reference: float = None
    '''The distance where the sound has a gain of 1.0 

    :type: float
    '''

    gain_3d_max: float = None
    '''The maximum gain of the sound, no matter how near it is 

    :type: float
    '''

    gain_3d_min: float = None
    '''The minimum gain of the sound, no matter how far it is away 

    :type: float
    '''

    mode: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    pitch: float = None
    '''Pitch of the sound 

    :type: float
    '''

    rolloff_factor_3d: float = None
    '''The influence factor on volume depending on distance 

    :type: float
    '''

    sound: 'Sound' = None
    '''

    :type: 'Sound'
    '''

    use_sound_3d: bool = None
    '''Enable/Disable 3D Sound 

    :type: bool
    '''

    volume: float = None
    '''Initial volume of the sound 

    :type: float
    '''


class SoundSequence:
    '''Sequence strip defining a sound to be played over a period of time '''

    animation_offset_end: int = None
    '''Animation end offset (trim end) 

    :type: int
    '''

    animation_offset_start: int = None
    '''Animation start offset (trim start) 

    :type: int
    '''

    pan: float = None
    '''Playback panning of the sound (only for Mono sources) 

    :type: float
    '''

    pitch: float = None
    '''Playback pitch of the sound 

    :type: float
    '''

    show_waveform: bool = None
    '''Whether to draw the sound’s waveform 

    :type: bool
    '''

    sound: 'Sound' = None
    '''Sound data-block used by this sequence 

    :type: 'Sound'
    '''

    volume: float = None
    '''Playback volume of the sound 

    :type: float
    '''


class Space:
    '''Space data for a screen area '''

    show_locked_time: bool = None
    '''

    :type: bool
    '''

    type: typing.Union[int, str] = None
    '''Space data type 

    :type: typing.Union[int, str]
    '''

    def draw_handler_add(self, ):
        '''Undocumented 

        '''
        pass

    def draw_handler_remove(self, ):
        '''Undocumented 

        '''
        pass


class SpaceClipEditor:
    '''Clip editor space data '''

    clip: 'MovieClip' = None
    '''Movie clip displayed and edited in this space 

    :type: 'MovieClip'
    '''

    clip_user: 'MovieClipUser' = None
    '''Parameters defining which frame of the movie clip is displayed 

    :type: 'MovieClipUser'
    '''

    grease_pencil_source: typing.Union[int, str] = None
    '''Where the grease pencil comes from 

    :type: typing.Union[int, str]
    '''

    lock_selection: bool = None
    '''Lock viewport to selected markers during playback 

    :type: bool
    '''

    lock_time_cursor: bool = None
    '''Lock curves view to time cursor during playback and tracking 

    :type: bool
    '''

    mask: 'Mask' = None
    '''Mask displayed and edited in this space 

    :type: 'Mask'
    '''

    mask_draw_type: typing.Union[int, str] = None
    '''Draw type for mask splines 

    :type: typing.Union[int, str]
    '''

    mask_overlay_mode: typing.Union[int, str] = None
    '''Overlay mode of rasterized mask 

    :type: typing.Union[int, str]
    '''

    mode: typing.Union[int, str] = None
    '''Editing context being displayed 

    :type: typing.Union[int, str]
    '''

    path_length: int = None
    '''Length of displaying path, in frames 

    :type: int
    '''

    pivot_point: typing.Union[int, str] = None
    '''Pivot center for rotation/scaling 

    :type: typing.Union[int, str]
    '''

    scopes: 'MovieClipScopes' = None
    '''Scopes to visualize movie clip statistics 

    :type: 'MovieClipScopes'
    '''

    show_blue_channel: bool = None
    '''Show blue channel in the frame 

    :type: bool
    '''

    show_bundles: bool = None
    '''Show projection of 3D markers into footage 

    :type: bool
    '''

    show_disabled: bool = None
    '''Show disabled tracks from the footage 

    :type: bool
    '''

    show_filters: bool = None
    '''Show filters for graph editor 

    :type: bool
    '''

    show_graph_frames: bool = None
    '''Show curve for per-frame average error (camera motion should be solved first) 

    :type: bool
    '''

    show_graph_hidden: bool = None
    '''Include channels from objects/bone that aren’t visible 

    :type: bool
    '''

    show_graph_only_selected: bool = None
    '''Only include channels relating to selected objects and data 

    :type: bool
    '''

    show_graph_tracks_error: bool = None
    '''Display the reprojection error curve for selected tracks 

    :type: bool
    '''

    show_graph_tracks_motion: bool = None
    '''Display the speed curves (in “x” direction red, in “y” direction green) for the selected tracks 

    :type: bool
    '''

    show_grease_pencil: bool = None
    '''Show grease pencil for this view 

    :type: bool
    '''

    show_green_channel: bool = None
    '''Show green channel in the frame 

    :type: bool
    '''

    show_grid: bool = None
    '''Show grid showing lens distortion 

    :type: bool
    '''

    show_marker_pattern: bool = None
    '''Show pattern boundbox for markers 

    :type: bool
    '''

    show_marker_search: bool = None
    '''Show search boundbox for markers 

    :type: bool
    '''

    show_mask_overlay: bool = None
    '''

    :type: bool
    '''

    show_mask_smooth: bool = None
    '''

    :type: bool
    '''

    show_metadata: bool = None
    '''Show metadata of clip 

    :type: bool
    '''

    show_names: bool = None
    '''Show track names and status 

    :type: bool
    '''

    show_red_channel: bool = None
    '''Show red channel in the frame 

    :type: bool
    '''

    show_seconds: bool = None
    '''Show timing in seconds not frames 

    :type: bool
    '''

    show_stable: bool = None
    '''Show stable footage in editor (if stabilization is enabled) 

    :type: bool
    '''

    show_tiny_markers: bool = None
    '''Show markers in a more compact manner 

    :type: bool
    '''

    show_track_path: bool = None
    '''Show path of how track moves 

    :type: bool
    '''

    use_grayscale_preview: bool = None
    '''Display frame in grayscale mode 

    :type: bool
    '''

    use_manual_calibration: bool = None
    '''Use manual calibration helpers 

    :type: bool
    '''

    use_mute_footage: bool = None
    '''Mute footage and show black background instead 

    :type: bool
    '''

    view: typing.Union[int, str] = None
    '''Type of the clip editor view 

    :type: typing.Union[int, str]
    '''

    def draw_handler_add(self, ):
        '''Undocumented 

        '''
        pass

    def draw_handler_remove(self, ):
        '''Undocumented 

        '''
        pass


class SpaceConsole:
    '''Interactive python console '''

    font_size: int = None
    '''Font size to use for displaying the text 

    :type: int
    '''

    history: typing.List['ConsoleLine'] = None
    '''Command history 

    :type: typing.List['ConsoleLine']
    '''

    language: str = None
    '''Command line prompt language 

    :type: str
    '''

    prompt: str = None
    '''Command line prompt 

    :type: str
    '''

    scrollback: typing.List['ConsoleLine'] = None
    '''Command output 

    :type: typing.List['ConsoleLine']
    '''

    select_end: int = None
    '''

    :type: int
    '''

    select_start: int = None
    '''

    :type: int
    '''

    def draw_handler_add(self, ):
        '''Undocumented 

        '''
        pass

    def draw_handler_remove(self, ):
        '''Undocumented 

        '''
        pass


class SpaceDopeSheetEditor:
    '''Dope Sheet space data '''

    action: 'Action' = None
    '''Action displayed and edited in this space 

    :type: 'Action'
    '''

    auto_snap: typing.Union[int, str] = None
    '''Automatic time snapping settings for transformations 

    :type: typing.Union[int, str]
    '''

    dopesheet: 'DopeSheet' = None
    '''Settings for filtering animation data 

    :type: 'DopeSheet'
    '''

    mode: typing.Union[int, str] = None
    '''Editing context being displayed 

    :type: typing.Union[int, str]
    '''

    show_frame_indicator: bool = None
    '''Show frame number beside the current frame indicator line 

    :type: bool
    '''

    show_group_colors: bool = None
    '''Draw groups and channels with colors matching their corresponding groups (pose bones only currently) 

    :type: bool
    '''

    show_pose_markers: bool = None
    '''Show markers belonging to the active action instead of Scene markers (Action and Shape Key Editors only) 

    :type: bool
    '''

    show_seconds: bool = None
    '''Show timing in seconds not frames 

    :type: bool
    '''

    show_sliders: bool = None
    '''Show sliders beside F-Curve channels 

    :type: bool
    '''

    use_auto_merge_keyframes: bool = None
    '''Automatically merge nearby keyframes 

    :type: bool
    '''

    use_marker_sync: bool = None
    '''Sync Markers with keyframe edits 

    :type: bool
    '''

    use_realtime_update: bool = None
    '''When transforming keyframes, changes to the animation data are flushed to other views 

    :type: bool
    '''

    def draw_handler_add(self, ):
        '''Undocumented 

        '''
        pass

    def draw_handler_remove(self, ):
        '''Undocumented 

        '''
        pass


class SpaceFileBrowser:
    '''File browser space data '''

    active_operator: 'Operator' = None
    '''

    :type: 'Operator'
    '''

    bookmarks: typing.List['FileBrowserFSMenuEntry'] = None
    '''User’s bookmarks 

    :type: typing.List['FileBrowserFSMenuEntry']
    '''

    bookmarks_active: int = None
    '''Index of active bookmark (-1 if none) 

    :type: int
    '''

    operator: 'Operator' = None
    '''

    :type: 'Operator'
    '''

    params: 'FileSelectParams' = None
    '''Parameters and Settings for the Filebrowser 

    :type: 'FileSelectParams'
    '''

    recent_folders: typing.List['FileBrowserFSMenuEntry'] = None
    '''

    :type: typing.List['FileBrowserFSMenuEntry']
    '''

    recent_folders_active: int = None
    '''Index of active recent folder (-1 if none) 

    :type: int
    '''

    system_bookmarks: typing.List['FileBrowserFSMenuEntry'] = None
    '''System’s bookmarks 

    :type: typing.List['FileBrowserFSMenuEntry']
    '''

    system_bookmarks_active: int = None
    '''Index of active system bookmark (-1 if none) 

    :type: int
    '''

    system_folders: typing.List['FileBrowserFSMenuEntry'] = None
    '''System’s folders (usually root, available hard drives, etc) 

    :type: typing.List['FileBrowserFSMenuEntry']
    '''

    system_folders_active: int = None
    '''Index of active system folder (-1 if none) 

    :type: int
    '''

    def draw_handler_add(self, ):
        '''Undocumented 

        '''
        pass

    def draw_handler_remove(self, ):
        '''Undocumented 

        '''
        pass


class SpaceGraphEditor:
    '''Graph Editor space data '''

    auto_snap: typing.Union[int, str] = None
    '''Automatic time snapping settings for transformations 

    :type: typing.Union[int, str]
    '''

    cursor_position_x: float = None
    '''Graph Editor 2D-Value cursor - X-Value component 

    :type: float
    '''

    cursor_position_y: float = None
    '''Graph Editor 2D-Value cursor - Y-Value component 

    :type: float
    '''

    dopesheet: 'DopeSheet' = None
    '''Settings for filtering animation data 

    :type: 'DopeSheet'
    '''

    has_ghost_curves: bool = None
    '''Graph Editor instance has some ghost curves stored 

    :type: bool
    '''

    mode: typing.Union[int, str] = None
    '''Editing context being displayed 

    :type: typing.Union[int, str]
    '''

    pivot_point: typing.Union[int, str] = None
    '''Pivot center for rotation/scaling 

    :type: typing.Union[int, str]
    '''

    show_cursor: bool = None
    '''Show 2D cursor 

    :type: bool
    '''

    show_frame_indicator: bool = None
    '''Show frame number beside the current frame indicator line 

    :type: bool
    '''

    show_group_colors: bool = None
    '''Draw groups and channels with colors matching their corresponding groups 

    :type: bool
    '''

    show_handles: bool = None
    '''Show handles of Bezier control points 

    :type: bool
    '''

    show_seconds: bool = None
    '''Show timing in seconds not frames 

    :type: bool
    '''

    show_sliders: bool = None
    '''Show sliders beside F-Curve channels 

    :type: bool
    '''

    use_auto_merge_keyframes: bool = None
    '''Automatically merge nearby keyframes 

    :type: bool
    '''

    use_auto_normalization: bool = None
    '''Automatically recalculate curve normalization on every curve edit 

    :type: bool
    '''

    use_beauty_drawing: bool = None
    '''Draw F-Curves using Anti-Aliasing and other fancy effects (disable for better performance) 

    :type: bool
    '''

    use_normalization: bool = None
    '''Display curves in normalized to -1..1 range, for easier editing of multiple curves with different ranges 

    :type: bool
    '''

    use_only_selected_curves_handles: bool = None
    '''Only keyframes of selected F-Curves are visible and editable 

    :type: bool
    '''

    use_only_selected_keyframe_handles: bool = None
    '''Only show and edit handles of selected keyframes 

    :type: bool
    '''

    use_realtime_update: bool = None
    '''When transforming keyframes, changes to the animation data are flushed to other views 

    :type: bool
    '''

    def draw_handler_add(self, ):
        '''Undocumented 

        '''
        pass

    def draw_handler_remove(self, ):
        '''Undocumented 

        '''
        pass


class SpaceImageEditor:
    '''Image and UV editor space data '''

    cursor_location: float = None
    '''2D cursor location for this view 

    :type: float
    '''

    draw_channels: typing.Union[int, str] = None
    '''Channels of the image to draw 

    :type: typing.Union[int, str]
    '''

    grease_pencil: 'GreasePencil' = None
    '''Grease pencil data for this space 

    :type: 'GreasePencil'
    '''

    image: 'Image' = None
    '''Image displayed and edited in this space 

    :type: 'Image'
    '''

    image_user: 'ImageUser' = None
    '''Parameters defining which layer, pass and frame of the image is displayed 

    :type: 'ImageUser'
    '''

    mask: 'Mask' = None
    '''Mask displayed and edited in this space 

    :type: 'Mask'
    '''

    mask_draw_type: typing.Union[int, str] = None
    '''Draw type for mask splines 

    :type: typing.Union[int, str]
    '''

    mask_overlay_mode: typing.Union[int, str] = None
    '''Overlay mode of rasterized mask 

    :type: typing.Union[int, str]
    '''

    mode: typing.Union[int, str] = None
    '''Editing context being displayed 

    :type: typing.Union[int, str]
    '''

    pivot_point: typing.Union[int, str] = None
    '''Rotation/Scaling Pivot 

    :type: typing.Union[int, str]
    '''

    sample_histogram: 'Histogram' = None
    '''Sampled colors along line 

    :type: 'Histogram'
    '''

    scopes: 'Scopes' = None
    '''Scopes to visualize image statistics 

    :type: 'Scopes'
    '''

    show_grease_pencil: bool = None
    '''Show grease pencil for this view 

    :type: bool
    '''

    show_mask_overlay: bool = None
    '''

    :type: bool
    '''

    show_mask_smooth: bool = None
    '''

    :type: bool
    '''

    show_maskedit: bool = None
    '''Show Mask editing related properties 

    :type: bool
    '''

    show_paint: bool = None
    '''Show paint related properties 

    :type: bool
    '''

    show_render: bool = None
    '''Show render related properties 

    :type: bool
    '''

    show_repeat: bool = None
    '''Draw the image repeated outside of the main view 

    :type: bool
    '''

    show_stereo_3d: bool = None
    '''Display the image in Stereo 3D 

    :type: bool
    '''

    show_uvedit: bool = None
    '''Show UV editing related properties 

    :type: bool
    '''

    use_image_pin: bool = None
    '''Display current image regardless of object selection 

    :type: bool
    '''

    use_realtime_update: bool = None
    '''Update other affected window spaces automatically to reflect changes during interactive operations such as transform 

    :type: bool
    '''

    uv_editor: 'SpaceUVEditor' = None
    '''UV editor settings 

    :type: 'SpaceUVEditor'
    '''

    zoom: float = None
    '''Zoom factor 

    :type: float
    '''

    def draw_handler_add(self, ):
        '''Undocumented 

        '''
        pass

    def draw_handler_remove(self, ):
        '''Undocumented 

        '''
        pass


class SpaceInfo:
    '''Info space data '''

    show_report_debug: bool = None
    '''Display debug reporting info 

    :type: bool
    '''

    show_report_error: bool = None
    '''Display error text 

    :type: bool
    '''

    show_report_info: bool = None
    '''Display general information 

    :type: bool
    '''

    show_report_operator: bool = None
    '''Display the operator log 

    :type: bool
    '''

    show_report_warning: bool = None
    '''Display warnings 

    :type: bool
    '''

    def draw_handler_add(self, ):
        '''Undocumented 

        '''
        pass

    def draw_handler_remove(self, ):
        '''Undocumented 

        '''
        pass


class SpaceLogicEditor:
    '''Logic editor space data '''

    show_actuators_active_object: bool = None
    '''Show actuators of active object 

    :type: bool
    '''

    show_actuators_active_states: bool = None
    '''Show only actuators connected to active states 

    :type: bool
    '''

    show_actuators_linked_controller: bool = None
    '''Show linked objects to the actuator 

    :type: bool
    '''

    show_actuators_selected_objects: bool = None
    '''Show actuators of all selected objects 

    :type: bool
    '''

    show_controllers_active_object: bool = None
    '''Show controllers of active object 

    :type: bool
    '''

    show_controllers_linked_controller: bool = None
    '''Show linked objects to sensor/actuator 

    :type: bool
    '''

    show_controllers_selected_objects: bool = None
    '''Show controllers of all selected objects 

    :type: bool
    '''

    show_sensors_active_object: bool = None
    '''Show sensors of active object 

    :type: bool
    '''

    show_sensors_active_states: bool = None
    '''Show only sensors connected to active states 

    :type: bool
    '''

    show_sensors_linked_controller: bool = None
    '''Show linked objects to the controller 

    :type: bool
    '''

    show_sensors_selected_objects: bool = None
    '''Show sensors of all selected objects 

    :type: bool
    '''

    def draw_handler_add(self, ):
        '''Undocumented 

        '''
        pass

    def draw_handler_remove(self, ):
        '''Undocumented 

        '''
        pass


class SpaceNLA:
    '''NLA editor space data '''

    auto_snap: typing.Union[int, str] = None
    '''Automatic time snapping settings for transformations 

    :type: typing.Union[int, str]
    '''

    dopesheet: 'DopeSheet' = None
    '''Settings for filtering animation data 

    :type: 'DopeSheet'
    '''

    show_frame_indicator: bool = None
    '''Show frame number beside the current frame indicator line 

    :type: bool
    '''

    show_local_markers: bool = None
    '''Show action-local markers on the strips, useful when synchronizing timing across strips 

    :type: bool
    '''

    show_seconds: bool = None
    '''Show timing in seconds not frames 

    :type: bool
    '''

    show_strip_curves: bool = None
    '''Show influence F-Curves on strips 

    :type: bool
    '''

    use_realtime_update: bool = None
    '''When transforming strips, changes to the animation data are flushed to other views 

    :type: bool
    '''

    def draw_handler_add(self, ):
        '''Undocumented 

        '''
        pass

    def draw_handler_remove(self, ):
        '''Undocumented 

        '''
        pass


class SpaceNodeEditor:
    '''Node editor space data '''

    backdrop_channels: typing.Union[int, str] = None
    '''Channels of the image to draw 

    :type: typing.Union[int, str]
    '''

    backdrop_x: float = None
    '''Backdrop X offset 

    :type: float
    '''

    backdrop_y: float = None
    '''Backdrop Y offset 

    :type: float
    '''

    backdrop_zoom: float = None
    '''Backdrop zoom factor 

    :type: float
    '''

    cursor_location: float = None
    '''Location for adding new nodes 

    :type: float
    '''

    edit_tree: 'NodeTree' = None
    '''Node tree being displayed and edited 

    :type: 'NodeTree'
    '''

    id: 'ID' = None
    '''Data-block whose nodes are being edited 

    :type: 'ID'
    '''

    id_from: 'ID' = None
    '''Data-block from which the edited data-block is linked 

    :type: 'ID'
    '''

    insert_offset_direction: typing.Union[int, str] = None
    '''Direction to offset nodes on insertion 

    :type: typing.Union[int, str]
    '''

    node_tree: 'NodeTree' = None
    '''Base node tree from context 

    :type: 'NodeTree'
    '''

    path: typing.List['NodeTreePath'] = None
    '''Path from the data-block to the currently edited node tree 

    :type: typing.List['NodeTreePath']
    '''

    pin: bool = None
    '''Use the pinned node tree 

    :type: bool
    '''

    shader_type: typing.Union[int, str] = None
    '''Type of data to take shader from 

    :type: typing.Union[int, str]
    '''

    show_backdrop: bool = None
    '''Use active Viewer Node output as backdrop for compositing nodes 

    :type: bool
    '''

    show_grease_pencil: bool = None
    '''Show grease pencil for this view 

    :type: bool
    '''

    texture_type: typing.Union[int, str] = None
    '''Type of data to take texture from 

    :type: typing.Union[int, str]
    '''

    tree_type: typing.Union[int, str] = None
    '''Node tree type to display and edit 

    :type: typing.Union[int, str]
    '''

    use_auto_render: bool = None
    '''Re-render and composite changed layers on 3D edits 

    :type: bool
    '''

    use_insert_offset: bool = None
    '''Automatically offset the following or previous nodes in a chain when inserting a new node 

    :type: bool
    '''

    def cursor_location_from_region(self, x: int, y: int):
        '''Set the cursor location using region coordinates 

        :param x: x, Region x coordinate 
        :type x: int
        :param y: y, Region y coordinate 
        :type y: int
        '''
        pass

    def draw_handler_add(self, ):
        '''Undocumented 

        '''
        pass

    def draw_handler_remove(self, ):
        '''Undocumented 

        '''
        pass


class SpaceNodeEditorPath:
    '''Get the node tree path as a string '''

    to_string: str = None
    '''

    :type: str
    '''

    def clear(self, ):
        '''Reset the node tree path 

        '''
        pass

    def start(self, node_tree: 'NodeTree'):
        '''Set the root node tree 

        :param node_tree: Node Tree 
        :type node_tree: 'NodeTree'
        '''
        pass

    def append(self, node_tree: 'NodeTree', node: 'Node' = None):
        '''Append a node group tree to the path 

        :param node_tree: Node Tree, Node tree to append to the node editor path 
        :type node_tree: 'NodeTree'
        :param node: Node, Group node linking to this node tree 
        :type node: 'Node'
        '''
        pass

    def pop(self, ):
        '''Remove the last node tree from the path 

        '''
        pass


class SpaceOutliner:
    '''Outliner space data '''

    display_mode: typing.Union[int, str] = None
    '''Type of information to display 

    :type: typing.Union[int, str]
    '''

    filter_text: str = None
    '''Live search filtering string 

    :type: str
    '''

    show_restrict_columns: bool = None
    '''Show column 

    :type: bool
    '''

    use_filter_case_sensitive: bool = None
    '''Only use case sensitive matches of search string 

    :type: bool
    '''

    use_filter_complete: bool = None
    '''Only use complete matches of search string 

    :type: bool
    '''

    use_sort_alpha: bool = None
    '''

    :type: bool
    '''

    def draw_handler_add(self, ):
        '''Undocumented 

        '''
        pass

    def draw_handler_remove(self, ):
        '''Undocumented 

        '''
        pass


class SpaceProperties:
    '''Properties space data '''

    align: typing.Union[int, str] = None
    '''Arrangement of the panels 

    :type: typing.Union[int, str]
    '''

    context: typing.Union[int, str] = None
    '''Type of active data to display and edit 

    :type: typing.Union[int, str]
    '''

    pin_id: 'ID' = None
    '''

    :type: 'ID'
    '''

    texture_context: typing.Union[int, str] = None
    '''Type of texture data to display and edit 

    :type: typing.Union[int, str]
    '''

    use_limited_texture_context: bool = None
    '''Use the limited version of texture user (for ‘old shading’ mode) 

    :type: bool
    '''

    use_pin_id: bool = None
    '''Use the pinned context 

    :type: bool
    '''

    def draw_handler_add(self, ):
        '''Undocumented 

        '''
        pass

    def draw_handler_remove(self, ):
        '''Undocumented 

        '''
        pass


class SpaceSequenceEditor:
    '''Sequence editor space data '''

    display_channel: int = None
    '''The channel number shown in the image preview. 0 is the result of all strips combined 

    :type: int
    '''

    display_mode: typing.Union[int, str] = None
    '''View mode to use for displaying sequencer output 

    :type: typing.Union[int, str]
    '''

    draw_overexposed: int = None
    '''Show overexposed areas with zebra stripes 

    :type: int
    '''

    grease_pencil: 'GreasePencil' = None
    '''Grease pencil data for this space 

    :type: 'GreasePencil'
    '''

    overlay_type: typing.Union[int, str] = None
    '''Overlay draw type 

    :type: typing.Union[int, str]
    '''

    preview_channels: typing.Union[int, str] = None
    '''Channels of the preview to draw 

    :type: typing.Union[int, str]
    '''

    proxy_render_size: typing.Union[int, str] = None
    '''Draw preview using full resolution or different proxy resolutions 

    :type: typing.Union[int, str]
    '''

    show_backdrop: bool = None
    '''Display result under strips 

    :type: bool
    '''

    show_frame_indicator: bool = None
    '''Show frame number beside the current frame indicator line 

    :type: bool
    '''

    show_frames: bool = None
    '''Draw frames rather than seconds 

    :type: bool
    '''

    show_grease_pencil: bool = None
    '''Show grease pencil for this view 

    :type: bool
    '''

    show_metadata: bool = None
    '''Show metadata of first visible strip 

    :type: bool
    '''

    show_safe_areas: bool = None
    '''Show TV title safe and action safe areas in preview 

    :type: bool
    '''

    show_safe_center: bool = None
    '''Show safe areas to fit content in a different aspect ratio 

    :type: bool
    '''

    show_seconds: bool = None
    '''Show timing in seconds not frames 

    :type: bool
    '''

    show_separate_color: bool = None
    '''Separate color channels in preview 

    :type: bool
    '''

    show_strip_offset: bool = None
    '''Display strip in/out offsets 

    :type: bool
    '''

    use_marker_sync: bool = None
    '''Transform markers as well as strips 

    :type: bool
    '''

    view_type: typing.Union[int, str] = None
    '''Type of the Sequencer view (sequencer, preview or both) 

    :type: typing.Union[int, str]
    '''

    waveform_draw_type: typing.Union[int, str] = None
    '''How Waveforms are drawn 

    :type: typing.Union[int, str]
    '''

    def draw_handler_add(self, ):
        '''Undocumented 

        '''
        pass

    def draw_handler_remove(self, ):
        '''Undocumented 

        '''
        pass


class SpaceTextEditor:
    '''Text editor space data '''

    find_text: str = None
    '''Text to search for with the find tool 

    :type: str
    '''

    font_size: int = None
    '''Font size to use for displaying the text 

    :type: int
    '''

    margin_column: int = None
    '''Column number to show right margin at 

    :type: int
    '''

    replace_text: str = None
    '''Text to replace selected text with using the replace tool 

    :type: str
    '''

    show_line_highlight: bool = None
    '''Highlight the current line 

    :type: bool
    '''

    show_line_numbers: bool = None
    '''Show line numbers next to the text 

    :type: bool
    '''

    show_margin: bool = None
    '''Show right margin 

    :type: bool
    '''

    show_syntax_highlight: bool = None
    '''Syntax highlight for scripting 

    :type: bool
    '''

    show_word_wrap: bool = None
    '''Wrap words if there is not enough horizontal space 

    :type: bool
    '''

    tab_width: int = None
    '''Number of spaces to display tabs with 

    :type: int
    '''

    text: 'Text' = None
    '''Text displayed and edited in this space 

    :type: 'Text'
    '''

    top: int = None
    '''Top line visible 

    :type: int
    '''

    use_find_all: bool = None
    '''Search in all text data-blocks, instead of only the active one 

    :type: bool
    '''

    use_find_wrap: bool = None
    '''Search again from the start of the file when reaching the end 

    :type: bool
    '''

    use_live_edit: bool = None
    '''Run python while editing 

    :type: bool
    '''

    use_match_case: bool = None
    '''Search string is sensitive to uppercase and lowercase letters 

    :type: bool
    '''

    use_overwrite: bool = None
    '''Overwrite characters when typing rather than inserting them 

    :type: bool
    '''

    visible_lines: int = None
    '''Amount of lines that can be visible in current editor 

    :type: int
    '''

    def region_location_from_cursor(self, line: int, column: int) -> int:
        '''Retrieve the region position from the given line and character position 

        :param line: Line, Line index 
        :type line: int
        :param column: Column, Column index 
        :type column: int
        :rtype: int
        :return:  Region coordinates 
        '''
        pass

    def draw_handler_add(self, ):
        '''Undocumented 

        '''
        pass

    def draw_handler_remove(self, ):
        '''Undocumented 

        '''
        pass


class SpaceTimeline:
    '''Timeline editor space data '''

    cache_cloth: bool = None
    '''Show the active object’s cloth point cache 

    :type: bool
    '''

    cache_dynamicpaint: bool = None
    '''Show the active object’s Dynamic Paint cache 

    :type: bool
    '''

    cache_particles: bool = None
    '''Show the active object’s particle point cache 

    :type: bool
    '''

    cache_rigidbody: bool = None
    '''Show the active object’s Rigid Body cache 

    :type: bool
    '''

    cache_smoke: bool = None
    '''Show the active object’s smoke cache 

    :type: bool
    '''

    cache_softbody: bool = None
    '''Show the active object’s softbody point cache 

    :type: bool
    '''

    show_cache: bool = None
    '''Show the status of cached frames in the timeline 

    :type: bool
    '''

    show_frame_indicator: bool = None
    '''Show frame number beside the current frame indicator line 

    :type: bool
    '''

    show_seconds: bool = None
    '''Show timing in seconds not frames 

    :type: bool
    '''

    def draw_handler_add(self, ):
        '''Undocumented 

        '''
        pass

    def draw_handler_remove(self, ):
        '''Undocumented 

        '''
        pass


class SpaceUVEditor:
    '''UV editor data for the image editor space '''

    draw_stretch_type: typing.Union[int, str] = None
    '''Type of stretch to draw 

    :type: typing.Union[int, str]
    '''

    edge_draw_type: typing.Union[int, str] = None
    '''Draw type for drawing UV edges 

    :type: typing.Union[int, str]
    '''

    lock_bounds: bool = None
    '''Constraint to stay within the image bounds while editing 

    :type: bool
    '''

    other_uv_filter: typing.Union[int, str] = None
    '''Filter applied on the other object’s UV to limit displayed 

    :type: typing.Union[int, str]
    '''

    show_faces: bool = None
    '''Draw faces over the image 

    :type: bool
    '''

    show_metadata: bool = None
    '''Draw metadata properties of the image 

    :type: bool
    '''

    show_modified_edges: bool = None
    '''Draw edges after modifiers are applied 

    :type: bool
    '''

    show_normalized_coords: bool = None
    '''Display UV coordinates from 0.0 to 1.0 rather than in pixels 

    :type: bool
    '''

    show_other_objects: bool = None
    '''Draw other selected objects that share the same image 

    :type: bool
    '''

    show_smooth_edges: bool = None
    '''Draw UV edges anti-aliased 

    :type: bool
    '''

    show_stretch: bool = None
    '''Draw faces colored according to the difference in shape between UVs and their 3D coordinates (blue for low distortion, red for high distortion) 

    :type: bool
    '''

    show_texpaint: bool = None
    '''Draw overlay of texture paint uv layer 

    :type: bool
    '''

    sticky_select_mode: typing.Union[int, str] = None
    '''Automatically select also UVs sharing the same vertex as the ones being selected 

    :type: typing.Union[int, str]
    '''

    use_live_unwrap: bool = None
    '''Continuously unwrap the selected UV island while transforming pinned vertices 

    :type: bool
    '''

    use_snap_to_pixels: bool = None
    '''Snap UVs to pixel locations while editing 

    :type: bool
    '''


class SpaceUserPreferences:
    '''User preferences space data '''

    filter_text: str = None
    '''Search term for filtering in the UI 

    :type: str
    '''

    filter_type: typing.Union[int, str] = None
    '''Filter method 

    :type: typing.Union[int, str]
    '''

    def draw_handler_add(self, ):
        '''Undocumented 

        '''
        pass

    def draw_handler_remove(self, ):
        '''Undocumented 

        '''
        pass


class SpaceView3D:
    '''3D View space data '''

    active_layer: int = None
    '''Active 3D view layer index 

    :type: int
    '''

    background_images: typing.List['BackgroundImage'] = None
    '''List of background images 

    :type: typing.List['BackgroundImage']
    '''

    camera: 'Object' = None
    '''Active camera used in this view (when unlocked from the scene’s active camera) 

    :type: 'Object'
    '''

    clip_end: float = None
    '''3D View far clipping distance 

    :type: float
    '''

    clip_start: float = None
    '''3D View near clipping distance (perspective view only) 

    :type: float
    '''

    current_orientation: 'TransformOrientation' = None
    '''Current transformation orientation 

    :type: 'TransformOrientation'
    '''

    cursor_location: float = None
    '''3D cursor location for this view (dependent on local view setting) 

    :type: float
    '''

    fx_settings: 'GPUFXSettings' = None
    '''Options used for real time compositing 

    :type: 'GPUFXSettings'
    '''

    grid_lines: int = None
    '''Number of grid lines to display in perspective view 

    :type: int
    '''

    grid_scale: float = None
    '''Distance between 3D View grid lines 

    :type: float
    '''

    grid_scale_unit: float = None
    '''Grid cell size scaled by scene unit system settings 

    :type: float
    '''

    grid_subdivisions: int = None
    '''Number of subdivisions between grid lines 

    :type: int
    '''

    layers: bool = None
    '''Layers visible in this 3D View 

    :type: bool
    '''

    layers_local_view: bool = None
    '''Local view layers visible in this 3D View 

    :type: bool
    '''

    layers_used: bool = None
    '''Layers that contain something 

    :type: bool
    '''

    lens: float = None
    '''Viewport lens angle 

    :type: float
    '''

    local_view: 'SpaceView3D' = None
    '''Display an isolated sub-set of objects, apart from the scene visibility 

    :type: 'SpaceView3D'
    '''

    lock_bone: str = None
    '''3D View center is locked to this bone’s position 

    :type: str
    '''

    lock_camera: bool = None
    '''Enable view navigation within the camera view 

    :type: bool
    '''

    lock_camera_and_layers: bool = None
    '''Use the scene’s active camera and layers in this view, rather than local layers 

    :type: bool
    '''

    lock_cursor: bool = None
    '''3D View center is locked to the cursor’s position 

    :type: bool
    '''

    lock_object: 'Object' = None
    '''3D View center is locked to this object’s position 

    :type: 'Object'
    '''

    matcap_icon: typing.Union[int, str] = None
    '''Image to use for Material Capture, active objects only 

    :type: typing.Union[int, str]
    '''

    pivot_point: typing.Union[int, str] = None
    '''Pivot center for rotation/scaling 

    :type: typing.Union[int, str]
    '''

    region_3d: 'RegionView3D' = None
    '''3D region in this space, in case of quad view the camera region 

    :type: 'RegionView3D'
    '''

    region_quadviews: typing.List['RegionView3D'] = None
    '''3D regions (the third one defines quad view settings, the fourth one is same as ‘region_3d’) 

    :type: typing.List['RegionView3D']
    '''

    render_border_max_x: float = None
    '''Maximum X value for the render border 

    :type: float
    '''

    render_border_max_y: float = None
    '''Maximum Y value for the render border 

    :type: float
    '''

    render_border_min_x: float = None
    '''Minimum X value for the render border 

    :type: float
    '''

    render_border_min_y: float = None
    '''Minimum Y value for the render border 

    :type: float
    '''

    show_all_objects_origin: bool = None
    '''Show the object origin center dot for all (selected and unselected) objects 

    :type: bool
    '''

    show_axis_x: bool = None
    '''Show the X axis line in perspective view 

    :type: bool
    '''

    show_axis_y: bool = None
    '''Show the Y axis line in perspective view 

    :type: bool
    '''

    show_axis_z: bool = None
    '''Show the Z axis line in perspective view 

    :type: bool
    '''

    show_backface_culling: bool = None
    '''Use back face culling to hide the back side of faces 

    :type: bool
    '''

    show_background_images: bool = None
    '''Display reference images behind objects in the 3D View 

    :type: bool
    '''

    show_bundle_names: bool = None
    '''Show names for reconstructed tracks objects 

    :type: bool
    '''

    show_camera_path: bool = None
    '''Show reconstructed camera path 

    :type: bool
    '''

    show_floor: bool = None
    '''Show the ground plane grid in perspective view 

    :type: bool
    '''

    show_grease_pencil: bool = None
    '''Show grease pencil for this view 

    :type: bool
    '''

    show_manipulator: bool = None
    '''Use a 3D manipulator widget for controlling transforms 

    :type: bool
    '''

    show_occlude_wire: bool = None
    '''Use hidden wireframe display 

    :type: bool
    '''

    show_only_render: bool = None
    '''Display only objects which will be rendered 

    :type: bool
    '''

    show_outline_selected: bool = None
    '''Show an outline highlight around selected objects in non-wireframe views 

    :type: bool
    '''

    show_reconstruction: bool = None
    '''Display reconstruction data from active movie clip 

    :type: bool
    '''

    show_relationship_lines: bool = None
    '''Show dashed lines indicating parent or constraint relationships 

    :type: bool
    '''

    show_stereo_3d_cameras: bool = None
    '''Show the left and right cameras 

    :type: bool
    '''

    show_stereo_3d_convergence_plane: bool = None
    '''Show the stereo 3d convergence plane 

    :type: bool
    '''

    show_stereo_3d_volume: bool = None
    '''Show the stereo 3d frustum volume 

    :type: bool
    '''

    show_textured_shadeless: bool = None
    '''Show shadeless texture without lighting in textured draw mode 

    :type: bool
    '''

    show_textured_solid: bool = None
    '''Display face-assigned textures in solid view 

    :type: bool
    '''

    show_world: bool = None
    '''Display world colors in the background 

    :type: bool
    '''

    stereo_3d_camera: typing.Union[int, str] = None
    '''

    :type: typing.Union[int, str]
    '''

    stereo_3d_convergence_plane_alpha: float = None
    '''Opacity (alpha) of the convergence plane 

    :type: float
    '''

    stereo_3d_eye: typing.Union[int, str] = None
    '''Current stereo eye being drawn 

    :type: typing.Union[int, str]
    '''

    stereo_3d_volume_alpha: float = None
    '''Opacity (alpha) of the cameras’ frustum volume 

    :type: float
    '''

    tracks_draw_size: float = None
    '''Display size of tracks from reconstructed data 

    :type: float
    '''

    tracks_draw_type: typing.Union[int, str] = None
    '''Viewport display style for tracks 

    :type: typing.Union[int, str]
    '''

    transform_manipulators: typing.Set[typing.Union[int, str]] = None
    '''Transformation manipulators 

    :type: typing.Set[typing.Union[int, str]]
    '''

    transform_orientation: typing.Union[int, str] = None
    '''Transformation orientation 

    :type: typing.Union[int, str]
    '''

    use_matcap: bool = None
    '''Active Objects draw images mapped on normals, enhancing Solid Draw Mode 

    :type: bool
    '''

    use_occlude_geometry: bool = None
    '''Limit selection to visible (clipped with depth buffer) 

    :type: bool
    '''

    use_pivot_point_align: bool = None
    '''Manipulate center points (object, pose and weight paint mode only) 

    :type: bool
    '''

    use_render_border: bool = None
    '''Use a region within the frame size for rendered viewport (when not viewing through the camera) 

    :type: bool
    '''

    viewport_shade: typing.Union[int, str] = None
    '''Method to display/shade objects in the 3D View 

    :type: typing.Union[int, str]
    '''

    def draw_handler_add(self, ):
        '''Undocumented 

        '''
        pass

    def draw_handler_remove(self, ):
        '''Undocumented 

        '''
        pass


class Speaker:
    '''Speaker data-block for 3D audio speaker objects '''

    animation_data: 'AnimData' = None
    '''Animation data for this data-block 

    :type: 'AnimData'
    '''

    attenuation: float = None
    '''How strong the distance affects volume, depending on distance model 

    :type: float
    '''

    cone_angle_inner: float = None
    '''Angle of the inner cone, in degrees, inside the cone the volume is 100 % 

    :type: float
    '''

    cone_angle_outer: float = None
    '''Angle of the outer cone, in degrees, outside this cone the volume is the outer cone volume, between inner and outer cone the volume is interpolated 

    :type: float
    '''

    cone_volume_outer: float = None
    '''Volume outside the outer cone 

    :type: float
    '''

    distance_max: float = None
    '''Maximum distance for volume calculation, no matter how far away the object is 

    :type: float
    '''

    distance_reference: float = None
    '''Reference distance at which volume is 100 % 

    :type: float
    '''

    muted: bool = None
    '''Mute the speaker 

    :type: bool
    '''

    pitch: float = None
    '''Playback pitch of the sound 

    :type: float
    '''

    relative: bool = None
    '''Whether the source is relative to the camera or not 

    :type: bool
    '''

    sound: 'Sound' = None
    '''Sound data-block used by this speaker 

    :type: 'Sound'
    '''

    volume: float = None
    '''How loud the sound is 

    :type: float
    '''

    volume_max: float = None
    '''Maximum volume, no matter how near the object is 

    :type: float
    '''

    volume_min: float = None
    '''Minimum volume, no matter how far away the object is 

    :type: float
    '''


class SpeedControlSequence:
    '''Sequence strip to control the speed of other strips '''

    input_1: 'Sequence' = None
    '''First input for the effect strip 

    :type: 'Sequence'
    '''

    input_count: int = None
    '''

    :type: int
    '''

    multiply_speed: float = None
    '''Multiply the resulting speed after the speed factor 

    :type: float
    '''

    scale_to_length: bool = None
    '''Scale values from 0.0 to 1.0 to target sequence length 

    :type: bool
    '''

    use_as_speed: bool = None
    '''Interpret the value as speed instead of a frame number 

    :type: bool
    '''


class Spline:
    '''Element of a curve, either NURBS, Bezier or Polyline or a character with text objects '''

    bezier_points: typing.List['BezierSplinePoint'] = None
    '''Collection of points for Bezier curves only 

    :type: typing.List['BezierSplinePoint']
    '''

    character_index: int = None
    '''Location of this character in the text data (only for text curves) 

    :type: int
    '''

    hide: bool = None
    '''Hide this curve in Edit mode 

    :type: bool
    '''

    material_index: int = None
    '''

    :type: int
    '''

    order_u: int = None
    '''NURBS order in the U direction (for splines and surfaces, higher values let points influence a greater area) 

    :type: int
    '''

    order_v: int = None
    '''NURBS order in the V direction (for surfaces only, higher values let points influence a greater area) 

    :type: int
    '''

    point_count_u: int = None
    '''Total number points for the curve or surface in the U direction 

    :type: int
    '''

    point_count_v: int = None
    '''Total number points for the surface on the V direction 

    :type: int
    '''

    points: typing.List['SplinePoints'] = None
    '''Collection of points that make up this poly or nurbs spline 

    :type: typing.List['SplinePoints']
    '''

    radius_interpolation: typing.Union[int, str] = None
    '''The type of radius interpolation for Bezier curves 

    :type: typing.Union[int, str]
    '''

    resolution_u: int = None
    '''Curve or Surface subdivisions per segment 

    :type: int
    '''

    resolution_v: int = None
    '''Surface subdivisions per segment 

    :type: int
    '''

    tilt_interpolation: typing.Union[int, str] = None
    '''The type of tilt interpolation for 3D, Bezier curves 

    :type: typing.Union[int, str]
    '''

    type: typing.Union[int, str] = None
    '''The interpolation type for this curve element 

    :type: typing.Union[int, str]
    '''

    use_bezier_u: bool = None
    '''Make this nurbs curve or surface act like a Bezier spline in the U direction (Order U must be 3 or 4, Cyclic U must be disabled) 

    :type: bool
    '''

    use_bezier_v: bool = None
    '''Make this nurbs surface act like a Bezier spline in the V direction (Order V must be 3 or 4, Cyclic V must be disabled) 

    :type: bool
    '''

    use_cyclic_u: bool = None
    '''Make this curve or surface a closed loop in the U direction 

    :type: bool
    '''

    use_cyclic_v: bool = None
    '''Make this surface a closed loop in the V direction 

    :type: bool
    '''

    use_endpoint_u: bool = None
    '''Make this nurbs curve or surface meet the endpoints in the U direction (Cyclic U must be disabled) 

    :type: bool
    '''

    use_endpoint_v: bool = None
    '''Make this nurbs surface meet the endpoints in the V direction (Cyclic V must be disabled) 

    :type: bool
    '''

    use_smooth: bool = None
    '''Smooth the normals of the surface or beveled curve 

    :type: bool
    '''


class SplineBezierPoints:
    '''Collection of spline Bezier points '''

    def add(self, count: int = 1):
        '''Add a number of points to this spline 

        :param count: Number, Number of points to add to the spline 
        :type count: int
        '''
        pass


class SplineIKConstraint:
    '''Align ‘n’ bones along a curve '''

    bulge: float = None
    '''Factor between volume variation and stretching 

    :type: float
    '''

    bulge_max: float = None
    '''Maximum volume stretching factor 

    :type: float
    '''

    bulge_min: float = None
    '''Minimum volume stretching factor 

    :type: float
    '''

    bulge_smooth: float = None
    '''Strength of volume stretching clamping 

    :type: float
    '''

    chain_count: int = None
    '''How many bones are included in the chain 

    :type: int
    '''

    joint_bindings: float = None
    '''(EXPERIENCED USERS ONLY) The relative positions of the joints along the chain, as percentages 

    :type: float
    '''

    target: 'Object' = None
    '''Curve that controls this relationship 

    :type: 'Object'
    '''

    use_bulge_max: bool = None
    '''Use upper limit for volume variation 

    :type: bool
    '''

    use_bulge_min: bool = None
    '''Use lower limit for volume variation 

    :type: bool
    '''

    use_chain_offset: bool = None
    '''Offset the entire chain relative to the root joint 

    :type: bool
    '''

    use_curve_radius: bool = None
    '''Average radius of the endpoints is used to tweak the X and Z Scaling of the bones, on top of XZ Scale mode 

    :type: bool
    '''

    use_even_divisions: bool = None
    '''Ignore the relative lengths of the bones when fitting to the curve 

    :type: bool
    '''

    use_y_stretch: bool = None
    '''Stretch the Y axis of the bones to fit the curve 

    :type: bool
    '''

    xz_scale_mode: typing.Union[int, str] = None
    '''Method used for determining the scaling of the X and Z axes of the bones 

    :type: typing.Union[int, str]
    '''


class SplinePoint:
    '''Spline point without handles '''

    co: float = None
    '''Point coordinates 

    :type: float
    '''

    hide: bool = None
    '''Visibility status 

    :type: bool
    '''

    radius: float = None
    '''Radius for beveling 

    :type: float
    '''

    select: bool = None
    '''Selection status 

    :type: bool
    '''

    tilt: float = None
    '''Tilt in 3D View 

    :type: float
    '''

    weight: float = None
    '''NURBS weight 

    :type: float
    '''

    weight_softbody: float = None
    '''Softbody goal weight 

    :type: float
    '''


class SplinePoints:




