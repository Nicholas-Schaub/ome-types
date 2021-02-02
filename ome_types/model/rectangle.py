from ome_types.dataclasses import EMPTY, ome_dataclass

from .shape import Shape


@ome_dataclass
class Rectangle(Shape):
    """A simple rectangle object.

    If rotation is required apply a transformation at the Shape level.

    Parameters
    ----------
    height : float
        The height of the rectangle.
    width : float
        The width of the rectangle.
    x : float
        The X value of the left edge or the rectangle.
    y : float
        The y value of the top edge or the rectangle.
    annotation_ref : AnnotationRef, optional
    fill_color : Color, optional
        The color of the fill - encoded as RGBA The value "-1" is #FFFFFFFF so
        solid white (it is a signed 32 bit value) NOTE: Prior to the 2012-06
        schema the default value was incorrect and produced a transparent red
        not solid white.
    fill_rule : FillRule, optional
    font_family : FontFamily, optional
    font_size : NonNegativeInt, optional
        Size of the font. Units are set by FontSizeUnit.
    font_size_unit : UnitsLength, optional
        The units used for the font size.
    font_style : FontStyle, optional
    id : ShapeID
    locked : bool, optional
        Controls whether the shape is locked and read only, true is locked,
        false is editable.
    stroke_color : Color, optional
        The color of the stroke  - encoded as RGBA The value "-1" is #FFFFFFFF
        so solid white (it is a signed 32 bit value) NOTE: Prior to the
        2012-06 schema the default value was incorrect and produced a
        transparent red not solid white.
    stroke_dash_array : str, optional
        e.g. "none", "10 20 30 10"
    stroke_width : float, optional
        The width of the stroke. Units are set by StrokeWidthUnit.
    stroke_width_unit : UnitsLength, optional
        The units used for the stroke width.
    text : str, optional
    the_c : NonNegativeInt, optional
        The channel the ROI applies to. If not specified then the ROI applies
        to all the channels of the image. This is numbered from 0.
    the_t : NonNegativeInt, optional
        The timepoint the ROI applies to. If not specified then the ROI
        applies to all the timepoints of the image. This is numbered from 0.
    the_z : NonNegativeInt, optional
        The z-section the ROI applies to. If not specified then the ROI
        applies to all the z-sections of the image. This is numbered from 0.
    transform : AffineTransform, optional
        This is a matrix used to transform the shape. The element has 6
        xsd:float attributes. If the element is present then all 6 values must
        be included.
    """

    height: float = EMPTY  # type: ignore
    width: float = EMPTY  # type: ignore
    x: float = EMPTY  # type: ignore
    y: float = EMPTY  # type: ignore
