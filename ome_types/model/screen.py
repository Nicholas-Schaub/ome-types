from dataclasses import field
from typing import List, Optional

from ome_types.dataclasses import AUTO_SEQUENCE, EMPTY, ome_dataclass

from .annotation_ref import AnnotationRef
from .reagent import Reagent
from .reference import Reference
from .simple_types import PlateID, ScreenID


@ome_dataclass
class PlateRef(Reference):
    """The PlateRef element is a reference to a Plate element.

    Screen elements may have one or more PlateRef elements to define the plates
    that are part of the screen. Plates may belong to more than one screen.

    Parameters
    ----------
    id : PlateID
    """

    id: PlateID = EMPTY  # type: ignore


@ome_dataclass
class Screen:
    """The Screen element is a grouping for Plates.

    The required attribute is the Screen's Name and ID - both must be unique
    within the document. The Screen element may contain an ExternalRef attribute
    that refers to an external database. A description of the screen may be
    specified in the Description element. Screens may contain overlapping sets of
    Plates i.e.      Screens and Plates have a many-to-many relationship. Plates
    contain one or more ScreenRef elements to specify what screens they belong to.

    Parameters
    ----------
    annotation_ref : AnnotationRef, optional
    description : str, optional
        A description for the screen.
    id : ScreenID
    name : str, optional
    plate_ref : PlateRef, optional
        The PlateRef element is a reference to a Plate element. Screen
        elements may have one or more PlateRef elements to define the plates
        that are part of the screen. Plates may belong to more than one
        screen.
    protocol_description : str, optional
        A description of the screen protocol; may contain very detailed
        information to reproduce some of that found in a screening database.
    protocol_identifier : str, optional
        A pointer to an externally defined protocol, usually in a screening
        database.
    reagent_set_description : str, optional
        A description of the set of reagents; may contain very detailed
        information to reproduce some of that information found in a screening
        database.
    reagent_set_identifier : str, optional
        A pointer to an externally defined set of reagents, usually in a
        screening database/automation database.
    reagents : Reagent, optional
    type : str, optional
        A human readable identifier for the screen type; e.g. RNAi, cDNA,
        SiRNA, etc. This string is likely to become an enumeration in future
        releases.
    """

    annotation_ref: List[AnnotationRef] = field(default_factory=list)
    description: Optional[str] = None
    id: ScreenID = AUTO_SEQUENCE  # type: ignore
    name: Optional[str] = None
    plate_ref: List[PlateRef] = field(default_factory=list)
    protocol_description: Optional[str] = None
    protocol_identifier: Optional[str] = None
    reagent_set_description: Optional[str] = None
    reagent_set_identifier: Optional[str] = None
    reagents: List[Reagent] = field(default_factory=list)
    type: Optional[str] = None
