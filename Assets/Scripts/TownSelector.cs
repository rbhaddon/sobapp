using UnityEngine;
using System.Collections;

public class TownSelector : MonoBehaviour {

	public int townIndex;
	public GameObject townPanel;

	private Renderer rend;

	void Start() {
		rend = GetComponent<Renderer>();
	}

	void OnMouseEnter() {
		rend.material.color = Color.magenta;
	}

	void OnMouseOver() {
		//rend.material.color -= new Color(0.1F, 0, 0) * Time.deltaTime;
	}

	void OnMouseExit() {
		rend.material.color = Color.white;
	}

	void OnMouseDown() {
		GameControl.SetCurrentTown (townIndex);
		townPanel.SetActive (true);
	}
}