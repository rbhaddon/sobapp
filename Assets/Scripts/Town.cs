//using UnityEngine;
using System;
using System.Collections;
using System.Collections.Generic;

using HexCrawlConstants;

[Serializable]
public class Town
{
	public string name;
	public TownData.Status status;
	public int size; // should be a property
	public int max_size;
	public int max_builtins;
	public string type;
	public TownData.Trait trait;
	public JobData[] jobs;
	public TownData.BuiltInType[] builtIns;
	public TownData.LocationType[] locations;
	public string[] keywords;

	public Town()
	{
		name = "";
		status = TownData.Status.Okay;
		size = Roll.D8 ();
		max_size = TownData.MAX_LOCATIONS;
		max_builtins = TownData.MAX_BUILTINS;
		type = GetTownType ();
		trait = TownData.Trait.Trait1;
		jobs = new JobData [TownData.MAX_BUILTINS];
		builtIns = new TownData.BuiltInType[] {TownData.BuiltInType.Campsite, TownData.BuiltInType.Hotel};
		locations = new TownData.LocationType [size];
		keywords = new string[]{ "Town" };
	}

	public static Town Create()
	{
		Town town = new Town ();
		town.type = TownData.Types [Roll.D6 () + Roll.D6 () - 2];
		town.size = Roll.D8 ();

		return town;
	}

	// Return any town type
	public static string GetTownType()
	{
		int roll2d6 = Roll.D6() + Roll.D6();
		return TownData.Types [roll2d6];
	}

	// Return town types other than Rail or River, since those are designated by the map
	public static string GetNonGeographicTownType()
	{
		string type = "";
		do {
			type = GetTownType();
		} while (TownData.GeographicTypes.ContainsValue(type));

		return type;
	}
}

[Serializable]
public class JobData
{
	public int jobNumber;
	public int? timeRemaining = null;
	public string startLocation = "";
	public string turnInLocation = "";
	public TownData.JobState jobState;	
}

[Serializable]
public class LocationData
{
	public string locationId;
	public TownData.LocationType loctionType;
}