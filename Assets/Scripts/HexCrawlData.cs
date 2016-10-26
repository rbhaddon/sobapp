using UnityEngine;
using System.Collections;
using System;
using System.Collections.Generic;

/*
 * Town Traits
 */
[Serializable]
public class TraitChart
{
	public List<TraitEntry> array;
}

[Serializable]
public struct TraitEntry
{
	public int roll;
	public TownTrait data;
}
	
[Serializable]
public class TownTrait
{
	public string name;
	public string description;

	public TownTrait() {
		name = "";
		description = "";
	}
}

/*
 * Ailments (Madnesses, Injuries, and Mutations)
 */
[Serializable]
public class AilmentChart
{
	public List<AilmentEntry> array;
}

[Serializable]
public struct AilmentEntry
{
	public int roll;
	public Ailment data;
}

[Serializable]
public class Ailment
{
	public string name;
	public string flavor;
	public string effect;
}

/*
 * Terrain Encounters
 */
[Serializable]
public struct TerrainEncounter
{
	public string name;
	public List<string> keywords;
	public string description;
}

/*
 * Jobs
 */
[Serializable]
public class JobsBoard
{
	public string title;
	public List<string> keywords;
	public string background;
	public string location;
	public int time;
	public string description;
	public string reward;
	public string failure;
}