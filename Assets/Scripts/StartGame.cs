using UnityEngine;
using System.Collections;
using UnityEngine.SceneManagement;

public class StartGame : MonoBehaviour {

	public int nextScene;

	public void NewGame()
	{
		GenerateTownsAndMines ();
		LoadNextScene ();
	}

	public void LoadGame()
	{
		if (GameControl.Load ()) {
			LoadNextScene ();
			GameControl.UpdatePossePosition ();
		}
	}

	void GenerateTownsAndMines()
	{
		GameControl.gameData.GenerateTowns ();
		GameControl.Save ();
	}

	void LoadNextScene()
	{
		SceneManager.LoadScene (nextScene);
	}
}