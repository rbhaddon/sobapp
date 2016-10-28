using UnityEngine;
using System.Collections;
using System.Collections.Generic;
using System;
using System.Linq;
using System.Runtime.Serialization.Formatters.Binary;
using System.IO;
using UnityEngine.SceneManagement;
using HexCrawlConstants;

public class GameControl : MonoBehaviour {

	public static GameControl gameControl;
	public static GameData gameData;

	public GameObject posseMarkerPrefab;
	public GameObject overworld;

	static GameObject posseMarker;
	public int townSize = 0;
	public string townName = "None";
	public string townType = "None";
	public int nextScene = 0;
	public static Town currentTown = new Town ();
	public static int currentTownKey = 1;
	public static int prevTownKey = -1;

	//public static int debugTown = 1;

	static string saveFile; 

	void Enable()
	{
		Debug.Log ("GameControl.Enable()");
		//gameControl.Load ();
	}

	void Awake()
	{
		Debug.Log ("GameControl.Awake()");

		if (gameControl == null) {
			DontDestroyOnLoad (gameObject);
			gameControl = this;

		} else if (gameControl != this)
		{
			Destroy (gameObject);
			posseMarker = Instantiate (posseMarkerPrefab);
			UpdatePossePosition ();
		}
	}

	void Start() {
		Debug.Log ("GameControl.Start()");
		saveFile = Path.Combine(Application.persistentDataPath, "practice_project.dat");
		Debug.Log ("Save location: " + saveFile);
		gameData = new GameData ();
		gameData.posseName = "The Dead Bunnies";
		gameData.UpdateCharts ();
	}

	void OnGUI()
	{
		// First "column"
		GUI.Label (new Rect (10, 10, 200, 30), "Town Name: " + currentTown.name);
		GUI.Label (new Rect (10, 40, 100, 30), "Town Size: " + currentTown.size);

		if (GUI.Button (new Rect (10, 70, 100, 30), "Save")) 
		{
			Save ();
		}

		if (GUI.Button (new Rect (10, 100, 100, 30), "Load")) 
		{
			Load ();
		}
		if (GUI.Button (new Rect (10, 130, 100, 30), "Generate")) 
		{
			gameData.GenerateTowns ();
		}
		if (GUI.Button (new Rect (10, 160, 100, 30), "Next Scene")) 
		{
			nextScene += 1;
			SceneManager.LoadScene (nextScene % 2);
		}
		if (GUI.Button (new Rect (10, 190, 100, 30), "Set Town")) 
		{
			Town myTown = gameData.towns [1];
			SetCurrentTown (myTown);
		}
		if (GUI.Button (new Rect (10, 220, 100, 30), "Update Charts")) 
		{
			gameData.UpdateCharts()	;
		}
			
		// Second "column"
		GUI.Label (new Rect (250, 10, 200, 30), "Posse Name: " + gameData.posseName);
		GUI.Label (new Rect (250, 40, 300, 30), "Town Type: " + currentTown.type);
		GUI.Label (new Rect (250, 70, 300, 30), "Town Trait: " + currentTown.trait);
		GUI.Label (new Rect (250, 100, 300, 30), "Town max_size: " + currentTown.max_size);
		GUI.Label (new Rect (250, 130, 300, 30), "Town status: " + currentTown.status);
	}

	public static void Save()
	{
		Debug.Log ("Saving");
		if (posseMarker) {
			Vector3 possePosition = posseMarker.transform.position;
			gameData.possePositionX = possePosition.x;
			gameData.possePositionY = possePosition.y;
		}
		BinaryFormatter bf = new BinaryFormatter ();
		FileStream file = File.Create (saveFile);

		bf.Serialize (file, gameData);
		file.Close ();
	}

	public static bool Load()
	{
		bool returnValue = false;

		Debug.Log ("Loading...");
		if (File.Exists (saveFile)) {
			BinaryFormatter bf = new BinaryFormatter ();
			FileStream file = File.Open (saveFile, FileMode.Open);

			gameData = (GameData)bf.Deserialize (file);
			file.Close ();

			//currentTown = gameData.towns [debugTown % gameData.towns.Count];

			UpdatePossePosition ();

			//debugTown += 1;
			returnValue = true;
		} else {
			Debug.Log ("No save file to load.");
		}
		return returnValue;
	}

	public static void SetCurrentTown(Town town)
	{
		if (gameData.towns.ContainsValue (town)) {
			currentTown = town;
			prevTownKey = currentTownKey;
			currentTownKey = gameData.towns.FirstOrDefault (x => x.Value == town).Key;
		} else {
			Debug.Log ("Cannot set currentTown; town not found");
		}
	}

	public static void SetCurrentTown(int index)
	{
		if (gameData.towns.ContainsKey(index)) {
			prevTownKey = currentTownKey;
			currentTownKey = index;
			currentTown = gameData.towns [currentTownKey];
		} else {
			Debug.Log("Cannot set currentTown; key not found");
		}
	}

	public void NextTown()
	{
		Debug.Log ("next");
		prevTownKey = currentTownKey;
		currentTownKey += 1;
		try {
			currentTown = gameData.towns [currentTownKey];
			Debug.Log("currentTown updated");
		}
		catch (KeyNotFoundException) {
			//currentTownKey = new List<int>(gameData.towns.Keys)[0];
			currentTownKey = gameData.towns.First ().Key;
			currentTown = gameData.towns [currentTownKey];
		}
	}

	public void PrevTown()
	{
		prevTownKey = currentTownKey;
		currentTownKey -= 1;
		try {
			currentTown = gameData.towns [currentTownKey];
		}
		catch (KeyNotFoundException) {
			currentTownKey = gameData.towns.Last ().Key;
			currentTown = gameData.towns [currentTownKey];
		}
	}

	public static bool TownChanged() {
		return (prevTownKey != currentTownKey);
	}

	public static void UpdatePossePosition() {
		Debug.Log ("Updating posse position");
		if (posseMarker) {
			Vector2 position = new Vector2 (gameData.possePositionX, gameData.possePositionY);
			posseMarker.transform.position = position;
		}
	}

//	public static void DisplayDay()
//	{
//		calendarText.text = gameData.NextDay ();
//	}
}