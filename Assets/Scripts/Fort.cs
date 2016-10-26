using UnityEngine;
using System.Collections;
using System;
using HexCrawlConstants;

[Serializable]
public class Fort
{
	public string name;
	public TownData.Status status;
	public int size; // should be a property
	public int max_size;
	public int max_builtins;
	public string type;
	public TownTrait trait;
	public JobData[] jobs;
	public TownData.BuiltInType[] builtIns;
	public int[] locations;

	public Fort()
	{
		name = "";
		status = TownData.Status.Okay;
		size = 4;
		max_size = 4;
		max_builtins = TownData.MAX_BUILTINS;
		//type = GetType ();
		trait = GameControl.gameData.townTraits[Roll.D36 ()];
		jobs = new JobData [TownData.MAX_BUILTINS];
		builtIns = new TownData.BuiltInType[] {TownData.BuiltInType.Campsite, TownData.BuiltInType.Hotel};
	}

	public static Town Create()
	{
		Town town = new Town ();
		town.type = TownData.Types [Roll.D6 () + Roll.D6 () - 2];
		town.size = Roll.D8 ();

		return town;
	}
}
/*
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
*/