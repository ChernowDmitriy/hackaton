import typing

from pydantic import BaseModel


class ItemUnomSchemaOutput(BaseModel):
    statusMkd: typing.Optional[int]
    floor_count: typing.Optional[int]
    year: typing.Optional[int]  # год постройки
    total_area: typing.Optional[int]
    project_series: typing.Optional[int]
    materialWall: typing.Optional[int]
    count_passenger_elevators: typing.Optional[int]
    count_cargo_passenger_elevators: typing.Optional[int]
    total_area_of_residential_premises: typing.Optional[int]
    total_area_of_non_residential_premises: typing.Optional[int]
    number_of_entrances: typing.Optional[int]
    number_of_freight_elevators: typing.Optional[int]
    type_of_housing_stock: typing.Optional[int]
    a_sign_of_a_building_accident: typing.Optional[int]
    apartments_number: typing.Optional[int]
    materialRoof: typing.Optional[int]
    mcd_management_status: typing.Optional[int]
    appointment: typing.Optional[str]
    the_order_of_roof_cleaning: typing.Optional[int]
    construction_volume: typing.Optional[int]
    object_wear_and_tear: typing.Optional[str]
    reason_change_status: typing.Optional[str]
    parent_id: typing.Optional[int]
    year_reconstruction: typing.Optional[int]
    social_object_type: typing.Optional[str]
    ownership_form: typing.Optional[str]
    energy_efficiency_class: typing.Optional[str]


class UpdateItemUnomSchemaOutput(ItemUnomSchemaOutput):
    pass
