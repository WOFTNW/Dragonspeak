# Dragonspeak

Dragonspeak is a Minecraft resource pack for [Wings of Fire: The New World](https://woftnw.org). It was originally created by Stonley890 and Starinquirer and is now maintained by the WOFTNW staff team. It's primary feature is its collection of custom wings, but it also has smaller WOF-inspired changes as well as ability icons for [Elytras of Fire](https://github.com/iHeronGH/Elytras-of-Fire). You can read more about Dragonspeak on the [WOFTNW Wiki](https://wiki.woftnw.org/wiki/Dragonspeak).

## Contributing

Thanks for you interest in contributing! Please keep in mind the following when making contributions:

### Designing Wings

Elytras require two textures. One is the equipment model that appears on the player. This should be designed first. See the guide texture below.

![guide image](assets/minecraft/textures/entity/equipment/wings/guide.png)

Use this alongside the already-existing elytra textures to design your texture.

### Implementing Wings

Included in this repository is a Python script, `create_wings_gui.py`. You can use this to quickly implement wings into the existing structure.

1. **Select Item PNG File.** This is the square image that appears in the inventory.
2. **Select Equipment PNG File.** This is the model file that the player wears.
3. **Enter Item Name.** The item name is the internal name of the wing set. It should be snake_case, with no capital letters and underscores between words.
4. **Enter Subpath.** This is where the wings will be stored. The following paths exist:
   - `tribes`: contains a folder for each tribe, each of which contains tribe-specific wings.
   - `staff`: contains staff wings.
   - `special`: contains special wings.

You can test your wings in-game by running the command:

```mcfunction
/give @s elytra[equippable={slot:"chest",model:"minecraft:<subpath>/<itemname>"}]
```
