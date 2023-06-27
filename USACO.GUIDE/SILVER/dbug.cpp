//BeginCodeSnip{Solution code}
#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll difference_array[400005]; 
//difference_array[i] = the difference of the values between special intervals i-1 and i

int widths[400005]; //width[i] = the length of special interval i
ll interval_value[400005]; //interval_value[i] = the value of special interval i
//the sum of a special interval is interval_value[i] * width[i]

ll prefix_sums[400005]; //prefix_sums[i] = prefix sum of the sums of special intervals up to i

vector<int> indices; //sorted list of special indices
pair<int, int> queries[100005]; //queries given in the input <l, r>
pair<pair<int, int>, int> updates[100005]; //updates in given in the input <<l, r>, v>

//EndCodeSnip

//finds the "compressed index" of a special index (a.k.a. its position in the sorted list)
int getCompressedIndex(int a) {
	return lower_bound(indices.begin(), indices.end(), a) - indices.begin();
}

//BeginCodeSnip{Solution code}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int N, Q;
	cin >> N >> Q;

	for(int i = 0; i < N; i++) {
		int l, r, v;
		cin >> l >> r >> v;
		indices.push_back(l);
		indices.push_back(r);
		updates[i] = {{l, r}, v};
	}
	for(int i = 0; i < Q; i++) {
		int l, r;
		cin >> l >> r;
		indices.push_back(l);
		indices.push_back(r);
		queries[i] = {l, r};
	}
//EndCodeSnip
	//========= COORDINATE COMPRESSION =======
	sort(indices.begin(), indices.end());
	indices.erase(unique(indices.begin(), indices.end()), indices.end());
		/*
		You can find info on "unique" here: https://www.cplusplus.com/reference/algorithm/unique/

		Since our list is already sorted, the effect of "unique" is duplicates are removed. In total, these two lines
		give us a sorted list with duplicates removed.
		*/
	//========= COORDINATE COMPRESSION =======
//BeginCodeSnip{Solution code}
	//We create the difference array, using coordinate compression and binary search to get the compressed index of each special index
	//Note the 1-based indexing for convenience
	for(int i = 0; i < N; i++) {
		auto a = updates[i];

		difference_array[getCompressedIndex(a.first.first)+1] += a.second;
		difference_array[getCompressedIndex(a.first.second)+1] -= a.second;
	}

	//By keeping track of the original values of the special indices, we can also figure out the lengths of each special interval
	for(int i = 0; i < indices.size()-1; i++) {
		widths[i+1] = indices[i+1] - indices[i];
	}

	//We use prefix sums of the difference array to get the values of the intervals
	for(int i = 1; i < indices.size(); i++) {
		interval_value[i] = interval_value[i-1] + difference_array[i];
	}

	//We use prefix sums over the sums of the special intervals to be able to answer queries quickly
	for(int i = 1; i < indices.size(); i++) {
		prefix_sums[i] = prefix_sums[i-1] + interval_value[i] * widths[i];
	}

	//Classic use of prefix sum array to answer range sum queries
	for(int i = 0; i < Q; i++) {
		cout << prefix_sums[getCompressedIndex(queries[i].second)] - prefix_sums[getCompressedIndex(queries[i].first)] << "\n";
	}

	return 0;
}
//EndCodeSnip