# AUTO GENERATED FILE - DO NOT EDIT

export dummyinclude

"""
    dummyinclude(;kwargs...)

A DummyInclude component.
MyTextInput is an example component.
It takes a property, `label`, and
displays it.
It renders an input with the property `value`
which is editable by the user.
Keyword arguments:
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `label` (String; optional): The label used to show above of the input
- `value` (String; optional): The value used to set the default value for the input
"""
function dummyinclude(; kwargs...)
        available_props = Symbol[:id, :label, :value]
        wild_props = Symbol[]
        return Component("dummyinclude", "DummyInclude", "dummy_include", available_props, wild_props; kwargs...)
end

