using UnityEngine;
using System;
using System.Collections;
using System.Collections.Generic;

using HexCrawlConstants;

[Serializable]
public class GameData {
	
	public string posseName;
	public string[] players;
	public string world;
	public JobData[] jobs;
	public Dictionary<int, Town> towns;

	public GameData()
	{
		posseName = "";
		world = "";
		jobs = new JobData [100];
		towns = new Dictionary<int, Town>();
	}

	// This needs to be world-specific at some point
	public void GenerateTowns()
	{
		towns.Clear ();

		foreach (KeyValuePair<int, string> entry in TownData.Names)
		{
			Debug.Log ("Generating \"" + entry.Value + "\"");
			Town town = new Town ();
			town.name = entry.Value;
			switch ( entry.Value )
			{
			case "Brimstone":
				town.status = TownData.Status.Destroyed;
				break;
			case "Fort Burk":
			case "Fort Lopez":
			case "Fort Landy":
				town.max_size = 4;
				town.max_builtins = 1;
				town.builtIns = new TownData.BuiltInType[]{ TownData.BuiltInType.Campsite };
				town.locations = new TownData.LocationType [UnityEngine.Random.Range (0, town.max_size) + 1];
				town.locations [0] = TownData.LocationType.FrontierOutpost;
				town.trait = TownData.Trait.None;
				town.keywords = new string[] { "Fort", "Law" };
				town.type = Town.GetNonGeographicTownType ();
				break;
			case "Hill Town":
			case "Larberg's Landing":
			case "Wilshin's Lodge":
			case "Seto's Mill":
				town.type = "River Town";
				break;
			case "Serafin":
			case "Fringe":
			case "Wood's End":
			case "Stone's Crossing":
			case "Lestina":
			case "Last Chance":
				town.type = "Rail Town";
				break;
			case "Conradt's Claim":
				town.type = "River Town";
				town.keywords = new string[] { "Camp" };
				town.max_size = 2;
				town.max_builtins = 1;
				town.builtIns = new TownData.BuiltInType[]{ TownData.BuiltInType.Campsite };
				Debug.Log ("****" + town.name + town.max_size.ToString ());
				break;
			case "Flamme's Folly":
				town.type = Town.GetNonGeographicTownType ();
				town.keywords = new string[] { "Camp" };
				town.max_size = 2;
				town.max_builtins = 1;
				town.builtIns = new TownData.BuiltInType[]{ TownData.BuiltInType.Campsite };
				Debug.Log ("****" + town.name + town.max_size.ToString ());
				break;
			case "San Miguel Mission":
				town.type = "River Town";
				town.max_size = 1;
				town.max_builtins = 1;
				town.builtIns = new TownData.BuiltInType[]{ TownData.BuiltInType.Campsite };
				town.locations = new TownData.LocationType[]{ TownData.LocationType.Church };
				town.keywords = new string[] {"Settlement", "Holy"};
				break;
			default :
				town.type = Town.GetNonGeographicTownType ();
			break; }

			// save town to towns
			towns[entry.Key] = town;
		}
		//return towns;
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
	public Town.JobState jobState;	
}

[Serializable]
public class LocationData
{
	public string locationId;
	public Town.LocationType loctionType;
}
*/
